import requests
import sqlite3
from pprint import pprint
from datetime import datetime

class GetWeather:
    def __init__(self):
        self.Parameters = {
            'appid': '65e40f7a6232dded78790082a7c8308d',
            'units': 'metric',
            'lang': 'ru'
        }

    def GetInfo(self, City):
        self.Parameters['q'] = City
        Data = requests.get('https://api.openweathermap.org/data/2.5/weather', params=self.Parameters).json()
        Name = Data['name']
        Temp = Data['main']['temp']
        Weather = Data['weather'][0]['description']
        Timezone = Data['timezone']
        Sunrise = datetime.utcfromtimestamp(int(Data['sys']['sunrise']) + int(Timezone)).strftime('%Y-%m-%d %H-%M-%S')
        Sunset = datetime.utcfromtimestamp(int(Data['sys']['sunset']) + int(Timezone)).strftime('%Y-%m-%d %H-%M-%S')
        Wind = Data['wind']['speed']

        self.SaveToDataBase(Name, Temp, Weather, Sunrise, Sunset, Wind)
        self.GetDataBase(Name)

    def SaveToDataBase(self, Name, Temp, Weather, Sunrise, Sunset, Wind):
        DataBase = sqlite3.connect('DataBase.db')
        cursor = DataBase.cursor()
        cursor.execute('''
        INSERT INTO OpenWeather(Name, Temp, Weather, Sunrise, Sunset, Wind) VALUES (?,?,?,?,?,?);
        ''', (Name, Temp, Weather, Sunrise, Sunset, Wind))
        DataBase.commit()
        DataBase.close()

    def GetDataBase(self, Name):
        DataBase = sqlite3.connect('DataBase.db')
        cursor = DataBase.cursor()
        cursor.execute('''
        SELECT * FROM OpenWeather WHERE Name = (?) ORDER BY ID DESC LIMIT 1;
        ''', (Name, ))
        Info = cursor.fetchall()
        print(Info)
        DataBase.close()


def StartProgram():
    Program = GetWeather()
    CityInput = input('Введите город: ')
    Program.GetInfo(CityInput)


StartProgram()