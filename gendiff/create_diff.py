def key_changes(first_data, second_data, key):
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


def create_diff(data_file1, data_file2):
    keys = sorted(data_file1.keys() | data_file2.keys())
    diff = []
    # print(keys)

    for key in keys:
        children = dict([('key', key)])
        # print(children)
        children.update(key_changes(data_file1, data_file2, key))
        diff.append(children)    
    return diff
