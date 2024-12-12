from collections import defaultdict


DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


garden = dict()
with open("day12/data") as f:
    for y, row in enumerate(f.read().splitlines()):
        for x, plant in enumerate(row):
            garden[(x, y)] = plant



regions = list()  # [(x, y, num_nn)]
visited = set()
for (x, y), plant_xy in garden.items():
    if (x, y) in visited:
        continue
    curr_xy = [(x, y)]
    region = region()
    while curr_xy:
        curr_x, curr_y = curr_xy.pop()
        region[(curr_x, curr_y)] = 4
        visited.add((curr_x, curr_y))

        nn_curr_xy = list()
        for dx, dy in DIRS:
            nn_x, nn_y = curr_x + dx, curr_y + dy
            if garden.get((nn_x, nn_y)) == plant_xy:
                nn_curr_xy.append((nn_x, nn_y))


        for nn_x, nn_y in nn_curr_xy:
            region[(curr_x, curr_y)] -= 1
            if (nn_x, nn_y) not in visited:
                curr_xy.append((nn_x, nn_y))

    regions.append(region)


value = 0
for region in regions:
    area = len(region)
    perimeter = sum(region.values())
    value += area * perimeter

print(value)
    