import csv
import numpy as np
from PIL import Image


def main():
    with (open("views.csv", "r", encoding="utf-8") as file,
          open("analysis.csv", 'w', encoding="utf-8") as analysis):
        reader = csv.DictReader(file)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ['brightness'])
        writer.writeheader()

        for row in reader:
            # brightness = calculation_brightness(f"{row['id']}.jpeg")
            # writer.writerow({
            #     'id': row['id'],
            #     "english_title": row["english_title"],
            #     "japanese_title": row ['japanese_title'],
            #     'brightness' : round(brightness, 2)
            # })

            # the same
            row['brightness'] = round(calculation_brightness(f"{row['id']}.jpeg"),2)
            writer.writerow(row)

def calculation_brightness(filename):
    with Image.open(filename) as img:
        brightness = np.mean(np.array(img.convert('L'))) / 255
    return brightness


main()
