import math
a = input()
b = input()

array = [a,b]
array = [int(x) for x in array]

t =(array[1]/60 + array[0])
velocity = round(313/t)

print(velocity)
