from xlutils import copy
import xlrd
import file_path
print(file_path.get_path())
def writeExcel(row,value,col=10):
    path = file_path.get_path()
    file = xlrd.open_workbook(path)
    cp = copy.copy(file)
    sheet=cp.get_sheet(0)
    sheet.write(row,col,str(value))
    cp.save(path)
