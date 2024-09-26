import re

str="This table has four pillers"
pattern="has"
result=re.match(pattern, str)
if result:
    print("Match found, ", result.group())
else:
    print("No match")