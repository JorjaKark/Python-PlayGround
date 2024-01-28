def fib(n):
    list = []
    if n == 1:
        list.append(0)
        return list
    elif n == 2:
        list.append(1)        
        return list
    else:
        list = [0,1]
        while len(list)<n:
            list.append(list[-1] + list[-2])
    return list
