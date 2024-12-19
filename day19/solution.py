from functools import lru_cache


@lru_cache
def possible(towel, designs):
    if towel == "":
        return True

    for design in designs:
        if towel.startswith(design) and possible(towel[len(design):], designs):
            return True
        
    return False


@lru_cache
def all_possible(towel, designs):
    if towel == "":
        return True

    possible = False
    for design in designs:
        if towel.startswith(design):
            possible += all_possible(towel[len(design):], designs)
            
    return possible    


with open("day19/data") as f:
    designs, towels = f.read().split("\n\n")

single_designs = tuple(designs.split(", "))


# ==== PART 1 ====
print(sum(possible(towel, single_designs) for towel in towels.splitlines()))


# ==== PART 2 ====
print(sum(all_possible(towel, single_designs) for towel in towels.splitlines()))
