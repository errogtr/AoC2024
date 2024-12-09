from tqdm import tqdm


UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

CHANGES = {
    UP: RIGHT,
    RIGHT: DOWN,
    DOWN: LEFT,
    LEFT: UP
}


def parse(grid):
    obstacles = set()
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            match c:
                case "#":
                    obstacles.add((x, y))
                case "^":
                    start = (x, y)
    return start, obstacles



with open("day06/data") as f:
    grid = f.read().splitlines()

Ly = len(grid)
Lx = len(grid[0])

start, obstacles = parse(grid)

visited = {start}
(x, y), (dx, dy) = start, UP
x_next, y_next = x + dx, y + dy
while (0 <= x_next < Lx) and (0 <= y_next < Ly):
    if (x_next, y_next) in obstacles:
        dx, dy = CHANGES[(dx, dy)]
    else:
        x, y = x_next, y_next
        visited.add((x, y))
    x_next, y_next = x + dx, y + dy
print(len(visited))


c = 0
for ox, oy in tqdm(visited):
    obstacles.add((ox, oy))
    visited = {(start, UP)}
    (x, y), (dx, dy) = start, UP
    x_next, y_next = x + dx, y + dy
    while (0 <= x_next < Lx) and (0 <= y_next < Ly):
        if (x_next, y_next) in obstacles:
            dx, dy = CHANGES[(dx, dy)]
        else:
            x, y = x_next, y_next
            visited.add(((x, y), (dx, dy)))
        x_next, y_next = x + dx, y + dy
        if ((x_next, y_next), (dx, dy)) in visited:
            c += 1
            break
    obstacles.remove((ox, oy))
print(c)
