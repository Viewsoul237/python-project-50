import os

x = [{'key': 'common', 'status': 'nested',
      'nested': [{'key': 'follow', 'status': 'added', 'new_value': 'false'},
                 {'key': 'setting1', 'status': 'equal', 'old_value': 'Value 1'},
                 {'key': 'setting2', 'status': 'removed', 'old_value': 200},
                 {'key': 'setting3', 'status': 'updated', 'old_value': 'true', 'new_value': 'null'},
                 {'key': 'setting4', 'status': 'added', 'new_value': 'blah blah'},
                 {'key': 'setting5', 'status': 'added', 'new_value': {'key5': 'value5'}},
                 {'key': 'setting6', 'status': 'nested', 'nested': [
                     {'key': 'doge', 'status': 'nested', 'nested': [
                         {'key': 'wow', 'status': 'updated', 'old_value': '',
                          'new_value': 'so much'}]},
                     {'key': 'key', 'status': 'equal', 'old_value': 'value'},
                     {'key': 'ops', 'status': 'added', 'new_value': 'vops'}]}]},
     {'key': 'group1', 'status': 'nested',
      'nested': [{'key': 'baz', 'status': 'updated', 'old_value': 'bas', 'new_value': 'bars'},
                 {'key': 'foo', 'status': 'equal', 'old_value': 'bar'},
                 {'key': 'nest', 'status': 'updated', 'old_value': {'key': 'value'},
                  'new_value': 'str'}]},
     {'key': 'group2', 'status': 'removed', 'old_value': {'abc': 12345, 'deep': {'id': 45}}},
     {'key': 'group3', 'status': 'added',
      'new_value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]


def checkout_complex(elem):
    if isinstance(elem, (dict, list)):
        return "[complex value]"
    elif elem in ["true", "null", "false", "none"]:
        return elem
    return f"'{elem}'"


def format_plain(diff):
    lines = []

    def make_line(item, path):
        if item['status'] == 'added':
            new_value = checkout_complex(item["new_value"])
            lines.append(f"Property '{path}' was added with value: {new_value}")
        elif item['status'] == 'removed':
            lines.append(f"Property '{path}' was removed")
        elif item['status'] == 'updated':
            old_value = checkout_complex(item["old_value"])
            new_value = checkout_complex(item["new_value"])
            lines.append(f"Property '{path}' was updated. From {old_value} to {new_value}")

    def traverse_items(items, path):
        for item in items:
            item_path = os.path.join(path, item["key"])
            item_path = os.path.normpath(item_path).replace("/", ".") # for Windows                 
            
            if item['status'] == 'nested':
                traverse_items(item['nested'], item_path)
            else:
                make_line(item, item_path)

    traverse_items(diff, '')
    return "\n".join(lines)



