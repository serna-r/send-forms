import smtplib
from email.mime.text import MIMEText
from config import user_config, emails_config
import pandas as pd

# Get subject and body
subject = "Email Subject"
body = "This is the body of the text message"

# Get sender
sender = user_config.USER
password = user_config.PASSWORD

# Get recipients
emails_df = pd.read_excel(emails_config.RECIPIENTS_FILENAME, header=None, names=['recipients'])
recipients = emails_df['recipients'].to_list()

# Send e-mail function
def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

# Call send e-mail function
send_email(subject, body, sender, recipients, password)