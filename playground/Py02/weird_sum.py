a = int(input())
b= int(input())

result = (a+b)+(a+b)*((a-b)%2 ==0) + (a*b)*((a-b)%2 !=0)

print(result)
