from itertools import chain

from gendiff.diff_abstraction import get_status, get_key, get_nested, is_nested, get_old_value, \
    get_new_value

INDENT = '  '
STEP_INDENT = '    '
START_DEPTH = 0
STEP_INSIDE = 1
ITEMS_TO_CHECK = {True: "true", False: "false", None: "null"}


def format_stylish(diff):
    return format_diff(diff, START_DEPTH)


def format_diff(diff, depth):
    lines = [make_line(elem, depth) if isinstance(elem, dict) else
             make_line({"key": elem, "status": "equal", "old_value": diff.get(elem)}, depth)
             for elem in diff]

    final_result = chain("{", lines, [f"{STEP_INDENT * depth}" + "}"])
    return "\n".join(final_result)


def make_line(diff, depth):
    key = get_key(diff)
    status = get_status(diff)
    indent = f"{INDENT}{STEP_INDENT * depth}"

    if status == "equal":
        old_value = get_old_value(diff)
        value = resolve_value(old_value, depth)
        return f"{indent}  {key}: {value}"

    elif status == "added":
        new_value = get_new_value(diff)
        value = resolve_value(new_value, depth)
        return f"{indent}+ {key}: {value}"

    elif status == "removed":
        old_value = get_old_value(diff)
        value = resolve_value(old_value, depth)
        return f"{indent}- {key}: {value}"

    elif status == "updated":
        old_value = get_old_value(diff)
        value1 = resolve_value(old_value, depth)

        new_value = get_new_value(diff)
        value2 = resolve_value(new_value, depth)
        return f"{indent}- {key}: {value1}\n{indent}+ {key}: {value2}"

    elif is_nested(diff):
        nested = get_nested(diff)
        value = resolve_value(nested, depth)
        return f"{indent}  {key}: {value}"


def resolve_value(diff, depth):
    if isinstance(diff, (dict, list)):
        return format_diff(diff, depth + STEP_INSIDE)
    elif diff in ITEMS_TO_CHECK:
        return ITEMS_TO_CHECK[diff]
    return str(diff)
