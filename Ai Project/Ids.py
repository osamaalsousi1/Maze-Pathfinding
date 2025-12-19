import time
from maze import MAZE, START, GOAL, get_neighbors


def dls(current, depth, visited, parent, counter):
    counter[0] += 1

    if current == GOAL:
        return True

    if depth == 0:
        return False

    visited.add(current)

    for n in get_neighbors(current):
        if n not in visited:
            parent[n] = current
            if dls(n, depth - 1, visited, parent, counter):
                return True

    return False


def ids():
    depth = 0
    nodes_expanded = 0

    start_time = time.perf_counter()  

    while True:
        visited = set()
        parent = {}
        counter = [0]

        found = dls(START, depth, visited, parent, counter)
        nodes_expanded += counter[0]

        if found:
            time_ms = (time.perf_counter() - start_time) * 1000
            return parent, nodes_expanded, time_ms

        depth += 1


def get_path(parent):
    path = []
    current = GOAL

    while current != START:
        path.append(MAZE[current[0]][current[1]])
        current = parent[current]

    path.append('S')
    return path[::-1]


if __name__ == "__main__":
    parent, nodes, time_ms = ids()

    print("Algorithm: IDS")

    if parent:
        path = get_path(parent)
        print("Path:", " → ".join(path))
        print("Path Length:", len(path))
        print("Reached Goal: Yes")
    else:
        print("Reached Goal: No")

    print("Nodes Expanded:", nodes)
    print("Time (ms):", round(time_ms, 3))
