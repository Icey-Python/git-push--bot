import csv 
from datetime import datetime

#open and append to the csv file
with open('data.csv', mode='a', newline='') as file:
    # Define the fieldnames (header)
    fieldnames = ['time']
    # Create a CSV DictWriter object
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    # Write the header row
    writer.writeheader()
    # Write some data rows
    writer.writerow({'time':datetime.now()})
