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
            print(person_cell)
            return person_cell
            break
        else:
            n += 1
def get_date_list(person_cell):#this one uses get_name to locate the persons date
    course_cell=[5,8]#where the courses start
    date_list = []
    while True:
        check_course = ws1.cell(row=course_cell[0],column=course_cell[1]).value#the cell we are going to check
        if check_course == None:
            break
        date_list.append(ws1.cell(row=person_cell[0],column=course_cell[1]).value)
        course_cell[1] += 1
    return date_list

a=get_date_list(get_name())
print(a)
wb.save(r"C:\Users\aadri\Desktop\Escuela\Training_Matrix_2006_joke.xlsx")





