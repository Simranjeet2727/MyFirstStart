# QR Code generator with colors and borders

import qrcode
from PIL import Image

qr= qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("https://www.facebook.com/amarjeetsingh.jolly.1")
qr.make(fit=True)
img=qr.make_image(fill_color="blue",back_color="white")
img.save("amarjeet_singh_fb.png")

# QRCode when read PIL module this function is there it changes version of qrcode, border,color,etc.
# add_data() is used to add data to list