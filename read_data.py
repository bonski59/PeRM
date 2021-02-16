import pandas as pd

import folders


def read_report_details():  # reads csv and pulls valid query txt/corresponding csv location files into an array
    """This Function Works Explicitly for the VDC module"""
    df = pd.read_csv(folders.Paths.queryCSV, delimiter=',', engine="python")
    row_count = int(df.shape[0])        # defines num of rows in csv
    # print(row_count)
    dict_df = df.to_dict()              # turns csv into dict so we can referance values by headers
    # print(dict_df)                    # prints dict
    return_array = []
    i = 0
    while i < row_count:
        query_fp = dict_df['QUERY_TXT_FilePath'][i]
        csv_fp = dict_df['VDDC_CSV_FilePath'][i]
        if str(query_fp) == 'nan': # multiple conditions
            pass
        else:
            # print(dict_df['QUERY_TXT'][i])
            return_array.append([csv_fp, query_fp])
        i += 1  # iterates line by line
    return return_array

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
