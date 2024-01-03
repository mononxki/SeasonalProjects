from PIL import Image
import easygui
import os
import time


ASCII_CHARS = "@%


def resize_image(image, new_width=100):
    (original_width, original_height) = image.size
    aspect_ratio = original_height / float(original_width)
    new_height = int(aspect_ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image


def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image


def pixels_to_ascii(image, ascii_chars=ASCII_CHARS):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ascii_chars[pixel_value // 25]
    return ascii_str


def select_image():
    file_path = easygui.fileopenbox(filetypes=["*.jpg", "*.jpeg", "*.png", "*.bmp"])
    return file_path


def format_and_save_ascii(ascii_str, filename="ascii_art.txt", output_width=100):
    formatted_ascii = "\n".join([ascii_str[i:i + output_width] for i in range(0, len(ascii_str), output_width)])
    with open(filename, "w") as f:
        f.write(formatted_ascii)


RED_TO_GRAY_GRADIENT = [
    f"\033[38;2;255;{(255 - i)};{(255 - i)}m" for i in range(0, 256)
]


def image_to_ascii(image_path, output_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image, output_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    return ascii_str


def main(output_width=100):
    image_path = select_image()
    if image_path:
        ascii_str = image_to_ascii(image_path, output_width)

        if ascii_str:
            format_and_save_ascii(ascii_str, output_width=output_width)

            
            gradient_length = len(RED_TO_GRAY_GRADIENT)
            for line in ascii_str.split("\n"):
                for i, char in enumerate(line):
                    gradient_color = RED_TO_GRAY_GRADIENT[i % gradient_length]
                    print(gradient_color + char, end="")
                print("\033[0m")  

            
            time.sleep(30)

if __name__ == "__main__":
    main()
