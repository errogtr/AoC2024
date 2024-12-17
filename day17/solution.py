from copy import copy
from itertools import batched
import re


COMBO = dict(enumerate([0, 1, 2, 3, "A", "B", "C", 7]))


def exec(registers):
    i = 0
    output = list()
    while i < len(intructions):
        operator, operand = intructions[i : i + 2]
        combo = registers.get(COMBO[operand], operand)
        match operator:
            case 0:  # adv
                registers["A"] //= 2**combo
            case 1:  # bxl
                registers["B"] ^= operand
            case 2:  # bst
                registers["B"] = combo % 8
            case 3:  # jnz
                if registers["A"]:
                    i = operand
                    continue
                else:
                    pass
            case 4:  # bxc
                registers["B"] ^= registers["C"]
            case 5:  # out
                output.append(combo % 8)
            case 6:  # bdv
                registers["B"] = registers["A"] // (2**combo)
            case 7:  # cdv
                registers["C"] = registers["A"] // (2**combo)
        i += 2
    return output


with open("day17/data") as f:
    registers, program = f.read().split("\n\n")
    r = {x: int(y) for x, y in re.findall(r"([ABC]): (\d+)", registers)}
    intructions = [int(x) for x in re.findall(r"\d+", program)]


# ==== PART 1 ====
print(",".join(map(str, exec(copy(r)))))


# ==== PART 2 ====
operand = next(y for x, y in batched(intructions, 2) if x == 0)
factor = 2 ** COMBO[operand]
i, n = 0, 0
while True:
    output = exec(copy(dict(r, A=i)))
    truncated = intructions[-n - 1 :]
    if output == truncated:
        if n == len(intructions) - 1:
            break
        n += 1
        i *= factor
    else:
        i += 1
print(i)
