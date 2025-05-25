import mimetypes
import os
from email.message import EmailMessage
from appword import password, my_email
import ssl
import smtplib



Email_file = 'message.txt' #path to text file
email_sender = my_email
email_password = password
em = EmailMessage()

#Function to parse txt file
def parse_email_file(msg_file):
    subject = ""
    body = ""
    attachments = []

    with open(msg_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    mode = None
    for line in lines:
        line = line.strip()
        if line.startswith("Subject:"):
            subject = line[len("Subject:"):].strip()
        elif line.startswith("Body:"):
            mode = "body"
        elif line.startswith("Attachment(s):"):
            mode = "attachments"
        elif mode == "body":
            body += line + "\n"
        elif mode == "attachments" and line:
            attachments.append(line)

    return subject, body.strip(), attachments


recipient = 'fotec94441@dlbazi.com'
#recipient = input("Enter Recipient's Email Address, separate multiple recipients using comma ',': ")

#grab everything from file
#file structure: Subject, Body, Attachment
#separate file for recipients
subject, body, attachments = parse_email_file(Email_file) #''#grab from file

em['From'] = email_sender
em['To'] = recipient
em['Subject'] = subject
em.set_content(body)
with open('message.txt', 'rb') as f:
    file_data = f.read()
    file_name = f.name
    em.add_attachment(file_data, maintype='application', subtype='txt', filename=file_name)
'''
for file in attachments:
    # Guess MIME type based on file extension
    mime_type, _ = mimetypes.guess_type(file)
    maintype, subtype = mime_type.split('/')

    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(file)
        em.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file_name)




#em.add_attachment(filename='message.txt')
'''
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtpserver:
    smtpserver.login(email_sender, email_password)
    smtpserver.sendmail(email_sender, recipient, em.as_string())
