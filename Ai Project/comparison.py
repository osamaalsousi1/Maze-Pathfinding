from BFS import bfs
from DFS import dfs
from UCS import ucs
from Ids import ids
from A import astar
from Hill import hill_climbing
from Genetic import genetic
from maze import START, GOAL


def path_length_from_parent(parent):
    length = 0
    current = GOAL
    while current != START:
        current = parent[current]
        length += 1
    return length + 1


def print_row(name, parent, nodes, time_ms):
    if parent:
        path_len = path_length_from_parent(parent)
        reached = "Yes"
    else:
        path_len = "-"
        reached = "No"

    print(f"{name:<15} {path_len:<12} {nodes:<15} {round(time_ms,2):<10} {reached}")


print("Algorithm        Path Length  Nodes Expanded  Time (ms)  Reached")
print("-" * 65)

parent, nodes, time_ms = bfs()
print_row("BFS", parent, nodes, time_ms)

parent, nodes, time_ms = dfs()
print_row("DFS", parent, nodes, time_ms)

parent, nodes, time_ms = ucs()
print_row("UCS", parent, nodes, time_ms)

parent, nodes, time_ms = ids()
print_row("IDS", parent, nodes, time_ms)

parent, nodes, time_ms = astar()
print_row("A*", parent, nodes, time_ms)

parent, nodes, time_ms = hill_climbing()
print_row("Hill Climbing", parent, nodes, time_ms)

path, nodes, time_ms = genetic()
if path and path[-1] == GOAL:
    path_len = len(path)
    reached = "Yes"
else:
    path_len = "-"
    reached = "No"

print(f"{'Genetic':<15} {path_len:<12} {nodes:<15} {round(time_ms,2):<10} {reached}")
