from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os

#-------------------------------------------------------------------------
directory = r""
files = []
buttons_names = []
#-------------------------------------------------------------------------
def direct():
    global directory
    global label_debug
    global files
    try:
        directory = filedialog.askdirectory()
        files = set([file.split(".")[-1] for file in os.listdir(directory) if "." in file])
        print(files)
        if not files:
            directory = r""
            label_debug.config(text = "Dir_Error_No_Files",fg = "Red")
        else:
            label_debug.config(text = "Dir_Selected!",fg = "Blue")
    except:
        label_debug.config(text = "Dir_Error",fg = "Red")

def Thor(arg):
    return "selected" in arg.state()
        
def new_wind():
    global label_debug
    global files
    global buttons_names
    try:
        global directory
        new_app = Tk()
        new_app.title("Select Files")
        new_app.geometry("400x150")
        buttons_names = [ttk.Checkbutton(new_app, text = name, variable="") for name in files]
        line = -1
        col = 1
        for button in buttons_names:
            if col == 1:
                col = 0
                line += 1
            else:
                col = 1
            button.grid(row = line, column = col)
        new_app.mainloop()
    except Exception as e:
        print (e)
        label_debug.config(text = "Dir_Error",fg = "Red")



def run():
    pass
#-------------------------------------------------------------------------
app = Tk()
app.title("Folder Slayer")
app.geometry("700x300")
#-------------------------------------------------------------------------
button_dir = Button(app, text = "Select", font=("Calibri",10), activebackground = "blue", relief = "groove", command = direct)
button_dir.grid(row = 0, column = 2)

#button_run = Button(app, text = "Run", fg = "Red", command = run)
#button_run.grid(row = 1, column = 1)

button_files = Button(app, text = "Select", font = ("Calibri",10), activebackground = "blue", relief = "groove", command = new_wind)
button_files.grid(row = 2, column = 2)
#-------------------------------------------------------------------------

label_dir = Label(app, text = "Choose a directory: ", padx = 10, pady = 20)
label_dir.grid(row = 0, column = 0)

label_files = Label(app, text = "Choose files")
label_files.grid(row = 2, column = 0)

label_debug = Label(app,font = ("Calibri",10))
label_debug.grid(row = 3, column = 2)



#-------------------------------------------------------------------------
app.mainloop()

