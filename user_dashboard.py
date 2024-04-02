from tkinter import *
from PIL import Image, ImageTk
import subprocess
from check_assets import check_assets

class AMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Asset Management System")
        self.root.config(bg="#E3FDFD")

        # Make the window full screen
        self.root.attributes('-fullscreen', True)

        # Title
        self.icon_title = PhotoImage(file="images/logo1.png")
        title = Label(self.root, text="Asset Management System", image=self.icon_title, compound=LEFT, font=("times new roman", 40, "bold"), bg="#71C9CE", fg="white", anchor="w", padx=20)
        title.pack(fill=X)

        # Button logout
        btn_logout = Button(self.root, text="Logout", command=self.logout, font=("times new roman", 15, "bold"), bg="#579BB1", cursor="hand2")
        btn_logout.place(x=1380, y=10, height=50, width=150)


        self.dark_mode_state = False
        self.dark_mode_btn = Button(self.root, text='🌙', command=self.toggle_dark_mode, font=("times new roman", 20))
        self.dark_mode_btn.place(x=1490, y=80, width=40, height=40)

        # Menu
        self.MenuLogo = Image.open("images/menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="#A6E3E9")
        LeftMenu.place(x=0, y=70, width=200, height=250)

        lbl_menuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#71C9CE")
        lbl_menu.pack(side=TOP, fill=X)

        button_frame = Frame(root)
        button_frame.pack(side=LEFT, padx=2, pady=205, anchor='sw')

        # Create menu buttons
        add_assets_btn = Button(button_frame, text="Add Assets", padx=22, pady=10, font=('Arial', 14), command=self.run_api)
        add_assets_btn.pack(fill=X, padx=10, pady=5, anchor='w')

        check_assets_btn = Button(button_frame, text="Check Assets", padx=22, pady=10, font=('Arial', 14), command=check_assets)
        check_assets_btn.pack(fill=X, padx=10, pady=5, anchor='w')

        statistics_btn = Button(button_frame, text="Statistics", padx=22, pady=10, font=('Arial', 14), command=self.open_statistics)
        statistics_btn.pack(fill=X, padx=10, pady=5, anchor='w')

        help_btn = Button(button_frame, text="Help!", padx=22, pady=10, font=('Arial', 14))
        help_btn.pack(fill=X, padx=10, pady=5, anchor='w')

        exit_btn = Button(button_frame, text="Exit", padx=22, pady=10, font=('Arial', 14), command=self.exit_program)
        exit_btn.pack(fill=X, padx=10, pady=5, anchor='w')


    def run_api(self):
        subprocess.Popen(["python", "add_assets.py"])

    def open_statistics(self):
        subprocess.Popen(["python", "statistics.py"])

    def logout(self):
        self.root.destroy()
        subprocess.Popen(["python", "common_login.py"])

    def exit_program(self):
        root.destroy()  # Close the window

    def toggle_dark_mode(self):
        if self.dark_mode_state:
            # Light mode
            self.root.config(bg="#E3FDFD")
            self.dark_mode_btn.config(text='🌙')
            self.dark_mode_btn.config(fg="black")
        else:
            # Dark mode
            self.root.config(bg="#2E2E2E")
            self.dark_mode_btn.config(text='🌙')
            self.dark_mode_btn.config(fg="white")
        self.dark_mode_state = not self.dark_mode_state

if __name__ == "__main__":
    root = Tk()
    obj = AMS(root)
    root.mainloop()
