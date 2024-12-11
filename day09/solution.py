from itertools import batched


with open("day09/data") as f:
    diskmap = f.read()

free_space, files = list(), list()
for i, c in enumerate(diskmap):
    if i % 2:
        free_space.append(int(c))
    else:
        files.append(int(c) * chr(i // 2 + 48))


# ==== PART 1 ====
fragmented = ""
while files:
    fragmented += files.pop(0)
    free_slot = free_space and free_space.pop(0)
    while free_slot:
        last = files[-1]
        l = len(last)
        if l <= free_slot:
            fragmented += files.pop()
            _ = free_space.pop()
        else:
            fragmented += last[:-free_slot-1:-1]
            files[-1] = last[:-free_slot]
        free_slot = max(0, free_slot - l)
print(sum(i * (ord(c) - 48) for i, c in enumerate(fragmented)))


# ==== PART 2 ====
# (ID, len, space)
disk = list()
for id, batch in enumerate(batched(diskmap, 2)):
    if len(batch) == 2:
        l, slot = batch
    else:
        l, slot = batch[0], 0
    disk.append([id, int(l), int(slot)])

i = len(disk) - 1
checked = set()
while i > 0:
    for j in range(i):
        id_i, size_i, slot_i = disk[i]
        if id_i in checked:
            continue
        id_j, size_j, slot_j = disk[j]
        if size_i <= slot_j:
            _ = disk.pop(i)
            disk.insert(j+1, [id_i, size_i, slot_j - size_i])
            disk[j] = [id_j, size_j, 0]
            disk[i][2] += size_i + slot_i
            break
    else:
        i -= 1
    checked.add(id_i)
    
checksum = 0
i = 0
for id, size, slot in disk:
    checksum += sum(id * j for j in range(i, i+size))
    i += size + slot
print(checksum)
