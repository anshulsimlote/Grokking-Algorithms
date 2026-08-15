def findmin(classes, lastclass):
    temp_end = float("inf")
    temp_class = []

    for rec in classes:
        end_time = rec[1]
        start_time = rec[0]

        if (
            lastclass != rec
            and (not lastclass or lastclass[1] <= start_time)
            and temp_end > end_time
        ):
            temp_end = end_time
            temp_class = rec

    return temp_class


def maxclasses(classes):
    lastclass = []
    result = []

    while True:
        lastclass = findmin(classes, lastclass)

        if not lastclass:
            break

        result.append(lastclass)

    return result


# --------------------------------
# TEST CASES
# --------------------------------

test_cases = [
    ([], []),

    ([[0, 1]], [[0, 1]]),

    (
        [[0, 1], [1, 2], [2, 3], [3, 4]],
        [[0, 1], [1, 2], [2, 3], [3, 4]]
    ),

    (
        [[0, 5], [1, 4], [2, 3]],
        [[2, 3]]
    ),

    (
        [[0, 2], [1, 4], [3, 5], [1, 5], [0, 1], [2, 4]],
        [[0, 1], [2, 4]]
    ),

    (
        [[0, 2], [2, 4], [4, 6]],
        [[0, 2], [2, 4], [4, 6]]
    ),

    (
        [[0, 10], [1, 9], [2, 8], [3, 7]],
        [[3, 7]]
    ),

    (
        [[0, 10], [1, 2], [2, 3], [3, 4]],
        [[1, 2], [2, 3], [3, 4]]
    ),

    (
        [[0, 3], [1, 2], [2, 5], [5, 6]],
        [[1, 2], [2, 5], [5, 6]]
    ),
]


# --------------------------------
# RUN TESTS
# --------------------------------

for classes, expected in test_cases:

    result = maxclasses(classes)

    # Compare number of selected classes
    if len(result) == len(expected):
        print("PASS:", classes)
        print("  Selected:", result)
    else:
        print("FAIL:", classes)
        print("  Got:     ", result)
        print("  Expected:", expected)