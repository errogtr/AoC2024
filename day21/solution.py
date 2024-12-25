from collections import Counter, defaultdict
from functools import cache
from itertools import pairwise, product


NUMPAD = {c: (x, y) for c, (y, x) in zip("789456123 0A", product(range(4), range(3))) if c != " "}
KEYPAD = {c: (x, y) for c, (y, x) in zip(" ^A<v>", product(range(2), range(3))) if c != " "}


NN_NUMPAD = {
    "A": "03", "0": "A2",
    "1": "24", "2": "0135", "3": "A26",
    "4": "157", "5": "2468", "6": "359",
    "7": "48", "8": "579", "9": "68",
}


NUMPAD_MOVES = {
    ("A", "A"): "A", ("A", "0"): "<", ("A", "3"): "^",
    ("0", "0"): "A", ("0", "A"): ">", ("0", "2"): "^",
    ("1", "1"): "A", ("1", "2"): ">", ("1", "4"): "^",
    ("2", "2"): "A", ("2", "0"): "v", ("2", "1"): "<", ("2", "3"): ">", ("2", "5"): "^",
    ("3", "3"): "A", ("3", "A"): "v", ("3", "2"): "<", ("3", "6"): "^",
    ("4", "4"): "A", ("4", "1"): "v", ("4", "5"): ">", ("4", "7"): "^",
    ("5", "5"): "A", ("5", "2"): "v", ("5", "6"): ">", ("5", "4"): "<", ("5", "8"): "^",
    ("6", "6"): "A", ("6", "3"): "v", ("6", "5"): "<", ("6", "9"): "^",
    ("7", "7"): "A", ("7", "4"): "v", ("7", "8"): ">",
    ("8", "8"): "A", ("8", "7"): "<", ("8", "5"): "v", ("8", "9"): ">",
    ("9", "9"): "A", ("9", "6"): "v", ("9", "8"): "<",
}


NN_KEYPAD = {
    "A": ">^",
    "^": "vA",
    ">": "vA",
    "v": ">^<",
    "<": "v"
}


KEYPAD_MOVES = {
    ("A", "A"): "A", ("A", ">"): "v", ("A", "^"): "<",
    ("^", "^"): "A", ("^", "A"): ">", ("^", "v"): "v",
    (">", ">"): "A", (">", "A"): "^", (">", "v"): "<",
    ("v", "v"): "A", ("v", "<"): "<", ("v", "^"): "^", ("v", ">"): ">",
    ("<", "<"): "A", ("<", "v"): ">",
}


def manhattan(digit_1, digit_2, keypad):
    x1, y1 = keypad[digit_1]
    x2, y2 = keypad[digit_2]
    return abs(x1 - x2) + abs(y1-y2)


def get_paths(start, target, nn_map, max_length):
    paths = [start]
    final_paths = list()
    while paths:
        path = paths.pop()
        last_digit = path[-1]

        if len(path) == max_length:
            if last_digit == target:
                final_paths.append(path)
            continue

        for next_digit in nn_map[last_digit]:
            paths.append(path + next_digit)
    return final_paths


def get_pad_paths(pad, nn_pad, pad_moves):
    pad_paths = dict()
    for start, target in product(pad, repeat=2):
        max_length = manhattan(start, target, pad) + 1
        pad_paths[(start, target)] = get_paths(start, target, nn_pad, max_length)

    keypad_paths = defaultdict(list)
    for endpoints, paths in pad_paths.items():
        for path in paths:
            keypad_path = "".join(pad_moves[pair] for pair in pairwise(path))
            keypad_paths[endpoints].append(keypad_path + "A")

    return keypad_paths


def complexity(code, keypads_num, mappings):
    @cache
    def expand(counts, depth, max_depth):
        if depth == max_depth:
            return sum(len(path) * count for path, count in counts)

        length = 0    
        for atomic_path, count in counts:
            expansions = [mappings[pair] for pair in pairwise("A" + atomic_path)]
            expansions_counts = [Counter(exp * count) for exp in product(*expansions)]
            length += min(expand(tuple(c.items()), depth + 1, max_depth) for c in expansions_counts)

        return length
    
    min_length = expand(((code, 1),), 0, keypads_num)
    return int(code.strip("A")) * min_length


with open("day21/data") as f:
    codes = f.read().splitlines()


mappings = get_pad_paths(NUMPAD, NN_NUMPAD, NUMPAD_MOVES) | get_pad_paths(KEYPAD, NN_KEYPAD, KEYPAD_MOVES)


# ==== PART 1 ====
print(sum(complexity(code, 3, mappings) for code in codes))

# ==== PART 2 ====
print(sum(complexity(code, 26, mappings) for code in codes))
