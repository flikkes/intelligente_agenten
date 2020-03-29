from bs4 import BeautifulSoup
import re
import requests

def crawlWeather(city):
    url = 'https://wetter.de/suche.html?search='+city
    response = requests.get(url)
    text = response.text
    soup = BeautifulSoup(text, features="html.parser")
    dailyForecasts = soup.findAll('div', class_='forecast-item-day')

    result = []

    for dailyForecastString in dailyForecasts:
        daySoup = BeautifulSoup(str(dailyForecastString), features="html.parser")
        dayName = daySoup.find('div', class_='text-day').string
        maxTemp = daySoup.find('span', class_='wt-color-temperature-max').string
        minTemp = daySoup.find('span', class_='wt-color-temperature-min').string
        forecastDict = {"day": dayName, "max": maxTemp, "min": minTemp}
        result.append(forecastDict)

    return result;
