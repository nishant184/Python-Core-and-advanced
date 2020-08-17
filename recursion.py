"""Recursion is process of calling a function itself
   a good example is a factorial of a number,
   Recursion can be used whenever same logic is repeated
   problems like traversing binary trees are good candidate for 
   recursion,apply caution while using recursion.
   For recursion the very first important step is to come up 
   with a condition when the recusrsive call should stop if not
   then the application will run in an infinite loop
"""
#Factorial of a number
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print(factorial(5))