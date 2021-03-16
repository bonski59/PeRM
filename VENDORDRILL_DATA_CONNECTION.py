import pandas as pd
import pyodbc
from azure_api import azureDevTools as adt
from admin import *


def vendorDrillConnection(query_arr):  # designed to ingest array like "[[*.csv, *.txt], [*.csv, *.txt]]"
    for i in query_arr:
        output_filepath = i[0]  # this is the csv value from query_arr[i][0]
        admin_print("Sending Query to VDC: {}".format(i[1]))
        result_set = pd.read_sql(open(i[1]).read(), pyodbc.connect("DSN={}".format("VDDC_UFP"), autoCommit=True))
        admin_print("Txt query sent to dbc: {}".format(i[1]))

        """ 
        I did not write this part, it was received from Home Depot analysts 
        From what I can tell the above variable sets a pandas data frame to "result_set" from reading a SQL 
        query by using the text file from "query_arr[i][1]" and then python makes a database 
        connection using the input DSN, and pulls the query info
        -CK
        """

        result_set.to_csv(path_or_buf=output_filepath, index=False)
        admin_print("CSV location created : {}".format(output_filepath))

        """
        The variable above changes the output pandas data frame "result_set" to a csv and sends it to the csv filepath defined in "query_arr[i][0]"
        -CK
        """
    return

    # query_lookup = adt.siphon_blob_list(query)


def cloud_query_dbc_to_csv(query, dbc):
    output_blob = cloud_rename_query_to_csv(query)
    base, leaf = output_blob.split("/")
    admin_print("Sending Query to VDC: {}".format(query))
    result_set = pd.read_sql(adt.blob_to_txt(query), pyodbc.connect("DSN={}".format(dbc), autoCommit=True))
    admin_print("Txt query sent to dbc: {}".format(query))

    """ 
    I did not write this part, it was received from Home Depot analysts 
    From what I can tell the above variable sets a pandas data frame to "result_set" from reading a SQL 
    query by using the text file from "query_arr[i][1]" and then python makes a database 
    connection using the input DSN, and pulls the query info
    -CK
    """
    if not os.path.exists(folders.Paths.upload_path):
        os.mkdir(folders.Paths.upload_path)

    result_set.to_csv(path_or_buf=leaf, index=False)
    admin_print("CSV location created : {}".format(output_blob))
    return


def cloud_rename_query_to_csv(query_name):
    q = query_name
    head, tail = q.split("/")
    csvname = tail.replace(".txt", ".csv")
    csvpath = "{}/{}".format("sales_csv", csvname)
    return csvpath
# excercise can we run perm with every query text file and pull data from the HD server
