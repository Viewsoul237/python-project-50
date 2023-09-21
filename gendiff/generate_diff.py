import json

import yaml


def generate_diff(file_path1, file_path2):
    file1 = define_format(file_path1)
    file2 = define_format(file_path2)
    result = file1 | file2
    final_result = ["{"]

    for key in sorted(result.keys()):
        if file1.get(key) == file2.get(key):
            final_result.append(f"    {key}: {file1[key]}")
        elif key in file1 and key in file2:
            final_result.append(f"  - {key}: {file1[key]}")
            final_result.append(f"  + {key}: {file2[key]}")
        elif key in file1 and key not in file2:
            final_result.append(f"  - {key}: {file1[key]}")
        elif key in file2 and key not in file1:
            final_result.append(f"  + {key}: {file2[key]}")
    final_result.append("}")
    return '\n'.join(final_result)


def define_format(file_path):
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
