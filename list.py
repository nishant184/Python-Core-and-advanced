#List starts from index 0
lst=[10,20,"nishant",2,2,1]
print(lst)
print(lst[3])
#slicing in list
print(lst[3:9])
print(len(lst))

#Adding and removings
#Append to add elements in a list
lst.append("mango")
print(lst)
#We use remove function when we want to remove by value
lst.remove("mango")
lst.remove("nishant")
print(lst)
#We use del function when we want to remove by index
del(lst[0])
print(lst)

#List functions
#clear function is used to clear the list
#lst.clear()-commenting out because we want to use the list more
#Max-to get maximum element in a list
print(max(lst))
#Min-to get minimum element in a list
print(min(lst))
#Insert-insert is use to insert a element at a particular position
lst.insert(3,44)
print(lst)
#sort is used to sort the list in ascending order
lst.sort()
print(lst)
#for descending order we use reverse
lst.sort(reverse=True)
print(lst)

