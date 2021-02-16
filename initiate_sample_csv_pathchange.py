import os

import folders

cwd = os.getcwd()
sample_query_detail = r"{}\dataManagement\sample-QUERY_DETAIL.csv".format(cwd)
sample_report_detail = r"{}\dataManagement\sample-REPORT_DETAIL.csv".format(cwd)

def find_all_xl():
    reports_xlsx = folders.Paths.reports_xlsx
    files = os.listdir(reports_xlsx)
    print(files)
    for f in files:
        os.path.join(reports_xlsx, files)


find_all_xl()
