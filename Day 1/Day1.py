file = open("input.txt", "r").readlines()

total = 0

groups: [[int], ...] = [[]]

# print(file)

c = 0

for idx, val in enumerate(file):
    if val == "\n":
        groups.append([])
        c += 1
        continue
    groups[c].append(int(val))

# print(groups)

tmp = 0
sums = []

for arr in groups:
    sums.append(sum(arr))
    if sum(arr) > tmp:
        tmp = sum(arr)

print(f"Part 1: {tmp}")
print(f"Part 2: {sum(sorted(sums)[-1:-4:-1])}")

file.close()
