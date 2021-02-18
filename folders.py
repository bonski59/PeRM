# this shouldn't have any functions in it
# only classes
import os

import pandas as pd

"""
This a new technique I've been using. basically any important filepaths that we need to use 
are referenced here. Using this module as an import in most of the other modules inside PeRM 
has proven usefull for both testing and operational use. It is a quick an easy means to switch 
filepaths by just changing the "testing = "bool"" to whatever the situation is. we have yet to  
"""

class Paths:
    testing = True
    if not testing:
        cwd = r"{}\dataManagement\LiveData".format(os.getcwd())
    else:
        cwd = r"{}\dataManagement\SampleData".format(os.getcwd())

    query_txt = r"{}\query_txt".format(cwd)
    reports_xlsx = r"{}\reports_xlsx".format(cwd)
    sales_csv = r"{}\sales_csv".format(cwd)
    dataFolder = r"{}".format(cwd)
    queryCSV = r"{}\QUERY_DETAIL.csv".format(cwd)  # use this for local ops
    reportCSV = r"{}\REPORT_DETAIL.csv".format(cwd)  # use this for local ops


def change_csv_xl_filepaths_to_local_directory():   # explicit function that interacts with LiveData\REPORT_DETAIL.csv
    csv_path = r"{}\dataManagement\LiveData\REPORT_DETAIL.csv".format(os.getcwd())
    function_cwd = r"{}\dataManagement\LiveData".format(os.getcwd())
    live_reports = r"{}\dataManagement\LiveData\reports_xlsx".format(os.getcwd())
    df = pd.read_csv(csv_path)
    loop_length = int(df.shape[0]) - 1
    # print(df['Report_Filepath'])
    
    def this_file_is_in_line(string):
        local_files = os.listdir(live_reports)
        print(local_files)
        for i in local_files:
            if i in string:
                return i
            else:
                return False

    for fp in df['Report_Filepath']:
        print(fp)
        val = this_file_is_in_line(str(fp))
        if val:
            return val

change_csv_xl_filepaths_to_local_directory()
