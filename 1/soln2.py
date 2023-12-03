#! /usr/bin/env python3
DIGITS = "0123456789"
WORDS = [
    "zero", "one", "two", "three", "four", "five", "six", "seven",
    "eight", "nine"
]
w2d = {w: d for w, d in zip(WORDS, DIGITS)}

with open("input.txt", "r") as f:
    i = f.readlines()

val = 0
for line in i:
    nums = []
    for ci, c in enumerate(line):
        if c in DIGITS:
            nums.append(c)
        else:
            for w in WORDS:
                if line[ci:].startswith(w):
                    nums.append(w2d[w])
                    break
    assert len(nums) >= 1
    val += int(nums[0] + nums[-1])

print(val)
