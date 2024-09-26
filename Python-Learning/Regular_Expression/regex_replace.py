import re
str="This table is beautiful and has four pillers"
pattern="beautiful"
replacement="great"
result=re.sub(pattern, replacement, str)
print("Modified text : ", result)
