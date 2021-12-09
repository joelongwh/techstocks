import sqlite3
import csv
import re

conn = sqlite3.connect('TechStocks.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Tnx
    (id INTEGER UNIQUE, date TEXT, tnx TEXT)''')

# Pick up where we left off
start = None
cur.execute('SELECT max(id) FROM Tnx' )
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
file = open("^TNX.csv")
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
    cur.execute('SELECT id FROM Tnx WHERE id=?', (start,) )
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

    date = rows[start-1][0]
    tnx = rows[start-1][5]

    cur.execute('''INSERT OR IGNORE INTO Tnx (id, date, tnx)
        VALUES ( ?, ?, ? )''', ( start, date, tnx ))

file.close()
conn.commit()
cur.close()
