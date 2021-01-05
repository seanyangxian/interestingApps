import smtplib
from email.mime.text import MIMEText


def send_email(user_email, age, preferred_platform, average_age, preference_percentage, total_users):
    source_email = 'datacollectorwebapp@gmail.com'
    source_password = 'seanyangxian'
    destination_email = user_email

    subject = 'Thank you for using Data Collector Web App!'
    message = 'testing'

    msg = MIMEText(message,'html')
    msg['Subject'] = subject
    msg['To'] = destination_email
    msg['From'] = source_email

    sending_email = smtplib.SMTP('smtp.gmail.com', 587)
    sending_email.ehlo()
    sending_email.starttls()
    sending_email.login(source_email, source_password)
    sending_email.send_message(msg)