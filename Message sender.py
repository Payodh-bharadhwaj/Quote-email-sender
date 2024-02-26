import random
import smtplib
import datetime as dt

my_email = "123@gmail.com"
password = "***********"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="kavetisaisumedh@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}" f"BY Payodh Bharadhwaj",
        )
