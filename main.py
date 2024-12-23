import yagmail
from dotenv import load_dotenv
import os
import pandas as pd

# Load environment variables
load_dotenv()

# Initialize email sender and subject
sender = os.getenv('EMAIL_SENDER')
subject = "This is the subject"
yag = yagmail.SMTP(user=sender, password=os.getenv('EMAIL_PASSWORD'))

def send_email(receiver, name, amount):
    contents = [f"""
        Hello {name}, you must pay {amount}
        The bill is attached!
        """, f"Bills/{name}.txt"]

    yag.send(to=receiver, subject=subject, contents=contents)
    print(f"Email sent to {receiver}")

def generate_bill(name, amount):
    if not os.path.exists('Bills'):
        os.makedirs('Bills')

    filename = f"Bills/{name}.txt"
    with open(filename, 'w') as file:
        file.write(f'You will need to pay ${amount}')

def process_contacts(file_path):
    df = pd.read_csv(file_path)
    print(df)

    for index, row in df.iterrows():
        name = row['name']
        amount = row['amount']
        email = row['email']

        generate_bill(name, amount)
        send_email(email, name, amount)

# Process the contacts and send emails
process_contacts('contacts.csv')
