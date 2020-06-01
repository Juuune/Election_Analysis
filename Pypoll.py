# Open and read file 

##Import modules
import csv
import os  
# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources','election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file
with open(file_to_load) as election_data:
# Read the file object with teh reader function. 
    file_reader = csv.reader(election_data)
# Print the header row. 
    headers = next(file_reader)
    print(headers)
     # To do: perform analysis.
    


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")

## The data we need to retrieve. 
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote
