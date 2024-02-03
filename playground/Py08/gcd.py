def gcd_rec(n1, n2):
    if n1%n2 == 0:
        return n2
    
    else:
        return gcd_rec(n2, n1%n2)
