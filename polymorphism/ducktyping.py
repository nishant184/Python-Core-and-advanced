"""Duck typing is not a feature that programming language offers but it comes for 
free if the programming language is free if it is dynamic """
class Duck:
    def talk(self):
        print("quack quack")

class human:
    def talk(self):
        print("hello")

def calltalk(obj):
    obj.talk()

d=Duck()
calltalk(d)

h=human()
calltalk(h)