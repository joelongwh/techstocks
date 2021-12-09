import sqlite3
import time
import string

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
    cur.execute('SELECT date, aapl FROM Techstocks')
elif asset == "goog":
    cur.execute('SELECT date, goog FROM Techstocks')
elif asset == "msft":
    cur.execute('SELECT date, msft FROM Techstocks')
elif asset == "tnx":
    cur.execute('SELECT date, tnx FROM Tnx')

di = dict()
for row in cur:
    di[row[0]] = row[1]

prices = list()
for d,p in di.items():
    new_tuple = (p,d)
    prices.append(new_tuple)

prices = sorted(prices, reverse=True)
highest = prices[0][0]
lowest = prices[howmany-1][0]
print('Highest:', highest)
print('Lowest:', lowest)

# Spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

fhand = open('date.js','w')
fhand.write("date = [")
first = True
for price in prices[:howmany]:
    if not first : fhand.write( ",\n")
    first = False
    size = price[0]
    size = (size - lowest) / float(highest - lowest)
    size = int((size * bigsize) + smallsize)
    fhand.write("{text: '"+price[1]+"', size: "+str(size)+"}")
fhand.write( "\n];\n")
fhand.close()

cur.close()
print("Output written to date.js")
print("Open date.htm in a browser to see the vizualization")
