from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACb30fb494cc752aae4cdb99fac4d31b5a'
auth_token = 'db0302fa2ac0e022f763d6dbbf9eeb48'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="VAlue at sensor",
                     from_='+19292078819',
                     to='+918978434569'
                 )

print(message.sid)
