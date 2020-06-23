import smtplib
from email.message import EmailMessage
import imghdr

EMAIL_ADDRESS = "YourEmail"
EMAIL_PASSWORD = "YourEmailPassword"

msg = EmailMessage()
msg['Subject'] = 'Python Mail'
msg['From'] = EMAIL_ADDRESS
msg['To'] = EMAIL_ADDRESS
msg.set_content('This is Email Body')

with open('python.png', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    print('MAIL-SENT')
