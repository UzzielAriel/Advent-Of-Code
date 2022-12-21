file = [l.strip() for l in open("input.txt").readlines()]

f = lambda sa, sb, ea, eb: (sb <= sa and ea <= eb)

total = 0
total2 = 0

for p in file:
    fr, sr = p.split(",")
    (sa, ea), (sb, eb) = map(int, fr.split("-")), map(int, sr.split("-"))
    if f(sa, sb, ea, eb) or f(ea, eb, sa, sb):
        total += 1
    if sa in range(sb, eb+1) or ea in range(sb, eb+1) or  sb in range(sa, ea+1) or eb in range(sa, ea+1):
       total2 += 1

print(f"Part 1: {total}")
print(f"Part 2: {total2}")