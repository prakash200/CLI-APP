import requests

# 1. Humidity
# 2. Pressure
# 3. Average temperature
# 4. Wind Speed
# 5. Wind degree
# 6. UV Index 


#Reference_API_Link1 = "https://openweathermap.org/api/one-call-api"
#Peferance_API_Link2 = "https://openweathermap.org/current"


File = open("API_KEY.txt", "r")
API_KEY = File.read().strip()

cityname = input("Enter City name : ")

Api_link = "https://api.openweathermap.org/data/2.5/weather?q="+cityname+"&appid="+API_KEY

Request_Api = requests.get(Api_link)
Api_data = Request_Api.json()

if Api_data['cod'] == '404':
    print("Invalild city {}, Please check your city name".format(cityname))
else:
    coordinates = Api_data['coord']
    main = Api_data['main']
    wind = Api_data['wind']
    

lat = coordinates['lat']
long = coordinates['lon']
humidity = main['humidity']
pressure = main['pressure']
min_temp = main['temp_min']
max_temp = main['temp_max']
average_temperature = (min_temp+max_temp)/2
wind_speed = wind['speed']
wind_degree = wind['deg']


Api_link1 = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(lat)+"&lon="+str(long)+"&exclude=hourly,daily&appid="+API_KEY

Request_Api = requests.get(Api_link1)
Api_data = Request_Api.json()
uvi_index = Api_data['current']['uvi'] 

print("Humidity: {}".format(humidity))
print("Pressure: {}".format(pressure))
print("Avg.Temperature: {}".format(average_temperature))
print("Wind_speed: {}".format(wind_speed))
print("Wind_degree: {}".format(wind_degree))
print("UV index: {}".format(uvi_index))

