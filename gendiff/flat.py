def flat_diff(data_one, data_two):
    merged_files = data_one | data_two
    final_result = ["{"]

    for key in sorted(merged_files.keys()):
        if data_one.get(key) == data_two.get(key):
            final_result.append(f"    {key}: {data_one[key]}")
        elif key in data_one and key in data_two:
            final_result.append(f"  - {key}: {data_one[key]}")
            final_result.append(f"  + {key}: {data_two[key]}")
        elif key in data_one and key not in data_two:
            final_result.append(f"  - {key}: {data_one[key]}")
        elif key in data_two and key not in data_one:
            final_result.append(f"  + {key}: {data_two[key]}")

    final_result.append("}")
    return final_result
