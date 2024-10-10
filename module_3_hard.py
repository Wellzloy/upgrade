def calculate_structure_sum(*args):
    total_sum = 0

    def recursive_sum(item):
        nonlocal total_sum
        if isinstance(item, list):
            for subitem in item:
                recursive_sum(subitem)
        elif isinstance(item, dict):
            for key, value in item.items():
                recursive_sum(key)
                recursive_sum(value)
        elif isinstance(item, tuple):
            for subitem in item:
                recursive_sum(subitem)
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, set):
            for element in item:
                recursive_sum(element)
        else:
            try:
                total_sum += int(item)
            except ValueError:
                pass

    recursive_sum(args[0])
    return total_sum



data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)