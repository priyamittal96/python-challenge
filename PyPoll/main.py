import os
import csv

candidates = []
percentage = []
winner = []

count = 0

poll_csv = os.path.join('.','Resources','election_data.csv')
    with open(poll_csv) as poll_file:
    csvreader = csv.reader(poll_file, delimiter = ',')
    csv_reader = next(csvreader)
    for row in csvreader:
        if row[2] not in candidates: 
            count += 1
            candidates.append(row)
    candidates.append(row[2])
    






print("Election Results")
print("-------------------")
print(f"Total Votes: {total votes}")

print("-------------------")
print(f"Winner: {}")
print("-------------------")