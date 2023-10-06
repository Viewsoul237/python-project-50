# from gendiff.generate_diff import get_data_from_file # убрать
# from gendiff.create_diff import create_diff
# 
# data1 = get_data_from_file("nested1.json")
# data2 = get_data_from_file("nested2.json")
# x = create_diff(data1, data2)

def format_stylish(diff):
    result = ["{"]

    for elem in diff:
        status = elem.get("status")
        key = elem.get("key")
        old_value = elem.get("old_value")
        new_value = elem.get("new_value")

        if status == "removed":
            result.append(f"  - {key}: {old_value}")
        elif status == "equal":
            result.append(f"    {key}: {old_value}")
        elif status == "updated":
            result.append(f"  - {key}: {old_value}")
            result.append(f"  + {key}: {new_value}")
        elif status == "added":
            result.append(f"  + {key}: {new_value}")
    result.append("}")
    return result

# print(format_stylish(x))