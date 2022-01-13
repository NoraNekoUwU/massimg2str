try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os

os.system('figlet NoraNeko')
print('Processing....')
imgnum = 1

while imgnum <= 17:
##change y to your .txt directory to store the string
	f = open("z","a")
## change x to directory of your image source
	x = 'x/%d.png'%(imgnum)
	f.write(pytesseract.image_to_string(x))
	f.close
	imgnum += 1
##put massimg2str.py in parent directory of your image source and change the image to ordered number and make a text.txt
##in same directory as massimg2str.py
##change the figlet to make it look cool lmao

