from openpyxl import Workbook, load_workbook
wb = load_workbook(filename=r'C:\Users\aadri\Desktop\Escuela\Training_Matrix_2006.xlsx')
ws1 = wb["Crew"]
def get_name():#First this funtion looks for the name of the person we want data from
    name_wanted = input("Wich person do you need data from?\n> ")
    name_wanted = name_wanted.replace(" ","").lower()
    n = 7#Used just for the cell counting, we want the code to check all the names posible no matter the amount 
    while True:
        person_cell = [n,3]#cell we re looking in
        name_checking = ws1.cell(row=n,column=3).value
        try:
            name_checking = name_checking.replace(" ","").lower()
        except:
            print("Name not founded")
            break
        if name_checking == name_wanted:
            return person_cell
            break
        else:
            n += 1
def get_date_list():
    None
wb.save(r"C:\Users\aadri\Desktop\Escuela\Training_Matrix_2006_joke.xlsx")





