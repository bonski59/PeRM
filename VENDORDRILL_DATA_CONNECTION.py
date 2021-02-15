import pandas as pd
import pyodbc

import folders

output_csv_location = folders.Paths.reports_xlsx

def vendorDrillConnection(query_arr):
    for i in query_arr:
        output_filepath = output_csv_location + '\\' + i[0] + ".csv"

        result_set = pd.read_sql(open(i[1]).read(), pyodbc.connect("DSN=VENDORDRILL_DATA_CONNECTION", autoCommit=True))
        result_set.to_csv(path_or_buf=output_filepath, index=False)
    return
