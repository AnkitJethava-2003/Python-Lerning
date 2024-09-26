import re
string="apple, banana, orange, grape"
pattern=","
result=re.split(pattern, string)
print(result)