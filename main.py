##################### Extra Hard Starting Project ######################

import pandas as pd 
import datetime as dt
import random

LETTER_LIST = ['letter_1.txt','letter_2.txt','letter_3.txt']

# 1. - Update the birthdays.csv - Done
# 1.1 - Import the csv file using Pandas
birthdays = pd.read_csv(filepath_or_buffer='birthdays.csv')
data = birthdays.to_dict(orient='index')
print(data)

# 1.2 - Getting the current month and day
now = dt.datetime.now()
month = now.month
day = now.day

# 2. Check if today matches a birthday in the birthdays.csv
for index, person in data.items():
    if person['month'] == month and person['day'] == day:
        print(f"{person['name']}, happy birthday !!!!!!!")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

