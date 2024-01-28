def solver(a, b, c):
    array = []
    solution1 = ((-b + ((b**2-4*a*c)**(1/2)))/(2*a))
    solution2 = ((-b - ((b**2-4*a*c)**(1/2)))/(2*a))
    solution3 = ((-b)/(2*a))
    if (b**2-4*a*c) > 0:
        array.append(solution1)
        array.append(solution2)
        array.sort()
        
    elif (b**2-4*a*c)==0:
        array.append(solution3)
        
    else:
        pass

    return array 
        
