import json
import os
import yaml


def get_data_from_file(file_path):
    with open(file_path) as file:
        if file_path.endswith("json"):
            json_data = json.load(file)
            file = replace_bool_with_str(json_data)
        else:
            yaml_data = yaml.load(file, Loader=yaml.Loader)
            file = replace_bool_with_str(yaml_data)
    return file


def replace_bool_with_str(tree):
    if isinstance(tree, dict):
        for key, value in tree.items():
            tree[key] = replace_bool_with_str(value)
    elif str(tree) == "None":
        tree = str("null")
    elif isinstance(tree, bool):
        tree = str(tree).lower()
    return tree


file1 = os.path.abspath(r"..\nested1.json")
file2 = os.path.abspath(r"..\nested2.json")
file3 = os.path.abspath(r"..\nested1.yml")
file4 = os.path.abspath(r"..\nested2.yaml")
file5 = os.path.abspath(r"..\file1.json")
file6 = os.path.abspath(r"..\file2.yml")
data1 = get_data_from_file(file1)
data2 = get_data_from_file(file2)
data3 = get_data_from_file(file3)
data4 = get_data_from_file(file4)
data5 = get_data_from_file(file5)
data6 = get_data_from_file(file6)


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


print(create_diff(data5, data6))
# print(create_diff(data3, data4))
