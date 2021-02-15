# this shouldnt have any functions in it
# only classes

import os

class Paths:
    cwd = os.getcwd()
    query_txt = r"{}\dataManagement\query_txt".format(cwd)
    reports_xlsx = r"{}\dataManagement\report_xlsx".format(cwd)
    sales_csv = r"{}\dataManagement\sales_csv".format(cwd)
    dataFolder = r"{}\dataManagement".format(cwd)
    queryCSV = r"{}\dataManagement\QUERY_DETAIL.csv".format(cwd)
    reportCSV = r"{}\dataManagement\REPORT_DETAIL.csv".format(cwd)



