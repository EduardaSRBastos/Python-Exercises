# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 14:18:33 2022

@author: Eduarda
"""
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

texto = "https://www.reddit.com/user/BlackCat280"

img = qrcode.make(texto)
img.save("C:/Users/Duda Bastos/Desktop/Programing/QrCodeBlackCat280.png")

qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr.add_data(texto)
qr.make(fit = True)

img = qr.make_image(fill_color = "yellow", back_color = "black")
img.save("C:/Users/Duda Bastos/Desktop/Programing/QrCodeBlackCat280Y.png")

#Decode Qr Code----------------

img = Image.open("C:/Users/Duda Bastos/Desktop/Programing/QrCodeBlackCat280.png")
result = decode(img)
print(result)
