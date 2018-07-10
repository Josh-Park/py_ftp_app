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

    # Lists the files on the directory
    # ftp.retrlines("LIST")

    # Parse the current date
    # dayMONTHyear. Ex. 10JUL2018
    date = CURRENT_DATETIME.strftime("%d%b%Y").upper()
    # day-MONTH-year hour:minute:sec AM/PM. Ex. 10-JUL-2018 11:34:10 AM
    date_time = CURRENT_DATETIME.strftime("%d-%b-%Y %H:%M:%S %p").upper()
    # day/MONTH/year. Ex. 10/JUL/2018
    date_slashes = CURRENT_DATETIME.strftime("%d/%b/%Y").upper()
    # NAS_PATH\year\monthnum_MONTH. Ex. \\nas1\nas1\07_JUL
    store_path = os.path.join(auth_constants.NAS_PATH, str(CURRENT_DATETIME.year), CURRENT_DATETIME.strftime("%m_%b").upper())

    # Copy each file in FILENAMES list
    for i in range(4):
        print("Copying %s.txt" % (FILENAMES[i]))
        filepath = os.path.join(store_path, "%s.txt" % (FILENAMES[i] + "_" + date))

        # Creates a directory if one for the current year or month doesn't exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, "wb") as file_output:
            ftp.retrbinary("RETR %s.txt" % (FILENAMES[i]), file_output.write)
            print("Copy success")

    print("Disconnecting from FTP server")
    ftp.quit()

    # Send an email notifying that the files were downloaded
    email_subject = "%s - Ingram PUP Orders updated" % (date_slashes)
    email_body = """New Ingram PUP orders downloaded and stored at '%s'.
    
    Email sent on %s""" % (store_path ,date_time)

    email_script.send_email(
        auth_constants.AUTH_EMAIL,
        auth_constants.RCPT_EMAIL,
        email_subject,
        email_body,
        auth_constants.AUTH_EMAIL_USER,
        auth_constants.AUTH_EMAIL_PASS,
        auth_constants.STMP_SERVER,
        auth_constants.STMP_PORT)

    input("Press Enter to exit...")
    quit()

if __name__ == "__main__":
    main()