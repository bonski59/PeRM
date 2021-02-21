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
    # time.sleep(1)  # TODO: this is temporary
    book.Save()
    book.Close()
    Xlsx.Quit()

    print("REFRESHED COMPLETE: {}".format(xlsx_filepath))
    return  # just need to find a way to open the excel doc per the flow chart request




def refresh_xlsx_paths():
    """This explicit function is used to iterate through the REPORT_DETAILS.csv and refreshes
    all of the xlsx files needed for the future email build"""
    df = pd.read_csv(folders.Paths.reportCSV, index_col="INDEX_ID")
    df_status = df['Report_Filepath'].loc[df['REPORT_STATUS'] == 'ACTIVE']  # Dependant on correct string format
    # print(df_status.count())
    print(df_status)
    status_true = []
    status_false = []
    for i in df_status:
        # refresh(i)
        if not rd.confirm_xlsx_verification(i):
            status_false.append(i)
            # update pandas verification column to False .iloc "file"

        else:
            status_true.append(i)

    df_false = df['Verification_Status'].loc[df['Report_Filepath'].isin(status_false)]
    df_true = df['Verification_Status'].loc[df['Report_Filepath'].isin(status_true)]

    upd_false = pd.Series(0, name='Verification_Status')
    df.update(upd_false)
    print()
    input()
    true_val = []
    true_index = df_true.index.tolist()
    for i in true_index:
        true_val.append(1)
    upd = pd.Series(true_val, name='Verification_Status', index=true_index)
    df.update(upd)
    print(df['Verification_Status'])


    # print(df_true)
    df.to_csv(folders.Paths.reportCSV)

    return
# testing
refresh_xlsx_paths()

# testing
def time_refresh_xlsx_files():
    import os
    # fp = r"C:\Users\us160212\Documents\GitHub\PeRM\dataManagement\LiveData\reports_xlsx\New SKU Sales.xlsx"
    clock = time.time()
    """for root, dirs, files in os.walk(folders.Paths.reports_xlsx):

        for f in files:"""
    df = pd.read_csv(folders.Paths.reportCSV)
    df = df['Report_Filepath'].loc[df['REPORT_STATUS'] == 'ACTIVE']  # Dependant on correct string format
    # print(df)
    for i in df:
        print(i)
        x = time.time()
        refresh(i)
        y = time.time()
        t = y - x
        print("{} :Time elapsed to refresh {}".format(t, i))
    now = time.time()
    total_time = now - clock
    print("{} : Total time elapsed for entire .\\reports_xlsx folder".format(total_time))
    print("{} : average Time per file".format(total_time / len(os.listdir(folders.Paths.reports_xlsx))))
    return
# testing
# time_refresh_xlsx_files()

