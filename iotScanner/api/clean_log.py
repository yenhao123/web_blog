import os
def clean_log():
    cur_path = os.path.dirname(__file__)
    filename = cur_path + "/log/cens.log"
    os.remove(filename)
    filename = cur_path + "/log/cens_ip.log"
    os.remove(filename)
    #os.remove("./log/cveInfo.log")

if __name__ == "__main__":
    clean_log()
