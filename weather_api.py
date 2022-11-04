import requests
import smtplib

my_email = "Your Email"
my_password = "Your Password"
    
data = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?lat=9.838810&lon=77.448380&exclude=current,daily,minutely&appid=4b8d72199a7d0b5cc7df561389308f65")
weather_data = data.json()


rain = False
for n in range(12):
  p=(weather_data["hourly"][n]["weather"][0])
  desp = p["description"]
  iddt = p["id"]
  if iddt < 700:
    rain = True
    
if rain == True:
  connection = smtplib.SMTP("smtp.gmail.com", 587)
  connection.starttls()
  connection.login(user=my_email, password=my_password)
  connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:Today's Weather Condition\n\nIt is going to rain today🌧️")
  connection.close()    
 

