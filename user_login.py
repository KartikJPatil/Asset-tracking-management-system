from tkinter import *
import customtkinter as ctk
import tkinter.messagebox as tkmb
import mysql.connector
import subprocess

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1700x850+0+0")
app.title("LOGIN")
# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'K@rtik2004',
    'database': 'assettracking'
}

def login():
    # Get email and password from the entry fields
    entered_email = user_entry.get()
    entered_password = user_pass.get()

    print("Entered Email:", entered_email)  # Debug print

    # Connect to the database
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Query to fetch user details based on email
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (entered_email,))

        user_data = cursor.fetchone()

        # Consume all remaining rows in the result set
        cursor.fetchall()

        if user_data:
            db_email, db_password = user_data[2], user_data[5]  # Assuming the 'email' and 'password' columns are at index 2 and 5 respectively
            if entered_password == db_password:
                tkmb.showinfo(title="Login Successful", message="Welcome to Asset Management System")
                # Open the dashboard.py script
                subprocess.Popen(["python", "user_dashboard.py"])
                app.destroy()  # Close the login window
            else:
                tkmb.showerror(title="Login Failed", message="Incorrect password")
        else:
            tkmb.showerror(title="Login Failed", message="User not found")

    except mysql.connector.Error as err:
        print("Database Error:", err)
        tkmb.showerror(title="Database Error", message="Could not connect to the database")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

label = ctk.CTkLabel(app, text="LOGIN\n Asset Tracking Management System", font=("times new roman", 45, "bold"))
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Please Enter Email & Password')
label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Email")
user_entry.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
user_pass.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

app.mainloop()
