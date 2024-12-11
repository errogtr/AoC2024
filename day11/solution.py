from collections import Counter
from math import floor, log


def count_stones(stones):
    blink = Counter()
    for stone, count in stones.items():
        if stone == 0:
            blink[1] += count
        else:
            digits = floor(log(stone, 10)) + 1
            if digits % 2:  # number of digits is odd
                blink[2024 * stone] += count
            else:  # number of digits is even
                left, right = divmod(stone, 10**(digits // 2))
                blink[left] += count
                blink[right] += count
    return blink       


with open("day11/data") as f:
    stones = Counter(int(x) for x in f.read().split())

# ==== PART 1 ====
for _ in range(25):
    stones = count_stones(stones)
print(stones.total())


# ==== PART 2 ====
for _ in range(50):
    stones = count_stones(stones)
print(stones.total())
