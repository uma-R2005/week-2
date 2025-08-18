# Map and Filter equivalents for sets
def my_map_set(func, input_set):
    """
    Apply func to each item in input_set and return a new set with results.
    """
    return {func(item) for item in input_set}

def my_filter_set(func, input_set):
    """
    Return a new set containing only items for which func(item) is True.
    """
    return {item for item in input_set if func(item)}


# Map and Filter equivalents for dictionaries
def my_map_dict(func, input_dict):
    """
    Apply func to each (key, value) pair in input_dict and return a new dictionary.
    func should return a tuple (new_key, new_value).
    """
    return {new_k: new_v for k, v in input_dict.items() for new_k, new_v in [func(k, v)]}

def my_filter_dict(func, input_dict):
    """
    Return a new dictionary containing only items for which func(key, value) is True.
    """
    return {k: v for k, v in input_dict.items() if func(k, v)}


# Example usage:

# Working with sets
s = {1, 2, 3, 4}

mapped_set = my_map_set(lambda x: x * 2, s)
print("Mapped Set:", mapped_set)  # Output: {2, 4, 6, 8}

filtered_set = my_filter_set(lambda x: x % 2 == 0, s)
print("Filtered Set:", filtered_set)  # Output: {2, 4}


# Working with dictionaries
d = {'a': 1, 'b': 2, 'c': 3}

mapped_dict = my_map_dict(lambda k, v: (k.upper(), v ** 2), d)
print("Mapped Dict:", mapped_dict)  # Output: {'A': 1, 'B': 4, 'C': 9}

filtered_dict = my_filter_dict(lambda k, v: v % 2 == 0, d)
print("Filtered Dict:", filtered_dict)  # Output: {'b': 2}
