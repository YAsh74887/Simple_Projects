import datetime as dt
import requests
import smtplib
import time 

MYlat=18.520430
MYlng=73.856743

while True:
  time.sleep(60)

  def position_of_iss():
    if MYlat-5 <= latitude <= MYlat+5 and MYlng-5 <= longitude <= MYlng+5:
      return True
    else:
      return False 

  response = requests.get(url="http://api.open-notify.org/iss-now.json")
  data = response.json()
  longitude = float(data["iss_position"]["longitude"])
  latitude = float(data["iss_position"]["latitude"])


  def night():
    sunset_sunrise = requests.get(url="https://api.sunrise-sunset.org/json?lat=18.520430&lng=73.856743&formatted=0")
    sunset_sunrise_data = sunset_sunrise.json()
    sunrise = int(sunset_sunrise_data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(sunset_sunrise_data['results']['sunset'].split("T")[1].split(":")[0])

    today = dt.datetime.now()
    today = today.hour
    if sunset>=19 or sunset<=7:
      return True
    else:
      return False

  is_night = night()
  answer = position_of_iss() 
    
  if is_night==True  and answer==True:
    my_email = "Your email"
    my_password = "Your password"
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(to_addrs=my_email, from_addr=my_email, msg="Subject:Notification of ISS \n\n Look up ISS over your head")
    connection.close()
  
