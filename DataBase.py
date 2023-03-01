import sqlite3

DataBase = sqlite3.connect('DataBase.db')
cursor = DataBase.cursor()
cursor.execute('''
DROP TABLE IF EXISTS CountryInfo;
''')
DataBase.commit()
cursor.execute('''
CREATE TABLE IF NOT EXISTS CountryInfo(
    CountryId INTEGER PRIMARY KEY AUTOINCREMENT,
    CountryName Text UNIQUE,
    Capital TEXT,
    Currency TEXT,
    Languages TEXT,
    NativeName TEXT,
    Population INT,
    Region TEXT,
    Subregion TEXT
);
''')
DataBase.commit()
DataBase.close()