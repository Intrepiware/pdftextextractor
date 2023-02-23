from PIL import Image
import os
import pytesseract
import numpy as np


if os.path.exists("out") == False:
    os.mkdir("out")

with open(r"./out/output-tesseract.md", "w") as output_file:
    page = 1
    for (dirpath, dirnames, filenames) in os.walk('./img'):
        for file in filenames:
            if file.endswith('.png'):
                print(f"Parsing {file}...")
                output_file.write(f"___\n(page {page})\n\n")
                img = np.array(Image.open(f"img/{file}"))
                text = pytesseract.image_to_string(img)
                output_file.write(text + "\n\n")
                page += 1
    output_file.close()                    