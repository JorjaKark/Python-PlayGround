def is_prime(x):

    flag = True
    for s in range(2, x-1):
        if x%s == 0:
            flag = False
        else:
            pass
    return flag
