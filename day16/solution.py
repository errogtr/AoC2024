from collections import defaultdict
from heapq import heappop, heappush

W, S, E, N = (1, 0), (0, 1), (-1, 0), (0, -1)


def get_nn(score, x, y, dx, dy):
    nn = list()
    for nn_dx, nn_dy in (W, S, E, N):
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


curr_p = start
dp = (-1, 0)
visited = [curr_p]
queue = [(0, curr_p, dp)]
scores = list()
comes_from = defaultdict(list)
comes_from[(*start,  0)] = None
crossroads = list()
while queue:
    score, (curr_x, curr_y), (curr_dx, curr_dy) = heappop(queue)

    if (curr_x, curr_y) == end:
        scores.append(score)
    
    nn = get_nn(score, curr_x, curr_y, curr_dx, curr_dy)

    if len(nn) > 2:
        crossroads.append((curr_x, curr_y))

    for next_score, (next_x, next_y), (next_dx, next_dy) in nn: 
        comes_from[(next_x, next_y, next_score)].append((curr_x, curr_y, score))   
        if (next_x, next_y) not in visited or (next_x, next_y) in crossroads:
            heappush(queue, (next_score, (next_x, next_y), (next_dx, next_dy)))
            visited.append((next_x, next_y))


print(min(scores))


queue = [(*end, min(scores))]
paths = {end}
while queue:
    p = queue.pop(0)
    prev = comes_from[p]
    if prev:
        pts = {(x, y) for x, y, _ in prev}
        paths |= pts
        queue += prev
print(len(paths))