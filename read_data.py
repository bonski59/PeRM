import pandas as pd
import os
import folders


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
    df = pd.read_excel(fp, sheet_name='VERIFICATION', engine='openpyxl')
    df = str(df)
    if "True" in df:
        return True
    else:
        return False

def read_xlxs(xlsx_file):  # Used for Testing
    fp = xlsx_file
    df = pd.read_excel(fp, sheet_name='Sheet1', engine='openpyxl')
    df = str(df)
    print(df)

# print(read_report_details())
# query_list = read_report()
