import os
import csv

profits_losses = []
change_values = []
months =[]

net_total = 0
months_total = 0
next_amount = 0

bank_csv = os.path.join(".","Resources","budget_data.csv")
with open(bank_csv) as bank_file:
    csvreader = csv.reader(bank_file, delimiter = ',')
    csv_reader = next(csvreader)                   
    for row in csvreader:
        months_total += 1
        net_total += int(row[1])
        profits_losses.append(row[1])
        change_values = [int(profits_losses[i + 1]) - int(profits_losses[i]) for i in range(len(profits_losses)-1)]    
        change_total = sum(change_values)
        months.append(row[0])
        months.remove(0)
        
average_change = change_total/len(change_values)        
        
print("Financial Analysis") 
print("------------------------------")
print(f"Total Months: {months_total}")  
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Greated Increase in Profits: ${max(change_values)}")
print(f"Greatest Decrease in Profits: ${min(change_values)}")



