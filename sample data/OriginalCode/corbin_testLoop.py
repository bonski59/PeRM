import pandas as pd


# make fp a baseline filepathe acessable everyeh
report_details_fp = r'C:\Users\us160212\Documents\Python Projects\Reference Files\REPORT_DETAIL.csv' # this was bothering me that it wast a var
excel_data_df = pd.read_csv(report_details_fp)

# ------
# make fp a baseline filepathe acessable everyeh
def read_report():
    df = pd.read_csv(report_details_fp, delimiter=',', engine="python")
    row_count = int(df.shape[0])  # defines num of rows in csv
    dict_df = df.to_dict()  # turns csv into dict so we can referance values by headers
    # print(dict_df)  # prints dict
    return_array = []
    i = 0
    while i < row_count:
        if str(dict_df['QUERY_TXT'][i]) == 'nan':
            pass
        else:
            # print(dict_df['QUERY_TXT'][i])
            x = dict_df['QUERY_TXT'][i]
            # right here I would want to do is call the VENDORDRILL FUNCTION ()
            # and pass the following variables
            ## queryTxt and then the destination CSV
            #"C:\Users\us160212\Documents\Python Projects\Reference Files\DataConnectionExport_CSV"

            return_array.append(x)
        i += 1  # iterates line by line
    return return_array

query_list = read_report()  # execute
#print(query_list)

def pass_query_getcsv(query_arr):
    for i in query_arr:
        print(i)
    return

pass_query_getcsv(query_list)