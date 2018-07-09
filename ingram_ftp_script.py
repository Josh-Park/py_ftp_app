from ftplib import FTP
import auth_constants
import datetime
import email_script
import os

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
        filepath = os.path.join(auth_constants.NAS_PATH, "%s.txt" % (FILENAMES[i] + "_" + parsed_date))
        file_output = open(filepath, "wb")

        ftp.retrbinary = ("RETR %s.txt" % (FILENAMES[i]), file_output.write)
        print("Copy success")

        file_output.close()

    print("Disconnecting from FTP server")
    ftp.quit()

    input("Press any key to exit...")

def parse_date(day, month, year):
    dict_day = {"0":"00", "1":"01", "2":"02","3":"03","4":"04","5":"05","6":"06","7":"07","8":"08","9":"09"}
    dict_month = {"1":"JAN", "2":"FEB", "3":"MAR", "4":"APR", "5":"MAY", "6":"JUN", "7":"JUL", "8":"AUG", "9":"SEP", "10":"OCT", "11":"NOV", "12":"DEC", }

    parsed_day = str(day)
    parsed_month = str(month)

    if parsed_day in dict_day:
        parsed_day = dict_day[parsed_day]
    if parsed_month in dict_month:
        parsed_month = dict_month[parsed_month]

    return parsed_day + parsed_month + str(year)

main()