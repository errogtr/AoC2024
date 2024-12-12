from collections import Counter
from math import log10


def count_stones(stones):
    blink = Counter()
    for stone, count in stones.items():
        if stone == 0:
            blink[1] += count
        elif (digits := int(log10(stone)) + 1) % 2 == 0:
            # number of digits is even  
            left, right = divmod(stone, 10**(digits // 2))
            blink[left] += count
            blink[right] += count
        else:  # number of digits is odd
            blink[2024 * stone] += count
    return blink       


with open("day11/data") as f:
    stones = Counter(int(x) for x in f.read().split())

# ==== PART 1 & 2 ====
for n in (25, 50):
    for _ in range(n):
        stones = count_stones(stones)
    print(stones.total())
