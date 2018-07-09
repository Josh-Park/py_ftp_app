import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_addr = "datalockertestuser@gmail.com"
to_addr = "datalockertestuser@gmail.com"

msg = MIMEMultipart()

msg["From"] = from_addr
msg["To"] = to_addr
msg["Subject"] = "Test email"

print("Creating message body")
msg_body = "I sent this bad boy from a Python script."
msg.attach(MIMEText(msg_body, "plain"))

print("Connecting to SMTP server")
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(from_addr, "Datalocker1")

print("Sending email")
text = msg.as_string()

server.sendmail(from_addr, to_addr, text)
server.quit()
print("Email successfully sent")