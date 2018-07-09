import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(from_addr, to_addr, subject, msg_body, login, password, SMTP_server = "smtp.gmail.com", port = 587):

    msg = MIMEMultipart()

    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = subject

    print("Creating message body")
    msg.attach(MIMEText(msg_body, "plain"))

    print("Connecting to SMTP server")
    server = smtplib.SMTP(SMTP_server, port)
    server.starttls()
    server.login(from_addr, password)

    print("Sending email")
    text = msg.as_string()

    server.sendmail(from_addr, to_addr, text)
    server.quit()
    print("Email successfully sent")

def send_email_with_attachment(from_addr, to_addr, subject, msg_body, login, password, filename, filepath, SMTP_server = "smtp.gmail.com", port = 587):
    msg = MIMEMultipart()

    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = subject

    print("Creating message body")
    msg.attach(MIMEText(msg_body, "plain"))

    print("Attaching file")
    attachment = open(filepath, "rb")

    part = MIMEBase("application", "octet-stream")
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment; filename= %s" % filename)

    msg.attach(part)

    print("Connecting to SMTP server")
    server = smtplib.SMTP(SMTP_server, port)
    server.starttls()
    server.login(from_addr, password)

    print("Sending email")
    text = msg.as_string()

    server.sendmail(from_addr, to_addr, text)
    server.quit()
    print("Email successfully sent")