import re

f = file("./3_input.txt")

reg = "[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]"

f = open("./3_input.txt")
text = f.read().replace("\n","")
f.close()

ans =re.findall(reg, text)
print "".join(ans)