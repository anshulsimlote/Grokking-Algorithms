def dijkstra(graph, start, target):
    costs = {start: 0}
    parents = {}
    visited = set()

    while True:
        # Find cheapest unvisited node
        current = None
        lowest_cost = float("inf")

        for node, cost in costs.items():
            if node not in visited and cost < lowest_cost:
                lowest_cost = cost
                current = node

        # No more reachable nodes
        if current is None:
            break

        # Target found
        if current == target:
            break

        visited.add(current)

        # Relax neighbors
        for neighbor, edge_cost in graph.get(current, {}).items():
            new_cost = costs[current] + edge_cost

            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = current

    # Target unreachable
    if target not in costs:
        return None, []

    # Reconstruct path
    path = []
    current = target

    while current != start:
        path.append(current)
        current = parents[current]

    path.append(start)
    path.reverse()

    return costs[target], path

data_graph ={
    "A" : {"B":0,"C":5},
    "B" : {"F":35,"D":30},
    "C" : {"D":15,"F":20},
    "D":{"E":20},
    "F":{"E":10}
}

print("Dijkstra's Algorithm: ")
print(dijkstra(data_graph,"A","E"))

