import sys, math
from random import randint
    
from PIL import Image
WIDTH = 255
HEIGHT = 255

img = Image.new('RGB', (WIDTH, HEIGHT), color = 'blue')

#img.save("NewImage.png")

#img.show()

pixValues = list(img.getdata())

"""for i in range(len(pixValues)):
    if i % 6 == 0 or i % 6 == 1:
        pixValues[i] = (255, 0, 255)
    #if i % 6 == 2 or i % 6 == 3:
        pixValues[i] = (255, 0, 0)
    #if i % 8 == 0 or i % 8 == 1:
        pixValues[i] = (pixValues[i][0], 255, pixValues[i][2])
    if i % 16 == 0 or i % 16 == 1:
        pixValues[i] = (255 - pixValues[i][0], 255 - pixValues[i][1], 255 - pixValues[i][2])
for i in range(len(pixValues)):
    if (i // WIDTH) % 4 == 0:
        pixValues[i] = (i % WIDTH, 255 - i % WIDTH, ((i % WIDTH) % 3) * 100)
    else:
        pixValues[i] = (int((math.sin(i % 255) + 1) * (2 ** randint(3, 6))), int((math.cos(i % 255) + 1) * (2 ** randint(3, 6)) ), pixValues[i][2])
    #else:
    #    pixValues[i] = (0, 0, 0)"""

"""for i in range(len(pixValues)):
    x = i % WIDTH
    y = i // WIDTH
    pixValues[i] = (255 - (x + y), 0, 255 - (x - y))"""

for i in range(len(pixValues)):
    x = i % WIDTH
    y = i // WIDTH
    pixValues[i] = (255 - (x + y) % 100, 0, 255 - (x - y) % 100)

print(pixValues)

imgModified = Image.new(img.mode, img.size)
imgModified.putdata(pixValues)
imgModified.save("NewImage.png")

imgModified.show()
