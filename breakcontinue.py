#Break is used to break the loop if the condition ia true
lst=[3,1,2,5,6,2]
for i in lst:
    if i==5:
        break
    print(i)
#In the above for loop the loop stop executing after the value of is 5
#It will not print the elements after 5

#Continue
#To print numbers from 1 to 20 but skip multiples of 3
x=0
while x<20:
    x+=1
    if x%3==0:
        continue
    print(x)
#The continue is used to skip a particular element if the condition is true

#Assert
#To enter a number greater than 10 and assert(warn) the user
b=int(input("Enter a njumber greater than 10"))
assert b>10,"Wrong number entered"
#Assert is used to give an warning or error message to the use if the condition is not satisfied
