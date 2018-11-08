import qrcode
from PIL import Image
def generator(s):
    q=qrcode.main.QRCode()
    q.add_data(s)
    m=q.make_image()
    m.save("show.png")
s=input("请输入您想要生成的网址：")
generator(s)

