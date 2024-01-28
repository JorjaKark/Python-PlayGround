text = str(input())
num = int(input())

if num != 1 :
    for x in range(num - 1):
        print(text, end = "-")
    print (text)

else:
    print(text)

