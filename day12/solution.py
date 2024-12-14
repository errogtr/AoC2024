RIGHT, DOWN, LEFT, UP = (1, 0), (0, 1), (-1, 0), (0, -1)
DIRS = [RIGHT, DOWN, LEFT, UP]
CORNERS = [
    (UP, RIGHT),  # top right
    (UP, LEFT),  # top left
    (DOWN, RIGHT), # bottom right
    (DOWN, LEFT),  # bottom left
    ]


def get_nn(x, y, plant_xy, garden):
    nn_xy = list()
    for dx, dy in DIRS:
        nn_x, nn_y = x + dx, y + dy
        if garden.get((nn_x, nn_y)) == plant_xy:
            nn_xy.append((nn_x, nn_y))
    return nn_xy


def get_edges(region):
    """ num-of-edges = num-of-corners for polygons """
    return sum(get_corners(x, y, region) for x, y in region)


def get_corners(x, y, region):
    """Checks how many vertices of a (x, y) position are region's corners"""
    return sum(is_corner(x, y, *c1, *c2, region) for c1, c2 in CORNERS)


def is_corner(x, y, dx1, dy1, dx2, dy2, region):
    """
        yx.
        xA.
        ...

        upper-left vertex of A is a corner if 
        -   both x's are different from A (external corner)
        -   both x's equal A and y is different from A (internal corner)
    """
    nn1 = x + dx1, y + dy1
    nn2 = x + dx2, y + dy2
    diag = x + dx1 + dx2, y + dy1 + dy2
    if nn1 not in region and nn2 not in region:
        return True
    if nn1 in region and nn2 in region and diag not in region:
        return True
    return False


garden = dict()
with open("day12/data") as f:
    for y, row in enumerate(f.read().splitlines()):
        for x, plant in enumerate(row):
            garden[(x, y)] = plant


# ==== PART 2 ====
price, regions = 0, list()  # [{(x, y): num_nn)]
visited = set()  
for (x, y), plant_xy in garden.items():
    if (x, y) in visited:
        continue
    curr_xy = {(x, y)}
    region = dict()
    while curr_xy:
        curr_x, curr_y = curr_xy.pop()
        region[(curr_x, curr_y)] = 4  # start with 4 nn in same region
        visited.add((curr_x, curr_y))
        nn_xy = get_nn(curr_x, curr_y, plant_xy, garden)
        for nn_x, nn_y in nn_xy:
            region[(curr_x, curr_y)] -= 1  # if not in region, lower nn by 1
            if (nn_x, nn_y) not in visited:
                curr_xy.add((nn_x, nn_y))

    price += len(region) * sum(region.values())
    regions.append(region)

print(price)


# ==== PART 2 ====
print(sum(get_edges(region) * len(region) for region in regions))
