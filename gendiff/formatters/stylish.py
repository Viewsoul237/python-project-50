from itertools import chain

from gendiff.abstraction import get_status, get_key, get_nested, is_nested, get_old_value, \
    get_new_value

INDENT = '  '
STEP_INDENT = '    '
START_DEPTH = 0
STEP_INSIDE = 1


def format_stylish(diff):
    return create_elem(diff, START_DEPTH)


def create_elem(diff, depth):
    lines = [create_line(elem, depth) if isinstance(elem, dict) else
             create_line({"key": elem, "status": "equal", "old_value": diff.get(elem)}, depth)
             for elem in diff]

    final_result = chain("{", lines, [f"{STEP_INDENT * depth}" + "}"])
    return "\n".join(final_result)


def create_line(diff, depth):
    key = get_key(diff)
    status = get_status(diff)
    indent = f"{INDENT}{STEP_INDENT * depth}"

    if status == "equal":
        old_value = get_old_value(diff)
        value = create_value(old_value, depth)
        return f"{indent}  {key}: {value}"

    elif status == "added":
        new_value = get_new_value(diff)
        value = create_value(new_value, depth)
        return f"{indent}+ {key}: {value}"

    elif status == "removed":
        old_value = get_old_value(diff)
        value = create_value(old_value, depth)
        return f"{indent}- {key}: {value}"

    elif status == "updated":
        old_value = get_old_value(diff)
        value1 = create_value(old_value, depth)

        new_value = get_new_value(diff)
        value2 = create_value(new_value, depth)
        return f"{indent}- {key}: {value1}\n{indent}+ {key}: {value2}"

    elif is_nested(diff):
        nested = get_nested(diff)
        value = create_value(nested, depth)
        return f"{indent}  {key}: {value}"


def create_value(diff, depth):
    if isinstance(diff, (dict, list)):
        return create_elem(diff, depth + STEP_INSIDE)
    return str(diff)
