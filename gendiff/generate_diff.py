import json


def generate_diff(file_path1, file_path2):
    file1 = {k: str(v).lower() if isinstance(v, bool) else v for k, v in json.load(open(file_path1)).items()}
    file2 = {k: str(v).lower() if isinstance(v, bool) else v for k, v in json.load(open(file_path2)).items()}
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
