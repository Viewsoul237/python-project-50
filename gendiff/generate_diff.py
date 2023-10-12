import json

import yaml
from gendiff.diff_abstraction import create_diff
from gendiff.formatters import format_stylish, format_plain, format_json


def generate_diff(file_path1, file_path2, format_name="stylish"):
    # TODO сделать разные функции на формат и развести в else if
    file1 = get_data_from_file(file_path1)
    file2 = get_data_from_file(file_path2)
    data = create_diff(file1, file2)

    match format_name:
        case 'stylish':
            return format_stylish(data)
        case 'plain':
            return format_plain(data)
        case 'json':
            return format_json(data)


def get_data_from_file(file_path):
    with open(file_path) as file:
        if file_path.endswith("json"):
            json_data = json.load(file)
            file = replace_bool_with_str(json_data)
        else:
            yaml_data = yaml.load(file, Loader=yaml.Loader)
            file = replace_bool_with_str(yaml_data)
    return file


def replace_bool_with_str(elem):
    if isinstance(elem, dict):
        for key, value in elem.items():
            elem[key] = replace_bool_with_str(value)
    elif str(elem) == "None":
        elem = str("null")
    elif isinstance(elem, bool):
        elem = str(elem).lower()
    return elem
