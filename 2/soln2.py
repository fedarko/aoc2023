#! /usr/bin/env python3

gid2draws = {}
with open("input.txt", "r") as f:
    for line in f.readlines():
        colon_idx = line.index(":")
        gid = int(line[5 : colon_idx])
        draws = [d.strip() for d in line[colon_idx + 1:].split(";")]
        gid2draws[gid] = draws

powersum = 0
for gid in gid2draws:
    mins = [0, 0, 0]
    for draw in gid2draws[gid]:
        ccs = draw.split(", ")
        for c in ccs:
            cc = c.split()
            if cc[1] == "red":
                mins[0] = max(int(cc[0]), mins[0])
            elif cc[1] == "green":
                mins[1] = max(int(cc[0]), mins[1])
            elif cc[1] == "blue":
                mins[2] = max(int(cc[0]), mins[2])
            else:
                raise ValueError("bad color:", cc, cc[0], cc[1])
    power = mins[0] * mins[1] * mins[2]
    print(gid2draws[gid], power)
    powersum += power

print(powersum)
