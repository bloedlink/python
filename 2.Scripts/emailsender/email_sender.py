import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email ['from'] = 'yourmail@gmail.com'
email['to'] = 'targetmail@gmail.com'
email['subject'] = 'mailcontentakdqjdopqjfo^qfq'

email.set_content(html.substitute({'name':'dummyname'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#smtp hello message
    smtp.ehlo()
#start + encryption (tls = encryption)
    smtp.starttls()
    smtp.login('yourmail@gmail.com','yourpass')
    smtp.send_message(email)
    print('Mail sent!')
