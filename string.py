#the below code is for single line string 
s="  you are awesome  "
print(s)

#For multiple line string syntax is given below
#we use """(triple quotes)
s1="""you are the
creator of your destiny
    """
print(s1)

#Indexing is concept of reaching out a particular character or a line
print(s[2])
#repetition
print(s*2)

#Len() function-is used to return the length of the string
print(len(s))

#Slicing
print(s[0:5])
print(s[0:])
#The below print function will start from the end of the string because of the - sign
print(s[-3:-1])
#We can also pass a third value to a string
print(s[0:9:2])
"""when we will run the above command the last number represents how
    many letters in a string should it skip for eg,
    in (you are awesome) it will first print Y then skip o and print u 
    and  space and then it will print a and will skip r and print  ae 
    and goes to a
"""
#To reverse a string 
print(s[::-1])

#Strip-Strip function removes the spaces from a string
#First add some spaces in the string variable
print(s.strip())
#s.lstrip()-removes the spaces from the leading function
#s.rstrip()-removes the function from the right hand side
print(s.lstrip())
print(s.rstrip())

#String methods
#1.Find function
#Suppose we want to find a string in a string i.e we want to find substring
print(s.find("awe"),0,len(s))
#2.Count
print(s.count("a"))
#3.Replace
print(s.replace("awesome","super"))
#4.Upper,lower and title
print(s.upper())
print(s.lower())
print(s.title())
#In title function every word starts from a upper case

