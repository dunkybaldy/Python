from tkinter import *

class Window(Frame):
    def __init__(self, name="", size=""):
        master = Tk()
        Frame.__init__(self, master)               
        self.master = master
        self.init_window(name, size)

    #Creation of init_window
    def init_window(self, name, size):
        # changing the title of our master widget      
        self.master.title(name)
        self.master.geometry(size)
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)
        # create the file object)
        file = Menu(menu)
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)
        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)
        # create the file object)
        edit = Menu(menu)
        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")
        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

    def MainLoop(self):
        self.master.mainloop()

    def client_exit(self):
        exit()

    def AddButton(self, text, function, x, y):
        '''(str, func, float, float) -> None'''
        button = Button(self.master, text=text, command=function)
        button.pack()
        button.place(x=x, y=y)

    def CreateEntryBox(self) -> str:
        entryBox = Entry(self.master, bd = 5)
        entryBox.pack()
        entryBox.place(x=(self.master.winfo_width() / 2), y=(self.master.winfo_height() / 2))
        return entryBox.get()