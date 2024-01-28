from functools import reduce
def map_filter_reduce(lst, f1, f2, f3):
    result =  map(f2, filter(f1, lst))
    return reduce(f3, result)
