from heapq import heappop, heappush
import re


DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def escape(corrupted, Lx, Ly):
    # Dijkstra from start to end
    start = 0, 0
    end = Lx, Ly
    length = 0
    end_reached = False
    visited = {(start)}
    queue = [(length, *start)]
    while queue:
        length, curr_x, curr_y = heappop(queue)

        if (curr_x, curr_y) == end:
            end_reached = True
            break

        length += 1
        for next_x, next_y in get_nn(curr_x, curr_y, corrupted, Lx, Ly):
            if (next_x, next_y) not in visited and (next_x, next_y) not in corrupted:
                heappush(queue, (length, next_x, next_y))
                visited.add((next_x, next_y))
    
    return length, end_reached


def get_nn(x, y, corrupted, Lx, Ly):
    nn = list()
    for nn_dx, nn_dy in DIRS:
        nn_x, nn_y = x + nn_dx, y + nn_dy
        if 0 <= nn_x <= Lx and 0 <= nn_y <= Ly and (nn_x, nn_y) not in corrupted:
            nn.append((nn_x, nn_y))
    return nn


with open("day18/data") as f:
    corrupted = [(int(x), int(y)) for x, y in re.findall(r"(\d+),(\d+)", f.read())]

Lx, Ly = 70, 70

# ==== PART 1 ====
length, _ = escape(corrupted[:1024], Lx, Ly)
print(length)


# ==== PART 2 ====
blocking = list()
while True:
    blocking.append(corrupted.pop())
    _, end_reached = escape(corrupted, Lx, Ly)
    if end_reached:
        break

print(blocking[-1])
