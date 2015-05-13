
text = open("12_evil2.gfx", "rb").read()

for i in range (0,5):
	if text[i::5][6:10] == 'JFIF':
		extension = '.jpg'
	if text[i::5][0:3] == 'GIF':
		extension = '.gif'
	if text[i::5][1:4] == 'PNG':
		extension = '.png'
	filename = "level12_answer"+ str(i+1)+extension
	a = open(filename,"wb")
	a.write(text[i::5])
	a.close()
