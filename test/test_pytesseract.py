# -*- coding: UTF-8 –*-

import os
import sys
from PIL import Image 
sys.path.append('..\\')
from util import pytesseract

def get_captcha(file):
	img = Image.open(file)
	#print img.format, img.size, img.mode
	img = img.convert('RGBA')
	pix = img.load()

	for y in range(img.size[1]):  # 二值化处理，阈值为R=10，G=10，B=240
		for x in range(img.size[0]):
			if pix[x, y][0] < 10 and pix[x, y][1] < 10 and pix[x, y][2] > 240:
				pix[x, y] = (0, 0, 0, 255)
			else:
				pix[x, y] = (255, 255, 255, 255)
	img.convert("RGB").save("temp.jpg")  # 由于tesseract限制，这里必须存到本地文件
	text=pytesseract.image_to_string("temp.jpg")
	os.remove('temp.jpg')
	return text
		
if __name__ == "__main__":
	print get_captcha('./makecaptcha.gif')