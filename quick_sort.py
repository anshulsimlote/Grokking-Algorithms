def quicksortctrl(data, left, right):
    if(left >= right):
        return
    left_counter = left
    right_counter = right
    pivot = data[(left+right)//2]

    while left_counter <= right_counter:
        while data[left_counter] < pivot:
            left_counter += 1
        while data[right_counter] > pivot:
            right_counter -= 1

        if left_counter <= right_counter:
            data[left_counter], data[right_counter] = data[right_counter], data[left_counter]
            left_counter += 1
            right_counter -= 1
        
    quicksortctrl(data, left, right_counter)
    quicksortctrl(data, left_counter, right)

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
