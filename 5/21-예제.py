from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import random
num1 = random.randint(1, 99)
if num1 < 10:
    num1 = "0" + str(num1)
else:
    num1 = str(num1)
pic1 = "C:\파이썬 공부\img\picture"+num1+".jpg"
img = Image.open(pic1)
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img = img.transpose(Image.FLIP_TOP_BOTTOM)
img = img.rotate(45, expand=True)
img = img.filter(ImageFilter.CONTOUR)
img.show()
img.save(pic1)
print(num1)