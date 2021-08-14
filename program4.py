import math
side1 = 5
side2 =6
side3=8

#we need to find the semi perimeter

semi = (side1+side2+side3)/2

print(semi)
var1 = semi*(semi-side1)*(semi-side2)*(semi-side3)
print(var1)
area = math.sqrt(var1)
print(area)