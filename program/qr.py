import QRcode
qr=QRcode.QRCode(
    version=1,
    box_size=10,
    border=5

)
data="hello i am tirth"
qr.add_data(data)
qr.make(fit=true)
img=qr.make_image(fill="black",back_color="white")
img.save("qr-code-sample.jpg")