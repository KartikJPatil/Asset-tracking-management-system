import tkinter as tk
from tkinter import messagebox
import mysql.connector
import subprocess

def submit_data(action):
    # Retrieve data from entry fields and dropdown menu
    user_id = user_id_entry.get()

    # Connect to MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="K@rtik2004",
        database="assettracking"
    )
    cursor = connection.cursor()

    # Define query based on action
    if action == "Insert":
        query = "INSERT INTO users (user_id, name, email, gender, dob, password) VALUES (%s, %s, %s, %s, %s, %s)"
        message = "User created successfully"
    elif action == "Update":
        query = "UPDATE users SET name = %s, email = %s, gender = %s, dob = %s, password = %s WHERE user_id = %s"
        message = "User updated successfully"

    # Execute query with appropriate values
    try:
        if action == "Insert":
            # Retrieve other data for insertion
            name = name_entry.get()
            email = email_entry.get()
            gender = gender_var.get()
            dob = dob_entry.get()
            password = password_entry.get()
            values = (user_id, name, email, gender, dob, password)
        else:
            name = name_entry.get()
            email = email_entry.get()
            gender = gender_var.get()
            dob = dob_entry.get()
            password = password_entry.get()
            values = (name, email, gender, dob, password, user_id)
        cursor.execute(query, values)
        connection.commit()
        print("Data operation successful!")
        messagebox.showinfo("Success", message)
    except mysql.connector.Error as e:
        print(f"Error during data operation: {e}")
        messagebox.showerror("Error", "An error occurred")
    finally:
        cursor.close()
        connection.close()


def open_add_script():
    subprocess.Popen(["python", "existing_user.py"])

def go_back():
    root.destroy()  # Close the current window

# Create the main window
root = tk.Tk()
root.title("User Registration")
# Make the window full screen
root.attributes('-fullscreen', True)

root.config(bg="#E3FDFD")  # Set background color

# Add button to go back
back_button = tk.Button(root, text="Back", command=go_back, font=("times new roman", 15), bg="#03A9F4")
back_button.place(x=10, y=10)  # Place at the top-left corner

# Create labels and entry fields for each field with increased font size
font_size = 14

user_id_label = tk.Label(root, text="User_id:", font=("times new roman", 15), bg="#E3FDFD")  # Set background color
user_id_label.place(relx=0.2, rely=0.2, anchor="center")
user_id_entry = tk.Entry(root, font=("times new roman", 15))
user_id_entry.place(relx=0.35, rely=0.2, anchor="center")

name_label = tk.Label(root, text="Name:", font=("times new roman", 15), bg="#E3FDFD")  # Set background color
name_label.place(relx=0.6, rely=0.2, anchor="center")
name_entry = tk.Entry(root, font=("times new roman", 15))
name_entry.place(relx=0.75, rely=0.2, anchor="center")

email_label = tk.Label(root, text="Email:", font=("times new roman", 15), bg="#E3FDFD")  # Set background color
email_label.place(relx=0.2, rely=0.3, anchor="center")
email_entry = tk.Entry(root, font=("times new roman", 15))
email_entry.place(relx=0.35, rely=0.3, anchor="center")

gender_label = tk.Label(root, text="Gender:", font=("times new roman", 15), bg="#E3FDFD")  # Set background color
gender_label.place(relx=0.6, rely=0.3, anchor="center")
gender_var = tk.StringVar(root)
gender_var.set("")  # Set initial value
gender_dropdown = tk.OptionMenu(root, gender_var, "Male", "Female", "Other")
gender_dropdown.config(font=("times new roman", 15))
gender_dropdown.place(relx=0.75, rely=0.3, anchor="center")

dob_label = tk.Label(root, text="D.O.B(yyyy/mm/dd):", font=("times new roman", 15), bg="#E3FDFD")  # Set background color
dob_label.place(relx=0.15, rely=0.4, anchor="center")
dob_entry = tk.Entry(root, font=("times new roman", 15))
dob_entry.place(relx=0.35, rely=0.4, anchor="center")

password_label = tk.Label(root, text="Password:", font=("times new roman", 15), bg="#E3FDFD")  # Set background color
password_label.place(relx=0.6, rely=0.4, anchor="center")
password_entry = tk.Entry(root, show="*", font=("times new roman", 15))
password_entry.place(relx=0.75, rely=0.4, anchor="center")

# Submit buttons for Insert and Update
insert_button = tk.Button(root, text="Insert", command=lambda: submit_data("Insert"), font=("times new roman", 15), bg="#03A9F4")
insert_button.place(relx=0.3, rely=0.7, anchor="center")

update_button = tk.Button(root, text="Update", command=lambda: submit_data("Update"), font=("times new roman", 15), bg="#03A9F4")
update_button.place(relx=0.5, rely=0.7, anchor="center")

# Button to open existing_user.py script
add_button = tk.Button(root, text="Existing User", command=open_add_script, font=("times new roman", 15), bg="#03A9F4")
add_button.place(relx=0.8, rely=0.95, anchor="sw")  # Place at the bottom-left corner

root.mainloop()
