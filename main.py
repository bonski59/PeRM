# This will be the main file that calls all functions and classes when it is selected by the user
""""
step 1: initiate VDC and query HD server
    -Variables: Server, query file, output location
    -query server with data txt file from file path under QUERY_DETAIL.csv
    -output query data as csv to "sales_csv"

step 2: Refresh Data
    -get filepath/s: reports_xlsx
    -refresh reports_xlsx data
    -manage with simple refresh function

step 3: Verify Excel Report
    -Get Excel report filepaths: reports_xlsx
    -somehow find way to pull verification from xlsx file sheet1, grid:A1, value == True or False
    - - gonna need to find a xlsx read python method

step 4: Email results
    -Variables: Recipients, Sender, Attachments, SMTP server, Login info, Speech Text Message,
    -Send email using email module
    - - Using outlook
    - - - recommend using gmail if outlook is configured with gmail account instead of authentic microsoft account
"""
import VENDORDRILL_DATA_CONNECTION as VDC
import read_data as rd

q_arr = rd.read_report_details()

VDC.vendorDrillConnection(q_arr) # outputs multiple csv's through use of to reports_xlsx


if __name__ == "__main__":
    print("Program Initiated")
