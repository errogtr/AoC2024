from collections import defaultdict
from itertools import combinations, pairwise, product


with open("day05/data") as f:
    rules, updates = f.read().split("\n\n")

rules_dict = defaultdict(set)
for r in rules.split():
    a, b = r.split("|")
    rules_dict[a].add(b)


middle = 0
for update in updates.split():
    pages = update.split(",")
    for p, q in pairwise(pages):
        if q not in rules_dict[p]:
            break
    else:
        middle += int(pages[len(pages)//2])
print(middle)


middle = -middle
for update in updates.split():
    pages = update.split(",")
    for i, j in combinations(range(len(pages)), 2):
        p, q = pages[i], pages[j]
        if q not in rules_dict[p]:
            pages[i], pages[j] = pages[j], pages[i]
    middle += int(pages[len(pages)//2])
print(middle)
