import pandas as pd
import os

reportmetadata = r"C:\Users\us160212\PycharmProjects\Testing_Sandbox\report_metadata.csv"
# r/ = "read filepath"

dataframe = pd.read_csv(reportmetadata, error_bad_lines=False, sep=',', engine="python")
print(dataframe)


# query_filepath
# csvOUTPUT_filepath

def passqueryfilepath("")

