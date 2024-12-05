from collections import defaultdict
from itertools import combinations


def parse(data):
    r, u = data.split("\n\n")

    rules = defaultdict(set)
    for r in r.split():
        a, b = r.split("|")
        rules[a].add(b)

    return rules, u.split()


def get_middle(update):
    pages = update.split(",")
    return int(pages[len(pages)//2])


with open("day05/data") as f:
    rules, updates = parse(f.read())


ordered = list()
for update in updates:
    pages = update.split(",")
    for i, j in combinations(range(len(pages)), 2):
        p, q = pages[i], pages[j]
        if q not in rules[p]:
            pages[i], pages[j] = pages[j], pages[i]
    ordered.append(",".join(pages))


# ==== PART 1 ====
print(sum(get_middle(o) for u, o in zip(updates, ordered) if u == o))

# ==== PART 2 ====
print(sum(get_middle(o) for u, o in zip(updates, ordered) if u != o))
