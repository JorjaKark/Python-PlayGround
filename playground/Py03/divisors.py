num = int(input())

divisor = 1
final = 0

while divisor <= num :
    if num%divisor == 0:
        final =  final + divisor
        divisor = divisor + 1
    else:
        divisor = divisor + 1
        
print(final)

