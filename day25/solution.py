from itertools import combinations, product


with open("day25/data") as f:
    schematics = f.read().split("\n\n")

keys, locks = [], []
for schematic in schematics:
    rows  = schematic.split()
    first_row, *_ = rows
    if first_row.count("#") == 0:
        keys.append(rows)
    else:
        locks.append(rows)

valid = 0
unique_pairs = set()
for k, l in product(range(len(keys)), range(len(locks))):
    if (k, l) in unique_pairs:
        continue

    unique_pairs.add((k, l))
    key = keys[k]
    lock = locks[l]
    
    Ly = len(key)
    for col_k, col_l in zip(zip(*key), zip(*lock)):
        if "".join(col_k).count("#") + "".join(col_l).count("#") > Ly:
            break
    else:
        valid += 1

print(valid)