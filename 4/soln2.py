with open("input.txt", "r") as f:
    cardnum2ct = {}
    cardnum2wh = {}
    for line in f.readlines():
        data = line.strip().split(": ")
        cardnum = int(data[0].split()[1])
        nums = data[1].split(" | ")
        winning_nums = nums[0].split()
        have_nums = nums[1].split()
        cardnum2wh[cardnum] = (set(winning_nums), set(have_nums))
        cardnum2ct[cardnum] = 1

    for c in list(range(1, len(cardnum2wh) + 1)):
        wh = cardnum2wh[c]
        matches = len(wh[0] & wh[1])
        won_cardnums = list(range(c + 1, c + 1 + matches))
        for nc in won_cardnums:
            cardnum2ct[nc] += cardnum2ct[c]

print(sum(cardnum2ct.values()))
