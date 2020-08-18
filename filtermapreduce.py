from functools import reduce

#Using filter to retrieve only even numbers from a given list
lst=[10,20,51,3]
result=list(filter(lambda x: x%2==0,lst))#We need to convert filter into list or else it will show it as a filter object
print(result)

#Map function
#Using map function to double the value of each element in the list
l1=[1,2,3,5,4]
res=list(map(lambda n: n*2,l1))#We need to convert filter into list or else it will show it as a filter object
print(res)

#Reduce function
#Sum of all elements in a list using reduce function
#To use reduce function it is inside a module called functool
l2=[2,3,21,1]
res2=reduce(lambda x,y: x+y,l2)
print(res2)