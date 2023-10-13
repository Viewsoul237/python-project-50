ITEMS_TO_CHECK = {True: "true", False: "false", None: "null", }


def check_and_modify(value):
    is_none_or_bool = isinstance(value, bool) or value is None
    return ITEMS_TO_CHECK.get(value) if is_none_or_bool else value
