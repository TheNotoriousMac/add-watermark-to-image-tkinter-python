from tkinter import *
from PIL import Image, ImageDraw, ImageFont

window = Tk()
window.title("Image Watermark App")
window.minsize(500, 500)
window.config(padx=100, pady=200)

def add_watermark():
    image_filepath_input = image_filepath.get()
    watermark_text_input = watermark_text.get()

    img = Image.open(image_filepath_input)

    img_edit = ImageDraw.Draw(img)
    watermark_text_font = ImageFont.truetype('Gidole-Regular.ttf', 60)
    img_edit.text((0,0), watermark_text_input, font=watermark_text_font, fill=(255,255,255))

    img.show()

    img.save("edit.png")

#Add Header Label
header_label = Label(text="Image Watermark App", font=("Arial", 24, "bold"))
header_label.grid(column=0, row=0)
header_label.config(padx=50, pady=20)

#Add Input Label to tell user to enter image file path
image_label = Label(text="Enter image filepath below:", font=("Arial", 16, "normal"))
image_label.grid(column=0, row=1)
image_label.config(padx=20, pady=20)

#Add Input Entry to take in the file path to the image
image_filepath = Entry(width=80)
image_filepath.grid(column=0, row=2)



#Add Watermark Label to tell user to enter text needed for watermark
watermark_label = Label(text="Enter watermark text below:", font=("Arial", 16, "normal"))
watermark_label.grid(column=0, row=3)
watermark_label.config(padx=20, pady=20)

#Add Input Entry to take in the file path to the image
watermark_text = Entry(width=80)
watermark_text.grid(column=0, row=4)

#Add Button to confirm submission of image
submit_btn = Button(text="Submit", command=add_watermark)
submit_btn.grid(column=0, row=5)



window.mainloop()