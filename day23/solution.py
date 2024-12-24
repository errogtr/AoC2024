from collections import defaultdict
from copy import copy


links = defaultdict(list)
with open("day23/data") as f:
    for line in f.read().splitlines():
        c1, c2 = line.split("-")
        links[c1].append(c2)
        links[c2].append(c1)


# ==== PART 1 ====
clusters = set()
for u, links_u in links.items():
    for v in links_u:
        links_v = links[v]
        for w in set(links_u) & set(links_v):
            clusters.add(tuple(sorted((u, v, w))))

print(sum(any(c.startswith("t") for c in cluster) for cluster in clusters))


# ==== PART 2 ====
largest_clique = set()
for u, links_u in links.items():
    queue = copy(links_u)
    clique_u = {u}
    while queue:
        v = queue.pop()
        links_v = links[v]

        if v in clique_u or clique_u - set(links_v):
            continue
        
        clique_u.add(v)
        for w in links_v:
            links_w = links[w]
            if w not in clique_u and clique_u <= set(links_w):
                clique_u.add(w)
                queue += links_w
    largest_clique = max(clique_u, largest_clique, key=len)
print(",".join(sorted(largest_clique)))
