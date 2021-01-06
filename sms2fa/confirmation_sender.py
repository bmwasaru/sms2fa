import random

from flask import session
import africastalking

from . import app

username = app.config['AT_USERNAME']
api_key = app.config['AT_API_KEY']
sender_id = app.config['AT_SENDER_ID']
africastalking.initialize(username, api_key)

sms = africastalking.SMS


def send_confirmation_code(to_number):
    verification_code = generate_code()
    numbers = []
    numbers.append(to_number)
    sms.send(verification_code, numbers, sender_id)
    del numbers
    session['verification_code'] = verification_code
    return verification_code


def generate_code():
    return str(random.randrange(100000, 999999))
