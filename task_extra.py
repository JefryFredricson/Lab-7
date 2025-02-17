import requests
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk

def get_pic():
    api_key = 'YOUR_API_KEY'
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    response = requests.get(url).json()
    return [response['url'], response['explanation']]

def loading_image():
    url, text = get_pic()
    text = text.replace('  ', ' ')

    response = requests.get(url)
    pil_image = Image.open(BytesIO(response.content))
    (wid, hei) = pil_image.size

    root = tk.Tk()
    canvas = tk.Canvas(root, height=hei, width=wid)
    image = ImageTk.PhotoImage(pil_image)
    canvas.create_image(0, 0, anchor='nw', image=image)
    canvas.grid(row=1, column=1)
    root.mainloop()


loading_image()
