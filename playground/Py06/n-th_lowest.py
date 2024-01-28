def nth_lowest(lnum, n):
    acc = 1
    while acc<n:
        lnum.remove(min(lnum))
        acc += 1
    return min(lnum)
