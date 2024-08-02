#1. Write a Python program to read a CSV file and display its contents.
 

import csv

file_path = 'credit_risk_dataset.csv'  # Give CSV file path/name

with open(file_path, mode='r') as file: #open and read csv file hear
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)


