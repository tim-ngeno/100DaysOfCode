#!/usr/bin/env python3
""" Sending quotes via email """

import smtplib
import os
from datetime import datetime
from random import choice

email = os.getenv('email')
password = os.getenv('password')

now = datetime.now()

# Read data from the quotes file
with open('quotes.txt', 'r') as file:
    content = file.read()
    quotes = content.splitlines()

    print(choice(quotes))


# Send an email if it is a Monday
if now.weekday() == 0:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f'Subject:Monday Motivation\n\n{choice(quotes)}'
        )
