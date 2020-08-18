"""List Comprehensions help us a easy to use syntax for creating one list
   from other using some logic
   Syntax for list comprehension is
   l=[expression for item in itearble if  condition]
"""
#Cubes of numbers from 1 to 10
#This is normal programming
"""lst=[]
for x in range(1,11):
    lst.append(x**3)
print(lst)"""

#Using list comprehension
lst=[]
lst=[x**3 for x in range(1,11)]
print(lst)

#Even numbers in a list
"""l1=[x for in range(2,20,2)]
print(l1)"""
#Without using third parameter
l2=[x for x in range(2,20) if x%2==0]
print(l2)

#Product of numbers in a list
a=[1,2,4,5]
b=[2,3,1,2]

"""z=[]
for i in range(len(a)):
    z.append(a[i]*b[i])
print(z)"""
#Now by using list comprehension
z=[a[i]*b[i] for i in range(len(a))]
print(z)