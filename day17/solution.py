from itertools import count
import re


with open("day17/data") as f:
    registers, program = f.read().split("\n\n")
    r = {x: int(y) for x, y in re.findall(r"([ABC]): (\d+)", registers)}
    intructions = [int(x) for x in re.findall(r"\d+", program)]

COMBO = dict(enumerate([0, 1, 2, 3, "A", "B", "C", 7]))
i = 0
output = list()
while i < len(intructions):
    operator, operand = intructions[i:i+2]
    combo = r.get(COMBO[operand], operand)
    match operator:
        case 0:  # adv
            r["A"] //= 2 ** combo
        case 1:  # bxl
            r["B"] ^= operand
        case 2:  # bst 
            r["B"] = combo % 8
        case 3:  # jnz
            if r["A"]:
                i = operand
                continue
            else:
                pass
        case 4:  # bxc
            r["B"] ^= r["C"]
        case 5:  # out
            output.extend(list(str(combo % 8)))
        case 6:  # bdv
            r["B"] = r["A"] // (2 ** combo)
        case 7:  # cdv
            r["C"] = r["A"] // (2 ** combo)
    i += 2
print(",".join(output))
