#Generators are functions that returns a sequence of value pack
"""Generators function is used like just any other function but it uses yield
   statement"""

def customgen(x,y):
    while x<y:
        yield x
        x+=1

result=customgen(10,20)

for i in result:
    print(i)

