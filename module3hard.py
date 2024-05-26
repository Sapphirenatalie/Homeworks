data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data):
    total = 0

    def helper(element):
        nonlocal total
        if isinstance(element, int):
            total += element
        elif isinstance(element, str):
            total += len(element)
        elif isinstance(element, list) or isinstance(element, tuple) or isinstance(element, set):
            for item in element:
                helper(item)
        elif isinstance(element, dict):
            for key, value in element.items():
                helper(key)
                helper(value)

    helper(data)
    return total


result = calculate_structure_sum(data_structure)

print(result)