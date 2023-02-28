import os
import fitz

for file in os.listdir('./pdf'): 
    if os.path.isfile(f"./pdf/{file}") and file.endswith('.pdf'):
        print(file)
        doc = fitz.open(f"./pdf/{file}")

        index = 1
        dir_name = f"img"
        if os.path.exists(dir_name) == False:
            os.mkdir(dir_name)

        for page in doc:
            matrix = fitz.Matrix(2, 2)
            pix = page.get_pixmap(matrix=matrix)
            output = f"{dir_name}/{file}-page-{index:03}.png"
            pix.save(output)
            index += 1

        doc.close()