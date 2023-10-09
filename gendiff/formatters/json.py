import json


def format_json(diff):
    json_data = json.dumps(diff, indent=4)
    return json_data
