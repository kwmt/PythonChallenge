import pickle

f = open('5_input.txt')
l = pickle.load(f)
i=0
for line in l:
	s =""
	for char in line:
		s +=  char[0] * char[1]
	i=i+1
	print i
	print s
