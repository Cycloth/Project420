import qrcode

image = qrcode.make("http://potsnob.net")
image.save("potsnob.png")
