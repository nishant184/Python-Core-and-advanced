"""
   Inheritance is the process of defining a new object using a existing object.
   In inheritance the two key features are accessing the existing objects
   functionality and updating the existing object functionality.
   Two other terms of inheritance are reusability and IS-A realtion.
"""
"""Define a class called BMW with make,model and year as feilds of it,
   and then we will define two more classes which will inherit the fields of
   BMW and it will also contain it own fields
"""
class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    def start(self):
        print("Starting a car")

    def stop(self):
        print("Stoping the car")

class Threeseries(BMW):
    def __init__(self,cruisecontrolenabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.cruisecontrolenabled=cruisecontrolenabled
    def display(self):
        print(self.cruisecontrolenabled)

class Fiveseries(BMW):
    def __init__(self,parkingassistenabled,make,model,year):
        super().__init__(make,model,year)#we can use super instead of parent class name and we also wont need to use self
        self.parkingassist=parkingassistenabled

threeseries=Threeseries(True,"BMW","328i","2018")
print(threeseries.cruisecontrolenabled)
print(threeseries.make)
print(threeseries.model)
print(threeseries.year)
#Inheriting the functionality
threeseries.start()
threeseries.stop()
threeseries.display()

fs=Fiveseries(True,"audi","28i","2012")
print(fs.make)