from PIL import Image

img = Image.open("crypt.png")
obj = img.load()
width = img.size[0]
height = img.size[1]

color = {}
for j in range(width):
    for i in range(height):
        if obj[i, j] not in color:
            color[obj[i, j]] = 1
        if obj[i, j] in color:
            color[obj[i, j]] += 1

for i, j in color:
    print(i, j)
