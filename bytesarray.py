lst=[20,30,40,50]
print(type(lst))
#To convert it into bytes type we use byte attribute
b=bytes(lst)
print(type(b))
#Bytes does not support item assignment

b1=bytearray(lst)
print(type(b1))
b1[2]=12
#We cannot perform indexing and slicing operations on byte or bytearray
#But we can modify bytearray