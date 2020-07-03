s=str(input("Enter the string:"))#how to input a string 
quiz='MyCaptain'
quiz2='Aye'
print(str.upper(quiz))#capitalize whole string 
print(str.lower(quiz))#lower case whole string 
print(quiz[0])
print(quiz[-9])
print(quiz[3:-2])#position from 3 to -2 (goes to the number after -2 (rhs to lhs))
print(quiz+'12')#to add stuff to string 
print(str.capitalize(quiz))#to make the first letter capital 
#0   1  2  3  4  5  6  7 8
#M   y  C  a  p  t  a  i n
#-9 -8 -7 -6 -5 -4 -3 -2 -1 

a="Oh"
b="Baby when you talk like that"
c="You make"
d="A woman go mad"
print(a,b,c,d)
print(a)
print(b)
print(c)
print(d)
print("\n")

#tuples:A collection of items which cannot be modified
a=(1,'lady',5,'gaga')
print(a)
print(a[1],a[3])
print(a[1])
print(a[0])#position always starts from zero like arrays
print("\n")

#list:Also a collection of items but can be modified 
a=[1,'SNSD',30,'Gee']
print(a)
print(a[1],a[3])
a[3]="Mr. Mr."
print(a[1],a[3])

#isalpha(): if all the characters are alphabets in the string then fucntion returns "True" otherwise "False"
































