with open("input.txt", "r") as f:
    i = f.read()
val = 0
for line in i.splitlines():
    nums = []
    for c in line:
        if c in "0123456789":
            nums.append(c)
    print(line)
    assert len(nums) >= 1
    val += int(nums[0] + nums[-1])
print(val)
