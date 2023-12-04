import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime

ARTICLE_LIST = [
    "House Plant Resources:",
    "Essential Watering Guide: https://wallygrow.com/blogs/feature/essential-watering-guide",
    "Overwatering: https://www.missouribotanicalgarden.org/gardens-gardening/your-garden/help-for-the-home-gardener/advice-tips-resources/pests-and-problems/environmental/overwatering",
    "Root Rots & Houseplants: https://hort.extension.wisc.edu/articles/root-rots-houseplants/",
    "Signs of Underwatering Plants: https://www.trifectanatural.com/problem-identifier/signs-of-underwatering-plants/",
    "\n",
    "Lawn Resources:",
    "Ascochyta Leaf Blight: https://organolawn.com/services/lawn-fungus/ascochyta-leaf-blight/",
    "Can Weeds Damage Your Lawn and Garden?: https://www.getpond.com/can-weeds-damage-your-lawn-and-garden",
    "How to Build a Living Soil in a Lawn: https://organolawn.com/lawn-care-company/living-soil/",
    "Managing Thatch in Lawns: https://extension.psu.edu/managing-thatch-in-lawns",
    "Mowing Mistakes That Damage the Lawn: https://ngturf.com/5-mowing-mistakes-that-damage-the-lawn/",
    "Mowing Wet Grass: https://www.bobvila.com/articles/mowing-wet-grass/",
    "The Negative Impacts of Weeds: https://weedman.com/blog/the-negative-impacts-of-weeds",
    "Signs of an Overwatered Lawn: https://www.lawnandreticulation.com.au/blog/signs-of-an-overwatered-lawn/",
    "Symptoms of Underwatering a Lawn: https://organolawn.com/lawn-care-tips/watering/under-watering/",
    "What to do About Lawn Dormancy: https://www.getsunday.com/shed/lawn/what-is-dormancy"
]
LINK_TO_SITE = "For Information regarding your weekly ground moisture information please visit: https://cs370team.github.io/"
LAWN_REMINDER = "Lawn upkeep reminder: Check lawn height. Mow to 1/3 of grass height if lawn has grown to 6'' or more.\n"
MOISTURE_REMINDER = "Lawn/Plant moisture reminder: Moisture levels are currently low, please water your plant or lawn.\n"

def read_last_notification(file_path):
    try:
        with open(file_path, "r") as file:
            last_notification_date = datetime.datetime.strptime(file.read().strip(), "%Y-%m-%d %H:%M:%S")
            return last_notification_date
    except ValueError:
        return datetime.datetime.min

def write_last_notification_date(file_path, date_time):
    with open(file_path, "w") as file:
        file.write(date_time.strftime("%Y-%m-%d %H:%M:%S"))

def send_notification(email_content):
    sender_email = 'cs370lawnnotification@gmail.com'
    sender_password = 'dcnm btut dtfb rqkn'
    receiver_email = 'ayoungren94@gmail.com'


    # This creates the object that represents the email we're sending
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Lawn Information Notification"
    msg.attach(MIMEText(email_content, 'plain'))

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

def lawn_notification():
    file_path = "lastLawnNotification.txt"
    last_notification_date = read_last_notification(file_path)
    email_content = f"{LAWN_REMINDER}\n{LINK_TO_SITE}\n\n" + "\n".join(ARTICLE_LIST)

    if datetime.datetime.now() - last_notification_date >= datetime.timedelta(weeks=1):
        send_notification(email_content)
        write_last_notification_date(file_path, datetime.datetime.now())
    else:
        print("A week has not passed since the last lawn notification.")

def moisture_notification():
    email_content = f"{MOISTURE_REMINDER}\n{LINK_TO_SITE}\n\n" + "\n".join(ARTICLE_LIST)
    send_notification(email_content)
