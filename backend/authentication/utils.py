import os
from twilio.rest import Client
account_sid = "AC23ee15bcbaae5c9a9de670f9cfea67f8"
auth_token = "45aad8f48cd6121309ead5dd20d4ceb8"
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
