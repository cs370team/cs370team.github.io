from format_index import get_moisture_data
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def lawn_notification():
    # Need to replace empty strings with info for emails
    sender_email = 'cs370lawnnotification@gmail.com'
    sender_password = 'dcnm btut dtfb rqkn'
    receiver_email = 'luke.elerson@yahoo.com'
    lawn_reminder = "Lawn upkeep reminder: Check lawn height. Mow to 1/3 of grass height if lawn has grown to 6'' or more.\n"

    # This creates the object that represents the email we're sending
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Lawn Information Notification"
    msg.attach(MIMEText(lawn_reminder, 'plain'))

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

lawn_notification()