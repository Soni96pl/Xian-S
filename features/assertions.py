def assert_somewhere_in(value, data, msg=None):
    def process_level(data):
        if not isinstance(data, (dict, list)):
            if data == value:
                return True
            return False

        if isinstance(data, dict):
            data = data.values()

        return any(map(process_level, data))

    if not process_level(data):
        raise AssertionError(msg or "Couldn't find %s" % (value))


def assert_somewhere_equals(data, key, value, msg=None):
    def process_level(data):
        if not isinstance(data, (dict, list)):
            return False

        if isinstance(data, dict):
            if data.get(key, None) == value:
                return True

            data = data.values()

        return any(map(process_level, data))

    if not process_level(data):
        raise AssertionError(msg or "Couldn't find %s = %s" % (key, value))
