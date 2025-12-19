import time
import heapq
from maze import MAZE, START, GOAL, get_neighbors


def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def astar():
    pq = [(0, START)]
    g = {START: 0}
    parent = {}
    nodes_expanded = 0

    start_time = time.time()

    while pq:
        _, current = heapq.heappop(pq)
        nodes_expanded += 1

        if current == GOAL:
            time_ms = (time.time() - start_time) * 1000
            return parent, nodes_expanded, time_ms

        for n in get_neighbors(current):
            new_g = g[current] + 1
            if n not in g or new_g < g[n]:
                g[n] = new_g
                f = new_g + heuristic(n, GOAL)
                parent[n] = current
                heapq.heappush(pq, (f, n))

    time_ms = (time.time() - start_time) * 1000
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
    parent, nodes, time_ms = astar()

    print("Algorithm: A*")
    if parent:
        path = get_path(parent)
        print("Path:", " → ".join(path))
        print("Path Length:", len(path))
        print("Reached Goal: Yes")
    else:
        print("Reached Goal: No")

    print("Nodes Expanded:", nodes)
    print("Time (ms):", round(time_ms, 3))
