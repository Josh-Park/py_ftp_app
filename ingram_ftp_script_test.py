import ingram_ftp_script
from ftplib import FTP
import datetime
import auth_constants
import os
import email_script

CURRENT_DATETIME = datetime.datetime.now()
FILENAMES = ["PUP702", "PUP702SA", "PUP702SU", "PUP702WKLY"]

def main():
    ftp = FTP(auth_constants.HOST, auth_constants.AUTH_USER, auth_constants.AUTH_PASS)
    ftp.cwd("fusion")
    ftp.cwd("vendor")
    ftp.cwd("grcd3")
    ftp.retrlines("LIST")

    output_file = open("%s.txt" % (FILENAMES[0]) , "wb")

    # ftp.retrbinary("RETR %s.txt" % (FILENAMES[0]), output_file.write)
    output_file.close()
    # parsed_date = ingram_ftp_script.parse_date(CURRENT_DATETIME.day, CURRENT_DATETIME.month, CURRENT_DATETIME.year)

    # for i in range(4):
    #     filepath = os.path.join(auth_constants.NAS_PATH, "%s.txt" % (FILENAMES[i] + "_" + parsed_date))
    #     print(filepath)
    # filename = ingram_ftp_script.parse_date(CURRENT_DATETIME.day, CURRENT_DATETIME.month, CURRENT_DATETIME.year)
    # filepath = os.path.join(auth_constants.NAS_PATH, "%s.txt" % filename)
    # output_file = open(filepath, "wb")
    # print(filename)
    # print(filepath)

    # email_script.send_email_with_attachment(
    #     "datalockertestuser@gmail.com", 
    #     "mmiller@datalocker.com",
    #     "Test email",
    #     "Hopefully this works.",
    #     auth_constants.TEST_EMAIL,
    #     auth_constants.TEST_EMAIL_PASS,
    #     "date_test.txt",
    #     "date_test.txt",
    #     "smtp.gmail.com",
    #     587)

    # with open("date_test.txt", "w") as test_file:
    #     for year in range(2000, 2018):
    #         for month in range(1, 12):
    #             for day in range(32):
    #                 parsed_date = ingram_ftp_script.parse_date(day, month, year) + "\n"
    #                 test_file.write(parsed_date)

    # ftp.retrbinary('RETR date_test.txt', output_file.write)

    # output_file.close()
    ftp.quit()

main()