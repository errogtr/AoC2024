from collections import defaultdict
from itertools import combinations, count


def coords(x0, y0, dx, dy, k):
    x = x0 + k * (-1)**(dx < 0) * abs(dx)
    y = y0 + k * (-1)**(dy < 0) * abs(dy)
    return x, y


def line(x0, y0, dx, dy, Lx, Ly):
    points = list()
    for k in count(1):
        x, y = coords(x0, y0, dx, dy, k)
        if x < 0 or x >= Lx or y < 0 or y >= Ly:
            break
        points.append((x, y))
    return points


antennas = defaultdict(set)
with open("day08/data") as f:
    grid = f.read().splitlines()

Lx = len(grid[0])
Ly = len(grid)

for y, row in enumerate(grid):
    for x, freq in enumerate(row):
        if freq != ".":
            antennas[freq].add((x, y))


antinodes, harmonic = set(), set()
for positions in antennas.values():
    for (x1, y1), (x2, y2) in combinations(positions, 2):
        dx, dy = x2 - x1, y2 - y1

        points_pos = line(x1, y1, dx, dy, Lx, Ly)
        if len(points_pos) > 1:
            antinodes.add(points_pos[1])
        
        points_neg = line(x2, y2, -dx, -dy, Lx, Ly)
        if len(points_neg) > 1:
            antinodes.add(points_neg[1])

        harmonic |= set(points_neg) | set(points_pos)


# ==== PART 1 ====
print(len(antinodes))


# ==== PART 2 ====
print(len(harmonic))
