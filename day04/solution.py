from itertools import product
import re
from time import time


# positive lookahead for overlapping XMAS/SAMX substrings
xmas = re.compile(r'(?=(XMAS|SAMX))')  
mas = re.compile(r'MAS|SAM')


def get_diagonal(schema):
    shifts = [l[shift:] for shift, l in enumerate(schema)]
    diagonal = " ".join("".join(l) for l in zip(*shifts))
    return diagonal


with open("day04/data") as f:
    wordsearch = f.read().splitlines()

Ly = len(wordsearch)
Lx = len(wordsearch[0])


# ==== PART 1 ====
horizontal = " ".join(wordsearch)
vertical = " ".join("".join(l) for l in zip(*wordsearch))

pad = "." * (Lx-1)
padded = [pad + l + pad for l in wordsearch]
diagonal = get_diagonal(padded)
antidiagonal = get_diagonal(padded[::-1])

full_schema = " ".join((horizontal, vertical, diagonal, antidiagonal))
print(len(xmas.findall(full_schema)))


# ==== PART 2 ====
count = 0
for x, y in product(range(1, Lx-1), range(1, Ly-1)):
    if wordsearch[y][x] == "A":
        diagonal = "".join(
            wordsearch[y-1][x-1] + wordsearch[y][x] + wordsearch[y+1][x+1]
        )
        antidiagonal = "".join(
            wordsearch[y-1][x+1] + wordsearch[y][x] + wordsearch[y+1][x-1]
        )
        count += (
            (mas.match(diagonal) and mas.match(antidiagonal)) is not None
        )
print(count)
