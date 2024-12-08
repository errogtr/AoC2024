from collections import defaultdict
from itertools import combinations


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

        for (x, y, dir) in ((x1, y1, 1), (x2, y2, -1)):
            ax = x + dir * (-1) ** (dx > 0) * abs(dx)
            ay = y + dir * (-1) ** (dy > 0) * abs(dy)
            if 0 <= ax < Lx and 0 <= ay < Ly:
                antinodes.add((ax, ay))

            while 0 <= x < Lx and 0 <= y < Ly:
                harmonic.add((x, y))
                x, y = x + dir * dx, y + dir * dy


# ==== PART 1 ====
print(len(antinodes))


# ==== PART 2 ====
print(len(harmonic))
