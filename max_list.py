data = [1, 2, 8, 2, 9, 0]

def max_item(items, index=0):
    """Recursively find the maximum element in a list (no slicing)."""
    if index == len(items) - 1:   # base case: last element
        return items[index]
    
    rest_max = max_item(items, index + 1)
    return items[index] if items[index] > rest_max else rest_max

print(f"Max: {max_item(data)}")
