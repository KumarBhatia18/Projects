# import xlsxwriter module
import xlsxwriter
from datetime import datetime
from SIPObject import SipObject
from dateutil.relativedelta import relativedelta
import xlwings as xw

def getweeklydata(inputStartDate, sipAmount, currentWorth):

    book = xlsxwriter.Workbook('C:\Kumar\Projects\sample\JavaBooks.xlsx')
    sheet = book.add_worksheet()

    startDate = datetime.fromisoformat(inputStartDate)
    endDate = datetime.now()
    print(endDate)
    sipObject = SipObject(startDate.strftime("%Y-%m-%d"), sipAmount)

    sipData = []
    sipData.append(sipObject)
    while endDate > startDate:
        if startDate.year == endDate.year and startDate.month == endDate.month:
            break
        startDate = startDate + relativedelta(months=1)
        sipObject = SipObject(startDate.strftime("%Y-%m-%d"), sipAmount)
        sipData.append(sipObject)

    print(len(sipData))

    # Rows and columns are zero indexed.
    row = 0
    column = 0
    # iterating through the content list
    for item in sipData:
        # write operation perform
        sheet.write(row, column, item.localDate)
        sheet.write(row, column + 1, item.amount)

        # incrementing the value of row by one with each iterations.
        row += 1

    sheet.write(row, column, endDate.strftime("%Y-%m-%d"))
    sheet.write(row, column + 1, currentWorth)
    row += 1
    xirr = "=XIRR("
    xirr = xirr + "B1:B" + str(row) + ","
    xirr = xirr + "A1:A" + str(row) + ")*100"

    sheet.write(row, column + 1, xirr)

    book.close()
    xirr = readExcel(row, column)
    print(round(xirr, 2))
    return round(xirr, 2)

def readExcel(row, column) :
    file_name = 'C:\Kumar\Projects\sample\JavaBooks.xlsx'
    wbxl = xw.Book(file_name)
    xirr = wbxl.sheets['Sheet1'].range('B' + str(row + 1)).value
    wbxl.close()
    return xirr

getweeklydata("2019-04-04", -2000, 116329)