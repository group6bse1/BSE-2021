import math #importing module for math to calculate the square root
print("Enter the first point: ")

#entering the first point coordinates
x1=float(input())
y1=float(input())

#entering the second point coordinates
print("Enter the second point: ")
x2=float(input())
y2=float(input())

#formula for computing the distance between the two points
dist=math.sqrt((x2-x1)**2+(y2-y1)**2)

print("The distance from (",x1,",",y1,") to (",x2,",",y2,") is", dist)
