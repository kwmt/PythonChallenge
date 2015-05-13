from PIL import Image

img = Image.open("11_cave.jpg")
ans = Image.new(img.mode,  (img.size[0]/2, img.size[1]/2),'white')

for y in range(img.size[1]):
	for x in range(img.size[0]):
		if x % 2 == 1 and y % 2 == 1:
			p= img.getpixel((x,y))
			ans.putpixel((x/2,y/2),p)


ans.show()