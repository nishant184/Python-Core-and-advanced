x=123   #This is a global  variable
def display(x):
    print(x)
display(x)

def display1():
    b=345   #This is local variable
    print(b)
display1()

#Accessing global variables by same name
#Use globals function to call same name variables

#Assign function to a variable
y=display
y(x)