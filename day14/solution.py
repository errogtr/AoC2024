from math import prod
from operator import itemgetter
import re


W = 101  # 11 in the example
H = 103   # 7 in the example


Q1 = [0, W // 2 - 1, 0, H // 2 - 1]
Q2 = [W // 2 + 1, (W-1), 0, H // 2 - 1]
Q3 = [0, W // 2 - 1, H // 2 + 1, (H-1)]
Q4 = [W // 2 + 1, (W-1), H // 2 + 1, (H-1)]
QUAD = [Q1, Q2, Q3, Q4]


def simulate(robots, t=1):
    return [((x0 + t*vx) % W, (y0 + t*vy) % H) for x0, y0, vx, vy in robots]


pattern = re.compile(r"p=(\d+),(\d+) v=(-*\d+),(-*\d+)")
with open("day14/data") as f:
    robots = [[int(x) for x in pattern.search(l).groups()] for l in f.readlines()]


# ==== PART 1 ====
simulation = simulate(robots, t=100)
print(prod(sum(a <= x <= b and c <= y <= d for x, y in simulation) for a, b, c, d in QUAD))


# ==== PART 2 ====
T = range(10_000)
simulations = [simulate(robots, t) for t in T]
tree_time = 0
for i in range(1, min(W, H)):
    a, b, c, d = 0+i, W-i, 0+i, H-i  # target region
    area = (b - a) * (d - c)   # target region area
    densities = [sum(a<=x<=b and c<=y<=d for x, y in sim) / area for sim in simulations]
    t, _ = max(zip(T, densities), key=itemgetter(1))
    if t == tree_time:
        break
    tree_time = t
print(tree_time)
