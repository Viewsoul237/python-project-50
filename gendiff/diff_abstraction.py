def create_diff(first_file_data, second_file_data):
    keys = sorted(first_file_data.keys() | second_file_data.keys())
    diff = []

    for key in keys:
        children = dict([('key', key)])
        children.update(make_differences_in_keys(first_file_data, second_file_data, key))
        diff.append(children)
    return diff


def make_differences_in_keys(first_data, second_data, key):
    result = {}
    first_value = first_data.get(key)
    second_value = second_data.get(key)

    if first_value == second_value:
        result["status"] = "equal"
        result["old_value"] = first_value

    elif key in first_data and key in second_data:
        if isinstance(first_value, dict) and isinstance(second_value, dict):
            result["status"] = "nested"
            result["nested"] = create_diff(first_value, second_value)
        else:
            result["status"] = "updated"
            result["old_value"] = first_value
            result["new_value"] = second_value

    elif key in first_data:
        result["status"] = "removed"
        result["old_value"] = first_value

    elif key in second_data:
        result["status"] = "added"
        result["new_value"] = second_value

    return result


def get_status(item):
    return item["status"]


def get_key(item):
    return item["key"]


def get_nested(item):
    return item["nested"]


def is_nested(item):
    return item.get("nested")


def get_old_value(item):
    return item["old_value"]


def get_new_value(item):
    return item["new_value"]
