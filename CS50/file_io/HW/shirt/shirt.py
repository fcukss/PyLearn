import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    input = sys.argv[1]
    output = sys.argv[2]
    if not output.endswith(".jpg"):
        sys.exit("Invalid output")
    input_ext = os.path.splitext(input)[1].lower()
    output_ext = os.path.splitext(output)[1].lower()
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")
    try:
        image = Image.open(input)
        shirt = Image.open("shirt.png")

        image = ImageOps.fit(image, shirt.size)
        image.paste(shirt, shirt)
        image.save(output)

    except FileNotFoundError:
        sys.exit("Input file does not exist")


main()
