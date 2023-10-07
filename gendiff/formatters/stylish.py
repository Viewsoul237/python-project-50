from itertools import chain

INDENT = '  '
STEP_INDENT = '    '
START_DEPTH = 0
STEP_INSIDE = 1


def create_value(diff, depth):
    if isinstance(diff, (dict, list)):
        return create_elem(diff, depth + STEP_INSIDE)
    return str(diff)


def create_line(diff, depth):
    key = diff.get("key")
    status = diff.get("status")
    indent = f"{INDENT}{STEP_INDENT * depth}"

    if status == "equal":
        old_value = diff.get("old_value")
        value = create_value(old_value, depth)
        line = f"{indent}  {key}: {value}"

    elif status == "added":
        new_value = diff.get("new_value")
        value = create_value(new_value, depth)
        line = f"{indent}+ {key}: {value}"

    elif status == "removed":
        old_value = diff.get("old_value")
        value = create_value(old_value, depth)
        line = f"{indent}- {key}: {value}"

    elif status == "updated":
        old_value = diff.get("old_value")
        new_value = diff.get("new_value")
        value1 = create_value(old_value, depth)
        value2 = create_value(new_value, depth)
        line = f"{indent}- {key}: {value1}\n" \
               f"{indent}+ {key}: {value2}"

    else:  # nested
        nested = diff.get("nested")
        value = create_value(nested, depth)
        line = f"{indent}  {key}: {value}"

    return line


def create_elem(diff, depth):
    temp_result = []
    for elem in diff:
        if isinstance(elem, dict):
            temp_result.append(create_line(elem, depth))
        else:
            temp_result.append(create_line(
                {
                    "key": elem,
                    "status": "equal",
                    "old_value": diff.get(elem)
                },
                depth,
            ))

    final_result = list(chain("{", temp_result, [f"{STEP_INDENT * depth}" + "}"]))
    return "\n".join(final_result)


def format_stylish(diff):
    return create_elem(diff, START_DEPTH)
