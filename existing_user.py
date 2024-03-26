from tkinter import *
from tkinter import ttk
import mysql.connector

class UserClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Asset Management System")
        self.root.config(bg="#E3FDFD")
        self.root.focus_force()

        # Set the font size for the entire window
        self.root.option_add("*Font", "Roboto")

        # Set the window to fullscreen
        self.root.attributes('-fullscreen', True)

        # Search Frame
        SearchFrame = Frame(self.root, bg="#E3FDFD")
        SearchFrame.place(relx=0.5, rely=0.05, anchor="n")

        # Search Label
        search_label = Label(SearchFrame, text="Search User", font=("Goudy old style", 20, "bold"), bg="#E3FDFD")
        search_label.grid(row=0, column=0, padx=10, pady=5)

        # Entry for searching user
        self.search_entry = Entry(SearchFrame, font=("times new roman", 20), width=40)
        self.search_entry.grid(row=0, column=1, padx=10, pady=5)

        # Search button
        search_button = Button(SearchFrame, text="Search", font=("times new roman", 14), bg="#03A9F4", fg="white",
                               cursor="hand2", bd=1, relief=RIDGE, command=self.search_data)
        search_button.grid(row=0, column=2, padx=10, pady=5)

        # "Go Back" button
        back_button = Button(self.root, text="Back", font=("times new roman", 14), bg="#03A9F4", fg="white",
                             cursor="hand2", bd=1, relief=RIDGE, command=self.go_back)
        back_button.place(x=10, y=10)

        # Frame for buttons
        button_frame = Frame(self.root, bg="#E3FDFD")
        button_frame.place(relx=0.5, rely=0.95, anchor=CENTER)

        # Delete Button
        self.delete_button = Button(button_frame, text="Delete Selected", font=("times new roman", 14), bg="white", fg="black",
                                    cursor="hand2", bd=1, relief=RIDGE, command=self.delete_selected)
        self.delete_button.pack()

        # Bind hover events to change button color
        self.delete_button.bind("<Enter>", lambda event: self.delete_button.config(bg="red", fg="white"))
        self.delete_button.bind("<Leave>", lambda event: self.delete_button.config(bg="white", fg="black"))

        # Treeview to display data
        self.style = ttk.Style()
        self.style.configure("Treeview", font=("Roboto"))  # Set font for Treeview
        self.tree = ttk.Treeview(self.root, columns=("Name", "Email", "Gender", "D.O.B", "Password"), height=20, show="headings")
        self.tree.heading("#0", text="User ID")
        self.tree.heading("Name", text="Name")  # Increase font size for column header
        self.tree.heading("Email", text="Email")  # Increase font size for column header
        self.tree.heading("Gender", text="Gender")  # Increase font size for column header
        self.tree.heading("D.O.B", text="D.O.B")  # Increase font size for column header
        self.tree.heading("Password", text="Password")  # Increase font size for column header
        self.tree.place(relx=0.5, rely=0.2, anchor="n")

        # Add lines between columns
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_column(c, False))
            self.tree.column(col, width=180, stretch=True)  # Increase column width

        # Fetch data from MySQL database
        self.fetch_data()

    def fetch_data(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="K@rtik2004",
            database="assettracking"
        )
        cursor = connection.cursor()

        query = "SELECT user_id, name, email, gender, dob, password FROM users"
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            self.tree.insert("", "end", text=row[0], values=row[1:])

        connection.close()

    def search_data(self):
        search_query = self.search_entry.get()

        # Clear existing items in the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="K@rtik2004",
            database="assettracking"
        )
        cursor = connection.cursor()

        query = "SELECT user_id, name, email, gender, dob, password FROM users WHERE name LIKE %s"
        cursor.execute(query, (f'%{search_query}%',))
        rows = cursor.fetchall()

        for row in rows:
            self.tree.insert("", "end", text=row[0], values=row[1:])

        connection.close()

    def go_back(self):
        self.root.destroy()

    def delete_selected(self):
        selected_item = self.tree.selection()
        if selected_item:
            user_id = self.tree.item(selected_item)['text']
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="K@rtik2004",
                database="assettracking"
            )
            cursor = connection.cursor()

            query = "DELETE FROM users WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            connection.commit()

            connection.close()

            # Remove selected item from treeview
            self.tree.delete(selected_item)

if __name__ == "__main__":
    root = Tk()
    obj = UserClass(root)
    root.mainloop()
