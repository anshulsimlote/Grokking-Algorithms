def quicksortctrl(data, left, right):
    if left >= right:
        return

    pivot = data[(left + right) // 2]

    i = left
    j = right

    while i <= j:

        while i <= right and data[i] < pivot:
            i += 1

        while j >= left and data[j] > pivot:
            j -= 1

        if i <= j:
            data[i], data[j] = data[j], data[i]

            i += 1
            j -= 1

    quicksortctrl(data, left, j)
    quicksortctrl(data, i, right)


def quicksort(data):
    try:
        quicksortctrl(data, 0, len(data) - 1)
        return data
    except RecursionError:
        return data


# --------------------------------
# TEST CASES
# --------------------------------

test_cases = [
    [],
    [1],
    [2, 1],
    [1, 2],
    [3, 5, 2, 1, 4],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
    [2, 2, 2, 2],
    [3, 1, 3, 2, 1],
    [-3, 5, -1, 0, 2],
    [10, -5, 7, 3, -2, 0],
]


# --------------------------------
# RUN TESTS
# --------------------------------

for test in test_cases:
    data = test.copy()

    quicksort(data)

    expected = sorted(test)

    if data == expected:
        print("PASS:", test)
    else:
        print("FAIL:")
        print("  Input:   ", test)
        print("  Got:     ", data)
        print("  Expected:", expected)
