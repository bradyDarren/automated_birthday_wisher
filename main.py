##################### Extra Hard Starting Project ######################

import pandas as pd 
import datetime as dt
import random
import smtplib

MY_EMAIL = "bradydarren056@gmail.com"
LETTER_LIST = ['letter_templates/letter_1.txt','letter_templates/letter_2.txt','letter_templates/letter_3.txt']
PASSWORD = "ayae lpxi ubzt vhfh"

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def load_birthday_file(file_path):
    with open (file=file_path, mode='r', encoding='utf-8') as file:
       return file.read()
    
# 4. Send the letter generated in step 3 to that person's email address.

def send_wishes(name, email, message):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection: 
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        subject = f"HAPPY BIRTHDAY {name}!!!!"
        body =f'Subject:{subject}\n\n {message}'
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=email, 
                            msg= message.encode('utf-8'))
 
def main(): 
    selected_file = random.choice(LETTER_LIST)
    birthday_letter = load_birthday_file(selected_file)

    # 1. - Update the birthdays.csv - Done
    # 1.1 - Import the csv file using Pandas
    birthdays = pd.read_csv(filepath_or_buffer='birthdays.csv')
    data = birthdays.to_dict(orient='index')

    # 1.2 - Getting the current month and day
    now = dt.datetime.now()
    current_month = now.month
    current_day = now.day

    # 2. Check if today matches a birthday in the birthdays.csv
    for _, person in data.items():
        if person['month'] == current_month and person['day'] == current_day:
            personalized_letter = birthday_letter.replace('[NAME]', person['name'])
            # print(personalized_letter)
            send_wishes(person['name'], person['email'], personalized_letter)

main()