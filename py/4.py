

#12345
#44827
#45439
#94485
#72198
#80992
#8880
#40961
#58765
#46561
#13418
#41954
#46782
#92730
#89229


def next_page(nothing):
	import requests
	import re

	baseurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
	text = requests.get("".join(baseurl + nothing)).text
	m = re.match('and the next nothing is ([0-9]+)',text)
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