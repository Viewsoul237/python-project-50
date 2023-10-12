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
            file = json.load(file)
        else:
            file = yaml.load(file, Loader=yaml.Loader)

    return file
