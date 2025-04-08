from PIL import Image
from PIL import ImageFilter

def main():
   with Image.open("in.jpeg") as img:
        print(img.size)
        print(img.format)
        #rotate our image
        img = img.rotate(180)
        img = img.filter(ImageFilter.BLUR)
        img.save("out.jpg")


if __name__ == '__main__':
    main()