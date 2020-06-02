## The data we need to retrieve. 
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote
# Open and read file 

#Import modules
import csv
import os  
# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources','election_results.csv')
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote count 
total_votes = 0 
# Initialize candidate option and candidate votes
candidate_options = []
candidate_votes = {}
# Winning Candidate and winning count tracker 
winning_candidate =""
winning_count = 0 
winning_percentage = 0
#Initialize county list
county_options = []
county_votes = {}
# Initialize largest county turn out 
largest_county =""
turnout_vote = 0 


# Open the election results and read the file
with open(file_to_load) as election_data:
# Read the file object with teh reader function. 
    file_reader = csv.reader(election_data)
# Print the header row. 
    headers = next(file_reader)  
# Print each row in csv file 
    for row in file_reader:
        #  Add to the total vote count 
        total_votes += 1
    
        # Print the candidate name for each row 
        candidate_name = row[2]
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list 
            candidate_options.append(candidate_name)
        # Begin tracking candidate's vote count 
            candidate_votes[candidate_name] = 0
        # Increase candidate's vote count 
        candidate_votes[candidate_name] += 1 
        
        # Print county name
        county_name = row[1]
        # If the county name is not in list add county name 
        if county_name not in county_options:
            # Add county name to list 
            county_options.append(county_name)
            # Begin tracking county vote count
            county_votes[county_name] = 0
        # Increase county vote count 
        county_votes[county_name] += 1 

    # Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Print and write election results.
    election_results =(
            f"\nElection Results\n"
            f"-------------------------------------\n"
            f"Total Votes : {total_votes:,}\n"
            f"-------------------------------------\n")
    print(election_results,end="")
    txt_file.write(election_results)

    # Create county header
    county_header = (
        f"\n"
        f"County Votes:"
        f"\n")
    # Print and write the county header to text file 
    print(county_header)
    txt_file.write(county_header)

    # Calculate county vote percentage
    for county in county_votes :
        county_total = county_votes[county]
        county_percentage = int(county_total)/int(total_votes)*100
        # Create election results for each county 
        county_results =(f"{county} : {county_percentage:.1f}% ({county_total:,})\n")
        # Print and save the results to text file 
        print(county_results)
        txt_file.write(county_results)

        # Determine lagest turn out county 
        if (county_total>turnout_vote) :
            # Set largest county turnout
            turnout_vote = county_total
            largest_county = county
            # Print largest county turn out result
            county_turnout_result = (
            f"-------------------------------------\n"
            f"Largest County Turnout : {county}\n"
            f"-------------------------------------\n" 
            )
    print( county_turnout_result)
    txt_file.write(county_turnout_result)

    # Calculate candidate's vote percentage    
    # Iterate through the candidate list    
    for candidate in candidate_votes:
        # Retrieve vote count for candidate
        votes = candidate_votes[candidate]
        # Calculate the vote percentage 
        vote_percentage = int(votes)/int(total_votes) *100 
        
        # Print the candidate name and vote percentage 
        candidate_results=(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        # Save candidate results to the text file 
        txt_file.write(candidate_results)
        
        # Determine winning vote count and candidate
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            # Set vote count as a winning count 
            winning_count = votes
            winning_percentage = vote_percentage 
            # Set candidate's name as a winning_candidate
            winning_candidate = candidate
        # Print the winning candidate and winning percentage 
        winning_candidate_summary =(
        f"-------------------------------------\n"
        f"Winner : {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------------------\n")
    print (winning_candidate_summary)
    # Save the winning candidate summary to the text file 
    txt_file.write(winning_candidate_summary)


   


