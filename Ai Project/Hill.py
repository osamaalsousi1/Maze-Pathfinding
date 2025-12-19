import time
from maze import MAZE, START, GOAL, get_neighbors


def heuristic(pos):
    
    return abs(pos[0] - GOAL[0]) + abs(pos[1] - GOAL[1])


def hill_climbing():
    current = START
    parent = {}
    nodes_expanded = 0

    start_time = time.perf_counter()  

    while current != GOAL:
        nodes_expanded += 1
        neighbors = get_neighbors(current)

        if not neighbors:
            break

       
        next_node = min(neighbors, key=heuristic)

        if heuristic(next_node) >= heuristic(current):
            break

        parent[next_node] = current
        current = next_node

    time_ms = (time.perf_counter() - start_time) * 1000

    if current == GOAL:
        return parent, nodes_expanded, time_ms
    else:
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
    parent, nodes, time_ms = hill_climbing()

    print("Algorithm: Hill Climbing")

    if parent:
        path = []
        current = GOAL
        while current != START:
            path.append(MAZE[current[0]][current[1]])
            current = parent[current]
        path.append('S')
        path.reverse()

        print("Path:", " → ".join(path))
        print("Path Length:", len(path))
        print("Reached Goal: Yes")
    else:
        print("No Path Found")
        print("Reached Goal: No")

    print("Nodes Expanded:", nodes)
    print("Time (ms):", round(time_ms, 3))
