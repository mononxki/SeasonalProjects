import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageEnhance
import tempfile
import os
import sys

def enhance_image(image_path, output_path, brightness_factor=1.2, contrast_factor=1.2, sharpness_factor=1.5, saturation_factor=1.5):

    image = Image.open(image_path)

    image = image.convert("RGB")


    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness_factor)

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast_factor)

    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(sharpness_factor)

    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(saturation_factor)


    image.save(output_path, "JPEG")

def process_image(image_path):
  
    brightness_factor = 1.2
    contrast_factor = 1.2
    sharpness_factor = 1.5
    saturation_factor = 1.5

   
    script_directory = os.path.dirname(sys.argv[0])

 
    output_path = os.path.join(script_directory, "enhanced_image.jpg")

 
    enhance_image(image_path, output_path, brightness_factor, contrast_factor, sharpness_factor, saturation_factor)


    os.startfile(output_path)

def on_drop(event):
    file_path = event.data
    process_image(file_path)


root = TkinterDnD.Tk()
root.title("Image Enhancer")


canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(padx=10, pady=10)


canvas.drop_target_register(DND_FILES)
canvas.dnd_bind('<<Drop>>', on_drop)


root.mainloop()
