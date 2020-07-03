#to find whether triangle is equilateral,scalene or isosceles
a=float(input("Enter the value of first side:"))
b=float(input("Enter the value of second side:"))
c=float(input("Enter the value of third side:"))
if a==b==c:
    print("It is an equilateral triangle.")
elif a==b!=c or a==c!=b or b==c!=a:
    print("It is an isosceles triangle.")
elif a!=b!=c:
    print("It is a scalene triangle.")
else:
    print("Error")
    
#To convert months to number of days
print("List:January,February,March,April,May,June,July,August,Septemebr,November,December")
month_name=input("Enter the month:")
if month_name=="February":
    print("No. of days:28/29 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("No. of days:31 days")
elif month_name in ("April", "June", "September", "November"):
    print("No. of days:30 days")
else:
    print("Wrong name")