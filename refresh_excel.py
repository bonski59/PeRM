# most of this will be a test environment to verify this works

import time

import win32com.client as win32


def refresh(filepath):
    """this is difficult to test due to my lack of experience in excel.
     however it should work as intended with the UFP files."""

    """# Start an instance of Excel
    xlapp = win32com.client.DispatchEx("Excel.Application")

    # Open the workbook in said instance of Excel
    wb = xlapp.workbooks.open(filepath)

    # Optional, e.g. if you want to debug
    # xlapp.Visible = True

    # Refresh all data connections.
    wb.RefreshAll()
    wb.Save()

    # Quit
    xlapp.Quit()"""
    # TODO: Fix this so it doesnt hold up operations
            # could it be fixed with a foreign  macro in each excel file?
    Xlsx = win32.DispatchEx('Excel.Application')
    Xlsx.DisplayAlerts = False
    Xlsx.Visible = False
    book = Xlsx.workbooks.open(filepath)
    # Refresh my two sheets
    # time.sleep(2)
    book.RefreshAll()
    # Xlsx.CalculateUntilAsyncQueriesDone()  # this will actually wait for the excel workbook to finish updating
    time.sleep(5)
    book.Save()
    book.Close()
    Xlsx.Quit()

    return  # just need to find a way to open the excel doc per the flow chart request

