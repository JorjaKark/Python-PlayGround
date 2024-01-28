first = int(input())
second = int(input())
third = int(input())
fourth = int(input())
grade = 0
if first < 0 or first >100 or second <0 or second >100 or third<0 or third>100 or fourth<0 or fourth>100:
    print("Input error")
elif (third<40) or (fourth<40):
    print("RFF")
else:
    grade = (first + second + 13*third + 5*fourth)/100
    if (grade*10)%10 == 5:
        grade = ((grade*10)-5)//10
        print(grade)
    else:
        grade = round(grade)
        print(grade)
