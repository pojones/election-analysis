####################################################################################
#You've helped Seth and Tom submit the election audit results to the election comm-#
#ission. But wait! The election commission has requested some additional data to   #
#complete the audit:                                                               #
#   1. The voter turnout for each county                                           #
#   2. The percentage votes from each county out of the total count                #
#   3. The county with the highest turnout                                         #
#Print the results to terminal, in a text file, and then do written analysis of the#
#election audit in a README.                                                       #
####################################################################################

import csv
import os
# dependencies imported

file_to_load = os.path.join("..", "Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
# initiate variables to load from and save to the path

total_votes = 0
# intialize a vote counter

candidate_options = []
candidate_votes = {}
# creates empty candidate options list and candidate votes dictionary
list_of_counties = []
county_votes = {}
# creates empty counties list and county votes dictionary
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# tracks winning candidate, their vote count, and percentage
county_turnout = ""
turnout_votes = 0
# tracks county with highest turnout and its number of votes

###################################################################################
# The first 'with' statement will read the csv file and convert the data into a   #
# list of dictionaries.                                                           #
###################################################################################

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    # apply csv reader function to election_data file, and assign it 'reader'
    header = next(reader)
    # read the header 
    for row in reader:
    # for each row in the csv file: 
        total_votes += 1
        candidate_name = row[2]
        # extracts candidate name from each row and increments vote count by one
        candidate_county = row[1]
        # extracts county name from each row
        if candidate_name not in candidate_options:
        # if candidate doesn't match existing entry, then:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            # add candidate's name to list, and start tracking their vote count
        candidate_votes[candidate_name] += 1
        # increment vote count per candidate by one
        if candidate_county not in list_of_counties:
        # if the county is not already in the list of counties, then:
            list_of_counties.append(candidate_county)
            county_votes[candidate_county] = 0
            # add candidate's county to list of counties, and start tracking votes
        county_votes[candidate_county] += 1
        # increment vote count per county by one

###################################################################################
# This second 'with' statement will print the results to terminal, then write and #
# save the results to our text file.                                              #
###################################################################################

with open(file_to_save, "w") as txt_file:
# save the results to our text file
    election_results = (
        f"\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-----------------------\n\n"
        f"County Votes\n")
    print(election_results, end="")
    # prints the election results to terminal
    txt_file.write(election_results)
    # writes the election results to our text file

    for candidate_county in county_votes:
    # for the each county in the county dictionary:

        votes_by_county = county_votes.get(candidate_county)
        county_percentage = float(votes_by_county) / float(total_votes) * 100
        county_results = (
            f"{candidate_county}: {county_percentage:.1f}% (votes_by_county:,)\n")
        # retrieve vote count per county and percentage of total
        print(county_results)
        txt_file.write(county_results)
        # print each county's voter count and percentage to terminal and text file

        if (votes_by_county > turnout_votes) and (county_percentage > county_turnout):
            turnout_votes = votes_by_county
            county_turnout = county_percentage
        # find county with highest vote count and highest percentage turnout

        winning_county_summary = (
            f"\n\n----------------------\n"
            f"Largest County Turnout: {county_turnout}\n"
            f"--------------------------\n")
        print(winning_county_summary)
        txt_file.write(winning_county_summary)

    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

