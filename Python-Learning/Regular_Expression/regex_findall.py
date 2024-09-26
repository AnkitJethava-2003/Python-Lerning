import re

str="This table has four pillers"
pattern="table"
result=re.search(pattern, str)
if result:
    print("Pattern found", result.group())
else:
    print("pattern not found")


