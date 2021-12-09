import sqlite3
from collections import defaultdict

conn = sqlite3.connect('index.sqlite')
cur = conn.cursor()

while True:
    howmany = input("How many days from 1 Dec 2015? ")
    if ( len(howmany) < 1 ) : exit()
    try:
        howmany = int(howmany)
        howmany2 = howmany
        break
    except:
        print("Error: invalid input. Please enter an integer")

cur.execute('SELECT date, aapl, goog, msft FROM Techstocks')
techstocks = dict()
for row in cur:
    if howmany > 0:
        techstocks[row[0]] = row[1],row[2],row[3]
        howmany = howmany - 1
        date = row[0]
        print(row)
print('Techstocks done')

cur.execute('SELECT date, tnx FROM Tnx')
tnx = dict()
for row in cur:
    if howmany2 > 0:
        tnx[row[0]] = row[1]
        howmany2 = howmany2 - 1
        print(row)
print('Tnx done')

fhand = open('line.js','w')
fhand.write("line = [ ['Day','aapl','goog','msft','tnx']")

for key, value in techstocks.items():
    fhand.write(",\n['"+key+"'")
    for item in value:
        fhand.write(","+str(item))
    fhand.write(","+str(tnx.get(key)))
    fhand.write("]");

fhand.write("\n];\n")
fhand.close()

cur.close()
print("Output written to line.js")
print("Open line.htm to visualize the data")
