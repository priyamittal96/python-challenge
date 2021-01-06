import os
import csv

people =[]
candidates = []
percentage = []
winner = []
results = [0,0,0,0]

count = 0

poll_csv = os.path.join(".","Resources","election_data.csv")
with open(poll_csv) as poll_file:
    csvreader = csv.reader(poll_file, delimiter = ',')
    csv_reader = next(csvreader)
    for row in csvreader:
        candidates.append(row[2])
        if row[2] not in people:
            people.append(row[2])
        if people[0] == row[2]:
            results[0] += 1
        elif people[1] == row[2]:
            results[1] += 1
        elif people[2] == row[2]:
            results[2] += 1
        else:
            results[3] += 1
        
print(people)
print(len(people))
print(results)
            
print("Election Results")
print("-------------------")
print(f"Total Votes: {len(candidates)}")
print(f"{people[0]}: {(results[0]/len(candidates))*100}% ({results[0]})")
print(f"{people[1]}: ({results[1]})")
print(f"{people[2]}: ({results[2]})")
print(f"{people[3]}: ({results[3]})")
print("-------------------")
# print(f"Winner: {}")
print("-------------------")