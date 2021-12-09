import sqlite3
from datetime import datetime

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS Techstocks ''')
cur.execute('''DROP TABLE IF EXISTS Tnx ''')

cur.execute('''CREATE TABLE IF NOT EXISTS Techstocks
    (id INTEGER UNIQUE, date DATE, aapl FLOAT,
     goog FLOAT, msft FLOAT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Tnx
    (id INTEGER UNIQUE, date DATE, tnx FLOAT)''')

# Open the main content (Read only)
conn_1 = sqlite3.connect('file:TechStocks.sqlite?mode=ro', uri=True)
cur_1 = conn_1.cursor()

cur_1.execute('''SELECT * FROM Techstocks''')
for item in cur_1:
    id = item[0]
    date_str = item[1]
    date = datetime.strptime(date_str, '%m/%d/%Y').date()
    aapl = item[2]
    goog = item[3]
    msft = item[4]

    cur.execute('''INSERT OR IGNORE INTO Techstocks (id, date, aapl, goog, msft)
        VALUES ( ?, ?, ?, ?, ? )''', ( id, date, aapl, goog, msft ))
    conn.commit()

print('Techstock table transferred from TechStock.sqlite db to index.sqlite db')

cur_1.execute('''SELECT * FROM Tnx''')
for item in cur_1:
    id = item[0]
    date_str = item[1]
    date = datetime.fromisoformat(date_str).date()
    try:
        tnx = float(item[2])
    except:
        continue

    cur.execute('''INSERT OR IGNORE INTO Tnx (id, date, tnx)
        VALUES ( ?, ?, ? )''', ( id, date, tnx ))
    conn.commit()

print('Tnx table transferred from TechStock.sqlite db to index.sqlite db')

cur.close()
cur_1.close()
