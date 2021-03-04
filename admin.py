from datetime import datetime
import sys

def admin_print(string):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print("{}:   {}".format(now, string))
    return

def start_admin():
    sys.stdout = open("admin_report.txt", "w")
    return

def end_admin():
    sys.stdout.close()

