

from email.message import EmailMessage
from appword import password
from appword import my_email
import ssl
import smtplib




email_sender = my_email
email_password = password


recipient = 'fotec94441@dlbazi.com' # test email

subject = 'Subject of Email'
body = """Body of Email
        We keep typing hte body on the second line for no reason.
        Just to prove that this is the body of the email."""

em = EmailMessage()

em['From'] = email_sender
em['To'] = recipient
em['Subject'] = subject
em.set_content(body)
em.add_attachment()

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtpserver:
    smtpserver.login(email_sender, email_password)
    smtpserver.sendmail(email_sender, recipient, em.as_string())
