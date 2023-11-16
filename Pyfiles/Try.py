import tkinter as tk
from tkinter import filedialog

class FileSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Selector")

        # Create a StringVar to store the file path
        self.file_path_var = tk.StringVar()

        # Create Entry widget to display the selected file path
        self.file_path_entry = tk.Entry(root, textvariable=self.file_path_var, width=40)
        self.file_path_entry.grid(row=0, column=0, padx=10, pady=10)

        # Create buttons to open the file dialog and use the selected file
        open_button = tk.Button(root, text="Open File", command=self.open_file)
        open_button.grid(row=0, column=1, padx=10, pady=10)

        use_button = tk.Button(root, text="Use File", command=self.use_file)
        use_button.grid(row=1, column=0, columnspan=2, pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        # Update the StringVar with the selected file path
        self.file_path_var.set(file_path)

    def use_file(self):
        # Get the file path from the StringVar
        file_path = self.file_path_var.get()
        # Now you can use the file_path variable in your program as needed
        print("Selected file path:", file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSelectorApp(root)
    root.mainloop()

