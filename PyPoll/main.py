import os
import csv

people =[]
candidates = []
percentage = []
winner = []

count = 0

poll_csv = os.path.join(".","Resources","election_data.csv")
with open(poll_csv) as poll_file:
    csvreader = csv.reader(poll_file, delimiter = ',')
    csv_reader = next(csvreader)
    for row in csvreader:
        candidates.append(row[2])
        if row[2] not in people:
            people.append(row[2])
        people_count = [candidates.count(ind) for ind in set(candidates)]
        
print(people)
print(people_count)
            
print("Election Results")
print("-------------------")
print(f"Total Votes: {len(candidates)}")

print("-------------------")
# print(f"Winner: {}")
print("-------------------")