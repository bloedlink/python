# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'enter account sid here'
auth_token = 'enter auth token here'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Enter text message here",
                     from_='+14....',
                     to='+32...'
                 )

print(message.sid)
