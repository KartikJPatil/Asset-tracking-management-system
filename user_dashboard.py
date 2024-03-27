import tkinter as tk
import subprocess
from check_assets import check_assets
from tkinter import colorchooser

def change_background_color():
    color = colorchooser.askcolor(title="Choose Background Color")
    if color[1]:
        root.configure(bg=color[1])

def change_button_color():
    color = colorchooser.askcolor(title="Choose Button Color")
    if color[1]:
        add_assets_btn.config(bg=color[1])
        check_assets_btn.config(bg=color[1])
        statistics_btn.config(bg=color[1])
        help_btn.config(bg=color[1])
        logout_btn.config(bg=color[1])
        exit_btn.config(bg=color[1])

def change_text_color():
    color = colorchooser.askcolor(title="Choose Text Color")
    if color[1]:
        add_assets_btn.config(fg=color[1])
        check_assets_btn.config(fg=color[1])
        statistics_btn.config(fg=color[1])
        help_btn.config(fg=color[1])
        logout_btn.config(fg=color[1])
        exit_btn.config(fg=color[1])

def open_statistics():
    subprocess.Popen(["python", "statistics.py"])
def logout():
    root.destroy()
    subprocess.Popen(["python","user_login.py"])

def run_api():
    subprocess.Popen(["python", "add_assets.py"])

def exit_fullscreen():
    root.attributes('-fullscreen', False)  # Disable fullscreen
    root.destroy()  # Destroy the window

# Create main window
root = tk.Tk()
root.configure(bg="lightblue")
root.title("Asset Tracking Management System")

# Make the window fullscreen
root.attributes('-fullscreen', True)
label = tk.Label(root, text="Asset Tracking Management System", font=("times new roman", 45, "underline"))
label.pack()

# Load profile image
profile_image = tk.PhotoImage(file=r"C:\Users\Admin\Downloads\asset_management_system_django\Asset Tracking management system\images\user.png")
profile_image = profile_image.subsample(4)

# Create profile icon
canvas = tk.Canvas(root, width=100, height=100)
canvas.pack(padx=60, pady=20, anchor='nw')
canvas.create_image(50, 50, image=profile_image)

# Create frame to hold buttons
button_frame = tk.Frame(root)
button_frame.pack(side=tk.LEFT, padx=20, pady=20, anchor='nw')

# Create menu buttons
add_assets_btn = tk.Button(button_frame, text="Add Assets", padx=20, pady=10, font=('Arial', 14), command=run_api)
add_assets_btn.pack(fill=tk.X, padx=10, pady=5)

check_assets_btn = tk.Button(button_frame, text="Check Assets", padx=20, pady=10, font=('Arial', 14), command=check_assets)
check_assets_btn.pack(fill=tk.X, padx=10, pady=5)

statistics_btn = tk.Button(button_frame, text="Statistics", padx=20, pady=10, font=('Arial', 14), command=open_statistics)
statistics_btn.pack(fill=tk.X, padx=10, pady=5)

help_btn = tk.Button(button_frame, text="Help!", padx=20, pady=10, font=('Arial', 14))
help_btn.pack(fill=tk.X, padx=10, pady=5)

# Create logout button
logout_btn = tk.Button(root, text="Logout", padx=5, pady=5, font=('Arial', 14), command=logout)
logout_btn.place(relx=1.0, rely=0.0, anchor='ne', x=-20, y=60)

# Create exit button
exit_btn = tk.Button(root, text="Exit", padx=65, pady=10, font=('Arial', 14), command=exit_fullscreen)
exit_btn.place(relx=1.0, rely=0.0, anchor='n', x=-1420, y=515)

settings_btn = tk.Button(root, text="⚙️", padx=1, pady=1, font=('Arial', 14), command=lambda: None)
settings_btn.place(relx=1.0, rely=0.0, anchor='ne', x=-20, y=120)  # Adjust the position as needed

# Create a frame to hold the submenu buttons
submenu_frame = tk.Frame(root, bg="lightblue")
submenu_frame.pack_forget()  # Initially hide the submenu frame

# Create submenu buttons
background_color_btn = tk.Button(submenu_frame, text="Change Background Color", padx=20, pady=10, font=('Arial', 14), command=change_background_color)
background_color_btn.pack(fill=tk.X, padx=10, pady=5)

button_color_btn = tk.Button(submenu_frame, text="Change Button Color", padx=20, pady=10, font=('Arial', 14), command=change_button_color)
button_color_btn.pack(fill=tk.X, padx=10, pady=5)

text_color_btn = tk.Button(submenu_frame, text="Change Text Color", padx=20, pady=10, font=('Arial', 14), command=change_text_color)
text_color_btn.pack(fill=tk.X, padx=10, pady=5)

# Function to show/hide the submenu frame
def toggle_submenu():
    if submenu_frame.winfo_ismapped():
        submenu_frame.pack_forget()
    else:
        submenu_frame.pack(side=tk.TOP, padx=10, pady=10)

# Configure the settings button to toggle the visibility of the submenu
settings_btn.config(command=toggle_submenu)

root.mainloop()
