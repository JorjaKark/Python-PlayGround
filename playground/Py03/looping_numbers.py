def is_looping_number(n):
   
    if n < 10:
        return True
    
    n_str = str(n)
    for i in range(1, len(n_str)):
        diff = abs(int(n_str[i]) - int(n_str[i-1]))
        if diff != 1 and not (n_str[i] == '0' and n_str[i-1] == '9'):
            return False

    return True

n = int(input("Enter a number: "))

if is_looping_number(n):
    print("Looping number")
else:
    print("Not a looping number")

