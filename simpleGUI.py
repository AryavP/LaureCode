#simple GUI

from Tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.button1 = Button(self, text="fuck")
        self.button1.grid()

        self.button2 = Button(self)
        self.button2.grid()
        self.button2.configure(text = "you")

root = Tk()
root.title("object")
root.geometry("1000x500")
app = Application(root)

root.mainloop()
