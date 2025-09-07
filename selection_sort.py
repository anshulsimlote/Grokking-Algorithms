def find_smallest_index(data_list):
    """Return the index of the smallest element in the list."""
    smallest_index = 0
    smallest = data_list[0]

    for index, value in enumerate(data_list[1:], start=1):
        if value < smallest:
            smallest, smallest_index = value, index

    return smallest_index


def selection_sort(data_list):
    """Sort a list using selection sort (returns a new list)."""
    data = data_list[:]  # copy so we don't modify the original
    result = []
    while data:
        smallest_index = find_smallest_index(data)
        result.append(data.pop(smallest_index))
    return result


# Example
data_list = [5, 2, 99, 0, 3]
result = selection_sort(data_list)
print(f"Result: {result}")
