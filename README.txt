Analyzing the closing prices of 3 tech stocks and the US ten year treasury bonds 
and vizualizing the data using the D3 JavaScript library

You should install the SQLite browser to view and modify the databases from:

http://sqlitebrowser.org/

The first step is to extract the data from two csv files.
The extractts.py file extracts the data from the TechStocks.csv file
while the extracttnx.py file extracts the data from the ^TNX.csv file.   
It stores all of its data in a database (TechStocks.sqlite) and can be interrupted and re-started 
as often as needed.

The TechStocks.sqlite data is pretty raw, with an innefficient data model, and not compressed.
The second process is running the program clean.py.  clean.py reads the rough/raw 
data from TechStocks.sqlite and produces a cleaned-up and well-modeled version of the 
data in the file index.sqlite.  The file index.sqlite will be much smaller (often 10X
smaller) than TechStocks.sqlite because it also compresses the header and body text.

Each time clean.py runs - it completely wipes out and re-builds index.sqlite, allowing
you to adjust its parameters and edit the mapping tables in TechStocks.sqlite to tweak the 
data cleaning process.

You can re-run the clean.py over and over as you look at the data, and add mappings
to make the data cleaner and cleaner.   When you are done, you will have a nicely
indexed version of the email in index.sqlite.   This is the file to use to do data
analysis.   With this file, data analysis will be really quick.

The first, simplest data analysis is to find out the dates for which 
the closing prices of the stocks are the highest?  This is done using dump.py:

There is a simple vizualization of the dates which had the highest closing prices
in the file date.py:

This produces the file date.js which you can visualize using the file 
date.htm.

A second visualization is in line.py.  It visualizes closing prices of the stocks over time.

Its output is written to line.js which is visualized using gline.htm.
