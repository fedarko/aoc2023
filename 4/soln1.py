with open("input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        data = line.strip().split(": ")
        nums = data[1].split(" | ")
        winning_nums = nums[0].split()
        have_nums = nums[1].split()
        pts = 0
        # do we need to acct for duplicates? assuming not
        for h in have_nums:
            if h in winning_nums:
                if pts == 0:
                    pts = 1
                else:
                    pts *= 2
        total += pts

print(total)
