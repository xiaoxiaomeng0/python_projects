##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "annaxie652@gmail.com"
PASSWORD = "abc!@#123"
# 1. Update the birthdays.csv

# data = {
#     "name": ["hubby", "mom"],
#     "email": ["annaxiao46@yahoo.com", "annaxie652@gmail.com"],
#     "year": ["1990", "1955"],
#     "month": ["08", "04"],
#     "day": ["12", "17"]}
#
# data_add = pandas.DataFrame(data)
# data_add.to_csv("birthdays.csv", mode="a", index=False, header=False)

new_df = pandas.read_csv("birthdays.csv")
# month_list = new_df.month.tolist()
# month_list_round = [round(num) for num in month_list]
# day_list = new_df.day.tolist()
# day_list_round = [round(num) for num in day_list]

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
cur_month = now.month
cur_day = now.day
for (index, row) in new_df.iterrows():
    if cur_month == row.month and cur_day == row.day:
        # selected = new_df[(new_df["month"] == cur_month) & (new_df["day"] == cur_day)]
        # selected_name = selected.name.to_string()
        # selected_email = selected.email
        rand_letter_num = random.randint(1,3)
        with open(f"letter_templates/letter_{rand_letter_num}.txt") as letter:
            content = letter.read()
        new_content = content.replace("[NAME]", row["name"].capitalize())
        print(new_content)

        with smtplib.SMTP("smtp.gmail.com", port="587") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=selected_email,
                msg=f"Subject: Happy Birthday\n\n{new_content}"
            )
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




