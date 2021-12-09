import sqlite3
from datetime import datetime

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

while True:
    asset = input("Asset class of interest (aapl, goog, msft or tnx): ")
    if ( len(asset) < 1 ) : exit()
    if asset not in {"aapl", "goog", "msft", "tnx"}:
        print("Error: invalid asset class.")
        continue
    else: break

while True:
    howmany = input("Dates and prices of best ___ days ")
    if ( len(howmany) < 1 ) : exit()
    try:
        howmany = int(howmany)
        break
    except:
        print("Error: invalid input. Please enter an integer")

if asset == "aapl":
    sqlstr = 'SELECT date, aapl FROM Techstocks ORDER BY aapl DESC'
elif asset == "goog":
    sqlstr = 'SELECT date, goog FROM Techstocks ORDER BY goog DESC'
elif asset == "msft":
    sqlstr = 'SELECT date, msft FROM Techstocks ORDER BY msft DESC'
elif asset == "tnx":
    sqlstr = 'SELECT date, tnx FROM Tnx ORDER BY tnx DESC'

for row in cur.execute(sqlstr):
    if howmany > 0:
        print('Date:', row[0], '|', 'Closing price:', row[1])
        howmany = howmany - 1

cur.close()
