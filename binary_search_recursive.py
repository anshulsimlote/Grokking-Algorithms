data = [1, 2, 3, 6, 9, 12, 32, 0]

def binary_search(arr, key, left=0, right=None):
    """
    Recursive binary search.
    Returns the index of `key` in sorted `arr`, or -1 if not found.
    """
    if right is None:
        right = len(arr) - 1

    # base case: empty range
    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, left, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, right)


# ensure list is sorted before searching
sorted_data = sorted(data)
print(f"Data (sorted): {sorted_data}")
print(f"Search 9  -> index: {binary_search(sorted_data, 9)}")
print(f"Search 91 -> index: {binary_search(sorted_data, 91)}")
