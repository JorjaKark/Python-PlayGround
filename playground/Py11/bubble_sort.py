def bubble_sort(alist):
    n = len(alist)

    for i in range(n):
        for j in range(0, n - i - 1):
            a = alist[j]
            b = alist[j + 1]

            if isinstance(a, str):
               
                char_list_a = list(a)
                char_list_b = list(b)

                for char_a, char_b in zip(char_list_a, char_list_b):
                    if char_a > char_b:
                        
                        alist[j], alist[j + 1] = b, a
                        break
                    elif char_a < char_b:
                       
                        break
            else:
                if b < a:
                   
                    alist[j], alist[j + 1] = b, a

    return alist

