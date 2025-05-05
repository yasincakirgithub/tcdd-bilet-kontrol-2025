from twilio.rest import Client
import config
from win11toast import notify

# This function is used to send a notification to the user using the Windows 11 toast notification system.
def send_win11_notification(message):
    notify(message, duration='long')


# This function is used to send an SMS using the Twilio API.
# Use in careful, as it will charge you for each SMS sent.
def send_sms(message, notificated_number):

    account_sid = config.twilio_account_sid
    auth_token = config.twilio_auth_token
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_=config.twilio_number, body=message, to=notificated_number)

    print(message.sid)

# As long as you don't answer the call, it does not charge you.
def make_call(notificated_number):
    account_sid = config.twilio_account_sid
    auth_token = config.twilio_auth_token
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        url="http://demo.twilio.com/docs/voice.xml",
        to=notificated_number,
        from_=config.twilio_number,
    )

    print(call.sid)    
