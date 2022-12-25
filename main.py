import csv
# Only interested in Pink Morsels, Sales produced in a given day, the date of the sales and the region
# Need to take the three csv files as input and then output a singular csv files with the fields:
# Sales, Date, Region

with open('data/daily_sales_data_0.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)