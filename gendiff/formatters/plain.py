import os


def checkout_complex(elem):
    if isinstance(elem, (dict, list)):
        return "[complex value]"
    elif elem in ["true", "null", "false", "none"]:
        return elem
    return f"'{elem}'"


def format_plain(diff):
    lines = []

    def traverse_items(items, path):
        for item in items:
            item_path = os.path.join(path, item["key"])
            item_path = os.path.normpath(item_path).replace("/", ".")  # for Windows
            if item['status'] == 'nested':
                traverse_items(item['nested'], item_path)
            else:
                lines.append(make_line(item, item_path))

    traverse_items(diff, '')
    lines = filter(None, lines)
    return "\n".join(lines)


def make_line(item, path):
    if item['status'] == 'added':
        new_value = checkout_complex(item["new_value"])
        return f"Property '{path}' was added with value: {new_value}"
    elif item['status'] == 'removed':
        return f"Property '{path}' was removed"
    elif item['status'] == 'updated':
        old_value = checkout_complex(item["old_value"])
        new_value = checkout_complex(item["new_value"])
        return f"Property '{path}' was updated. From {old_value} to {new_value}"
