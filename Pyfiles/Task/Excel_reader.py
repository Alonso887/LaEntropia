from openpyxl import Workbook
from openpyxl import load_workbook

wb = Workbook()
wb = load_workbook(filename=r"C:\Users\aadri\Desktop\Escuela\Promedio calificaciones Alo.xlsx")
worksheets = wb.sheetnames
ws1 = wb.active
ws1['A1'] = 8
wb.save("Promedio_calificaciones_OMG.xlsx")