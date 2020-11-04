f=open("myfile.txt","w")# A file will be created with name as myfile
print("enter text (type # when you are done)")
s=''
while(s!='#'):
    s = input()
    f.write(s)
f.close() 