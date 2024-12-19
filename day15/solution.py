from itertools import count


class Tile:
    BOX = "O"
    LBOX = "["
    RBOX = "]"
    EMPTY = "."
    ROBOT = "@"
    WALL = "#"

DIRS = {"^": -1j, ">": 1, "<": -1, "v": 1j}


def get_warehouse(grid):
    warehouse = dict()
    for y, row in enumerate(grid.splitlines()):
        for x, c in enumerate(row):
            warehouse[x + y * 1j] = c
    return warehouse


def double_warehouse(grid):
    warehouse = dict()
    for y, row in enumerate(grid.splitlines()):
        for x, c in enumerate(row):
            if c == Tile.BOX:
                warehouse[2*x + y * 1j] = Tile.LBOX
                warehouse[2*x + 1 + y * 1j] = Tile.RBOX
            elif c == Tile.ROBOT:
                warehouse[2*x + y * 1j] = Tile.ROBOT
                warehouse[2*x + 1 + y * 1j] = Tile.EMPTY
            else:  # c in "#."
                warehouse[2*x + y * 1j] = warehouse[2*x + 1 + y * 1j] = c
    return warehouse


def gps(warehouse, c):
    return int(sum(100 * z.imag + z.real for z in warehouse if warehouse[z] == c))


with open("day15/data") as f:
    grid, moves = f.read().split("\n\n")

dirs = [DIRS[move] for move in moves if move != "\n"]

# ==== PART 1 ====
warehouse = get_warehouse(grid)
curr_z = next(c for c, val in warehouse.items() if val == Tile.ROBOT)
for dz in dirs:
    move = False
    for k in count(1):
        w = curr_z + k * dz
        if warehouse[w] == Tile.WALL:
            break
        if warehouse[w] == Tile.EMPTY:
            move = True
            break

    if move:
        warehouse[w] = Tile.BOX
        warehouse[curr_z + dz] = warehouse[curr_z]
        warehouse[curr_z] = Tile.EMPTY
        curr_z += dz
    
print(gps(warehouse, Tile.BOX))


# ==== PART 2 ====
warehouse = double_warehouse(grid)
curr_z = next(c for c, val in warehouse.items() if val == Tile.ROBOT)
for dz in dirs:
    move = False
    boxes = [curr_z]
    queue = [curr_z]
    while queue:
        w = queue.pop(0) + dz
        if w in boxes:
            continue
        match warehouse[w]:
            case Tile.LBOX:
                boxes.extend([w, w+1])
                queue += [w, w+1]
            case Tile.RBOX:
                boxes.extend([w, w-1])
                queue += [w, w-1]
            case Tile.EMPTY:
                move = True
            case Tile.WALL:
                move = False
                break

    if move:
        for box in reversed(boxes):
            warehouse[box+dz] = warehouse[box]
            warehouse[box] = Tile.EMPTY
        curr_z += dz
  
print(gps(warehouse, Tile.LBOX))
