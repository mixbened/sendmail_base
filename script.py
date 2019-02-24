import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmail_user = input("Enter Gmail Adress: ")
gmail_password = input("Enter Gmail Password: ")

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
receiver_list = ["some@mail.com"]

message = MIMEMultipart()
message["From"] = gmail_user
message["To"] = receiver_list
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

filename = "file.csv"

with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

encoders.encode_base64(part)

part.add_header(
    "Content-Disposition",
    "attachment; filename=%s"%filename,
)


message.attach(part)
text = message.as_string()

try:  
    server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server_ssl.ehlo()
    server_ssl.login(gmail_user, gmail_password)
    server_ssl.sendmail(gmail_user, receiver_list, text)
    server_ssl.close()
except:  
    print("Something went wrong sending the email...")