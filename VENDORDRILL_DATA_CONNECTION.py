import pandas as pd
import pyodbc

import folders

output_csv_location = folders.Paths.sales_csv


def vendorDrillConnection(query_arr):
    for i in query_arr:
        output_filepath = i[0]

        result_set = pd.read_sql(open(i[1]).read(), pyodbc.connect("DSN=VENDORDRILL_DATA_CONNECTION", autoCommit=True))
        result_set.to_csv(path_or_buf=output_filepath, index=False)
    return

# excercise can we run perm with every query text file and pull data from the HD server
