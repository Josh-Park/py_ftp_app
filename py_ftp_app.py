from ftplib import FTP
import auth_constants
import datetime
import email_script

LOCAL_HOST = "10.10.0.112"
CURRENT_DATE = datetime.datetime.now()

def test():
    ftp = FTP(LOCAL_HOST, auth_constants.AUTH_USER, auth_constants.AUTH_PASS)
    ftp.retrlines("LIST")

    filename = parse_date(CURRENT_DATE.day, CURRENT_DATE.month, CURRENT_DATE.year)
    output_file = open("%s.txt" % (filename), "wb")
    print(filename)

    # email_script.send_email_with_attachment(
    #     "datalockertestuser@gmail.com", 
    #     "mmiller@datalocker.com",
    #     "Test email",
    #     "Hopefully this works.",
    #     "datalockertestuser@gmail.com",
    #     "Datalocker1",
    #     "date_test.txt",
    #     "date_test.txt",
    #     "smtp.gmail.com",
    #     587)
    # with open("date_test.txt", "w") as test_file:
    #     for year in range(2000, 2018):
    #         for month in range(1, 12):
    #             for day in range(32):
    #                 parsed_date = parse_date(day, month, year) + "\n"
    #                 test_file.write(parsed_date)

    # ftp.retrbinary('RETR test.txt', output_file.write)

    output_file.close()
    ftp.quit()

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

test()