from PIL import Image, ImageFilter, ImageEnhance, ImageOps

img = Image.open("C:\파이썬 공부\img\picture05.jpg")
img.show()


#img = img.transpose(Image.FLIP_LEFT_RIGHT) #좌우반전
#img = img.transpose(Image.FLIP_TOP_BOTTOM) #상하반전
# img = img.rotate(45, expand=True) #각도도
# img = img.crop((100,100,600,600)) #x1, y1, 좌표에서 x2, y2 좌표 까지의 이미지를 자름 그리고 반환함
# img = ImageEnhance.Brightness(img).enhance(3.0) #이미지를 밝게함 1.0에서 5.0 까지의 값을 넣음 인핸스에
# img = ImageEnhance.Brightness(img).enhance(0.4) #밝게 하는것과 반대로 0.0에서 0.4사이
# img = ImageOps.grayscale(img) #흑백으로 변경 ImageOps.grasyscale
# img = img.filter(ImageFilter.EMBOSS) #엠보싱 효과를 줌 효과 주는거여서  mg.filter(ImageFilter.EMBOSS)
# img = img.filter(ImageFilter.CONTOUR) #이미지에 윤곽 효과를 줌 CONTOUR 
# img = img.filter(ImageFilter.FIND_EDGES) #경계선을 추출하고 추출된 결과를 반환함 FIND_EDGES

img.show()
