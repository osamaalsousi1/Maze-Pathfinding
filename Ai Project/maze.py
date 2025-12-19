MAZE = [
    ['S', 'A', 'B', 'X', 'C', 'D'],
    ['X', 'E', 'X', 'X', 'F', 'X'],
    ['G', 'H', 'I', 'J', 'K', 'L'],
    ['X', 'X', 'X', 'M', 'X', 'N'],
    ['O', 'P', 'Q', 'R', 'S', 'T'],
    ['X', 'X', 'U', 'X', 'V', 'G']
]

ROWS = len(MAZE)
COLS = len(MAZE[0])


def find(symbol):
    for i in range(ROWS):
        for j in range(COLS):
            if MAZE[i][j] == symbol:
                return (i, j)
    return None


START = find('S')
GOAL  = find('G')


def get_neighbors(pos):
    x, y = pos
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbors = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < ROWS and 0 <= ny < COLS:
            if MAZE[nx][ny] != 'X':
                neighbors.append((nx, ny))

    return neighbors
