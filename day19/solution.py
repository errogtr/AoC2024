from functools import lru_cache


@lru_cache
def is_possible(towel, designs):
    if towel == "":
        return True

    for design in designs.split(", "):
        if towel.startswith(design) and is_possible(towel[len(design):], designs):
            return True
    return False


@lru_cache
def all_possible(towel, designs):
    if towel == "":
        return 1

    possible = 0
    for design in designs.split(", "):
        if towel.startswith(design):
            possible += all_possible(towel[len(design):], designs)
            
    return possible    



with open("day19/data") as f:
    designs, towels = f.read().split("\n\n")


# ==== PART 1 ====
print(sum(is_possible(towel, designs) for towel in towels.splitlines()))


# ==== PART 2 ====
print(sum(all_possible(towel, designs) for towel in towels.splitlines()))
