nested_dict = {'key1': {'nested_key1': 1, 'nested_key2': 2}, 'key2': {'nested_key3': 3}}


def flatten_dict(dictionary, parent_key=''):
    flattened_dict = {}
    for key, value in dictionary.items():
        new_key = f"{parent_key}.{key}" if parent_key else key
        if isinstance(value, dict):
            flattened_dict.update(flatten_dict(value, parent_key=new_key))
        else:
            flattened_dict[new_key] = value
    return flattened_dict


flattened_dict = flatten_dict(nested_dict)
print(flattened_dict)
