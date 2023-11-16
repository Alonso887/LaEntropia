import tkinter as tk
import Functions as fu
from tkinter import ttk, font
from tkinter import filedialog as fd

def select_file():
     global file_path
     filetypes = (('Excel files', '*.xlsx'),('All files', '*.*'))
     file_path.set(fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes))

main = tk.Tk()
main_x = 640#width of the main window
main_y = 360#height of the main window
main.geometry(f"{main_x}x{main_y}+{round(main.winfo_screenwidth()/2 - main_x/2)}+{round(main.winfo_screenheight()/2 - main_y/2)}")
main.resizable(False,False)
main.iconbitmap(r"imagenes\LaEntropia_icon.ico")
file_path = tk.StringVar()

title_1 = ttk.Label(main,text="Course Manager",font=("Tahoma",16))
title_1.pack(anchor=tk.W,padx=10,pady=5)

entry_1 = ttk.Entry(main,font=("Tahoma",10),textvariable= file_path)
entry_1.pack(anchor=tk.NW,padx=15,pady=5,side=tk.LEFT)

boton_1 = ttk.Button(main,text="Open file",command=select_file)
boton_1.pack(anchor=tk.NW,padx=15,pady=5,side=tk.LEFT)

main.mainloop()
