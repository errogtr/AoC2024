from itertools import product
import re

xmas = re.compile(r'(?=(XMAS|SAMX))')
mas = re.compile(r'(?=(MAS|SAM))')


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
directions = [
    [(0, 0), (1, 1), (2, 2)], # 3x3 block diagonal
    [(0, 2), (1, 1), (2, 0)], # 3x3 block antidiagonal
]
count = 0
for x, y in product(range(Lx-2), range(Ly-2)):
    diagonals = [
        "".join(wordsearch[y + dy][x + dx] for dx, dy in d) for d in directions
        ]
    count += all(mas.match("".join(l)) is not None for l in diagonals)
print(count)
