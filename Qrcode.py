import qrcode
import cv2
from PIL import Image
qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10,border=4,)
#qr = qrcode.QRCode(box_size=2)
n=int(input("1. URL to QR-Code\n2. Text to QR-Code\n3. Exit\nEnter the Option : "))
if(n==1):
    url=input("Enter the URL : ")
    qr.add_data(url)
elif(n==2):
    txt=input("Enter the Text : ")
    qr.add_data(txt)
else:
    print("Exit...")
    exit()

#Colour of QR-Code
qr.make(fit=True)

#img=qr.make_image(fill_color="red", back_color="blue")
#img=qr.make_image(fill_color="blue", back_color="black")
img=qr.make_image(fill_color="black", back_color="white")
#img=qr.make_image(fill_color="white", back_color="black")

n=int(input("\n1. Add QR-Code to image\n2. Only QR-Code\nEnter the option : "))
if(n==1):
    path=input("Enter Image path : ")
    img_bg=Image.open(path)
    pos=(img_bg.size[0]-img.size[0],img_bg.size[1]-img.size[1])
    img_bg.paste(img,pos)
    f_name=input("Enter new image name : ")
    img_bg.save(f_name+".png")
else:
    f_name=input("Enter new image name : ")
    img.save(f_name+".png")
print("QR-Code generated successfully...")
