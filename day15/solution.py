DIRS = {
    "^": complex(0, -1),
    ">": complex(1, 0),
    "<": complex(-1, 0),
    "v": complex(0, 1)
}


with open("day15/data") as f:
    grid, moves = f.read().split("\n\n")
    dirs = [DIRS[move] for move in moves if move != "\n"]

boxes = set()
walls = set()
for y, row in enumerate(grid.splitlines()):
    for x, c in enumerate(row):
        if c == "#":
            walls.add(complex(x, y))
        if c == "O":
            boxes.add(complex(x, y))
        if c == "@":
            curr_z = complex(x, y)


pos = [curr_z]
for dz in dirs:
    next_z = curr_z + dz
    
    # do nothing if it hits a wall
    if next_z in walls:
        continue
    
    # move all boxes in same x/y direction if it hits a box
    if next_z in boxes:
        w = next_z
        block = [next_z]
        while w + dz in boxes:
            w += dz
            block.append(w)
        
        if block[-1] + dz in walls:
            continue

        for box in reversed(block):
            boxes.remove(box)
            boxes.add(box + dz)

    curr_z = next_z
    pos.append(curr_z)


gps = 0
for box in boxes:
    gps += 100 * box.imag + box.real
print(gps)
