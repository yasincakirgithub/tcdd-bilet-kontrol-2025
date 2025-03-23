from twilio.rest import Client
import config


def send_sms(message, notificated_number):

    account_sid = config.twilio_account_sid
    auth_token = config.twilio_auth_token
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_=config.twilio_number, body=message, to=notificated_number)

    print(message.sid)
