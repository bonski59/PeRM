import pandas as pd
import pywintypes
import win32com.client as win32

import folders
import read_data as rd
from admin import admin_print


def refresh(xlsx_filepath):
    Xlsx = win32.DispatchEx('Excel.Application')
    Xlsx.DisplayAlerts = False
    Xlsx.Visible = False
    book = Xlsx.workbooks.open(xlsx_filepath)

    try:
        book.RefreshAll()
    except pywintypes:
        admin_print("An error occurred with file {}".format(xlsx_filepath))

    book.Save()
    book.Close()
    Xlsx.Quit()

    admin_print("REFRESHED COMPLETE: {}".format(xlsx_filepath))
    return  # just need to find a way to open the excel doc per the flow chart request


def refresh_xlsx_paths():
    """This explicit function is used to iterate through the REPORT_DETAILS.csv and refreshes
    all of the xlsx files needed for the future email build"""
    df = pd.read_csv(folders.Paths.reportCSV, index_col="INDEX_ID")
    df_status = df['Report_Filepath'].loc[df['REPORT_STATUS'] == 'ACTIVE']  # Dependant on correct string format
    # print(df_status.count())
    # print(df_status)
    status_true = []
    status_false = []
    for i in df_status:
        refresh(i)
        if not rd.confirm_xlsx_verification(i):
            status_false.append(i)
            # update pandas verification column to False .iloc "file"

        else:
            status_true.append(i)
    admin_print("Output Verified Files: \n {} \n The following have been verified".format(status_true))
    df_true = df['Verification_Status'].loc[df['Report_Filepath'].isin(status_true)]

    for col in df.columns:
        df['Verification_Status'].values[:] = 0

    # print(df['Verification_Status'])
    true_val = []
    true_index = df_true.index.tolist()
    for i in true_index:
        true_val.append(1)
    upd = pd.Series(true_val, name='Verification_Status', index=true_index)
    df.update(upd)
    # print(df['Verification_Status'])


    # print(df_true)
    df.to_csv(folders.Paths.reportCSV)
    return
