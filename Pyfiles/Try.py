import tkinter as tk 
from tkcalendar import Calendar

root = tk.Tk()
root.geometry("800x600")

cal = Calendar(root,selectmode="day", year=2023, month=1, day=1)
cal.pack(pady=10)

root.mainloop()

