def merge(left_arr, right_arr):
    print(f"    MERGE: {left_arr} + {right_arr}")

    res = []
    left = 0
    right = 0

    while left < len(left_arr) and right < len(right_arr):
        if left_arr[left] <= right_arr[right]:
            res.append(left_arr[left])
            left += 1
        else:
            res.append(right_arr[right])
            right += 1

    while left < len(left_arr):
        res.append(left_arr[left])
        left += 1

    while right < len(right_arr):
        res.append(right_arr[right])
        right += 1

    print(f"    RESULT: {res}")

    return res


def mergesort(data):
    if len(data) < 2:
        return data

    mid = len(data) // 2

    left_arr = data[:mid]
    right_arr = data[mid:]

    print(f"SPLIT:  {data}")
    print(f"LEFT:   {left_arr}")
    print(f"RIGHT:  {right_arr}")

    left_arr = mergesort(left_arr)
    right_arr = mergesort(right_arr)

    return merge(left_arr, right_arr)


# --------------------------------
# TEST CASES
# --------------------------------

test_cases = [
    [70,30,50,10],
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
    print("\n" + "=" * 50)
    print("INPUT:", test)
    print("=" * 50)

    data = test.copy()

    data = mergesort(data)

    expected = sorted(test)

    if data == expected:
        print("PASS:", test)
    else:
        print("FAIL:")
        print("  Input:   ", test)
        print("  Got:     ", data)
        print("  Expected:", expected)