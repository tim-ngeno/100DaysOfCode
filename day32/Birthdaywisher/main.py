#!/usr/bin/env python3
""" Sending out automated birthday wishes """

import os
import pandas
import smtplib
from datetime import datetime
from random import randint

EMAIL = os.getenv('email')
PASSWORD = os.getenv('password')

# Get todays month and day
today = (datetime.now().month, datetime.now().day)
print(today)

content = pandas.read_csv('birthdays.csv')

# Create a dictionary with the details of from the csv
birthdays_dict = {
    (row.month, row.day): row for (index, row) in content.iterrows()
}


# Check if birthday exists today
if today in birthdays_dict:
    # Get the data on the person whose birthday it is
    person = birthdays_dict[today]

    # Get a letter template
    file_path = f'letter_templates/letter_{randint(1, 3)}.txt'
    with open(file_path) as template:
        content = template.read()
        content = content.replace('[NAME]', person['name'])

    # Send a birthday email
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=person['email'],
            msg=f'Subject: Happy Birthday!🎂\n\n{content}'
        )
