def lost_element(s1, s2):

    count = 0

    for a in s1:
        count = 0
        for b  in s2:
            if a == b:
                break
            else:
                count += 1

                if count == len(s2):
                    return a
    for b in s2:
        count = 0
        for a in s1:
            if a == b:
                break
            else:
                count +=1
                if count == len(s1):
                    return b
    
    my_list2 = list(s2)

    if s1== set():
        my_list2 = list(s2)
        return my_list2[0]

    elif s2 == set():
        my_list1 = list(s1)
        return my_list1[0]
