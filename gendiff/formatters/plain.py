import os

from gendiff.abstraction import get_status, get_key, get_nested, is_nested, get_old_value, \
    get_new_value

BOOLEAN_VALUES = ["true", "null", "false", "none"]


def make_value(item):
    if isinstance(item, (dict, list)):
        return "[complex value]"
    elif item in BOOLEAN_VALUES:
        return item
    return f"'{item}'"


def format_plain(diff):
    lines = []

    def walk(items, path):
        for item in items:
            item_path = os.path.join(path, get_key(item))
            item_path = os.path.normpath(item_path).replace("/", ".")  # for Windows
            if is_nested(item):
                walk(get_nested(item), item_path)
            else:
                lines.append(make_line(item, item_path))

    walk(diff, '')
    lines = filter(None, lines)
    return "\n".join(lines)


def make_line(item, path):
    status = get_status(item)
    if status == 'added':
        new_value = make_value(get_new_value(item))
        return f"Property '{path}' was added with value: {new_value}"
    elif status == 'removed':
        return f"Property '{path}' was removed"
    elif status == 'updated':
        old_value = make_value(get_old_value(item))
        new_value = make_value(get_new_value(item))
        return f"Property '{path}' was updated. From {old_value} to {new_value}"
