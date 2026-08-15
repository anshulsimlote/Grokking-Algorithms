def maxclasses(classes):
    # Sort by ending time
    classes = sorted(classes, key = lambda x:x[1])

    result = []
    last_end = float("-inf")

    for start, end in classes:
        # Class doesn't overlap with previous class
        if start >= last_end:
            result.append([start, end])
            last_end = end

    return result


# --------------------------------
# TEST CASES
# --------------------------------

test_cases = [
    # 1. Empty
    (
        [],
        0
    ),

    # 2. One class
    (
        [[0, 1]],
        1
    ),

    # 3. All non-overlapping
    (
        [[0, 1], [1, 2], [2, 3], [3, 4]],
        4
    ),

    # 4. All overlapping
    (
        [[0, 5], [1, 4], [2, 3]],
        1
    ),

    # 5. Original example
    (
        [[0, 2], [1, 4], [3, 5], [1, 5], [0, 1], [2, 4]],
        2
    ),

    # 6. Touching classes are allowed
    (
        [[0, 2], [2, 4], [4, 6]],
        3
    ),

    # 7. Nested intervals
    (
        [[0, 10], [1, 9], [2, 8], [3, 7]],
        1
    ),

    # 8. Long class should be skipped
    (
        [[0, 10], [1, 2], [2, 3], [3, 4]],
        3
    ),

    # 9. Skip overlapping class
    (
        [[0, 3], [1, 2], [2, 5], [5, 6]],
        3
    ),

    # 10. Multiple optimal solutions possible
    (
        [[0, 2], [2, 4], [0, 1], [1, 4]],
        2
    ),

    # 11. Unsorted input
    (
        [[5, 7], [0, 2], [3, 4], [1, 5], [4, 6]],
        3
    ),
]


# --------------------------------
# RUN TESTS
# --------------------------------

for classes, expected in test_cases:

    result = maxclasses(classes)

    if len(result) == expected:
        print("PASS:", classes)
        print("  Selected:", result)
    else:
        print("FAIL:", classes)
        print("  Got:", result)
        print("  Expected count:", expected)