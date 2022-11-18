import requests
import base64
from PIL import Image,ImageDraw
import cv2
from pyzbar.pyzbar import decode

BLACK = (0,0,0)
WHITE = (255,255,255)

def mystere(i):
    l, h = i.size
    for y in range(h):
        for x in range(l):
            a,b,c = i.getpixel((x, y))
            t =  a+b+c
            
            if t > 700:
            	i.putpixel((x, y),WHITE)
            else:
            	i.putpixel((x, y),BLACK)

def fix_image(image) :
    
    draw = ImageDraw.Draw(image)

    w = 9
    w2 = w * 2
    w5 = w * 5
    w6 = w * 6
    w7 = w * 7
    for x, y in [(18, 18), (18, 216), (216, 18)] :
        draw.rectangle([(x, y), (x + w7, y + w7)], fill = BLACK)
        draw.rectangle([(x + w, y + w), (x + w6, y + w6)], fill = WHITE)
        draw.rectangle([(x + w2, y + w2), (x + w5, y + w5)], fill = BLACK)

    return draw


while True:
	s = requests.Session()
	html = s.get('http://challenge01.root-me.org/programmation/ch7/')

	img = html.text.split('<br/><img src="data:image/png;base64,')[1].split('" /><br/><br/>')[0]

	pngBin = base64.b64decode(img)

	imgfile = open('./test.png', 'wb+')
	imgfile.write(pngBin)
	imgfile.close()

	im1 = Image.open("test.png")

	img = fix_image(im1)

	mystere(im1)

	im1.save("final.png")

	decocdeQR = decode(Image.open('final.png'))
	a = decocdeQR[0].data.decode('ascii').split(" ")[3]

	payload = {'metu': a}
	d = s.post('http://challenge01.root-me.org/programmation/ch7/', data=payload)
	out = d.text
	if not "retente ta chance." in out:
		print(out)
 
