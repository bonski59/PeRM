import pandas as pd
import pyodbc
import datetime
import os
import RUN_layer as runlayer

output_csv_location = r"C:\Users\us160212\Documents\Python Projects\Reference Files\DataConnectionExport_CSV"
# REPORT_FOLDER + REPORT_NAME

directory = r"{}\CSV_Output".format(os.getcwd())
q_arr = runlayer.read_report()
#print(q_arr)
#injects variable asd string

def VendorDrillConnection(query_arr):
    for i in query_arr:
        output_filepath = output_csv_location + '\\' + i[0] + ".csv"

        resultSet = pd.read_sql(open(i[1]).read(), pyodbc.connect("DSN=VENDORDRILL_DATA_CONNECTION", autoCommit=True))
        resultSet.to_csv(path_or_buf=output_filepath, index=False)
    return

VendorDrillConnection(q_arr)