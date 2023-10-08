def get_status(item):
    return item["status"]


def get_key(item):
    return item["key"]


def get_nested(item):
    return item["nested"]


def is_nested(item):
    return item.get("nested")


def get_old_value(item):
    return item["old_value"]


def get_new_value(item):
    return item["new_value"]
