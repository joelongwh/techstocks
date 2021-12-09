import sqlite3
import csv
import re

conn = sqlite3.connect('TechStocks.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Techstocks
    (id INTEGER UNIQUE, date TEXT, aapl TEXT,
     goog TEXT, msft TEXT)''')

# Pick up where we left off
start = None
cur.execute('SELECT max(id) FROM Techstocks' )
try:
    row = cur.fetchone()
    if row is None :
        start = 0
    else:
        start = row[0]
except:
    start = 0

if start is None : start = 0

print('Starting from day', start+1)

# Open and read csv file
file = open("TechStocks.csv")
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)

many = 0
while True:
    if ( many < 1 ) :
        conn.commit()
        sval = input('How many days:')
        if ( len(sval) < 1 ) : break
        many = int(sval)

    start = start + 1
    cur.execute('SELECT id FROM Techstocks WHERE id=?', (start,) )
    try:
        row = cur.fetchone()
        if row is not None : continue
    except:
        row = None

    try:
        print(rows[start-1])
    except:
        break
        continue

    many = many - 1

    id = rows[start-1][0]
    date = rows[start-1][1]
    aapl = rows[start-1][2]
    goog = rows[start-1][3]
    msft = rows[start-1][4]

    cur.execute('''INSERT OR IGNORE INTO Techstocks (id, date, aapl, goog, msft)
        VALUES ( ?, ?, ?, ?, ? )''', ( id, date, aapl, goog, msft ))

file.close()
conn.commit()
cur.close()
