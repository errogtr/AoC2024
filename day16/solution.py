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
visited = {curr_p}
queue = [(0, curr_p, dp)]
while queue:
    score, (curr_x, curr_y), (curr_dx, curr_dy) = heappop(queue)

    if (curr_x, curr_y) == end:
        break
    
    nn = get_nn(score, curr_x, curr_y, curr_dx, curr_dy)
    for next_score, (next_x, next_y), (next_dx, next_dy) in nn:    
        if (next_x, next_y) not in visited:
            heappush(queue, (next_score, (next_x, next_y), (next_dx, next_dy)))
            visited.add((next_x, next_y))

print(score)