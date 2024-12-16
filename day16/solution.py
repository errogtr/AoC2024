from collections import defaultdict
from heapq import heappop, heappush
from math import inf
from time import sleep


DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get_nn(score, x, y, dx, dy):
    nn = list()
    for nn_dx, nn_dy in DIRS:
        nn_x, nn_y = x + nn_dx, y + nn_dy
        score_nn = 1 if (nn_dx, nn_dy) == (dx, dy) else 1001
        if maze[(nn_x, nn_y)] in ".E":
            nn.append((score_nn + score, (nn_x, nn_y), (nn_dx, nn_dy)))
    return nn


maze = dict()
with open("day16/data") as f:
    for y, row in enumerate(f.read().splitlines()):
        for x, val in enumerate(row):
            maze[(x, y)] = val


start = next((x, y) for (x, y), val in maze.items() if val == "S")
end = next((x, y) for (x, y), val in maze.items() if val == "E")


# ==== PART 1 ====
visited = {(start)}
queue = [(0, start, (-1, 0))]
comes_from = defaultdict(list)
crossroads = set()
lowest_score = inf
while queue:
    score, (curr_x, curr_y), (curr_dx, curr_dy) = heappop(queue)

    if (curr_x, curr_y) == end:
        lowest_score = min(score, lowest_score)
    
    nn = get_nn(score, curr_x, curr_y, curr_dx, curr_dy)

    if len(nn) > 2:
        crossroads.add((curr_x, curr_y))

    for next_score, (next_x, next_y), (next_dx, next_dy) in nn: 
        comes_from[(next_x, next_y, next_score)].append((curr_x, curr_y, score))   
        if (next_x, next_y) not in visited or (next_x, next_y) in crossroads:
            heappush(queue, (next_score, (next_x, next_y), (next_dx, next_dy)))
            visited.add((next_x, next_y))

print(lowest_score)


# ==== PART 2 ====
queue = [(*end, lowest_score)]
best_tiles = {end}
while queue:
    x, y, score = queue.pop()
    best_tiles.add((x, y))
    queue += comes_from[(x, y, score)]
print(len(best_tiles))
