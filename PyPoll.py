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

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #Print Each row in CSV file
    #for row in file_reader:
     #   print(row[0])

     #Print header row
    headers = next(file_reader)
    print (headers)
