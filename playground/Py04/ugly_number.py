def ugly(n):
    if n == 1:
        boolean = True
    else:
        for x in range(10,1,-1):
            while n != 1 and n >0:
                if x == 2 or x == 3 or x == 5:
                    prime = True
                elif x == 7:
                    prime = False
                else:
                    break

                if n%x == 0 and prime:
                    if x == 5:
                        n = n/5
                    if x == 3:
                        n = n/3
                    if x == 2:
                        n = n/2
                    
                elif n%x == 0 and prime == False:
                    n = -1
                    break
                else:
                    break

            if n == 1:
                boolean = True
                return boolean
            
            else:
                boolean = False

    return boolean
