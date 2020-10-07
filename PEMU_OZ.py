#PEMU OldManOZ version

from tkinter import *
from tkinter import filedialog

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()


        self.label = Label(frame, text="Please Select the location of CEMU")
        self.label.pack(side=LEFT)

        self.choose_cemu = Button(frame, text="Browse", command=self.choose_cemu)
        self.choose_cemu.pack(side=LEFT)
        self.client_exit = Button(frame, text="Exit",command=self.client_exit)
        self.client_exit.pack(side=LEFT)

    def client_exit(self):
        root.destroy()
    def choose_cemu(self):
        root.filename = filedialog.askopenfilename(filetypes = (("Cemu Executable","*.exe"),("all files","*.*")))
        print (root.filename)
root = Tk()
root.geometry("400x100")
root.title("Welcome to PEMU!")
app = App(root)

root.mainloop()