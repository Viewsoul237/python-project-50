import json

import yaml
from gendiff.flat import flat_diff


def generate_diff(file_path1, file_path2, format="stylish"):
    # TODO сделать разные функции на формат и развести в else if
    if format == "stylish":
        file1 = get_data_from_file(file_path1)
        file2 = get_data_from_file(file_path2)
        final_result = flat_diff(file1, file2)
    else:
        final_result = ["lox", "pidr"]
    return '\n'.join(final_result)


def get_data_from_file(file_path):
    with open(file_path) as file:
        if file_path.endswith("json"):
            json_data = json.load(file)
            file = {k: str(v).lower() if isinstance(v, bool) else v for k, v in
                    json_data.items()}
        else:
            yaml_data = yaml.load(file, Loader=yaml.Loader)
            file = {k: str(v).lower() if isinstance(v, bool) else v for k, v in
                    yaml_data.items()}
    return file
