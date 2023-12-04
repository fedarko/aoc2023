with open("ex.txt", "r") as f:
    total = 0
    lines = f.readlines()
    cardnum2wh = {}
    for line in lines:
        data = line.strip().split(": ")
        cardnum = int(data[0].split()[1])
        nums = data[1].split(" | ")
        winning_nums = nums[0].split()
        have_nums = nums[1].split()
        cardnum2wh[cardnum] = (set(winning_nums), set(have_nums))

    table = [(c, cardnum2wh[c]) for c in range(1, len(cardnum2wh) + 1)]
    li = 0
    while li < len(table):
        c, wh = table[li]
        print(c, wh)
        matches = len(wh[0] & wh[1])
        won_cardnums = list(range(c + 1, c + 1 + matches))
        table = (
            table[:li + 1] + [(nc, cardnum2wh[nc]) for nc in won_cardnums] + table[li + 1:]
        )
        li += 1

print(len(table))
