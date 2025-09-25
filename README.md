## Programming Assignment 3 – Python Data Analysis

_____________________________________________________________________________________________________________________________________

## Summary

This repository contains solutions to programming experiments involving Python Data Analysis. 
The experiment focuses on practicing data handling, subsetting, slicing, and indexing using the Pandas library in Python.

_____________________________________________________________________________________________________________________________________

**The problems included are:**

Problem 1: Load and display data from the provided CSV file.

Problem 2: Perform subsetting, slicing, and indexing operations to extract the dataframe cars.

_____________________________________________________________________________________________________________________________________
## Problem Descriptions and Solutions

## 1. 
**Problem:**
a. Load the .csv file into a data frame
b. Display the first five and last five rows of the resulting cars

**Code Snippet:**

```python
import pandas as pd

cars = pd.read_csv('cars.csv')
cars

cars.head()

cars.tail()
```
_____________________________________________________________________________________________________________________________________

**Explanation:**
import pandas as pd → imports the Pandas library and gives it the shorter name pd

cars = pd.read_csv('cars.csv') → reads the file cars.csv, stores in the variable cars, and loads the data into a DataFrame

cars.head() → shows the first 5 rows of the DataFrame by default

cars.tail() → shows the last 5 rows of the DataFrame by default

**Example Output:**
	Model	mpg	cyl	disp	hp	drat	wt	qsec	vs	am	gear	carb
0	Mazda RX4	21.0	6	160.0	110	3.90	2.620	16.46	0	1	4	4
...
31	Volvo 142E	21.4	4	121.0	109	4.11	2.780	18.60	1	1	4	2
_____________________________________________________________________________________________________________________________________

## 2.
**Problem:**
a. Display the first five rows with odd-numbered columns of cars.
b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
c. Identify the cylinders (‘cyl’) that the car model ‘Camaro Z28’ has.
d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’, and ‘Honda Civic’ have.

**Code Snippet:**
```python
import pandas as pd

cars = pd.read_csv('cars.csv')
cars

cars.iloc[:5, ::2]

cars.loc[(cars['Model']=='Mazda RX4')]

cars.loc[cars['Model']=='Camaro Z28', ['cyl']]

cars.loc[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl','gear']]
```
_____________________________________________________________________________________________________________________________________
**Explanation:**
import pandas as pd → imports the Pandas library and gives it the shorter name pd

cars = pd.read_csv('cars.csv') → reads the file cars.csv, stores in the variable cars, and loads the data into a DataFrame

cars.iloc[:5, ::2] → pick rows/columns by position; the first 5 rows, every other column

cars.loc[(cars['Model']=='Mazda RX4')] → pick rows/columns by name; rows have the Model column equal to "Mazda RX4"

cars.loc[cars['Model']=='Camaro Z28', ['cyl']] → filters the DataFrame to only the row(s) with Model = Camaro Z28 and return only the cyl column

cars.loc[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']), ['Model', 'cyl','gear']] → checks if each Model is one of the given values, and selects and show only their rows

**Example Output:**
	Model	cyl	gear
1	Mazda RX4 Wag	6	4
18	Honda Civic	4	4
28	Ford Pantera L	8	5
_____________________________________________________________________________________________________________________________________
## Libraries Used
Pandas – for DataFrame creation, data selection, slicing, and indexing
_____________________________________________________________________________________________________________________________________
## Conclusion
Through the experiment I learned how to:

- Load external data into Pandas DataFrames

- Use .head(), .tail(), .iloc, .loc, and .isin() for data selection

- Apply subsetting, slicing, and indexing operations effectively

- Analyze structured data using Python and Pandas


