import openpyxl as xl

wb = xl.load_workbook("transaction.xlsx")
sheet = wb["Sheet1"]

cell = sheet.cell(1, 1)
print(cell.value)
print(sheet.max_row)

for row in range(2, sheet.max_row + 1):
    price_cell = sheet.cell(row, 3)

    if isinstance(price_cell.value, (int, float)):
        corrected_price_cell = sheet.cell(row, 4)
        corrected_price_cell.value = price_cell.value * 0.9

wb.save("transaction2.xlsx")

