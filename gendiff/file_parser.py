import json

import yaml


def get_data_from_file(file_path):
    with open(file_path) as file:
        file_extension = file_path.lower().split(".")[1]

        if file_extension == "json":
            file = json.load(file)
        elif file_extension in ("yml", "yaml"):
            file = yaml.load(file, Loader=yaml.Loader)
        else:
            raise ValueError('The entered filetype is not supported')
    return file
