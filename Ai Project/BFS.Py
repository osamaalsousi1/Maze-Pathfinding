from collections import deque
import time
from maze import MAZE, START, GOAL, get_neighbors


def bfs():
    queue = deque([START])
    visited = set([START])
    parent = {}
    nodes_expanded = 0

    start_time = time.perf_counter()   

    while queue:
        current = queue.popleft()
        nodes_expanded += 1

        if current == GOAL:
            time_ms = (time.perf_counter() - start_time) * 1000
            return parent, nodes_expanded, time_ms

        for n in get_neighbors(current):
            if n not in visited:
                visited.add(n)
                parent[n] = current
                queue.append(n)

    time_ms = (time.perf_counter() - start_time) * 1000
    return None, nodes_expanded, time_ms


def get_path_letters(parent):
    path = []
    current = GOAL

    while current != START:
        path.append(MAZE[current[0]][current[1]])
        current = parent[current]

    path.append('S')
    path.reverse()
    return path


if __name__ == "__main__":
    parent, nodes, time_ms = bfs()

    print("Algorithm: BFS")

    if parent:
        path = get_path_letters(parent)
        print("Path:", " → ".join(path))
        print("Path Length:", len(path))
        print("Reached Goal: Yes")
    else:
        print("No Path Found")
        print("Reached Goal: No")

    print("Nodes Expanded:", nodes)
    print("Time (ms):", round(time_ms, 3))
