# this shouldn't have any functions in it
# only classes
import os
"""
This a new technique I've been using. basically any important filepaths that we need to use 
are referenced here. Using this module as an import in most of the other modules inside PeRM 
has proven usefull for both testing and operational use. It is a quick an easy means to switch 
filepaths by just changing the "testing = "bool"" to whatever the situation is. we have yet to  
"""


class Paths:
    testing = False
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

