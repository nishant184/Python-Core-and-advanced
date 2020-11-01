"""In asbtract class we have to mark the method as abstract class by using
    @abstractmethod"""
from abc  import abstractmethod,ABC
class BMW(ABC):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    def start(self):
        print("Starting a car")

    def stop(self):
        print("Stoping the car")

    #Abstract method
    @abstractmethod
    def drive(self):
        pass

class Threeseries(BMW):
    def __init__(self,cruisecontrolenabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.cruisecontrolenabled=cruisecontrolenabled
    def display(self):
        print(self.cruisecontrolenabled)
    def drive(self):
        print("three series is being driven")


class Fiveseries(BMW):
    def __init__(self,parkingassistenabled,make,model,year):
        super().__init__(make,model,year)#we can use super instead of parent class name and we also wont need to use self
        self.parkingassist=parkingassistenabled
    def drive(self):
        print("five series is being driven")
        

threeseries=Threeseries(True,"BMW","328i","2018")
print(threeseries.cruisecontrolenabled)
print(threeseries.make)
print(threeseries.model)
print(threeseries.year)
#Inheriting the functionality
threeseries.start()
threeseries.stop()
threeseries.display()
threeseries.drive()
fs=Fiveseries(True,"audi","28i","2012")
print(fs.make)