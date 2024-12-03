from itertools import pairwise


def is_safe(levels):
    diff = set(y - x for x, y in pairwise(levels))
    return (diff <= {1, 2, 3}) or (diff <= {-1, -2, -3})


def is_tolerated(levels):
    for i in range(len(levels)):
        if is_safe(levels[:i] + levels[i + 1 :]):
            return True
    return False


with open("day02/data") as f:
    reports = [[int(x) for x in l.split()] for l in f.readlines()]


# ==== PART 1 ====
print(sum(is_safe(r) for r in reports))

# ==== PART 2 ====
print(sum(is_safe(r) or is_tolerated(r) for r in reports))
