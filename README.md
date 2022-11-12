# **Problem:**

Create a framework or function to process Forex transaction requests extracted from files produced by our customer's internal systems.

# Challenge

Employing any architectural solutions and design patterns of your choosing, you are asked to create a solution for processing these foreign exchange transaction requests.

# Outline:

- Files will be delivered to known folder locations 

- Files within each folder will all have the same format

- On processing each file we should:

Read the requests from the file, considering the ability to handle multiple data formats / schemas
Retrieve an FX rate to convert from source currency to destination currency
You can create your own pseudorandom FX rate generator for all combinations of USD, EUR, GBP &amp; AUD currencies, or as a shortcut, obtain rates from a web service such as https://fixer.io/ or https://free.currencyconverterapi.com/ using python requests library or url library.

Save details of each transaction, including the FX rate used, to the data store.
This can be a database, but for the purpose of this challenge an in memory solution will be sufficient, for example utilising any standard python collections or any suitable in-memory data structure. If, however, you wish to pursue a database solution a simple, file based RDBMS such as SQLite ( https://sqlite.org ) mapped via an ORM ( https://pypi.org/project/ORM-SQLite/ ) or (https://github.com/coleifer/peewee) or (SQL Alchemy) will be sufficient and will demonstrate your exposure to this ORM.

- Input Files should only be processed once

- Provide a View / GUI or Command line interface  to display these transactions with their corresponding FX rates

For Example: A command line interface where pointing to a folder would read all the csv files in that folder and output the results as well as storing the transaction details in the database.

Stretch Goal: Implement functionality that can consume 1,000,000 records from the file in a scalable, non-blocking manner. Measure the time taken and display it in the post-processing result. 

Note: If you wish to pursue this stretch goal, you may find that the database/ORM storage method above is better suited to supporting this volume of input.

You may design the data storage format as you see fit for the solution.

The input file will contain data representing an FX transaction request. There are currently 3 known CSV file formats that we need to handle but we know this will need to be extended in future.

We should also be able to support other file types, like JSON / XML / etc in future.

The three known formats right now (all CSV)

_**Format 1:**_

`ID, SourceCurrency, DestinationCurrency, SourceAmount

 USD, EUR, 1000.00
EUR, AUD, 2050.50`

_**Format 2:**_

ID|Currency1|Currency2|SrcAmount

EUR|GBP|999
AUD|USD|30000


_**Format 3:**_

TrxId, CurrencyFrom, CurrencyTo, AmountFrom

GBP, USD, 1928
USD, EUR, 150000

# **Setup:**

Enter the API key in the _credenitial.yml_

`"apikey": 'API KEY TO BE ENTERED HERE'`

Input of the folder to be selected for the files with tranactions
Select file from the list provided to be selected as an output.
