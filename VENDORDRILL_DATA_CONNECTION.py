import pandas as pd
import pyodbc
import shutil
from azure_api import azureDevTools as adt
from admin import *
from configparser import ConfigParser

config_file = r"{}\config.ini".format(os.getcwd())
config = ConfigParser()
config.read(config_file)

def vdc():
    for i in config.sections():
        if "query" in i:
            dbc = config[i]['dbc']
            q_arr = adt.siphon_blob_list(config[i]['query_txt'])
            admin_print("Starting Queries for {}: {}".format(dbc, q_arr))
            for query in q_arr:
                cloud_query_dbc_to_csv(query=query, dbc=dbc)
            admin_print("Ending Queries for {}: {}".format(dbc, q_arr))
        shutil.rmtree(folders.Paths.upload_path)
    # query_lookup = adt.siphon_blob_list(query)


def cloud_query_dbc_to_csv(query, dbc):
    print("DSN={}".format(dbc))
    output_blob = cloud_rename_query_to_csv(query)
    base, leaf = output_blob.split("/")
    admin_print("Sending Query to VDC: {}".format(query))
    result_set = pd.read_sql(adt.blob_to_txt(query), pyodbc.connect(dbc, autoCommit=True))
    admin_print("Txt query sent to dbc: {}".format(query))

    if not os.path.exists(folders.Paths.upload_path):
        os.mkdir(folders.Paths.upload_path)
    fp = r"{}\{}".format(folders.Paths.upload_path, leaf)
    print(fp)
    result_set.to_csv(path_or_buf=fp, index=False)
    admin_print("CSV location created : {}".format(output_blob))
    adt.upload_and_overwrite(fp, "sales_csv")
    return


def cloud_rename_query_to_csv(query_name):
    q = query_name
    head, tail = q.split("/")
    csvname = tail.replace(".txt", ".csv")
    csvpath = "{}/{}".format("sales_csv", csvname)
    return csvpath
# excercise can we run perm with every query text file and pull data from the HD server
