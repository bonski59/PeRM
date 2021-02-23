from datetime import datetime

def admin_print(string):
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print("{}:   {}".format(now, string))
    return


