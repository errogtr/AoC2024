from collections import defaultdict
from itertools import combinations


def get_middle(update):
    pages = update.split(",")
    return int(pages[len(pages)//2])


with open("day05/data") as f:
    rules, updates = f.read().split("\n\n")

rules_dict = defaultdict(set)
for r in rules.split():
    a, b = r.split("|")
    rules_dict[a].add(b)

ordered = list()
for update in updates.split():
    pages = update.split(",")
    for i, j in combinations(range(len(pages)), 2):
        p, q = pages[i], pages[j]
        if q not in rules_dict[p]:
            pages[i], pages[j] = pages[j], pages[i]
    ordered.append(",".join(pages))


# ==== PART 1 ====
print(sum(get_middle(o) for u, o in zip(updates.split(), ordered) if u == o))

# ==== PART 2 ====
print(sum(get_middle(o) for u, o in zip(updates.split(), ordered) if u != o))
