# most of this will be a test environment to verify this works


import time

import pandas as pd
import pywintypes
import win32com.client as win32

import folders
import read_data as rd


def refresh(xlsx_filepath):
    Xlsx = win32.DispatchEx('Excel.Application')
    Xlsx.DisplayAlerts = False
    Xlsx.Visible = False
    book = Xlsx.workbooks.open(xlsx_filepath)
    # Refresh my two sheets
    # time.sleep(2)
    try:
        book.RefreshAll()
    except pywintypes:
        print("An error occurred with file {}".format(xlsx_filepath))
    # Xlsx.CalculateUntilAsyncQueriesDone()  # this will actually wait for the excel workbook to finish updating
    time.sleep(5)  # TODO: this is temporary
    book.Save()
    book.Close()
    Xlsx.Quit()

    print("REFRESHED COMPLETE: {}".format(xlsx_filepath))
    return  # just need to find a way to open the excel doc per the flow chart request


def refresh_xlsx_paths():
    """This explicit function is used to iterate through the REPORT_DETAILS.csv and refreshes
    all of the xlsx files needed for the future email build"""
    df = pd.read_csv(folders.Paths.reportCSV,
                     delimiter=',',
                     engine="python")
    row_count = int(df.shape[0])        # defines num of rows in csv
    # print(row_count)
    dict_df = df.to_dict()              # turns csv into dict so we can reference values by headers
    # print(dict_df)                    # prints dict

    i = 0
    while i < row_count:
        xlsx_fp = dict_df['Report_Filepath'][i]
        if str(xlsx_fp) == 'nan':       # multiple conditions
            pass
        else:

            refresh(xlsx_fp)
            if not rd.confirm_xlsx_verification(xlsx_fp):
                print("FALSE VERIFICATION STATUS: {}".format(xlsx_fp))  # TODO: Define verification status
            else:
                print("TRUE VERIFICATION STATUS: {}".format(xlsx_fp))
        i += 1  # iterates line by line

    return  # just need to find a way to open the excel doc per the flow chart request
