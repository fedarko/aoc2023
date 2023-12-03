with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

DIGITS = "0123456789"

g2nums = {}
for li, line in enumerate(lines):
    for ci, c in enumerate(line):
        if c == "*":
            g2nums[(ci, li)] = []

print(g2nums)

for li, line in enumerate(lines):
    curr_num_start = None
    curr_num = None

    for ci, c in enumerate(line + "."):
        if c in DIGITS:
            if curr_num is None:
                curr_num = c
                curr_num_start = ci
            else:
                curr_num += c
        else:
            if curr_num is not None:
                # ok, we have a number
                isp = False
                left = max(curr_num_start - 1, 0)
                right = min(ci, len(line) - 1)
                gears = []
                if li > 0:
                    # check spaces above this number
                    for x, oc in enumerate(lines[li - 1][left:right + 1]):
                        if oc not in DIGITS and oc != ".":
                            isp = True
                            if oc == "*":
                                gears.append((x + left, li - 1))
                if li < len(lines) - 1:
                    # check below
                    for x, oc in enumerate(lines[li + 1][left:right + 1]):
                        if oc not in DIGITS and oc != ".":
                            isp = True
                            if oc == "*":
                                gears.append((x + left, li + 1))
                if curr_num_start > 0 and line[left] not in DIGITS and line[left] != ".":
                    isp = True
                    if line[left] == "*":
                        gears.append((left, li))

                if ci < len(line) - 1 and line[right] not in DIGITS and line[right] != ".":
                    isp = True
                    if line[right] == "*":
                        gears.append((right, li))

                if isp:
                    for g in gears:
                        g2nums[g].append(int(curr_num))
                curr_num = None
                curr_num_start = None

grs = 0
for g in g2nums:
    if len(g2nums[g]) == 2:
        grs += (g2nums[g][0] * g2nums[g][1])
print(grs)
