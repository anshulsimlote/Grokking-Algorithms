data = [1, 2, 8, 2, 9, 0]

def max_item(items, left=0, right=None):
    """Recursively find the maximum element in a list using divide & conquer."""
    if not items:
        raise ValueError("max_item() arg is an empty list")

    if right is None:
        right = len(items) - 1

    # base case: one element
    if left == right:
        return items[left]

    mid = (left + right) // 2
    left_max = max_item(items, left, mid)
    right_max = max_item(items, mid + 1, right)

    return max(left_max, right_max)  # more Pythonic
        

print(f"Max: {max_item(data)}")
