import yagmail
from dotenv import load_dotenv
import os
import pandas

load_dotenv()

sender = os.getenv('EMAIL_SENDER')
subject = "This is the subject"

yag = yagmail.SMTP(user=sender, password=os.getenv('EMAIL_PASSWORD'))


def send_email(receiver, name, amount, filepath):
    contents = [f"""
        Hello {name}, you must pay {amount}
        The bill is attached!
        """, filepath]

    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email sent")

df = pandas.read_csv('contacts.csv')
print(df)

for index, row in df.iterrows():
    send_email(row['email'], row['name'], row['amount'], 'Bills/' + row['filepath'])