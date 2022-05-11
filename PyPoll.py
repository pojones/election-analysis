###############################################################
#The data we need to retrieve:                                #
#1. The total number of votes cast                            #
#2. A complete list of candidates who received votes          #
#3. The percentage of votes each candidate won                #
#4. The total number of votes each candidate won              #
#5. The winner of the election based on popular vote          #
###############################################################

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
# assign a variable for the file to load and the path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# create a filename variable to a direct or indirect path to file
total_votes = 0
# initializes a total vote counter (requirement 1)
candidate_options = []
# initializes a new list 
candidate_votes = {}
# declare a new dictionary
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# winning candidate and winning count tracker


with open(file_to_load) as election_data:
# open file results and read the file 

    file_reader = csv.reader(election_data)
    # read the file object with the reader function
    
    headers = next(file_reader)
    print(headers)
    # read and print the header row

    for row in file_reader:
        total_votes += 1
        #add to total vote count
        candidate_name = row[2]
        # print candidate name from each row (requirement 2)
        
        if candidate_name not in candidate_options:
        # if candidate doesn't match existing entry
            candidate_options.append(candidate_name)
            # add candidate's names to list
            candidate_votes[candidate_name] = 0
            # begin tracking that candidates vote count
        candidate_votes[candidate_name] += 1 
        # add that vote to the candidate's count (requirement 4)

for candidate_name in candidate_votes:
# iterate through the candidate list
    votes = candidate_votes[candidate_name]
    # retrieve vote count of candidate
    vote_percentage = float(votes) / float(total_votes)*100
    # calculate the percentage of votes (requirement 3)
    print(f'{candidate_name}: received {vote_percentage:.1f}% of the vote')

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # determine if votes are greater than the winning count
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning vote count: {winning_count:,}\n"
    f"Winning percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)
print(total_votes)
print(candidate_votes)



