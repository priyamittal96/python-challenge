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
#Generate a count based on the candidates name and a list of the unique candidates in the data.         
        candidates.append(row[2])
        if row[2] not in people:
            people.append(row[2])
#Correspond the unique name of each candidate with the data and generate a count for each.
        if people[0] == row[2]:
            results[0] += 1
        elif people[1] == row[2]:
            results[1] += 1
        elif people[2] == row[2]:
            results[2] += 1
        else:
            results[3] += 1
#Compile the number of votes per person with the person's name.
        votes_people = {results[i]:people[i] for i in range(len(people))}

#Print to confirm the name of candidates, the number of candidates, and results along with how they correspond. 
print(people)
print(len(people))
print(results)
print(votes_people)
            
print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(candidates)}")
print(f"{people[0]}: {round((results[0]/len(candidates))*100,3)}% ({results[0]})")
print(f"{people[1]}: {round((results[1]/len(candidates))*100,3)}% ({results[1]})")
print(f"{people[2]}: {round((results[2]/len(candidates))*100,3)}% ({results[2]})")
print(f"{people[3]}: {round((results[3]/len(candidates))*100,3)}% ({results[3]})")
print("-------------------------")
print(f"Winner: {votes_people[max(votes_people)]}")
print("-------------------------")
