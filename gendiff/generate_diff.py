import json

import yaml
from gendiff.flat import flat_diff


def generate_diff(file_path1, file_path2, format_name="stylish"):
    # TODO сделать разные функции на формат и развести в else if
    file1 = get_data_from_file(file_path1)
    file2 = get_data_from_file(file_path2)
    if format_name == "stylish":

        final_result = flat_diff(file1, file2)
    else:
        final_result = ["lox", "pidr"]
    return '\n'.join(final_result)


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
