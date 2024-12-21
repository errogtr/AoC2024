from tqdm import tqdm


DIRS = [-1j, 1, -1, 1j]


def manhattan(z, w):
    return abs(z.real - w.real) + abs(z.imag - w.imag)


def get_neighborhood(z, min_pico, max_pico):
    queue = [z]
    visited = {z}
    neighborhood = set()
    while queue:
        w = queue.pop(0)
        for dw in DIRS:
            next_w = w + dw
            dist = manhattan(z, next_w)
            if next_w not in visited and dist <= max_pico:
                queue.append(next_w)
                visited.add(next_w)
                if dist >= min_pico:
                    neighborhood.add(next_w)
    return neighborhood


def cheat(track_points, neighbors):
    cheats = 0
    for z, pico in tqdm(regular_track.items()):
        for w in neighbors[z] & track_points:
            save = regular_track[w] - regular_track[z] - manhattan(z, w)
            if regular_track[w] > pico and save >= 100:
                cheats += 1
    return cheats


racetrack = dict()
with open("day20/data") as f:
    for y, row in enumerate(f.read().splitlines()):
        for x, val in enumerate(row):
            racetrack[x + y * 1j] = val


start = next(z for z, val in racetrack.items() if val == "S")
end = next(z for z, val in racetrack.items() if val == "E")

# get regular track
pico = 0
regular_track = {start: pico}
curr_z = start
while curr_z != end:
    for z in get_neighborhood(curr_z, 1, 1):
        if racetrack[z] in ".E" and z not in regular_track:
            pico += 1
            regular_track |= {z: pico}
            curr_z = z
            break


# ==== PART 1 ====
neighbors = {z: get_neighborhood(z, 2, 2) for z in regular_track}
print(cheat(set(regular_track), neighbors))


# ==== PART 2 ====
neighbors = {z: get_neighborhood(z, 2, 20) for z in tqdm(regular_track)}
print(cheat(set(regular_track), neighbors))