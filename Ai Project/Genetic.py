import time
import random
from maze import MAZE, START, GOAL, get_neighbors


POPULATION_SIZE = 30
GENERATIONS = 100
MUTATION_RATE = 0.1
MAX_STEPS = 30


def random_path():
    path = [START]
    current = START

    for _ in range(MAX_STEPS):
        neighbors = get_neighbors(current)
        if not neighbors:
            break
        current = random.choice(neighbors)
        path.append(current)
        if current == GOAL:
            break

    return path


def fitness(path):
    last = path[-1]
    distance = abs(last[0] - GOAL[0]) + abs(last[1] - GOAL[1])
    return distance + len(path)


def crossover(p1, p2):
    cut = min(len(p1), len(p2)) // 2
    return p1[:cut] + p2[cut:]


def mutate(path):
    if random.random() < MUTATION_RATE:
        idx = random.randint(0, len(path) - 1)
        neighbors = get_neighbors(path[idx])
        if neighbors:
            path[idx] = random.choice(neighbors)
    return path


def genetic():
    population = [random_path() for _ in range(POPULATION_SIZE)]
    nodes_expanded = 0

    start_time = time.perf_counter()   

    for _ in range(GENERATIONS):
        population.sort(key=fitness)
        best = population[0]
        nodes_expanded += len(population)

        if best[-1] == GOAL:
            time_ms = (time.perf_counter() - start_time) * 1000
            return best, nodes_expanded, time_ms

        new_population = population[:5]  

        while len(new_population) < POPULATION_SIZE:
            p1, p2 = random.sample(population[:10], 2)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    time_ms = (time.perf_counter() - start_time) * 1000
    return population[0], nodes_expanded, time_ms


def print_path_letters(path):
    letters = [MAZE[x][y] for x, y in path]
    print(" → ".join(letters))


if __name__ == "__main__":
    path, nodes, time_ms = genetic()

    print("Algorithm: Genetic Algorithm")

    if path and path[-1] == GOAL:
        print("Path:")
        print_path_letters(path)
        print("Path Length:", len(path))
        print("Reached Goal: Yes")
    else:
        print("Reached Goal: No")
        print("Best Found Path:")
        print_path_letters(path)

    print("Nodes Expanded:", nodes)
    print("Time (ms):", round(time_ms, 3))
