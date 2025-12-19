import time
from maze import MAZE, START, GOAL, get_neighbors


def dfs():
    stack = [START]
    visited = set()
    parent = {}
    nodes_expanded = 0

    start_time = time.perf_counter()

    while stack:
        current = stack.pop()
        nodes_expanded += 1

        if current not in visited:
            visited.add(current)

            if current == GOAL:
                time_ms = (time.perf_counter() - start_time) * 1000
                return parent, nodes_expanded, time_ms

            for n in get_neighbors(current):
                if n not in visited:
                    parent[n] = current
                    stack.append(n)

    time_ms = (time.perf_counter() - start_time) * 1000
    return None, nodes_expanded, time_ms


def get_path(parent):
    path = []
    current = GOAL
    while current != START:
        path.append(MAZE[current[0]][current[1]])
        current = parent[current]
    path.append('S')
    return path[::-1]


if __name__ == "__main__":
    parent, nodes, time_ms = dfs()

    print("Algorithm: DFS")
    if parent:
        path = get_path(parent)
        print("Path:", " → ".join(path))
        print("Path Length:", len(path))
        print("Reached Goal: Yes")
    else:
        print("Reached Goal: No")

    print("Nodes Expanded:", nodes)
    print("Time (ms):", round(time_ms, 3))
