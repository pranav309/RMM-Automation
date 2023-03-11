import openpyxl

workBook = openpyxl.load_workbook(r"C:\Users\Pranav Pawar\PycharmProjects\RMM_DataDriven\TestData\setAutoprovisionAndNIC.xlsx")
sheet = workBook.active
rows = sheet.max_row

print("Number Of Rows : ", rows)
