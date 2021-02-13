import pandas as pd
import pyodbc
import datetime
import os

        # PSEUDO CODE
        #loopthrough Reports variable()
        #    -get query string
        #    -get exportCSV location
        #    #get excelreport output filepath

# get report_detail info
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
            query_filepath = dict_df['QUERY_TXT'][i]
            report_name = dict_df['REPORT_NAME'][i]
            # right here I would want to do is call the VENDORDRILL FUNCTION ()
            # and pass the following variables
            ## queryTxt and then the destination CSV
            #"C:\Users\us160212\Documents\Python Projects\Reference Files\DataConnectionExport_CSV"

            return_array.append([report_name, query_filepath])
        i += 1  # iterates line by line
    return return_array

print(read_report())


#query_list = read_report()
"""# execute

## I'll do some busy work getting the files and then I'll get back to you. thanks again man

# it just needed an extra python package to read the .xlsx. copy that.
# after you "def" a function you need to call if for it to execute. makes sense


#-----

# ------- copy/pasted code since last screenshare ---------------

# pass SQL to server, download CSV


# ------------------
# --- START LOOP ---
# ------------------
for queryFile in excel_data_df.query_txt:
    query_filepath = excel_data_df.query_txt
    pyODBC_DSN = "DSN=VENDORDRILL_DATA_CONNECTION"
    resultSet = pd.read_sql(open('test_query.txt').read(), pyodbc.connect(pyODBC_DSN, autoCommit=True))
    resultSet.to_csv(path_or_buf=str(OutputCSV_FOLDER + excel_data_df.STANDARD_REPORT_NAME), index=False)

# loop through report_details.VDDC_CSV_FilePath to get the [query].txt filepaths. then I'll use these filepaths in the VENDORDRILL_DATA_CONNECTION.py
## first - thanks!! that was what I was trying to solve lol. next I think I need to compile my query.txt files. I don't have them yet
## but after I get them, I'll be passing the query.txt filepaths into the VENDORDRILL_DATA_CONNECTION function"""