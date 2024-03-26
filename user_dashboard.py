import tkinter as tk
import subprocess
from check_assets import check_assets

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
root.title("Asset Tracking Management System")

# Make the window fullscreen
root.attributes('-fullscreen', True)
label = tk.Label(root, text="Asset Tracking Management System", font=("times new roman", 45, "bold"))
label.pack()
# Load profile image
profile_image = tk.PhotoImage(file=r"C:\Users\Admin\Downloads\asset_management_system_django\Asset Tracking management system\images\user.png")

# Create profile icon
canvas = tk.Canvas(root, width=50, height=50)
canvas.pack(padx=20, pady=20, anchor='nw')
canvas.create_image(25, 25, image=profile_image)

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
logout_btn = tk.Button(root, text="Logout", padx=20, pady=10, font=('Arial', 14), command=logout)
logout_btn.place(relx=1.0, rely=0.0, anchor='ne', x=-20, y=20)

# Create exit button
exit_btn = tk.Button(root, text="Exit", padx=20, pady=10, font=('Arial', 14), command=exit_fullscreen)
exit_btn.place(relx=1.0, rely=1.0, anchor='se', x=-20, y=-20)

root.mainloop()
