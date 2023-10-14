NONE_BOOLEAN_MAPPING = {True: "true", False: "false", None: "null", }


def resolve_none_and_boolean(value):
    is_none_or_bool = isinstance(value, bool) or value is None
    return NONE_BOOLEAN_MAPPING.get(value) if is_none_or_bool else value
