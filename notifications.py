import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Need to replace empty strings with info for emails
sender_email = ''
sender_password = ''
receiver_email = ''
subject = 'Mow Lawn Notification'
message = 'Conditions are currently optimal for cutting your grass. \n maybe more info...'

# This creates the object that represents the email we're sending
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Try to connect to gmail's SMTP server, if not successful print error
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Use TLS encryption
    server.login(sender_email, sender_password)
    
    server.sendmail(sender_email, receiver_email, msg.as_string())
    
    print('Email sent successfully!')
    
except Exception as e:
    print(f'An error occurred: {str(e)}')
    
finally:
    server.quit()
