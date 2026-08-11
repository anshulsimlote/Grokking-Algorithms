from collections import deque

def dfs(start, graph):
    stack = [start]
    visited = set()

    while stack:
        person = stack.pop()

        print("person:", person)

        if person in visited:
            continue

        visited.add(person)

        if person.endswith("mango"):
            print(f"Found mango seller -> {person}")
            return True

        stack.extend(x for x in graph.get(person, []) if x not in visited)

    return False


# Example usage
graph = {
    "Naruto": {"Goku", "Witcher"},
    "Goku": {"Katy", "Naruto"},
    "Witcher": {"Katy", "Perry","Johnmango"},
    "Johnmango": {"Goku","Bobmango"},
    "Bobmango": {"Witcher"}
}

result = dfs("Naruto", graph)
print(f"Found mango seller? -> {result}")
