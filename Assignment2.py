import xlwt
import xlrd
#import pdb; pdb.set_trace()
workbook = xlrd.open_workbook('assignment.xlsx')
sheet = workbook.sheet_by_index(0)

data = [sheet.cell_value(0, col) for col in range(sheet.ncols)]
data1 = [sheet.cell_value(1, row) for row in range(sheet.nrows)]
data2 = [sheet.cell_value(2, row) for row in range(sheet.nrows)]
data3 = [sheet.cell_value(3, row) for row in range(sheet.nrows)]
data4 = [sheet.cell_value(4, row) for row in range(sheet.nrows)]
data5 = [sheet.cell_value(5, row) for row in range(sheet.nrows)]
data6 = [sheet.cell_value(6, row) for row in range(sheet.nrows)]
data7 = [sheet.cell_value(7, row) for row in range(sheet.nrows)]
data8 = [sheet.cell_value(8, row) for row in range(sheet.nrows)]
data9 = [sheet.cell_value(9, row) for row in range(sheet.nrows)]
data10 = [sheet.cell_value(10, row) for row in range(sheet.nrows)]

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('test')

for index, value in enumerate(data):
    sheet.write(0, index, value)

for index, value in enumerate(data1):
    sheet.write(1, index, value)

for index, value in enumerate(data2):
    sheet.write(2, index, value)

for index, value in enumerate(data3):
    sheet.write(3, index, value)

for index, value in enumerate(data4):
    sheet.write(4, index, value)

for index, value in enumerate(data5):
    sheet.write(5, index, value)

for index, value in enumerate(data6):
    sheet.write(6, index, value)

for index, value in enumerate(data7):
    sheet.write(7, index, value)

for index, value in enumerate(data8):
    sheet.write(8, index, value)

for index, value in enumerate(data9):
    sheet.write(9, index, value)

for index, value in enumerate(data10):
    sheet.write(10, index, value)

workbook.save('assignmentw.xlsx')
