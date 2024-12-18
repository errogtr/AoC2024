from heapq import heappop, heappush
import re


DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def escape(corrupted, nns, Lx, Ly):
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
        for x, y in nns[(curr_x, curr_y)]:
            if (x, y) not in visited and (x, y) not in corrupted:
                heappush(queue, (length, x, y))
                visited.add((x, y))
    
    return length, end_reached


def get_nn(x, y, Lx, Ly):
    nn = list()
    for nn_dx, nn_dy in DIRS:
        nn_x, nn_y = x + nn_dx, y + nn_dy
        if 0 <= nn_x <= Lx and 0 <= nn_y <= Ly:
            nn.append((nn_x, nn_y))
    return nn


with open("day18/data") as f:
    corrupted = [(int(x), int(y)) for x, y in re.findall(r"(\d+),(\d+)", f.read())]

Lx, Ly = 70, 70

nns = {(x, y): get_nn(x, y, Lx, Ly) for x in range(Lx+1) for y in range(Ly+1)}

# ==== PART 1 ====
length, _ = escape(set(corrupted[:1024]), nns, Lx, Ly)
print(length)


# ==== PART 2 ====
blocking = list()
while True:
    blocking.append(corrupted.pop())
    _, end_reached = escape(set(corrupted), nns, Lx, Ly)
    if end_reached:
        break

print(blocking[-1])
