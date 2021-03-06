#TO DO::  The data we need to retrieve.
#TO DO::  The total number of votes.
#TO DO::  A Complete list of candidates.
#TO DO::  Percentage of votes per candidite.
#TO DO::  Total number of votes each candidate won.
#TO DO::  The winner by popular vote.

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Total Votes
total_votes = 0

#Candidates
candidate_options = []

#candidate votes
candidate_votes = {}

#Winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

     #Print header row
    headers = next(file_reader)
    #print (headers)

    #Print Each row in CSV file
    for row in file_reader:
        #Calculate Total Votes
        total_votes+=1
        #print(row[0])

        #get candidate name from each row
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            #add candidate to list
            candidate_options.append(candidate_name)

            #track vote count
            candidate_votes[candidate_name]=0

        #tally votes
        candidate_votes[candidate_name]+=1

#get Vote Percentages
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percenatge = float(votes)/float(total_votes)*100
    
    #Winning Vote count
    print(f"{candidate_name}: {vote_percenatge:.1f}% ({votes:,})\n")

    if (votes > winning_count) and (vote_percenatge > winning_percentage):
        #set Winning Count & winning percenatge
        winning_count = votes
        winning_percentage = vote_percenatge
        winning_candidate = candidate_name

    # print(f"{candidate_name}: received {vote_percenatge:.1f}% of the vote.")
    
winning_candidate_summary = (
f"-------------------------\n"
f"Winner: {winning_candidate}\n"
f"Winning Vote Count: {winning_count:,}\n"
f"Winning Percentage: {winning_percentage:.1f}%\n"
f"-------------------------\n")
print(winning_candidate_summary)

print(f"Total Votes: {total_votes}:")
print(f"Candidates: {candidate_options}:")
print(candidate_votes)
