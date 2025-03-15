import datetime as dt
import random
import smtplib

MY_EMAIL = "bradydarren056@gmail.com"
PASSWORD = "ayae lpxi ubzt vhfh"

# 1. Obtain the current day of the week

now = dt.datetime.now()
day_of_the_week = now.weekday()
# print(day_of_the_week)

# 2. Open the quotes.txt file and obtain a list of motivational quotes

with open(file='quotes.txt', encoding="utf-8") as file: 
    quotes_list = file.readlines()
# print(quotes_list)  
      
# 3. Use the random module to pick a random quote from your list of quotes
todays_quote = random.choice(quotes_list).strip()
# print(todays_quote)

# 4. Use the smtplib to send the email to yourself

if day_of_the_week == 4:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user= MY_EMAIL, password=PASSWORD)
        subject = "Stay Motivated Son"
        body = f"Subject:{subject}\n\n{todays_quote}"
        connection.sendmail(from_addr=MY_EMAIL, 
                    to_addrs=MY_EMAIL, 
                    msg=body.encode("utf-8"))
