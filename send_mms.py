# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACf9098d25860f18278fbdffd32257fbd8'
auth_token = '33b07a3404a7aa8a000b9c30992ea52c'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='this da awesome sauce',
         from_='+12015281624',
         media_url=['https://i.imgur.com/Cd6JPow.jpg'],
         to='+17144684468'
     )

print(message.status)
