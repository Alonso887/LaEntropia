import tkinter as tk
import Functions as fu
from tkinter import ttk 
from tkinter import filedialog as fd
from tkcalendar import Calendar

def select_file():
     global file_path
     filetypes = (('Excel files', '*.xlsx'),('All files', '*.*'))
     file_path.set(fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes))


def get_starting_date():
     global starting_date
     selected_date = cal.get_date()
     label_2.config(text=f"Selected starting date: {selected_date}")
     starting_date.set(selected_date)
     cal_window.destroy()

def show_starting_calendar():#This creates a toplevel window so the user selects a date more easily
     global cal_window
     cal_window = tk.Toplevel(main)
     cal_window.title("Select a date")

     global cal
     cal = Calendar(cal_window, selectmode="day", year=2023, month=1, day=1)
     cal.pack(pady=10)

     close_calendar = tk.Button(cal_window,text="Select date",font=("Tahoma",10),command=get_starting_date)
     close_calendar.pack(pady=10)

def get_ending_date():
     global ending_date
     selected_date = cal.get_date()
     label_3.config(text=f"Selected ending date: {selected_date}")
     ending_date.set(selected_date)
     cal_window.destroy()

def show_ending_calendar():#This creates a toplevel window so the user selects a date more easily
     global cal_window
     cal_window = tk.Toplevel(main)
     cal_window.title("Select a date")

     global cal
     cal = Calendar(cal_window, selectmode="day", year=2023, month=1, day=1)
     cal.pack(pady=10)

     close_calendar = tk.Button(cal_window,text="Select date",font=("Tahoma",10),command=get_ending_date)
     close_calendar.pack(pady=10)

main = tk.Tk()
main_x = 640#width of the main window
main_y = 360#height of the main window
main.geometry(f"{main_x}x{main_y}+{round(main.winfo_screenwidth()/2 - main_x/2)}+{round(main.winfo_screenheight()/2 - main_y/2)}")#centers the main window
main.resizable(False,False)
main.iconbitmap(r"imagenes\LaEntropia_icon.ico")#My icon of course, sucks a bit but doesn't matter baby :)

file_path = tk.StringVar()#String vars used for getting the info
person = tk.StringVar()#Sets the person you want info of or if you use ALL shows info about all people in the excel file
starting_date = tk.StringVar()#sets the starting point where we want dates from
ending_date = tk.StringVar()#the finish point where you want dates from

title_1 = tk.Label(main,text="Course Manager",font=("Tahoma",16))#Title goes first
title_1.place(x=10,y=0)

entry_1 = tk.Entry(main,font=("Tahoma",10),textvariable= file_path)#Entry for the file path
entry_1.place(x=15,y=40)
boton_1 = tk.Button(main,text="Select file",command=select_file)# File selector buton
boton_1.place(x=175,y=40)

entry_2 = tk.Entry(main,font=("Tahoma",10),textvariable=person)#Check the asigned var
entry_2.place(x=15,y=80)
label_1 = tk.Label(main,font=("Tahoma",10),text="Data origin",bd=1,relief="solid")
label_1.place(x=175,y=80)

label_2 = tk.Label(main,font=("Tahoma",10),text="Selected starting date: ")#Selects the starting date
label_2.place(x=15,y=120)
boton_2 = tk.Button(main,text="Select starting date",command=show_starting_calendar)
boton_2.place(x=225,y=120)

label_3 = tk.Label(main,font=("Tahoma",10),text="Selected ending date: ")#Selects the ending date
label_3.place(x=15,y=160)
boton_3 = tk.Button(main,text="Select ending date",command=show_ending_calendar)
boton_3.place(x=225,y=160)

main.mainloop()
