
import pandas 
import datetime as dt
import random 
import smtplib

email = "Your Email"
password = "Your Password"

today = dt.datetime.now()
today = (today.month, today.day)

data =pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (key,data_row) in data.iterrows()}

if today in birthday_dict:
  birthday_per = birthday_dict[today]
  file = f"letter_templates/letter_{random.randint(1,3)}.txt"
  with open (file) as letter_file:
    content = letter_file.read()
    content = content.replace("[NAME]" , birthday_per["name"])
    
  connection = smtplib.SMTP("smtp.gmail.com",587)  
  connection.starttls()
  connection.login(email, password)
  connection.sendmail(from_addr=email, to_addrs=birthday_per["email"], msg=f"Subject:Happy Birthday to you!!\n\n{content}")