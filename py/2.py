import re
import sys
f = file("./2_input.txt")

#reg = "[^a-zA-Z]"
r = "[a-zA-Z]"
prog = re.compile(r)
#result = prog.match(f.read())
#print re.sub("[^a-zA-Z]","1", f.read())
#print result.string
i=1
write = sys.stdout.write
for line in open('./2_input.txt', 'r'):
	if line !=None:
		ma=prog.search(line)
		if ma != None:
	    		write(ma.group(0))
	    		#print i
	i=i+1

print ""

			