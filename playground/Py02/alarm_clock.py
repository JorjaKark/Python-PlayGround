hour = int(input())
min = int(input())

hour = hour * 60
hour_total = hour + min

alarm = hour_total + 411
 
alarm_converted = [int(alarm/60), alarm%60]

if alarm_converted[0] >= 24:
    alarm_converted[0] = alarm_converted[0]-24


if alarm_converted[0] < 10 and alarm_converted[1] < 10:
        print("0"+ str(alarm_converted[0]) + ":" + "0" + str(alarm_converted[1]))
    
elif (alarm_converted[0] < 10 and alarm_converted[1] > 10):
        print( "0"+ str(alarm_converted[0])+":"+ str(alarm_converted[1]))

elif ( alarm_converted[1] < 10 and alarm_converted[0] > 10):
        print(str(alarm_converted[0])+":"+"0"+ str(alarm_converted[1]) )

else:
        print(str(alarm_converted[0])+ ":"+str(alarm_converted[1]))
