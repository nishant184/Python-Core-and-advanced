import sys
lst=sys.argv
for i in lst:
    print(i)
print(len(lst))

#Keyword arguments
#average
def average(a,b):
    return (a+b)/2

print(average(b=10,a=20))