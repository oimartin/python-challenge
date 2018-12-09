# PyPoll
# Analyze votes from election_data.csv
import os
import csv

# Counter for total votes
totalVotes = 0

# List of all candidates
candidate_names = []

# Total vote counts per candidate
khan = 0
correy = 0
li = 0
otooley = 0

# Percent of votes per candidate
khan_percent = 0.0
correy_percent = 0.0
li_percent = 0.0
otooley_percent = 0.0

# List of percent of votes per candidate
candidate_vote_percentages = [0]

# Sting for the winner of the popular vote
winner = ""

# Call budget_data.csv
openPath = os.path.join('..', '..', 'NUCHI201811DATA2', 'Homework', '03-Python', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')

with open(openPath, newline='',encoding="utf8") as electionData:
    
    # Go past header
    next(electionData)

# Separate electionData by commas
    reader = csv.reader(electionData, delimiter=',')

    # Go through all of the electionData 
    for row in reader:
        
        # Increment totalVotes for each row counted
        totalVotes += 1

        # Cast column with candidate names as a string
        # and save in variable candidates
        candidates = str(row[2])
        
        # Only if a candidate name is not in the
        # candidate_name list, then add that candidate name
        if candidates not in str(candidate_names):
            candidate_names.append(candidates)
        
        # Increment each candidate count when name
        # appears in the candidate column in the csv data
        if candidates == "Khan":
            khan += 1
        elif candidates == "Correy":
            correy += 1
        elif candidates == "Li":
            li += 1
        elif candidates == "O'Tooley":
            otooley += 1

# Create a function to calculate a percent value and then round
def percent_round (name):
        return round(((name/ totalVotes)*100),2)

# Percent of votes per candidate
khan_percent = round_percent(khan)
correy_percent = round_percent(correy)
li_percent = round_percent(li)
otooley_percent = round_percent(otooley)

# Winner of election based on popular vote
# Add each candidates' vote percentages to list
candidate_vote_percentages = [khan_percent, correy_percent, li_percent, otooley_percent]

# Recored the highest voter percentage
max_voter_percentage = max(candidate_vote_percentages)

# Determine winner by matching max_voter_percentage
# to candidate percentage
if max_voter_percentage == khan_percent:
    winner = "Khan"
elif max_voter_percentage == correy_percent:
    winner = "Correy"
elif max_voter_percentage == li_percent:
    winner = "Li"
elif max_voter_percentage == otooley_percent:
    winner = "O'Tolley"


# Print analysis of election results
print("Election Results")
print("---------------------------")

print(f"Total Votes: {totalVotes}")
print("---------------------------")

print(f"Khan: {khan_percent}% ({khan})")
print(f"Correy: {correy_percent}% ({correy})")
print(f"Li: {li_percent}% ({li})")
print(f"O'Tooley: {otooley_percent}% ({otooley})")
print("----------------------------")
print(f"Winner: {winner}")


# Export a text file with the results
open_path = "PyPoll_analysis.txt"

with open(open_path, 'w', newline='',encoding="utf8") as analysis_file:

    # String of info to print and formatted for a .txt file
    analysis = ["Election Results \n", 
                "---------------------------\n", 
                f"Total Votes: {totalVotes}\n", 
                "---------------------------\n", 
                f"Khan: {khan_percent}% ({khan})\n", 
                f"Correy: {correy_percent}% ({correy})\n", 
                f"Li: {li_percent}% ({li})", 
                f"O'Tooley: {otooley_percent}% ({otooley})\n", 
                "----------------------------\n", 
                f"Winner: {winner}"]
    
    # Writing out analysis string
    analysis_file.writelines(analysis)