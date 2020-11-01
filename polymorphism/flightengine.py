#Dependency injection
"""Just like if you want to dynamically inject different types of object into another
object we will have to first create an interface called engine then each of the
classes will implement that interface then we can use that interface inside the 
object as a field"""
class flight: 
    def __init__(self,engine):
        self.engine=engine
    
    def startengine(self):
        self.engine.start()

class airbusengine():
    def start(self):
        print("starting air bus engine")

class boinengine():
    def start(self):
        print("starting boinengine ")

ae=airbusengine()
f=flight(ae)
f.startengine()


be=boinengine()
f1=flight(be)
f1.startengine()
