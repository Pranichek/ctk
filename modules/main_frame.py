import customtkinter as ctk 
from .read_json import read_json

dict = read_json(filename= "config.json")

width = dict["main_frame"]["width"]
height = dict["main_frame"]["height"]
title = dict["main_frame"]["title"]

app = ctk.CTk()

app.title(title)

screen_width =  app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

x_cor_of_window = (screen_width // 2) - (width //2)
y_cor_of_window = (screen_height // 2) - (height // 2)

app.geometry(f"{width}x{height}+{x_cor_of_window}+{y_cor_of_window}")