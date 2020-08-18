#THe syntax for lambda expression is
#lambda argument_list:expression
#Unlike functions lambda will always return a function back
"""lambda expression are very helpful and can be used in other functions 
   to for eg, filter,map,reduce
"""
#Calculate cube of a given number
def cube(n):
    return n**3
print(cube(3))

#Lambda expression
f=lambda n:n**3
print(f(4))

#Create a lambda expression that will give odd or even number
a=lambda x:"YES" if x%2==0 else 'NO'
print(a(20))
print(a(55))

#Sum of two numbers
"""def add(a,b):
    return a+b
print(add(10,20))"""

l=lambda a,b: a+b
print(l(20,30))

