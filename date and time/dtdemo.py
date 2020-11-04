import time,datetime
epochseconds = time.time()
print(epochseconds)

#To convert epochseconds into current time is given below
t=time.ctime(epochseconds)
print(t)

dt=datetime.datetime.today()
print(dt)
#we can also retrieve 
print(dt.day,dt.month,dt.year)
#we can also select the format
print("Current date : {}/{}/{}".format(dt.day,dt.month,dt.year))