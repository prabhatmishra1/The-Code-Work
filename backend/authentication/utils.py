import os
from twilio.rest import Client
account_sid = "AC23ee15bcbaae5c9a9de670f9cfea67f8"
auth_token = "5dd703ae040a7aa6344485331a74fa14"
client = Client(account_sid, auth_token)


def send_otp(mobile, otp):
    try:
        message = client.messages \
                        .create(
                            body="Your one time password is %s" % (otp),
                            from_='+19282550333',
                            to='+91'+mobile
                        )
        print(message.status)
        if message.status == "queued":
            return True
        else:
            return False
    except:
        return True
