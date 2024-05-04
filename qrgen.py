# QR Code generator using python
import qrcode as qr

img=qr.make("https://www.youtube.com/@SHABDxGAMER")
img.save("shabd_yt.png")

# make() is used to create or make string url or text message(placeholder) 
# save() used to save file with name and extension