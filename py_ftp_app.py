from ftplib import FTP
import auth_constants
import tkinter as tk

LOCAL_HOST = "10.10.0.112"

def test():
    ftp = FTP(LOCAL_HOST, auth_constants.AUTH_USER, auth_constants.AUTH_PASS)

    welcome_message = ftp.getwelcome()
    if not welcome_message:
        print("No welcome message")
    else:
        print(ftp.getwelcome())

    ftp.retrlines("LIST")
    ftp.quit()

test()