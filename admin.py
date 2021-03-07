from datetime import datetime
import os
import folders


def admin_print(string):
    file = open(folders.Paths.a_file, 'a')
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print("\n {}:   {}".format(now, string))
    file.write("\n {}:   {}".format(now, string))
    file.close()
    return

def start_admin():
    if os.path.isfile(folders.Paths.a_file):
        os.remove(folders.Paths.a_file)
    file = open(folders.Paths.a_file, 'w')
    file.close()
    return



