import openpyxl

path = r"C:\Users\Pranav Pawar\PycharmProjects\RMM_DataDriven\TestData\addCloudUser.xlsx"
workBook = openpyxl.load_workbook(path)
sheet = workBook.active
rows = sheet.max_row
cols = sheet.max_column
print("Row Count : ", rows)
print("Column Count : ", cols)
