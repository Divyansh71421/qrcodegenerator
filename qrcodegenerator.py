import qrcode
qr=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
data="https://leetcode.com/problems/two-sum/" #data=link of any site
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white") #image formation
img.save('text.png')
