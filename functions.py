"""We are going to create our own functions it this programs,
   a function is a group of statements that will perform a particular task.
   Advantages of function mainly are three
   1.Reusable
   2.Modularity
   3.Maintenance
"""
#To calculate average of two numbers
#We use def to create a user-defined function

def average(a,b):
    return ((a+b)/2)
#to return a result of a function we use return statement
print("The average of the numbers are",average(10,20))

#Return multiple values
def calc(a,b):
    x=a+b
    y=a-b
    z=a*b
    u=a/b
    return x,y,z,u

print(calc(5,4))

#Function inside another function
def display(name):
    def message():
        return "Hello "
    result=message()+name
    return result
print(display("Nishant"))

#Returning functions
def display1():
    def message1():
        return "Hello "
    return message1
func1=display1()
print(func1())