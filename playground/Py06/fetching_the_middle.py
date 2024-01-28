def fetch_middle(llists):
    a = []
    for i in llists:
        if len(i)% 2 == 0:
            m = i[len(i)//2]
            l = i[(len(i)//2)-1]
            x = (m+l)/2
            a.append(x)
            
        else:
            n = len(i)//2
            a.append(i[n])
           
    return a
