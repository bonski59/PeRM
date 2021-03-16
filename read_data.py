import os
import pandas as pd
import folders
from admin import *
from azure_api import azureDevTools as az
from configparser import ConfigParser

config_file = r"{}\config.ini".format(os.getcwd())
config = ConfigParser()
config.read(config_file)

def read_report_details():  # pulls valid query txt/corresponding csv location files into an array
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

def parse_arr_match_string(arr, string):
    matching = [s for s in arr if str(string) in s]
    return matching

def azure_get_querypaths(match_string):
    blob_list = az.list()
    print("All Blobs listed \n Parsing for matching string ... \n Listing: Strings Found - \n")
    matching = [s for s in blob_list if str(match_string) in s]  #config['query-blob']['query_txt']
    return matching


def azure_build_csvpaths_from_query_path(match_string):
    query_arr = azure_get_querypaths(match_string=match_string)
    for i in query_arr:
        head, tail = i.split('/')
        csv_path = "{}{}".format(config['blob']['sales_csv'], tail.replace(".txt", ".csv"))
        i.append(csv_path)
    return query_arr


"""
read_report_details cloud integration notes
s1: define blob with query txt files
    
    return blob arr query-txt/{file}.txt
s1.1: format csv output name
        blob, file = split(blob_name at "/")
        csv_name = replace(".txt", ".csv")
        
s2: for i in blob arr:
        download(i)
        vdc(i) 
            return(csv)
"""




def confirm_xlsx_verification(xlsx_file):  # Explicit to files with a 'VERIFICATION' sheet_name
    fp = xlsx_file
    try:
        df = pd.read_excel(fp, sheet_name='verification', engine='openpyxl')
        df = str(df.iloc[0])
        df = df[:6]
    except UserWarning:
        admin_print("Flagged during the following File:  {} ".format(xlsx_file))

        return
    # print(df)
    if "True" in df:
        return True
    else:
        return False


