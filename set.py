#Sets are denoted by curly braces {}
#Sets does not allow duplicate values which means it does not displays it
s={1,2,3,4,5,1}
print(s)
print(type(s))
s.update([23,44])
print(s)
#print(s[0])#Indexing is not allowed in set type because and also slicing and repetition
s.remove(2)
print(s)

#Frozen set-It does not allow update and remove function 
f=frozenset(s)
print(f)
#f.update([23])