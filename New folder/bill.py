from tkinter import *
class Bill:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color= "#074463"
        self.title = Label(self.root, text="Billing System",bd=12,relief = GROOVE,bg=bg_color,fg="white", font=("times new roman", 30,"bold"),pady=2).pack(fill=X)

root = Tk()
obj = Bill(root)
root.mainloop()