from collections import defaultdict

RIGHT, DOWN, LEFT, UP = (1, 0), (0, 1), (-1, 0), (0, -1)
DIRS = [RIGHT, DOWN, LEFT, UP]


def get_nn(x, y, plant_xy, garden):
    nn_xy = list()
    for dx, dy in DIRS:
        nn_x, nn_y = x + dx, y + dy
        if garden.get((nn_x, nn_y)) == plant_xy:
            nn_xy.append((nn_x, nn_y))
    return nn_xy


def in_line(pts):
    x_coords, y_coords = zip(*pts)
    return len(set(x_coords)) == 1 or len(set(y_coords)) == 1


garden = dict()
with open("day12/example") as f:
    for y, row in enumerate(f.read().splitlines()):
        for x, plant in enumerate(row):
            garden[(x, y)] = plant


price, regions = 0, list()
visited = set()  # [(x, y, num_nn)]
for (x, y), plant_xy in garden.items():
    if (x, y) in visited:
        continue
    curr_xy = {(x, y)}
    region = defaultdict(int)
    while curr_xy:
        curr_x, curr_y = curr_xy.pop()
        region[(curr_x, curr_y)] = 0
        visited.add((curr_x, curr_y))
        nn_xy = get_nn(curr_x, curr_y, plant_xy, garden)
        for nn_x, nn_y in nn_xy:
            region[(curr_x, curr_y)] += 1
            if (nn_x, nn_y) not in visited:
                curr_xy.add((nn_x, nn_y))

    price += len(region) * sum(4 - i for i in region.values())
    regions.append(region)

print(price)


# ==== PART 2 ====
price = 0
for region in regions:
    edges = 0
    for (x, y) in region:
        # top left
        if (x, y - 1) not in region and (x - 1, y) not in region:
            edges += 1
        elif (x, y - 1) in region and (x - 1, y) in region and (x - 1, y - 1) not in region:
            edges += 1

        # top right
        if (x, y - 1) not in region and (x + 1, y) not in region:
            edges += 1
        elif (x, y - 1) in region and (x + 1, y) in region and (x + 1, y - 1) not in region:
            edges += 1

        # bottom right
        if (x, y + 1) not in region and (x + 1, y) not in region:
            edges += 1
        elif (x, y + 1) in region and (x + 1, y) in region and (x + 1, y + 1) not in region:
            edges += 1

        # bottom left
        if (x - 1, y) not in region and (x, y + 1) not in region:
            edges += 1
        elif (x - 1, y) in region and (x, y + 1) in region and (x - 1, y + 1) not in region:
            edges += 1
    
    price += edges * len(region)

print(price)