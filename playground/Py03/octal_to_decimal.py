number = str(input())
x= int(len(str(number))-1)
result = 0
valid = True
for n in number:
    n = int(n)
    if n == 8 or n >8:
        print("Not a valid number.")
        valid =False
        break

if valid == True:
    for n in number:
        n = int(n)
        
        
        result = result + n*8**x
        x = x-1
        
    print(result)

