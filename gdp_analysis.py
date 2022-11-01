import csv

def get_highest_gdp(data, year):
    highest = float(data[0][year])
    for row in data:
        if float(row[year]) > highest:
            highest = float(row[year])
            state = row["GeoName"]
    return state, highest


def get_lowest_gdp(data, year):
    lowest = float(data[0][year])
    for row in data:
        if float(row[year]) < lowest:
            lowest = float(row[year])
            state = row["GeoName"]
    return state, lowest

def get_state_gdp(data, state, year):
    gdp = -1
    for row in data:
        if row["GeoName"] == state:
            gdp = row[year]
    return gdp

# save each row into a list (TODO: change to your path!)
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)

#print(list_data)


year = '2004'

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"
state_high, high = get_highest_gdp(list_data, year)

# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"
state_low, low = get_lowest_gdp(list_data, year)

print(f"year: {year}, lowest: {state_low} {low}, highest: {state_high} {high}")

gdp = get_state_gdp(list_data, "New York", "2020")

print(f"gdp {gdp}")

print(1772260.7 - 1699044.7)

print("\nHighests GDP per year\n")
for year in range(1997, 2021):
    state_high, high = get_highest_gdp(list_data, str(year))
    print(year, state_high, high)

print("\nLowests GDP per year\n")
for year in range(1997, 2021):
    state_low, low = get_lowest_gdp(list_data, str(year))
    print(year, state_low, low)
