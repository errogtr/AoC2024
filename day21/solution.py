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
    ("A", "0"): "<", ("A", "3"): "^",
    ("0", "A"): ">", ("0", "2"): "^",
    ("1", "2"): ">", ("1", "4"): "^",
    ("2", "0"): "v", ("2", "1"): "<", ("2", "3"): ">", ("2", "5"): "^",
    ("3", "A"): "v", ("3", "2"): "<", ("3", "6"): "^",
    ("4", "1"): "v", ("4", "5"): ">", ("4", "7"): "^",
    ("5", "2"): "v", ("5", "6"): ">", ("5", "4"): "<", ("5", "8"): "^",
    ("6", "3"): "v", ("6", "5"): "<", ("6", "9"): "^",
    ("7", "4"): "v", ("7", "8"): ">",
    ("8", "7"): "<", ("8", "5"): "v", ("8", "9"): ">",
    ("9", "6"): "v", ("9", "8"): "<",
}


NN_KEYPAD = {
    "A": ">^",
    "^": "vA",
    ">": "vA",
    "v": ">^<",
    "<": "v"
}


KEYPAD_MOVES = {
    ("A", ">"): "v", ("A", "^"): "<",
    ("^", "A"): ">", ("^", "v"): "v",
    (">", "A"): "^", (">", "v"): "<",
    ("v", "<"): "<", ("v", "^"): "^", ("v", ">"): ">",
    ("<", "v"): ">",
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
        if start != target:
            max_length = manhattan(start, target, pad) + 1
            pad_paths[(start, target)] = get_paths(start, target, nn_pad, max_length)
        else:
            pad_paths[(start, target)] = ["A"]

    keypad_paths = defaultdict(list)
    for endpoints, paths in pad_paths.items():
        for path in paths:
            keypad_path = ""
            for x, y in pairwise(path):
                keypad_path += pad_moves[(x, y)]
            keypad_paths[endpoints].append(keypad_path + "A")

    return(keypad_paths)

@cache
def expand(counts, depth, max_depth):
    if depth == max_depth:
        return sum(len(path) * count for path, count in counts)

    paths_counter = Counter({pair: count for pair, count in counts})

    length = 0    
    for atomic_path, count in paths_counter.items():
        expansions = list()
        for pair in pairwise("A" + atomic_path):
            expansions.append(mappings[pair])
        expansions_counts = [Counter(exp * count) for exp in product(*expansions)]
        length += min(expand(tuple(counter.items()), depth + 1, max_depth) for counter in expansions_counts)

    return length


with open("day21/data") as f:
    codes = f.read().splitlines()


mappings = get_pad_paths(NUMPAD, NN_NUMPAD, NUMPAD_MOVES) | get_pad_paths(KEYPAD, NN_KEYPAD, KEYPAD_MOVES)


complexity = 0
for code in codes:
    keypad_expansions = [mappings[pair] for pair in pairwise("A" + code)]
    keypad_counters = [Counter(p) for p in product(*keypad_expansions)]
    min_length = min(expand(tuple(counter.items()), 1, 26) for counter in keypad_counters)
    complexity += int(code.strip("A")) * min_length
print(complexity)
