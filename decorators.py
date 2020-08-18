#Decorators is a function that performs additional logic to a function
#It also returns the function back as a result

#Create a decorator function that will return the doubles the number entered
def decor(fun):
    def inner():
        result=fun()
        return result*2
    return inner

#Commenting out for the use of @ decorator
"""def num():
    return 5

resultfun=decor(num)
print(resultfun())
"""
#We can also use another way to use decorator 
#just put @ symbol with the function name for eg,
@decor
def num():
    return 5

print(num())



