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

with open(file_to_load) as election_data:
# open file results and read the file 

    file_reader = csv.reader(election_data)
    # read the file object with the reader function
    
    headers = next(file_reader)
    print(headers)
    # read and print the header row


