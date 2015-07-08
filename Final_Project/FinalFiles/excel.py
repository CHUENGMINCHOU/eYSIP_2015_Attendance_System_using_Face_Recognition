import datetime
import xlwt
import xlrd
import xlutils.copy

currentRow = 0

font_head = xlwt.Font()
font_head.name = 'Times New Roman'
#font_head.colour_index = 2
font_head.bold = True
font_head.height = 220

font_data = xlwt.Font()
font_data.name = 'Times New Roman'
#font_data.colour_index = 2
font_data.bold = False
font_data.height = 200

style_head = xlwt.XFStyle()
style_head.font = font_head

style_data = xlwt.XFStyle()
style_data.font = font_data

try:
    #Open the existing workbook. This workbook is read only
    book_rd = xlrd.open_workbook("LogBook.ods")
    #Convert it to the writable book that can be written using xlwt library functions.
    book_wt = xlutils.copy.copy(book_rd)

except IOError as e:
    book_wt = xlwt.Workbook()  
    activeSheet = book_wt.add_sheet(datetime.datetime.now().strftime("%d %b %Y"))    
    activeSheet.write(0, 0, "NAME", style_head)
    activeSheet.write(0, 1, "ROLL", style_head)
    activeSheet.write(0, 2, "Entry", style_head)
    book_wt.save("LogBook.ods")    
    book_wt = xlrd.open_workbook("LogBook.ods")

    book_rd = xlrd.open_workbook("LogBook.ods")
    #Convert it to the writable book that can be written using xlwt library functions.
    book_wt = xlutils.copy.copy(book_rd)
    
n = book_rd.nsheets

#If the last sheet is from the current day, then update the same sheet.
if datetime.datetime.now().strftime("%d %b %Y") == book_rd.sheet_by_index(n - 1).name:
    activeSheet = book_wt.get_sheet(n - 1)
    currentRow = book_rd.sheet_by_index(n - 1).nrows

#Otherwise, create a new sheet. Also add column headers in this case
else:
    activeSheet = book_wt.add_sheet(datetime.datetime.now().strftime("%d %b %Y"))
    activeSheet.write(0, 0, "NAME", style_head)
    activeSheet.write(0, 1, "ROLL", style_head)
    activeSheet.write(0, 2, "Entry", style_head)
    currentRow = 1

    
def new_entry(name, roll, time):
    global currentRow
    activeSheet.write(currentRow, 0, name, style_data)
    activeSheet.write(currentRow, 1, roll, style_data)
    activeSheet.write(currentRow, 2, time, style_data)    
    currentRow = currentRow + 1

def save_excel():
    book_wt.save("LogBook.ods")

def close_excel():
    book_wt.save("LogBook.ods")  
