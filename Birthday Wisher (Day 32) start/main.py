# import smtplib
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection = smtplib.SMTP("smtp.gmail.com", port=587)
#     connection.starttls() # to secure our emails
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="annaxiao46@yahoo.com", msg=f"Subject:Quote\n\n{quote}")



# import datetime as dt
#
# now = dt.datetime.now() # give you the current date and time
# year = now.year # to give you the current year
#
# date_of_birth = dt.datetime(year=1995, month=8, day=12, hour=4)
# print(date_of_birth)

import random
import smtplib

# TODO use the datetime module to obtain the current day of the week.
import datetime as dt

my_email = "annaxie652@gmail.com"
password = "abc!@#123"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    # TODO Open the quotes.txt file and obtain a list of quotes.

    with open("quotes.txt") as file:
        quote_list = file.readlines()
        # TODO use the randome module to pick a random quote from your list of quotes.
        quote = random.choice()

    # TODO Use the smtplib to send the email to yourself.

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="annaxiao46@yahoo.com",
        msg=f"Subject: Monday Motivation\n\n{quote}"
    )


