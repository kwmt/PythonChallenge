
def next_page(nothing):
	import re

	baseurl = "channel/"
	text = open("".join(baseurl + nothing + ".txt")).readline()
	m = re.match('Next nothing is ([0-9]+)',text)
	if not m: print text
	print m.group(1)
    	return m.group(1)
	# while True:
	# 	s=urllib.urlopen(baseurl + nothing).read()
	# 	print s
	# 	nothing ="".join(re.findall('\d+)$', s))
	# 	if len(nothing) == 0:
	# 		break


if __name__ == '__main__':
	import sys
	if len(sys.argv) >1:
		p = sys.argv[1]
		while True:
			p= next_page(p)
	else:
		print 'Usage:%s[nothing]' % sys.argv[0]