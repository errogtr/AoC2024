import re
from operator import and_, or_, xor


OP_PATTERN = re.compile(r"(\w+) (AND|OR|XOR) (\w+)")
OPS = {"AND": and_, "OR": or_, "XOR": xor}

def solve(res, inputs, ops_results):
    x, op, y = OP_PATTERN.search(ops_results[res]).groups()
    
    if x in inputs and y in inputs:
        return OPS[op](int(inputs[x]), int(inputs[y]))

    res =  OPS[op](solve(x, inputs, ops_results), solve(y, inputs, ops_results))
    return res


with open("day24/data") as f:
    inputs_raw, ops = f.read().split("\n\n")


# ==== PART 1 ====
ops_results = dict(reversed(op.split(" -> ")) for op in ops.split("\n"))
inputs = dict(inp.split(": ") for inp in inputs_raw.split("\n"))
outputs = sorted(n for n in ops_results if n.startswith("z"))
z_bin = "".join(str(solve(n, inputs, ops_results)) for n in reversed(outputs))
print(int(z_bin, 2))


# ==== PART 2 ====
""" PEN AND PAPER
qjj <-> gjc 
wmp <-> z17
gvm <-> z26
qsb <-> z39
"""