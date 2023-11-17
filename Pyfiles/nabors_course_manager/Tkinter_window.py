import tkinter as tk
from tkinter import ttk 
import Functions as fu
from tkinter import filedialog as fd
from tkcalendar import Calendar

def select_file():
     global file_path
     filetypes = (('Excel files', '*.xlsx'),('All files', '*.*'))
     file_path.set(fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes))


def get_starting_date():
     global starting_date
     selected_date = cal.get_date()
     starting_date_label.config(text=f"Selected starting date: {selected_date}")
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
     ending_date_label.config(text=f"Selected ending date: {selected_date}")
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

def show_info(number):
     info_window = tk.Toplevel(main)
     info_window.title("Data otigin info")
     info = ""

     if number == 1:
          info = "Data origin is used when you want info from an specific person, write here the exact name you see in the excel file"
     elif number == 2:
          info = "Course cell is used to indicate where the first course appears, write here it's coordinates like this: row,column"
     elif number== 3:
          info = "Name cell is used to indicate where the first  name appears, write here it's coordinates like this: row,column"
     elif number == 4:
          info = "Date cell is used to indicate where the first date appears, write here it's coordinates like this: row,column"
     info_label = tk.Label(info_window,font=("Tahoma",9),text=info)
     info_label.pack()

     close_info_window = tk.Button(info_window,font=("Tahoma",9),text="Close",command=info_window.destroy)
     close_info_window.pack()

main = tk.Tk()
main_x = 640#width of the main window
main_y = 360#height of the main window
main.geometry(f"{main_x}x{main_y}+{round(main.winfo_screenwidth()/2 - main_x/2)}+{round(main.winfo_screenheight()/2 - main_y/2)}")#centers the main window
main.resizable(False,False)
main.iconbitmap(r"imagenes\LaEntropia_icon.ico")#My icon of course, sucks a bit but doesn't matter baby :)

file_path = tk.StringVar()#String vars used for getting the info
person = tk.StringVar()#Sets the person you want info from if you want info about just a single person
starting_date = tk.StringVar()#sets the starting point where we want dates from
ending_date = tk.StringVar()#the finish point where you want dates from
course_cell = tk.StringVar()#indicates where the course starts
name_cell = tk.StringVar()#indicates where the the names start
date_cell = tk.StringVar()#

title = tk.Label(main,text="Course Manager",font=("Tahoma",16))#Title goes first
title.place(x=10,y=0)

file_path_entry = tk.Entry(main,font=("Tahoma",10),textvariable= file_path)#Entry for the file path
file_path_entry.place(x=15,y=40)
file_path_boton = tk.Button(main,text="Select file",command=select_file)# File selector buton
file_path_boton.place(x=175,y=40)

starting_date_label = tk.Label(main,font=("Tahoma",10),text="Selected starting date: ")#Selects the starting date
starting_date_label.place(x=13,y=80)
starting_date_boton = tk.Button(main,text="Select starting date",command=show_starting_calendar)
starting_date_boton.place(x=225,y=80)

ending_date_label = tk.Label(main,font=("Tahoma",10),text="Selected ending date: ")#Selects the ending date
ending_date_label.place(x=13,y=120)
ending_date_boton = tk.Button(main,text="Select ending date",command=show_ending_calendar)
ending_date_boton.place(x=225,y=120)

subtitle = tk.Label(main,font=("Tahoma",12),text="Advanced confiurations (Optional)")
subtitle.place(x=10,y=150)

person_entry = tk.Entry(main,font=("Tahoma",10),textvariable=person)#Check the asigned var
person_entry.place(x=15,y=190)
person_label = tk.Label(main,font=("Tahoma",10),text="Data origin",bd=1,relief="solid")
person_label.place(x=175,y=190)
person_button = tk.Button(main,font=("Tahoma",10),text="i",command=lambda:show_info(1))
person_button.place(x=245,y=185)

course_cell_entry = tk.Entry(main,font=("Tahoma",10),textvariable=course_cell)
course_cell_entry.place(x=15,y=225)
course_cell_label = tk.Label(main,font=("Tahoma",10),text="Course cell",bd=1,relief="solid")
course_cell_label.place(x=175,y=225)
course_cell_button = tk.Button(main,font=("Tahoma",10),text="i",command=lambda:show_info(2))
course_cell_button.place(x=245,y=220)

name_cell_entry = tk.Entry(main,font=("Tahoma",10),textvariable=name_cell)
name_cell_entry.place(x=15,y=260)
name_cell_label = tk.Label(main,font=("Tahoma",10),text="Name cell",bd=1,relief="solid")
name_cell_label.place(x=175,y=260)
name_cell_button = tk.Button(main,font=("Tahoma",10),text="i",command=lambda:show_info(3))
name_cell_button.place(x=245,y=255)

date_cell_entry = tk.Entry(main,font=("Tahoma",10),textvariable=date_cell)
date_cell_entry.place(x=15,y=295)
date_cell_label = tk.Label(main,font=("Tahoma",10),text="Date cell",bd=1,relief="solid")
date_cell_label.place(x=175,y=295)
date_cell_button = tk.Button(main,font=("Tahoma",10),text="i",command=lambda:show_info(4))
date_cell_button.place(x=245,y=290)

main.mainloop()

a = fu.get_data(file_path.get(),person.get(),course_cell.get(),date_cell.get(),name_cell.get(),starting_date.get(),ending_date.get())
print(a)