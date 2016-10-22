def get_data(data, path):
    def extract(data, keys):
        if isinstance(data, dict):
            key = keys[0]
        elif isinstance(data, list):
            key = int(keys[0])

        if len(keys) == 1:
            return data[key]
        return extract(data[key], keys[1:])

    if path[0] == '/':
        if len(path) == 1:
            return data
        path = path[1:]

    return extract(data, path.split('/'))
