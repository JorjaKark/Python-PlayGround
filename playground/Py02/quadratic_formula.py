import math
a = int(input())
b = int (input())
c = int(input())

x = round(((-b - (b**2 - 4*a*c)**(1/2))/(2*a) ),2)
y = round(((-b + (b**2 - 4*a*c)**(1/2))/(2*a) ),2)

print("The solutions are", y, "and", x)
