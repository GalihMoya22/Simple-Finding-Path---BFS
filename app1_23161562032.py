from collections import deque

def bfs_shortest_path(city_map, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in city_map[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None

city_map = {
    'Home': ['Mall', 'School'],
    'Mall': ['Gym', 'Hospital'],
    'School': ['Library'],
    'Gym': ['Hospital'],
    'Library': ['Hospital'],
    'Hospital': []
}

start = 'Home'
goal = 'Hospital'
shortest_path = bfs_shortest_path(city_map, start, goal)

if shortest_path:
    print(f"Shortest path from {start} to {goal}: {' -> '.join(shortest_path)}")
else:
    print(f"No path found from {start} to {goal}.")
