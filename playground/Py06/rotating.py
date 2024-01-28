def rotate_list(l):
    if len(l)<= 3:
        return l
    else:
        first = l[:3]
        rest = l[3:]
        l = rest + first

    return l
