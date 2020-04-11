
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACfab76e86f0283d9c763e5b4bff363410'
auth_token = 'fc5aef1e1e1c6f6b0172651126f46b32'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='I love you babe. Smsje via python.',
         from_='+14156495151',
         to='+32491138057'
     )

print(message.sid)