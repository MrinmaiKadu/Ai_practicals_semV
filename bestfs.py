from queue import PriorityQueue

# Graph represented as an adjacency list
graph = {'A': [('B', 2), ('C', 1)],'B': [('D', 3), ('E', 4)],'C': [('F', 5)],'D': [('G', 1)],'E': [],'F': [('H', 3)],'G': [],'H': []}

# Heuristic function (estimated cost to goal)
heuristic = {'A': 7,'B': 6,'C': 3,'D': 5,'E': 4,'F': 2,'G': 2,'H': 0}

def b_f_s(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, [start]))

    while not pq.empty():
        cost, path = pq.get()

        node = path[-1]

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor, neighbor_cost in graph[node]:
            if neighbor not in visited:
                est_cost = neighbor_cost + heuristic[neighbor]
                new_path = list(path)
                new_path.append(neighbor)
                pq.put((est_cost, new_path))

    return []

start_node = 'A'
goal_node = 'H'

path = b_f_s(graph, start_node, goal_node, heuristic)

if path:print(f"Path from {start_node} to {goal_node}: {' -> '.join(path)}")

else:print(f"No path found from {start_node} to {goal_node}.")
