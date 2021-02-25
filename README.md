# PeRM
Python Executeable: Report Manager

Python Script that pulls CSV data from a server using queries, then it updates a file dependant excel sheet and emails them to clients using verification/activation techniques using values from a static data CSV. 

-

Flowchart Breakdown

step 1: initiate VDC and query HD server
    -Variables: Server, query file, output location
    -query server with data txt file from file path under .\query_txt 
    -output query data as csv to "sales_csv"

step 2: Refresh Data
    -get filepath/s: .\reports_xlsx
    -refresh all files in .\reports_xlsx 
    
step 3: Verify Excel Report
    -Get Excel report filepaths: .\reports_xlsx
    -pull verification from xlsx file sheet = 'verification' , grid:A1, value == True or False

step 4: Email results
    -Variables: Recipients, Sender, Attachments, SMTP server, Login info, Speech Text Message,
    -Send email using email module
    - - Using Gmail
