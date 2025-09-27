from collections import deque

def bfs(start, graph):
    """Perform BFS to find a node whose name ends with 'mango'."""
    visited = set()
    queue = deque([start])

    while queue:
        person = queue.popleft()
        if person in visited:
            continue
        visited.add(person)

        if person.endswith("mango"):
            return True
        
        queue.extend(neighbor for neighbor in graph.get(person, []) if neighbor not in visited)

    return False


# Example usage
graph = {
    "Naruto": {"Goku", "Witcher"},
    "Goku": {"Katy", "Naruto"},
    "Witcher": {"Katy", "Perry","Johnmango"},
    "Johnmango": {"Goku","Bobmango"},
    "Bobmango": {"Witcher"}
}

result = bfs("Naruto", graph)
print(f"Found mango seller? -> {result}")
