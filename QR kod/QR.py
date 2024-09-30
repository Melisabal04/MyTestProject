import pyqrcode

url= input("enter a url for generating a qr code: ")

qr_code= pyqrcode.create(url)
qr_code.svg('qrcode.svg',scale=5)