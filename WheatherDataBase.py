import sqlite3

DataBase = sqlite3.connect('DataBase.db')
cursor = DataBase.cursor()
cursor.execute('''
DROP TABLE IF EXISTS OpenWeather;
''')
DataBase.commit()
cursor.execute('''
CREATE TABLE IF NOT EXISTS OpenWeather(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Temp FLOAT,
    Weather TEXT,
    Sunrise TEXT,
    Sunset TEXT,
    Wind FLOAT
);
''')
DataBase.commit()
DataBase.close()