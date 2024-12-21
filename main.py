import yagmail
import time
from datetime import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()

sender = os.getenv('EMAIL_SENDER')
receiver = 'sxtapm0r@mailpwr.com'

subject = "This is the subject"

contents = """
Here's the email contents!
HELLO
"""

def send_email():
    yag = yagmail.SMTP(user=sender, password=os.getenv('EMAIL_PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email sent")

while True:
    now = dt.now()
    if now.hour == 15 and now.minute == 42:
        send_email()
        time.sleep(60)