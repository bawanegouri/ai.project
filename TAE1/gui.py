import os
import sys
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Function to get correct path for images (works for exe also)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Recommendation function
def recommend():

    soil = soil_var.get()
    rainfall = rain_var.get()
    season = season_var.get()

    if soil == "Black Soil" and rainfall == "High":
        crop = "Cotton"
        img = resource_path("images/cotton.jpg")

    elif soil == "Red Soil" and rainfall == "Medium":
        crop = "Groundnut"
        img = resource_path("images/groundnut.jpg")

    elif soil == "Alluvial Soil" and season == "Rabi":
        crop = "Wheat"
        img = resource_path("images/wheat.jpg")

    elif soil == "Clay Soil" and rainfall == "High":
        crop = "Rice"
        img = resource_path("images/rice.jpg")

    # NEW CROPS

    elif soil == "Black Soil" and season == "Kharif":
        crop = "Maize"
        img = resource_path("images/maize.jpg")

    elif soil == "Alluvial Soil" and rainfall == "High":
        crop = "Sugarcane"
        img = resource_path("images/sugarcane.jpg")

    elif soil == "Red Soil" and season == "Summer":
        crop = "Millet"
        img = resource_path("images/millet.jpg")

    elif soil == "Clay Soil" and season == "Kharif":
        crop = "Soybean"
        img = resource_path("images/soybean.jpg")

    else:
        result_label.config(text="No suitable crop found")
        image_label.config(image="", text="")
        return

    result_label.config(text="Recommended Crop: " + crop)

    try:
        image = Image.open(img)
        image = image.resize((150,150))
        photo = ImageTk.PhotoImage(image)

        image_label.config(image=photo)
        image_label.image = photo
    except:
        image_label.config(text="Image not found", image="")

# Window
root = tk.Tk()
root.title("Agricultural Advisory System")
root.geometry("600x500")
root.configure(bg="#dcedc8")

# Header
header = tk.Label(
    root,
    text="🌾 Agricultural Crop Recommendation System 🌾",
    font=("Arial",20,"bold"),
    bg="#2e7d32",
    fg="white",
    pady=12
)
header.pack(fill="x")

# Frame
frame = tk.Frame(root,bg="#dcedc8")
frame.pack(pady=30)

soil_var = tk.StringVar()
rain_var = tk.StringVar()
season_var = tk.StringVar()

# Soil
tk.Label(frame,text="Soil Type",font=("Arial",12,"bold"),bg="#dcedc8").grid(row=0,column=0,padx=20,pady=10)

soil_menu = ttk.Combobox(frame,textvariable=soil_var,width=20)
soil_menu["values"] = ("Black Soil","Red Soil","Alluvial Soil","Clay Soil")
soil_menu.grid(row=0,column=1)

# Rainfall
tk.Label(frame,text="Rainfall Level",font=("Arial",12,"bold"),bg="#dcedc8").grid(row=1,column=0,padx=20,pady=10)

rain_menu = ttk.Combobox(frame,textvariable=rain_var,width=20)
rain_menu["values"] = ("Low","Medium","High")
rain_menu.grid(row=1,column=1)

# Season
tk.Label(frame,text="Season",font=("Arial",12,"bold"),bg="#dcedc8").grid(row=2,column=0,padx=20,pady=10)

season_menu = ttk.Combobox(frame,textvariable=season_var,width=20)
season_menu["values"] = ("Kharif","Rabi","Summer")
season_menu.grid(row=2,column=1)

# Button
btn = tk.Button(
    root,
    text="Recommend Crop",
    font=("Arial",13,"bold"),
    bg="#388e3c",
    fg="white",
    padx=20,
    pady=8,
    command=recommend
)

btn.pack(pady=15)

# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial",16,"bold"),
    bg="#dcedc8",
    fg="#1b5e20"
)

result_label.pack(pady=10)

# Image
image_label = tk.Label(root,bg="#dcedc8")
image_label.pack(pady=15)

root.mainloop()