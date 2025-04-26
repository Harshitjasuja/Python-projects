#python project to convert image to pdf
#using img2pdf library

#importing necessary libraries
import img2pdf
from PIL import Image
import os

#storing image path
img_path = "image.png"

#storing pdf path
pdf_path = "output.pdf"

#opening image
image = Image.open(img_path)

#converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# opening or creating pdf file
file = open(pdf_path, "wb")

#writing pdf file with chunks
file.write(pdf_bytes)

#closing files
image.close()
file.close()

#output
print("image converted to pdf successfully")