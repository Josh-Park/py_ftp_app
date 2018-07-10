import ingram_ftp_script
from ftplib import FTP
import datetime
import auth_constants
import os
import email_script

CURRENT_DATETIME = datetime.datetime.now()
FILENAMES = ["PUP702", "PUP702SA", "PUP702SU", "PUP702WKLY"]

def test():
    parsed_date = "_".join(parse_month(CURRENT_DATETIME.month))
    date = CURRENT_DATETIME.strftime("%m_%b").upper()
    print(parsed_date)
    print(date)
    ftp = FTP(auth_constants.TEST_HOST, auth_constants.TEST_USER, auth_constants.TEST_PASS)
    ftp.cwd("fusion")
    ftp.cwd("vendor")
    ftp.cwd("grcd3")
    ftp.retrlines("LIST")

    output_file = open("%s.txt" % (FILENAMES[0]) , "wb")

    parsed_date = parse_date(CURRENT_DATETIME.day, CURRENT_DATETIME.month, CURRENT_DATETIME.year)

    for i in range(4):
        filepath = os.path.join(auth_constants.NAS_PATH, "%s.txt" % (FILENAMES[i] + "_" + parsed_date))
        print(filepath)
    filename = parse_date(CURRENT_DATETIME.day, CURRENT_DATETIME.month, CURRENT_DATETIME.year)
    filepath = os.path.join(auth_constants.NAS_PATH, "%s.txt" % filename)
    output_file = open(filepath, "wb")
    print(filename)
    print(filepath)

    date_time = CURRENT_DATETIME.strftime("%d-%b-%Y %H:%M:%S %p").upper()
    date = CURRENT_DATETIME.strftime("%d/%b/%Y").upper()
    filepath = os.path.join(auth_constants.NAS_PATH, str(CURRENT_DATETIME.year), "_".join(parse_month(CURRENT_DATETIME.month)))

    email_subject = "%s - Ingram PUP Orders updated" % (date)
    email_body = """New Ingram PUP orders downloaded and stored at '%s'.
    
    Email sent on %s""" % (filepath ,date_time)

    print(filepath)
    email_script.send_email(
        auth_constants.AUTH_EMAIL, 
        auth_constants.RCPT_EMAIL,
        email_subject,
        email_body,
        auth_constants.AUTH_EMAIL_USER,
        auth_constants.AUTH_EMAIL_PASS,
        auth_constants.STMP_SERVER,
        auth_constants.STMP_PORT)

    date_time = CURRENT_DATETIME.strftime("%d-%b-%Y %H:%M:%S %p").upper()
    print("Sent on %s" % (date_time))
    with open("date_test.txt", "w") as test_file:
        for year in range(2000, 2018):
            for month in range(1, 12):
                for day in range(32):
                    parsed_date = parse_date(day, month, year) + "\n"
                    test_file.write(parsed_date)

    ftp.retrbinary('RETR date_test.txt', output_file.write)

    output_file.close()
    ftp.quit()
def parse_date(day, month, year):
    dict_day = {"0":"00", "1":"01", "2":"02","3":"03","4":"04","5":"05","6":"06","7":"07","8":"08","9":"09"}

    parsed_day = str(day)
    parsed_month = parse_month(month)[1]

    if parsed_day in dict_day:
        parsed_day = dict_day[parsed_day]

    return parsed_day + parsed_month + str(year)

def parse_month(month):
    dict_month_num = {"0":"00", "1":"01", "2":"02","3":"03","4":"04","5":"05","6":"06","7":"07","8":"08","9":"09"}
    dict_month = {"1":"JAN", "2":"FEB", "3":"MAR", "4":"APR", "5":"MAY", "6":"JUN", "7":"JUL", "8":"AUG", "9":"SEP", "10":"OCT", "11":"NOV", "12":"DEC", }

    parsed_month_num = str(month)
    parsed_month = str(month)

    if parsed_month_num in dict_month_num:
        parsed_month_num = dict_month_num[parsed_month_num]
    if parsed_month in dict_month:
        parsed_month = dict_month[parsed_month]

    return (parsed_month_num, parsed_month)

if __name__ == "__main__":
    test()