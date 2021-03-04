import os
import pandas as pd
import folders
from admin import *

start_admin()

def read_report_details():  # reads csv and pulls valid query txt/corresponding csv location files into an array
    q_arr = []
    root = folders.Paths.query_txt
    file_list = os.listdir(root)
    for fp in file_list:
        csv_name = fp.replace(".txt", ".csv")
        csv_file = os.path.join(folders.Paths.sales_csv, csv_name)
        query_name = fp
        query_file = os.path.join(root, query_name)
        q_arr.append([csv_file, query_file])
    return q_arr

def confirm_xlsx_verification(xlsx_file):  # Explicit to files with a 'VERIFICATION' sheet_name
    fp = xlsx_file
    try:
        df = pd.read_excel(fp, sheet_name='verification', engine='openpyxl')
        df = str(df.iloc[0])
        df = df[:6]
    except UserWarning:
        admin_print("Flagged during the following File:  {} ".format(xlsx_file))

        return
    # print(df)
    if "True" in df:
        return True
    else:
        return False


end_admin()