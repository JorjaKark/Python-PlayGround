def count_until(tup):
    x = 0
    for n in tup:
        if isinstance(n, tuple):
            return x
        x += 1
    return -1
