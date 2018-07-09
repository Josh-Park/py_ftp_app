from ftplib import FTP
import auth_constants
import datetime
import email_script
import os
import ingram_ftp_script_test

CURRENT_DATETIME = datetime.datetime.now()
FILENAMES = ["PUP702", "PUP702SA", "PUP702SU", "PUP702WKLY"]

def main():
    # Connect to FTP server and navigate to correct directory
    print("Connecting to FTP server")
    ftp = FTP(auth_constants.HOST)
    ftp.login(auth_constants.AUTH_USER, auth_constants.AUTH_PASS)
    print("Connection successful")
    ftp.cwd("fusion")
    ftp.cwd("vendor")
    ftp.cwd("grcd3")
    ftp.retrlines("LIST")

    # Parse the current date
    parsed_date = parse_date(CURRENT_DATETIME.day, CURRENT_DATETIME.month, CURRENT_DATETIME.year)

    # Copy each file in FILENAMES list
    for i in range(4):
        print("Copying %s.txt" % (FILENAMES[i]))
        filepath = os.path.join(auth_constants.NAS_PATH, str(CURRENT_DATETIME.year), "_".join(parse_month(CURRENT_DATETIME.month)), "%s.txt" % (FILENAMES[i] + "_" + parsed_date))

        # Creates a directory if one for the current year or month doesn't exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, "wb") as file_output:
            
        # file_output = open(filepath, "wb")

            ftp.retrbinary("RETR %s.txt" % (FILENAMES[i]), file_output.write)
            print("Copy success")

        # file_output.close()

    print("Disconnecting from FTP server")
    ftp.quit()

    input("Press Enter to exit...")
    quit()

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

main()