with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

DIGITS = "0123456789"
pns = 0
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
                if li > 0:
                    # check spaces above this number
                    for oc in lines[li - 1][left : right + 1]:
                        if oc not in DIGITS and oc != ".":
                            isp = True
                            break
                if li < len(lines) - 1:
                    # check below
                    for oc in lines[li + 1][left : right + 1]:
                        if oc not in DIGITS and oc != ".":
                            isp = True
                            break
                if not isp:
                    # check the characters to the left and right of the number
                    # (no need to check that the characters are not in DIGITS,
                    # we already know that they aren't -- if they were, then
                    # this would be a different number ;)
                    isp = (curr_num_start > 0 and line[left] != ".") or (
                        ci < len(line) - 1 and line[right] != "."
                    )
                if isp:
                    pns += int(curr_num)
                curr_num = None
                curr_num_start = None
print(pns)
