import Image
import re

im = Image.open("7_oxygen.png")
size = im.size

y=0
for j in range(0,size[1]):
	rgb = im.getpixel((0,j))
	if rgb[0] == rgb[1] == rgb[2]:
		 y = j
		 break

tmp =""

for i in range(0,size[0]-1,7):
	rgb = im.getpixel((i,y))
	rgb_next = im.getpixel((i+1,y))

	if rgb[0] == rgb[1] == rgb[2]:
		tmp += chr(rgb[0])

print tmp

ans = ""
for a in re.findall('\d+', tmp):
	ans  += chr(int(a))
print ans