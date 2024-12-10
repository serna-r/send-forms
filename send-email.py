import smtplib
from email.mime.text import MIMEText
from config import user_config, emails_config
import pandas as pd

# Get sender
sender = user_config.USER
password = user_config.PASSWORD

# Get subject and body for Spanish and English
subject_es = emails_config.spanish.SUBJECT
links_es = emails_config.spanish.LINKS
body_es = emails_config.spanish.BODY

subject_en = emails_config.english.SUBJECT
links_en = emails_config.english.LINKS
body_en = emails_config.english.BODY

# Get recipients
emails_df = pd.read_excel(emails_config.RECIPIENTS_FILENAME, header=None, names=['names', 'emails', 'empty', 'language'])
recipients_es = emails_df[pd.isna(emails_df['language'])]
recipients_en = emails_df[emails_df['language'] == 'EN'].reset_index()

# Send e-mail function
def send_email(subject, body, sender, recipient, password, link, linknumber):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient['emails']

    print(f"Prepared message for {recipient['names']} ({recipient['emails']}), link n {linknumber} ({link})")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipient['emails'], msg.as_string())
    print(f"Message sent to {recipient['names']} ({recipient['emails']})\n")

# Prepare personalized emails
def prepare_and_send_emails(subject, body_template, sender, recipients, links, password, language):
    print(f"\n\nStart sending messages for language {language}\n----------------------------------\n")

    for i, recipient in recipients.iterrows():
        # Replace placeholders with personalized data
        personalized_body = body_template.replace('$name', recipient['names']).replace('$link', links[i%len(links)])
        send_email(subject, personalized_body, sender, recipient, password, links[i%len(links)], i%len(links))

# Send Spanish emails
prepare_and_send_emails(subject_es, body_es, sender, recipients_es, links_es, password, language='ES')

# Send English emails
prepare_and_send_emails(subject_en, body_en, sender, recipients_en, links_en, password, language='EN')
