from collections import deque

# BFS implementation
def bfs(start, mango_seller):
    visited = set()
    seller_queue = deque([start])
    while seller_queue:
        key = seller_queue.popleft()
        if key in visited:
            continue
        visited.add(key)
        if key.endswith("mango"):
            return True
        if key in mango_seller:
            seller_queue.extend(mango_seller[key])
    return False


# Example usage
mango_seller = {
    "Naruto": {"Goku", "Witcher"},
    "Goku": {"Katy", "Naruto"},
    "Witcher": {"Katy", "Perry"},
    "Johnmango": {"Goku"},
    "Bobmango": {"Witcher"}
}

res = bfs("Naruto", mango_seller)
print(f"->{res}")
