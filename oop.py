#1st python class called product which will have three variables name,description,price
class Product:
    def __init__(self):
        self.name = 'Iphone'
        self.description = 'Its expensive'
        self.price = '700$'

    #Define instance methods
    def display(self):
        print(self.name)
        print(self.price)
        print(self.description)

p1 = Product()
p1.display()


#Using parameterized constructor
#Create a class Course and its instances will be name and ratings
class Course: 
    def __init__(self,name,ratings):#This is parametrized constructor
        self.name=name#You can also name it as self.n=name ,same for ratings
        self.ratings=ratings

    def average(self):
        numberofratings= len(self.ratings)
        average=sum(self.ratings)/numberofratings
        print("average ratings for ",self.name," is ",average)

c1=Course('Python course',[1,2,3,4,5])
print(c1.name)
print(c1.ratings)
c1.average()

c2=Course('Java Course',[5,5,5,5,5])
print(c2.name)
print(c2.ratings)
c2.average()


#Immitater and accessor Method i.e setter and getter
#Create a class programmer with three fields name,salary,technologies
class Programmer:
    def setname(self,n):
        self.name=n
    def getname(self):
        return self.name
    def setsalary(self,sal):
        self.salary=sal
    def getsalary(self):
        return self.salary
    def settechnologies(self,techs):
        self.technologies=techs
    def gettechnologies(self):
        return self.technologies

p1=Programmer()
p1.setname("Nishant")
p1.setsalary(10000)
p1.settechnologies(["Java","hibberrate","spring","Python"])

print(p1.getname())
print(p1.getsalary())
print(p1.gettechnologies())


#Define static field
#to define a static a field you simply define it in the class 
#and to access it unlike instances you dont need an object you can call it simply using the class name
class student:
    major='CSE' #the static field

    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name

s1=student(1,'Nishant')
s2=student(2,'Sumit')
print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(student.major)