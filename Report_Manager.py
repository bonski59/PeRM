import pandas as pd

reportmetadata = r"C:\Users\us160212\PycharmProjects\Testing_Sandbox\report_metadata.csv"
# r/ = "read filepath"

dataframe = pd.read_csv(reportmetadata, error_bad_lines=False, sep=',', engine="python")
print(dataframe)


# query_filepath
# csvOUTPUT_filepath

