gid2draws = {}
with open("input.txt", "r") as f:
    for line in f.readlines():
        colon_idx = line.index(":")
        gid = int(line[5 : colon_idx])
        draws = [d.strip() for d in line[colon_idx + 1:].split(";")]
        gid2draws[gid] = draws

REDMAX = 12
GREENMAX = 13
BLUEMAX = 14

possible_gid_sum = 0
for gid in gid2draws:
    possible = True
    for draw in gid2draws[gid]:
        ccs = draw.split(", ")
        for c in ccs:
            cc = c.split()
            if cc[1] == "red":
                if int(cc[0]) > REDMAX:
                    possible = False
                    break
            elif cc[1] == "green":
                if int(cc[0]) > GREENMAX:
                    possible = False
                    break
            elif cc[1] == "blue":
                if int(cc[0]) > BLUEMAX:
                    possible = False
                    break
            else:
                raise ValueError("bad color:", cc, cc[0], cc[1])
    if possible:
        possible_gid_sum += gid

print(possible_gid_sum)
