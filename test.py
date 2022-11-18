import requests
import base64
from PIL import Image,ImageDraw
from qrtools.qrtools import QR


BLACK = (0,0,0)
WHITE = (255,255,255)

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

    TMP_QRCODE_PATH = './tmp_qrcode.png'
    image.save(TMP_QRCODE_PATH, format='PNG')
    return TMP_QRCODE_PATH



s = requests.Session()
html = s.get('http://challenge01.root-me.org/programmation/ch7/')

img = html.text.split('<br/><img src="data:image/png;base64,')[1].split('" /><br/><br/>')[0]

pngBin = base64.b64decode(img)

imgfile = open('./test.png', 'wb+')
imgfile.write(pngBin)
imgfile.close()

im1 = Image.open("test.png")

fix_image(im1)

im1.save("final.png")

qr = qrtools.QR()
qr.decode("final.png")
print(qr.data.decode())
