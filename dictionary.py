#Dicitonary is denoted by curly braces and it has key and values
d1={"nishant":22,"sumit":21}
print(d1)

#Items attribute will display all the elements in a dictionary 
print(d1.items())

#Keys attribute will display all the keys
d2=d1.keys()
for i in d2:
    print(i)

#Values attribute will display all the values 
d3=d1.values()
for i in d3:
    print(i)

#We can also access values one at a time
print(d1["sumit"])