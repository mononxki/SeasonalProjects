import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import Image, ImageTk
import tempfile
import os
import sys

# Fully Made by Simon [ Disease / SleepTght ]
# Simply turns images into their pixel art version.
# This is just a silly side project to kill my time.
# I have no clue where it would be used lol.

def process_image(image_path):

    image = Image.open(image_path)


    pixel_width, pixel_height = 10, 10  


    pixelated_image = image.resize((image.width // pixel_width, image.height // pixel_height), Image.NEAREST)


    pixelated_image = pixelated_image.resize((image.width, image.height), Image.NEAREST)


    pixelated_image = pixelated_image.convert('P', palette=Image.ADAPTIVE, colors=16)


    script_directory = os.path.dirname(sys.argv[0])
    output_path = os.path.join(script_directory, "pixel_art.png")
    pixelated_image.save(output_path)

  
    os.startfile(output_path)

def on_drop(event):
    file_path = event.data
    process_image(file_path)


root = TkinterDnD.Tk()
root.title("(Drag and Drop) Image2PixelArt")


canvas = tk.Canvas(root, width=400, height=400)
canvas.pack(padx=10, pady=10)


canvas.drop_target_register(DND_FILES)
canvas.dnd_bind('<<Drop>>', on_drop)


root.mainloop()
