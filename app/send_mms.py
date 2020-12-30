# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='this da awesome sauce',
         from_='+1',
         media_url=['https://i.imgur.com/Cd6JPow.jpg'],
         to='+1'
     )

print(message.status)
