import os

from gendiff.diff_abstraction import get_status, get_key, get_nested, is_nested, get_old_value, \
    get_new_value
from gendiff.formatters.stylish import check_and_modify


def resolve_value(value):
    if isinstance(value, str):
        return f"'{value}'"

    elif isinstance(value, dict):
        return '[complex value]'

    return check_and_modify(value)


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
        new_value = resolve_value(get_new_value(item))
        return f"Property '{path}' was added with value: {new_value}"
    elif status == 'removed':
        return f"Property '{path}' was removed"
    elif status == 'updated':
        old_value = resolve_value(get_old_value(item))
        new_value = resolve_value(get_new_value(item))
        return f"Property '{path}' was updated. From {old_value} to {new_value}"
