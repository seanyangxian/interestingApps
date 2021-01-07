import smtplib
from email.mime.text import MIMEText


def send_email(user_email, age, preferred_platform, average_age, preference_percentage, total_users):
    source_email = 'datacollectorwebapp@gmail.com'
    source_password = 'seanyangxian'
    destination_email = user_email

    subject = 'Thank you for using Data Collector Web App!'
    user_name = user_email.split('@')[0]
    message = f'Dear {user_name},<br><br>' \
              f'Thanks for completing the survey!<br><br>' \
              f'You are {age} years old and you watch video mostly on {preferred_platform}.<br>' \
              f'Based on data we collected from all {total_users} participates, ' \
              f'the average age of participates is {average_age} years old. ' \
              f'There is {preference_percentage} percent of participates watch videos on {preferred_platform} like you!<br>' \
              f'Hope you enjoy the result. Have a wonderful day!'

    msg = MIMEText(message,'html')
    msg['Subject'] = subject
    msg['To'] = destination_email
    msg['From'] = source_email

    sending_email = smtplib.SMTP('smtp.gmail.com', 587)
    sending_email.ehlo()
    sending_email.starttls()
    sending_email.login(source_email, source_password)
    sending_email.send_message(msg)