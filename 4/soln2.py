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

    deck = list(range(1, len(cardnum2wh) + 1))
    i = 0
    while i < len(deck):
        c = deck[i]
        wh = cardnum2wh[c]
        print(c, wh, len(deck))
        matches = len(wh[0] & wh[1])
        won_cardnums = list(range(c + 1, c + 1 + matches))
        for nc in won_cardnums:
            nci = deck.index(nc)
            deck.insert(nci, nc)
        i += 1

print(len(deck))
