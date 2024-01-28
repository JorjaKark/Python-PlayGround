import math
angle = int(input("Angle of cannon: "))*math.pi/180
cos_angle = math.cos(angle)
sin_angle = math.sin(angle)
tan_angle = cos_angle / sin_angle
gravitational_acceleration = -10
velocity = 18
fall_distance = -tan_angle/((gravitational_acceleration/2)*(1/(velocity**2)*(1+ tan_angle**2)))
fall_distance_rounded = round(fall_distance)
print(fall_distance_rounded)
