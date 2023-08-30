import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Label # Import Label from ttk module
import tensorflow as tf
from PIL import ImageTk
import numpy as np
import os


window = tk.Tk()
window.title("Cyclone_eye_GUI")
window.geometry("700x500")
window.config(bg="#A9ACA9")

scale=1./255

#model:inputsize:path
models={"              Choose a Model              ":"None Selected",
        "VGG19 v1":"VGG19_try.h5",
        "Xception v1":"Xception_try1.h5",
        "DenseNet121 v1":"DenseNet121_try1.h5",
        "Resnet50v2 v1":"Resnet50V2_try1.h5",}


def choose_model():
    global model_path 
    model_path = models[clicked.get()]
    return 

def load_model():
    global model
    choose_model()
    model = tf.keras.models.load_model(model_path)
    return

    
def upload_image():
    filename = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg *.png")])
    image = tf.io.read_file(filename)
    image = tf.image.decode_jpeg(image, channels=3)

    image = tf.image.resize(image, [224, 224])
    image = image * scale
    image = tf.expand_dims(image, axis=0)
    return image,filename

def run_model():
    image,filename = upload_image()
    filename=os.path.basename(filename)


    prediction = model.predict(image)
    result = f"The coordinates of Cyclone eye in {filename} are {prediction[0]}"
    print(result)

    canvas.config(bg="#BFC3BA")
    result_label.config(text=result,background="#BFC3BA",foreground="black")

    pil_image = tf.keras.preprocessing.image.array_to_img(image[0])
    tk_image = ImageTk.PhotoImage(pil_image)
    img_label.config(image=tk_image)
    img_label.image = tk_image
    




clicked = tk.StringVar()
clicked.set("Choose a model")
drop= tk.OptionMenu(window, clicked, *models.keys(),)
drop.config(width=14,bg="#A9ACA9",fg="black",highlightthickness=0.5,highlightcolor="#938f8f",font=("times", 16))
drop.pack(side="top",anchor="nw",expand=True,)
drop.place(x=70,y=10)

button = tk.Button(window, text="load model",font=("times", 16), bg="#A9ACA9" ,command=load_model,fg="black",highlightthickness=0.5,highlightcolor="#938f8f",)
# button.pack(side="top",expand=True,padx=260,pady=10)
button.place(x=280,y=10)
button = tk.Button(window, text="Upload an image",font=("times", 16), bg="#A9ACA9" ,command=run_model,fg="black",highlightthickness=0.5,highlightcolor="#938f8f",)
# button.pack(side="top",expand=True,padx=260,pady=10)
button.place(x=430,y=10)

canvas = tk.Canvas(window, width=600, height=100, bd=0, bg="#A9ACA9", highlightthickness=0, relief="ridge")
canvas.pack(pady=75)

result_label = Label(canvas, text="", style="Result.TLabel",background="#A9ACA9",font=("time", 11), anchor="center",borderwidth=0)
result_label.place(relx=0.5, rely=0.5, anchor="center")

img_label = tk.Label(window,width=224, height=224, bg="#A9ACA9")
img_label.place(x=250,y=200)

window.mainloop()