import tkinter as tk
import Functions as fu
from tkinter import ttk
def print_key():
    print("sexoooo")

main = tk.Tk()
main_x = 640#width of the main window
main_y = 360#height of the main window
main.geometry(f"{main_x}x{main_y}+{round(main.winfo_screenwidth()/2 - main_x/2)}+{round(main.winfo_screenheight()/2 - main_y/2)}")
main.resizable(False,False)

main.iconbitmap(r"imagenes\LaEntropia_icon.ico")

ttk.Label(main,text="Hello world").pack()

boton_1 = ttk.Button(main,text="Boton",command=print_key)
boton_1.focus()
boton_1.pack(expand=True)

main.mainloop()
