import cv2
from PIL import Image
from PIL import ImageFilter
from PIL import ImageDraw
from PIL import ImageEnhance
from bina import *
import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print("Hello There!")
print('Press','SPACE','for taking a fresh snap')
print('Press','ESCAPE','for using a previosly saved image')

cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k%256 == 32:
        # SPACE pressed
        img_name = "my_pic.png"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} written!")
        break
    elif k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break

cam.release()
cv2.destroyAllWindows()

img = Image.open("my_pic.png") 

width=img.width
height=img.height
mode=img.mode
print("{}x{}  {}".format(width,height,mode))

bunch=[]
bunch.append(img)
bunch.append(img.convert('L'))
bunch.append(img.convert('1'))

enhancer = ImageEnhance.Color(img)
bunch.append(enhancer.enhance(0.25))
bunch.append(enhancer.enhance(0.75))

enhancer = ImageEnhance.Sharpness(img)
bunch.append(enhancer.enhance(2))

enhancer = ImageEnhance.Brightness(img)
bunch.append(enhancer.enhance(0.25))
bunch.append(enhancer.enhance(0.75))

bunch.append(binarize(img, 100))

from PIL import Image
# creating a blank image
sheet=Image.new(mode,(3*width,3*height))
for x in range(3):
    for y in range(3):
        sheet.paste(bunch[x + 3*y], (width * x, height * y))
sheet.show()

text=[]
for i in bunch:
    text.append(tess.image_to_string(i))

for i in text:
    print(i)