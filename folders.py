# this shouldnt have any functions in it
# only classes

import os

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



