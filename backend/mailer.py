import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = "mohsinces@gmail.com"
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login("mohsinces@gmail.com", "tthy hram oxoh jwib")
        server.send_message(msg)
