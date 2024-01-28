def evaluate(a, x):
    polinómio = sum([a[i]*x**i for i in range(len(a))])
    
    return polinómio
