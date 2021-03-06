# Election-Analysis
## Project Overview
A Colorado Board of Elections employee assigned the following tasks to complete the election audit of a recent local congressional election.
1.	Calculate the total number of votes cast.
2.	Get a complete list of candidates who received votes.
3.	Calculate the total number of votes for each candidate received.
4.	Calculate the percentage of votes each candidate won.
5.	Determine the winner of the election based on popular vote.
6.	Calculate the voter turnout for each county.
7.	Calculate the percentage of votes from each county out of the total.
8.	Determine the county with the highest turnout.
## Resources
- Data Source: election_results.csv
- Software: Python 3.9.1, Visual Studio Code 1.52.1

![Election Results text file image](https://github.com/pojones/election-analysis/blob/0bedf97b15cdf0bc0800000acafb10d62a0391cd/election-results.png)
## Summary
- The analysis of the election shows that:
  - There were 369,711 votes cast in the election
  - The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
  - The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote, for a total of 85,213 votes.
    - Diana DeGette received 73.8% of the vote, for a total of 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote, for a total of 11,606 votes.
  - The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote for a total of 272,892 votes.
  - The voter turnout for each county was:
    - Jefferson produced 10.5% of voters, for a total of 38,855 voters.
    - Denver produced 82.8% of voters, for a total of 306,055 voters.
    - Arapahoe produced 6.7% of voters, for a total of 24,801 voters.
  - The county with the largest voter turnout was:
    - Denver, which produced 82.8% of voters, for a total of 306,055 voters.
 
## Election Audit Summary
Since the bulk of this script is simply referencing a data file and returning information within it, there isn’t very much mathematical analysis occurring. As a result, this program can easily be scaled out to accommodate larger audit jobs without many changes to the logic structure of the script. For example, adapting the script to observe state voter turnouts versus county turnouts would be as simple as altering some variables, and referencing a new piece of data. With more data, we could extract more information about voter demographics and candidate effectiveness on the lines of household income, race, gender, marital status, household size, and other potential independent variables. 

