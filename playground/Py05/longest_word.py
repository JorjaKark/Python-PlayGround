def longest(s):
    list = s.split()
    maior = 0
    for i in list:
        if len(i) > maior :
            maior = len(i)
    return maior
