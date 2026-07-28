import config
from src.util import turkce_ascii
from twilio.rest import Client


def send_sms(message, notificated_number):

    message = turkce_ascii(message)
    account_sid = config.twilio_account_sid
    auth_token = config.twilio_auth_token
    client = Client(account_sid, auth_token)
    message = client.messages.create(from_=config.twilio_number, body=message, to=notificated_number)
    print(message.sid)


def call_number(notificated_number):

    account_sid = config.twilio_account_sid
    auth_token = config.twilio_auth_token
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        to=notificated_number,
        from_=config.twilio_number,
        twiml="""
    <Response>
        <Say>Merhaba, tren bileti bulundu</Say>
    </Response>
    """,
    )
