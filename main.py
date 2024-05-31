import os
import datetime as dt
import smtplib
import pandas as pd
import random

now = dt.datetime.now()
day = now.day
month = now.month
file = pd.read_csv('birthdays.csv')
day_list = file['day']
month_list = file['month']


my_email = os.getenv("smtp_username")
password = os.getenv('smtp_password')
for d in range(len(day_list)):
    if day_list[d] == day:
        if month_list[d] == month:
            n = random.randint(1, 3)
            path = f"letter_templates/letter_{n}.txt"
            with open(path, 'r') as file2:
                text = file2.read()
                new_text = text.replace('[NAME]', file['name'][d])
            print(new_text)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=file['email'][d],
                                    msg=f'Subject:Happy BirthDay Wishes\n\n{new_text}')
