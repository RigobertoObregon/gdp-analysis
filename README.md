## GDP Analysis 

For this lab, you will create the following 3 functions:

`def get_highest_gdp(data, year):`  
  This function will return the name of the state had the highest GDP for a specified year. It takes in a string `year` as an argument. `data` will be a `DictReader` object containing data.  

`def get_lowest_gdp(data, year):`  
  This function will return the name of the state had the lowest GDP for a specified year. It takes in a string `year` as an argument. `data` will be a `DictReader` object containing data.  

`def get_state_gdp(data, state, year):`  
  This function will return gdp value of some specific state for some specific year column. The name of the state will be passed in `state`, and the year will be passed in via `year`.

Code to read in this data will already exist. We simply need to modify our filepath to ensure that we are reading data in correctly. This data is being saved to a list called `list_data`.

We will pass this `list_data` list to the `get_highest_gdp` and `get_lowest_gdp` functions and find the state with both the highest & lowest gdp's for the year *2020*.

You will also use your `get_state_gdp()` function to calculate the GDP of New York (or your choice of state) for the year 2019 and the year 2020. You will calculate the difference between these two years:

```python
prev = get_state_gdp(data, "New York", "2019")
new = get_state_gdp(data, "New York", "2020")

print(new - prev)
```

## README (writeup)

Within your `README` file, you will provide a writeup of your project. It will come in the following format:

```
# gdp-analysis

[quick description of your code]
get_highest_dep(data, year)
This method receives as parameters, a list of dictionaries, and the year to be evaluated.
Assign an initial value to the variable highest, with the first value in the
list for the column year.
Then go through the list, evaluating for each dictionary, the column year, and comparing if the value is greater than the variable highest. If the loop
finds a higher value, assign this value to the variable highest, until 
finish looping the list (of dictionaries).
Then returns the state and the highest value.

get_lowest_dep(data, year)
This method receives as parameters, a list of dictionaries, and the year to be evaluated.
Assign an initial value to the variable lowest, with the first value in the
list for the column year.
Then go through the list, evaluating for each dictionary, the column year, and comparing if the value is lower than the variable lowest. If the loop
finds a lower value, assign this value to the variable lowest, until 
finish looping the list (of dictionaries).
Then returns the state and the lowest value.

get_state_gdp(data, state, year):
This method receives as parameters, a list of dictionaries, the state and 
the year to get the gdp for that state and year.
Then go through the list and compares if the value in the column GeoName
is equals to the parameter state. If the loop finds the value, it assign
the value to the variable gdp in order to return the value.


## Results

[How much did New York drop in GDP from 2019 to 2020? Informally, what sorts of economic factors influenced this change? Provide evidence if relevant.]

2019       --> 1,772,260.7
2020       --> 1,699,044.7
Difference -->    73,216.0

New York's GDP dropped 73,216.0 (Units) from 2019 to 2020. This could
have happened due to the COVID impact on the economy. People spending
less, having uncertainty of the events to come.


```

You will replace any text in the square-brackets with your own text.

## Challenge 1 (optional)

You will create a csv file that describes which state had the highest GDP for each year.

We will create our list of years using the following line of code:

```python
years = [str(year) for year in range(1997, 2021)]
```

For validation, your csv file should look like the attached `highest_gdp.csv` file.

You will also create a csv file that describes which state had the lowest GDP for each year.

For validation, your csv file should look like the attached `lowest_gdp.csv` file.

## Challenge 2 (optional)
 
Create a function called `get_percent_change` that calculates the [percent change](https://www.investopedia.com/terms/p/percentage-change.asp) of a specific state from one year to another. 

`def get_percent_change(state, year1, year2):`
    This function will get the percent change of gdp for a specific state from one specific year `year1`, to another `year2`.

    Feel free to utilize `get_state_gdp()`

We will use this function to create a csv file of percent changes from 2019 to 2020 for each state.
  
