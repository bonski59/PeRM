# This will be the main file that calls all functions and classes when it is selected by the user
""""
Flowchart Breakdown

step 1: initiate VDC and query HD server
    -Variables: Server, query file, output location
    -quer y server with data txt file from file path under QUERY_DETAIL.csv
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
import email_functions as ef
import read_data as rd
import refresh_excel as re

"""
VERIFY TESTING BOOLEAN in folders.py BEFORE EXECUTION
VERIFY TESTING BOOLEAN in folders.py BEFORE EXECUTION
VERIFY TESTING BOOLEAN in folders.py BEFORE EXECUTION
VERIFY TESTING BOOLEAN in folders.py BEFORE EXECUTION
VERIFY TESTING BOOLEAN in folders.py BEFORE EXECUTION
VERIFY TESTING BOOLEAN in folders.py BEFORE EXECUTION
"""

q_arr = rd.read_report_details()    # step 1: initiate VDC and query HD server
input("q_arr var complete \n starting VDC")
VDC.vendorDrillConnection(q_arr)
input("VDC complete and CSV's comprised \n starting refresh and verify")
"""
outputs multiple csv's to sales_csv using query_txt
this satisfies Step 1 
"""

re.refresh_xlsx_paths()             # step 2: Refresh Data # this works for the new xl data
input("Refresh and verify complete \n composing email")     # referential data only works on Blake's computer
                                                            # timing the refresh function and applying its duration wont work because it will flag an excel error
                                    # includes step 3 (more efficient)
                                    # step 3: Verify XL data meets metadata criteria
"""
takes reports_xlsx file path and iterates through all files and refreshes them.
this is explicit to xlsx files 

also verifies xl paths that have met a given criteria 
"""

ef.email_everyone()                 # step 3: Email everyone
print("Program complete")
"""
Takes REPORT_DETAIL.csv and finds required items for email and sends content to desired email recipients 
"""
