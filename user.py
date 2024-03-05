from tkinter import*
from PIL import Image,ImageTk
class UserClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Asset Management System")
        self.root.config(bg="#E3FDFD")
        self.root.focus_force()
        
        #search
        SearchFrame=LabelFrame(self.root,text="Search User",font=("Goudy old style",12,"bold"),bd=2,relief=GROOVE, bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)
        
if __name__ == "__main__":
    root=Tk()
    obj=UserClass(root)
    root.mainloop()