NN_DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def get_nn(x, y, guide):
    nn = list()
    for dx, dy in NN_DIRS:
        z, w = x + dx, y + dy
        if guide.get((z, w), -1) - guide.get((x, y)) == 1:
            nn.append((z, w))
    return nn


guide = dict()
trailheads = list()
with open("day10/data") as f:
    for y, row in enumerate(f.read().splitlines()):
        for x, h in enumerate(row):
            guide[(x, y)] = int(h)
            if h == '0':
                trailheads.append((x, y))


scores, ratings = 0, 0
for xp, yp in trailheads:
    peaks = set()
    path = [(xp, yp)]
    while path:
        for x, y in get_nn(*path.pop(), guide):
            path.append((x, y))
            is_peak = guide[(x, y)] == 9
            ratings += is_peak
            if is_peak and (x, y) not in peaks:
                peaks.add((x, y))
                scores += 1
    
# ==== PART 1 ====
print(scores)

# ==== PART 2 ====
print(ratings)
