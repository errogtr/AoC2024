from collections import defaultdict
from functools import cmp_to_key, partial


def parse(data):
    r, u = data.split("\n\n")

    rules = defaultdict(set)
    for single_rule in r.split():
        a, b = single_rule.split("|")
        rules[a].add(b)
    
    updates = [l.split(",") for l in u.split()]
    return rules, updates


def cmp(pages, rules, a, b):
    return len(pages & rules[b]) - len(pages & rules[a]) 


def get_middle(update):
    return int(update[len(update)//2])


with open("day05/data") as f:
    rules, updates = parse(f.read())

sorted_updates = [
    sorted(u, key=cmp_to_key(partial(cmp, set(u), rules))) for u in updates
    ]

# ==== PART 1 ====
print(sum(get_middle(u) for u, s in zip(updates, sorted_updates) if u == s))

# ==== PART 2 ====
print(sum(get_middle(u) for u, s in zip(updates, sorted_updates) if u != s))
