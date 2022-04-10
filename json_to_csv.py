import json
import csv

with open("rates.json", "r") as f:
    data = json.load(f)
    rates = data["rates"]

with open ("rates.csv", "w") as f:
    fieldnames = rates[0].keys() 
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for rate in rates:
        writer.writerow(rate)