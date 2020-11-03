import logging
#Demo
try:
    a,b=[int(x) for x in input("ENter two numbers").split()]
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero number")
else:#else block is executed when there is no exception raised
    print("You have entered a non zero number")
finally:
    print("finally block is executed if the exception is raised or not") 


#Logging demo
logging.error("Error")
logging.critical("Critical")
logging.warn("warning")

#Assertdemo
num=int(input("Enter a even number"))
assert num%2==0,"You have entered an odd number"

#Assertion using try except
try:
    num=int(input("Enter a even number"))
    assert num%2==0,"You have entered an odd number"
except AssertionError as obj:
    print(obj)

print("After assertion")