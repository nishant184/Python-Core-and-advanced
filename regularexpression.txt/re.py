import re
str = "take up one idea at a time"
result=re.search(r'o\w\w',str)
print(result.group())