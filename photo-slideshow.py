# pillow library - used for image processing and manipulation
import tkinter as tk
from PIL import Image, ImageTk

# main Window 
root = tk.Tk()
root.title("Photo Slideshow Album")
root.geometry("900x900")

# List of image paths
image_paths = [
    r"images\image1.jpeg",
    r"images\image2.jpeg",
    r"images\image3.jpeg",
    r"images\image4.jpeg",
]

image_size = (700, 700)

# Load and resize images
images = []
for path in image_paths:
    img = Image.open(path)
    img = img.resize(image_size, Image.LANCZOS)
    images.append(img)

# Convert PIL images into tkinter compatible images
final_images = []
for img in images:
    photo = ImageTk.PhotoImage(img)
    final_images.append(photo)

# Label widget to display photo
image_label = tk.Label(root)
image_label.pack(pady=30)

# Slideshow function (fixed)
index = 0

def start_slideshow():
    global index

    photo = final_images[index]
    image_label.config(image=photo)
    image_label.image = photo

    index = (index + 1) % len(final_images)

    root.after(2000, start_slideshow)  # replaces time.sleep

# Button
play_button = tk.Button(
    root,
    text="Play the slideshow",
    font=("Arial", 17),
    command=start_slideshow
)

play_button.pack(pady=40)

root.mainloop()