class Overthelimit(Exception):
    def _init_(self,msg):
        self.msg=msg


#to create a custom exception lets create a function 

def withdraw(amount):
    if(amount>10000):
        raise Overthelimit("You can not withdraw over 10000 per day")

withdraw(100001)
