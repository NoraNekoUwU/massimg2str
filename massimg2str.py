try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os

os.system('figlet NoraNeko')
print("Mass image to string tool")
def img2str():
	dirtxt = str(input("masukkan dir .txt kalian contoh : home/slamet/Documents/text.txt\n"))
	dirimg = str(input("masukkan dir file image kalian contoh : home/slamet/Pictures/src/\n"))
	typefile = str(input("masukkan type file contoh : jpeg/png\n"))
	o = 1
	p = int(input("Masukkan jumlah foto yang akan di scan!!\n"))

	while o <= p:
		f = open("{}".format(dirtxt),"a")
		x = '{}/{}.{}'.format(dirimg,o,typefile)
		f.write(pytesseract.image_to_string(x))
		f.close
		print('Processing {}.{}....'.format(o,typefile))
		o += 1
	print("output file : {}".format(dirtxt))
x = int(input("Start = 1\nExit = 2\n"))
if x == 1 :
	img2str()
if x == 2 :
	print("thanks for using!!")
	exit()
if x > 3 :
	print("Don't be stupid")
	exit()
