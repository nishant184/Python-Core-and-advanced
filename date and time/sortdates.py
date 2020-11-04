from datetime import *
import time

starttime=time.perf_counter()

ldates = []

d1=date(2016,7,23)
d2=date(2015,7,23)
d3=date(2014,7,23)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()

time.sleep(3)#After using the sleep function the for loop will start working after 3 seconds

for d in ldates:
    print(d)

endtime =  time.perf_counter()
print("execution time",endtime-starttime)