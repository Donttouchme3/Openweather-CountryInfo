from countryinfo import CountryInfo
import sqlite3

def GetCountryInfo():
    Country = input('Введите страну: ')
    try:
        Info = CountryInfo(Country).info()
        Name = Info['name']
        Capital = Info['capital']
        Currencies = Info['currencies']
        Languages = Info['languages']
        NativeName = Info['nativeName']
        Population = Info['population']
        Region = Info['region']
        Subregion = Info['subregion']


    except Exception as e:
        print(f'Произошла ошибка {e}')
        GetCountryInfo()

    def SaveToData():
        DataBase = sqlite3.connect('DataBase.db')
        cursor = DataBase.cursor()
        try:
            cursor.execute('''
            INSERT INTO CountryInfo(CountryName, Capital, Currency, Languages, NativeName, Population, Region, Subregion) VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            ''', (str(Name), str(Capital), str(Currencies), str(Languages), str(NativeName), int(Population), str(Region), str(Subregion)))
            DataBase.commit()
            DataBase.close()

        except:
            pass

    def ShowData():
        try:
            DataBase = sqlite3.connect('DataBase.db')
            cursor = DataBase.cursor()
            cursor.execute('''
                    SELECT * FROM CountryInfo WHERE CountryName = (?)
                    ''', (Name,))
            Data = cursor.fetchall()
            print(Data)
            DataBase.close()
        except:
            pass

    SaveToData()
    ShowData()


GetCountryInfo()