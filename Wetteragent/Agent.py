from bs4 import BeautifulSoup
import re
import requests

def crawlWeather(city):
    url = 'https://wetter.de/suche.html?search='+city
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, features="html.parser")
    dailyForecasts = soup.findAll('div', class_=['base-box--level-0', 'weather-daybox'])
    result = []

    for dailyForecastString in dailyForecasts:
        daySoup = BeautifulSoup(str(dailyForecastString), features="html.parser")
        print(daySoup)
        dayName = daySoup.find('div', class_='weather-daybox__date__weekday').string
        maxTemp = daySoup.find('div', class_='weather-daybox__minMax__max').string
        minTemp = daySoup.find('div', class_='weather-daybox__minMax__max').string
        forecastDict = {"day": dayName, "max": maxTemp, "min": minTemp}
        result.append(forecastDict)

    return result
