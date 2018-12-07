# PyPoll
# Analyze votes from election_data.csv

# import os and csv modules
import os
import csv

totalVotes = 0

# Call budget_data.csv
openPath = os.path.join('..', '..', 'NUCHI201811DATA2', 'Homework', '03-Python', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')

with open(openPath, newline='',encoding="utf8") as electionData:
    # go past header
    next(electionData)

# separate electionData by commas
    reader = csv.reader(electionData, delimiter=',')

    # loop through
    for row in reader:
        
        # total number votes cast
        totalVotes += 1

        # list of candidates
        candidates = row[2]
        Khan = candidates.count("Khan")
        Correy = candidates.count("Correy")
        Li = candidates.count("Li")
        OTooley = candidates.count("O'Tooley")

print("Total Votes: " + str(totalVotes))
print(Khan, Correy, Li, OTooley )
