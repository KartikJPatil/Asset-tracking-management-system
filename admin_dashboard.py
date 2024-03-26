from tkinter import *
from PIL import Image, ImageTk
import subprocess
import mysql.connector


class AMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Asset Management System")
        self.root.config(bg="#E3FDFD")

        # Make the window full screen
        self.root.attributes('-fullscreen', True)

        # title
        self.icon_title = PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="Asset Management System", image=self.icon_title, compound=LEFT, font=("times new roman", 40, "bold"), bg="#71C9CE", fg="white", anchor="w", padx=20).pack(fill=X)

        # button logout
        btn_logout = Button(self.root, text="Logout", command=self.logout, font=("times new roman", 15, "bold"), bg="#579BB1", cursor="hand2").place(x=1380, y=10, height=50, width=150)

        # header
        self.header = Label(self.root, text="Welcome to Asset Management System")
        self.header.place(x=0, y=70, relwidth=1, height=30)

        # Menu
        self.MenuLogo = Image.open("images/menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="#A6E3E9")
        LeftMenu.place(x=0, y=102, width=200, height=590)

        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#71C9CE").pack(side=TOP, fill=X)

        btn_User = Button(LeftMenu, text="User", command=self.user, padx=15, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)

        btn_exit = Button(LeftMenu, text="Exit", padx=15, anchor="w", font=("times new roman", 20, "bold"), bg="white",  bd=3, cursor="hand2", command=self.exit_program).pack(side=TOP, fill=X)

        # content
        self.lbl_user = Label(self.root, text="Total Users\n[ 0 ]", bd=5, relief=GROOVE, bg="#A5DEE5", fg="white",font=("goudy old style", 20, "bold"))
        self.lbl_user.place(x=300, y=120, height=150, width=300)

        # footer
        lbl_footer = Label(self.root, text="Asset Management System | Group 11", font=("times new roman", 7),fg="black", bg="white").pack(side=BOTTOM, fill=X)

        # Fetch count of users and assets
        self.fetch_count()

    def fetch_count(self):
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="K@rtik2004",
            database="assettracking"
        )
        cursor = connection.cursor()

        # Fetch count of users
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]

        connection.close()

        # Update labels with the fetched counts
        self.lbl_user.config(text=f"Total Users\n[ {user_count} ]")

    def user(self):
        subprocess.Popen(["python", "create_user.py"])

    def exit_program(self):
        root.destroy()  # Close the window

    def logout(self):
        self.root.destroy()
        subprocess.Popen(["python", "admin_login.py"])


if __name__ == "__main__":
    root = Tk()
    obj = AMS(root)
    root.mainloop()
