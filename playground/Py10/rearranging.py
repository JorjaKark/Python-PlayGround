def rearrange(l):
    list1 = [x for x in l if x <= 0]
    list2 = [y for y in l if y > 0]
    return list1 + list2
