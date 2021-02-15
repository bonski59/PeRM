# most of this will be a test environment to verify this works

import os
import win32com.client

cwd = os.getcwd()

all_reports = r'{}\dataManagement\reports_xlsx'.format(cwd)
excelDoc = r"{}\mainExcel.xlsx".format(os.getcwd())


def refresh(filepath):
    """this is difficult to test due to my lack of experience in excel.
     however it should work as intended with the UFP files."""

    # Start an instance of Excel
    xlapp = win32com.client.DispatchEx("Excel.Application")

    # Open the workbook in said instance of Excel
    wb = xlapp.workbooks.open(filepath)

    # Optional, e.g. if you want to debug
    # xlapp.Visible = True

    # Refresh all data connections.
    wb.RefreshAll()
    wb.Save()

    # Quit
    xlapp.Quit()

    return  # just need to find a way to open the excel doc per the flow chart request


def refresh_all_reports():
    for root, dirs, files in os.walk(all_reports):
        for file in files:
            refresh(os.path.join(root, file))
