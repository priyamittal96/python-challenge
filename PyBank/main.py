import os
import csv

month = []
profits = []
losses = []

net_total = 0
months_total = 0

bank_csv = os.path.join(".","Resources","budget_data.csv")
with open(bank_csv) as bank_file:
    csvreader = csv.reader(bank_file, delimiter = ',')
    csv_reader = next(csvreader)                   
    for row in csvreader:
        months_total += 1
        net_total += int(row[1])
    

print("Financial Analysis") 
print("------------------------------")
print(f"Total Months: {months_total}")  
print(f"Total: ${net_total}")
                
        
    
    





