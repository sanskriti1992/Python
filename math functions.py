#math functions
#1.rounding 
import math 
a=2 
b=1.414
print("The addition is: ",round(a+b,2))
print("\n")

#2.factorial
c=input("Enter the value: ")
print("The factorial is ",math.factorial(int(c)))

#area of any shape
#method1
import math
radius=float(input("Enter the radius of the circle:"))
area=math.pi*(radius**2)
print("Area of circle is:")
print(round(area,2))

#method2
r=float(input("Enter the radius:"))
pi=3.14
area=pi*(r**2)
print("Area of circle is:")
print(area)



