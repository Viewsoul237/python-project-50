NONE_BOOLEAN_MAPPING = {True: "true", False: "false", None: "null", }


def resolve_none_and_boolean(value):
    return NONE_BOOLEAN_MAPPING.get(value, value)
