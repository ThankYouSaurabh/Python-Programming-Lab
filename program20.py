import re

s = "hello world"
sub = "world"

if re.search(sub, s):
    print("Substring found")
else:
    print("Not found")
