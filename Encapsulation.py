"""
   Encapsulation is about protecting the properties and the functionalities
   of an object from other objects another definition is writing the data
   or code in one single unit
"""
"""
   How to mark a field as private and also learn about name mangling which 
   means we can access the private field through objects
"""
class Student:
    def __init__(self):
        self.__id=123         #To make this two fields private we just need 
        self.__name="Nishant" #to use  __(two underscores) 
                              #now it will not show the id and name
    def display(self):#To display the private we have created this function
        print(self.__id)
        print(self.__name)


s = Student()
#print(s.id)  
#print(s.name)
s.display() #you can only access the private field using the methods of that object
#You can aslo use name mangling to access the private field 
print(s._Student__id)#This is name mangling
"""Syntax for Name Mangling is:
        object_name._classname__fieldname
"""
#Implementing encapsulation
class Student1:
    def setid(self,id):
        self.id=id
    def getid(self):
        return self.id
    
    def setname(self,name):
        self.name=name
    def getname(self):
        return self.name

s1 = Student1()
s1.setid(64)
s1.setname("Nishant")
print(s1.getid())
print(s1.getname())
#This is how encapsultion is done in OOP by using immitator and accessor method
#setid(setter) is immitator and getid is accessor(getter)

