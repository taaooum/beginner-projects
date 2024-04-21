import os
from PIL import Image

def open_image(path):
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print("Unable to find file!")
        return
    except Exception as e:
        print("Error opening image:", e)
        return
    return img

def save_image(path, ascii_img):
    try:
        newfile = "beginner-projects/{}.txt".format(os.path.basename(open(path).name))
        open(newfile, 'w').write(ascii_img)
    except Exception as e:
        print("Error opening image:", e)
        return
    print("ASCII art saved to:", newfile)

def resize_image(img, scale_factor):
    try:        
        # Calculate the new dimensions
        new_width = int(img.width * scale_factor)
        new_height = int(img.height * scale_factor)
        
        # Resize the image
        return img.resize((new_width, new_height))
    except Exception as e:
        print("Error:", e)
        return img

def ascii_image(img):

    img = img.convert("L")  # Convert image to grayscale
    pixels = img.load()

    width, height = img.size
    ascii_img = ""

    # list of different scales of grey
    char = ["@","%","#","+","=","~","-","."]
    for i in range(height):
        for j in range(width):
            pixel_value = pixels[j, i]
            ascii_img += char[pixel_value // 32] # Convert pixel value to ASCII

        ascii_img += "\n"
        
        # Calculate completion percentage
        completion = int((i + 1) / height * 100)
        print("{} % complete".format(completion), end='\r')
    
    print("Processing complete!")
    return ascii_img

path = input("Enter path of the image you want to convert into ascii: \n")
image = open_image(path)

if image:
    resize_factor = 0.05
    resized_image = resize_image(image, resize_factor)
    ascii_text = ascii_image(resized_image)
    save_image(path, ascii_text)