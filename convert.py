import os
import fitz

pdffile = "session-packet.pdf"
doc = fitz.open(pdffile)

index = 1

if os.path.exists("img") == False:
    os.mkdir("img")

for page in doc:
    matrix = fitz.Matrix(2, 2)
    pix = page.get_pixmap(matrix=matrix)
    output = f"img/page-{index:03}.png"
    pix.save(output)
    index += 1

doc.close()