import csv
# Only interested in Pink Morsels, Sales produced in a given day, the date of the sales and the region
# Need to take the three csv files as input and then output a singular csv files with the fields:
# Sales, Date, Region

filtered_data = []

with open('data/daily_sales_data_0.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        if row[0] == "pink morsel":
            price = 0
            quantity = 0
            total = 0
            filtered_row = [row[3], row[4]]
            price = float(row[1][1:3])
            quantity = int(row[2])
            total = price * quantity
            filtered_row.insert(0, total)
            filtered_data.append(filtered_row)

with open('data/daily_sales_data_1.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        if row[0] == "pink morsel":
            price = 0
            quantity = 0
            total = 0
            filtered_row = [row[3], row[4]]
            price = float(row[1][1:3])
            quantity = int(row[2])
            total = price * quantity
            filtered_row.insert(0, total)
            filtered_data.append(filtered_row)

with open('data/daily_sales_data_2.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        if row[0] == "pink morsel":
            price = 0
            quantity = 0
            total = 0
            filtered_row = [row[3], row[4]]
            price = float(row[1][1:3])
            quantity = int(row[2])
            total = price * quantity
            filtered_row.insert(0, total)
            filtered_data.append(filtered_row)

with open('test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["sales", "date", "region"])
    for i in range(len(filtered_data)):
        writer.writerow(filtered_data[i])