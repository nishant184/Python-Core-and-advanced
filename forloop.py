"""For loop is used to iterate etc
   It is same as while loop
"""
#to print numbers from 50 to 70
for i in range(50,70):
    print(i)

#product of numbers in a list
lst=[12,2,3,4,4]
prod=1
for i in lst:
    prod=prod*i
print(prod)

#Multiplication table of a given number
a=int(input("Enter a number whose table you want to display"))
for i in range(1,11):
    print(a,'X',i,'=',a*i)