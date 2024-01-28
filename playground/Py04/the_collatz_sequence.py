def collatz(n):
    ult = n
    res = str(n)

    while ult > 1:
        if ult % 2 == 0:
            ult = round((ult)/2)
            res = res + "," + str(ult)

        elif (ult % 2) != 0:
            ult = round(ult * 3 + 1)
            res =  res + "," + str(ult)

    return res
