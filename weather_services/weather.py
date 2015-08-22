__author__ = 'matt.livingston'

import json
import requests
import time
import datetime



class Day:
    def __init__(self, day, text, low, high):
        self.day = day
        self.text = text
        self.low = low
        self.high = high


class FiveDayForecast:
    def __init__(self):
        self.days = []

    def add_day(self, day):
        self.days.append(day)

    def get_forecast(self):
        return self.days


class Forecast:
    def __init__(self, loc):
        self.baseurl = "https://query.yahooapis.com/v1/public/yql?q="
        self.y_query = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="{0}")'
        self.url_format = '&format=json&env=store://datatables.org/alltableswithkeys'
        # Query paramaters with reasonable defaults
        self.text = 'oswego, il'
        if loc is None:
            loc = self.text

        self.get_forecast(loc)

    def get_forecast(self, loc):
        yql_url = self.baseurl + self.y_query.format(self.text) + self.url_format
        print(yql_url)
        r = requests.get(yql_url)
        data = json.loads(r.text)

        latest_forecast = data['query']['results']['channel']['item']['forecast']

        self.five_day = FiveDayForecast()

        for a in latest_forecast:
            day = Day(a['date'], a['text'], a['low'], a['high'])
            self.five_day.add_day(day)


    def get_todays_forecast(self):
        d = time.strftime("%d %b %Y")
        high = 0
        f_text = ""
        for day in self.five_day.get_forecast():
            if day.day == d:
                high = day.high
                f_text = day.text

        return "Today it will be {0} with a high of {1}".format(f_text, high)

    def get_specific_day(self, day):
        d = datetime.datetime.now()
        target_day = None
        response_template = "{0} will be {1} with a low of {2} and a high of {3}."
        if day.lower() == 'tomorrow':
            day = d + datetime.timedelta(days=1)
            target_day = self.search_forecast(day.strftime("%d %b %Y"))
        elif day.lower() == 'day after tomorrow':
            day = d + datetime.timedelta(days=2)
            target_day = self.search_forecast(day.strftime("%d %b %Y"))

        return response_template.format(day.strftime('%A'), target_day.text, target_day.low, target_day.high)

    def search_forecast(self, date):
        for day in self.five_day.get_forecast():
            if day.day == date:
                return day



#f = Forecast("oswego, il")
#print(f.get_specific_day('tomorrow'))

#print(f.get_specific_day('day after tomorrow'))





"""
'forecast': [{
				'day': 'Wed',
				'code': '30',
				'date': '12Aug2015',
				'text': 'PartlyCloudy',
				'low': '60',
				'high': '83'
			},
			{
				'day': 'Thu',
				'code': '32',
				'date': '13Aug2015',
				'text': 'Sunny',
				'low': '65',
				'high': '88'
			},
			{
				'day': 'Fri',
				'code': '30',
				'date': '14Aug2015',
				'text': 'PartlyCloudy',
				'low': '65',
				'high': '91'
			},
			{
				'day': 'Sat',
				'code': '32',
				'date': '15Aug2015',
				'text': 'Sunny',
				'low': '65',
				'high': '92'
			},
			{
				'day': 'Sun',
				'code': '34',
				'date': '16Aug2015',
				'text': 'MostlySunny',
				'low': '67',
				'high': '94'
			}]
		}
"""