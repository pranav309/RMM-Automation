import openpyxl
import time
import paramiko

# workBook = openpyxl.load_workbook(r"C:\Users\Pranav Pawar\PycharmProjects\RMM_DataDriven\TestData\allInOne\allInOne.xlsx")
# sheet = workBook.active
# rows = sheet.max_row
# cols = sheet.max_column
#
# for r in range(3, rows + 1):
#     operation = sheet.cell(row=r, column=1).value.lower()
#     if operation.find("add") != -1 and operation.find("wave") != -1:
#         print("1")
#     else:
#         print("0")
#     print(operation)

start = "NA"  # Initial value of 'start'

if start == "NA":
    start = 3  # Update 'start' to 3 if the current value is "NA"

print(start)
