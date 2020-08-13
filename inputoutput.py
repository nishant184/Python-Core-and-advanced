name="nishant"
marks=45.5
print("name is ",name,"marks are ",marks)
#anothe way is
print("Name is %s marks are %d"%(name,marks))
#another way is by placeholders
#print("name is {},marks are{}",format(name,marks))

#Input function
s=input()
print(s)
s1=input("Enter your name")
print(s1)
#Input function considers all the inputs as string types  you need to convert it into some other type which you want it to be
i=int(input("Enter an integer number"))
print(i)

#Reading multiple inputs
#Use split function for multiple inputs
lst=[int(x) for x in input("Enter three numbers by space").split()]
print(lst)