# import smtplib

# # note this is a email and password created for learning purposes.
# my_email = "bradydarren056@gmail.com"
# password = 'ayae lpxi ubzt vhfh'

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user= my_email, password=password)
#     connection.sendmail(from_addr=my_email, 
#                     to_addrs='db01151993@yahoo.com', 
#                     msg='Subject:Hello\n\nThis is the body of the email.')

import datetime as dt

now = dt.datetime.now()
year = now.year
print(year)
month = now.month
print(month)
day_of_the_week = now.weekday()
print(day_of_the_week)