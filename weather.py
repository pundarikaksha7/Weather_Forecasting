import requests

# api endpoint using open weather api
api_endpoint = "http://api.openweathermap.org/data/2.5/weather?"

# api key
api_key="a05691f26db748337be5b992f6b5fa06"

# city name
city_name = input("Enter city name : ")

# complete url
complete_url = api_endpoint + "appid=" + api_key + "&q=" + city_name

# get method of requests module
response = requests.get(complete_url)

# json method of response object

x = response.json()

if x["cod"] != "404":
    
    #store the value corresponding to the "main" key of y
    y = x["main"]

    # store the value corresponding to the "temp" key of y

    current_temperature = y["temp"]

    # store the value corresponding to the "pressure" key of y

    current_pressure = y["pressure"]

    #store the value of humidity key of y

    current_humidity = y["humidity"]

    #store the value of weather key of y

    current_weather = x["weather"]

    #store the value of description key of z

    weather_description = current_weather[0]["description"]

    #print following values
    print()
    print("-----------{}-----------".format(city_name))
    print("Current Temperature: ",current_temperature,"K")
    print("Current Pressure: ",current_pressure,"hPa")
    print("Current Humidity: ",current_humidity,"%")
    print("Current Weather: ",weather_description.capitalize())
    print()


else:
    print("City not found")
