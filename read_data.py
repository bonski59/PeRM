import pandas as pd

import folders


def read_report_details():  # reads csv and pulls valid query txt files into an array
    df = pd.read_csv(folders.Paths.reportCSV, delimiter=',', engine="python")
    row_count = int(df.shape[0])        # defines num of rows in csv
    dict_df = df.to_dict()              # turns csv into dict so we can referance values by headers
    print(dict_df)                    # prints dict
    return_array = []
    i = 0
    while i < row_count:
        if str(dict_df['QUERY_TXT'][i]) == 'nan':  # TODO: find out what the correct header/filepath so i can find the query.txt files needed to send to the VDC
            pass
        else:
            # print(dict_df['QUERY_TXT'][i])
            query_filepath = dict_df['QUERY_TXT'][i]
            report_name = dict_df['REPORT_NAME'][i]
            # right here I would want to do is call the VENDORDRILL FUNCTION ()
            # and pass the following variables
            # queryTxt and then the destination CSV
            # "C:\Users\us160212\Documents\Python Projects\Reference Files\DataConnectionExport_CSV"

            return_array.append([report_name, query_filepath])
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


# print(read_report_details())
# query_list = read_report()
