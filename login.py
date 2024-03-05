from tkinter import *
import customtkinter as ctk
import tkinter.messagebox as tkmb 
import os

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue") 

app = ctk.CTk() 
app.geometry("1350x700+0+0") 
app.title("LOGIN") 

def login(): 
    username = "Pranav"
    password = "2004"
    
    if user_entry.get() == "" or user_pass.get() == "": 
        tkmb.showinfo(title="Error", message="All fields are required")
    elif user_entry.get() == username and user_pass.get() != password: 
        tkmb.showwarning(title='Wrong password', message='Please check your password') 
    elif user_entry.get() != username and user_pass.get() == password: 
        tkmb.showwarning(title='Wrong username', message='Please check your username') 
    else: 
        tkmb.showinfo(title="Login Successful!!", message="Welcome to Asset Management System")
        app.withdraw()  
        os.system("python Dashboard.py")
        app.quit()

label = ctk.CTkLabel(app, text="LOGIN", font=("times new roman", 45, "bold")) 
label.pack(pady=20) 

frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20, padx=40, fill='both', expand=True) 

label = ctk.CTkLabel(master=frame, text='Please Enter Username & Password') 
label.pack(pady=12, padx=10) 

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username") 
user_entry.pack(pady=12, padx=10) 

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*") 
user_pass.pack(pady=12, padx=10) 

button = ctk.CTkButton(master=frame, text='Login', command=login) 
button.pack(pady=12, padx=10) 

checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me') 
checkbox.pack(pady=12, padx=10) 

app.mainloop()
