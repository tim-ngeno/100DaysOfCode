#!/usr/bin/env python3
""" Using smtplib library """

import smtplib
import os

email = os.getenv('email')
password = os.getenv('password')

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=email, password=password)
connection.sendmail(
    from_addr=email,
    to_addrs=email,
    msg='Subject:A Primer from the future!\n\nGreetings from ze future..ahoy')
connection.close()
