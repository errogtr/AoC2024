import re

MUL = "mul"
DO = "do()"

mul = re.compile(r"mul\((\d+),(\d+)\)")
dodontmul = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)")


with open("day03/data") as f:
    memory = f.read()

# ==== PART 1 ====
print(sum(int(x) * int(y) for x, y in mul.findall(memory)))


# ==== PART 2 ====
s = 0
curr = DO
for op in dodontmul.finditer(memory):
    if op.group().startswith(MUL):
        s += (curr == DO) * int(op.group(1)) * int(op.group(2))
    else:
        curr = op.group()
print(s)
