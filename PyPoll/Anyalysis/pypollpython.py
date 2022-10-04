# Import Modules
import os
import csv

from numpy import int0

# Variables and Values
voter_ids= []
Candidate_Ind=[0]
votes_for_ccs = []
votes_for_ccs = 0
votes_for_dg= []
votes_for_dg = 0
votes_for_rad =[]
votes_for_rad = 0
winning_votes = []
winning_votes = 0
winner = []
winner = 0

# Establish path to resouce file
pypoll_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Read file
with open(pypoll_csv) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter= ",")
    csv_header=next(csv_file)

    # Start loop, collect number of voter IDs
    for row in csv_reader:        
        voter_id=row[0]
        voter_ids.append(voter_id)


        # # (1) Total number of votes cast
        line_count = len(voter_ids)

        # (2) A complete list of candidates who received votes
        if row[2] not in Candidate_Ind:
            Candidate_Ind.append(row[2])
        
        # (3) The percentage of votes each candidate won
        # Calculate totals votes for each candidate
        if row[2] == "Charles Casper Stockham":
            votes_for_ccs += 1
        if votes_for_ccs > winner:
            winner = votes_for_ccs
            winner_name = row[2]
        if row[2] == "Diana DeGette":
            votes_for_dg += 1
        if votes_for_dg > winner:
            winner = votes_for_dg = winner
            winner_name = row[2]
        if row[2] == "Raymon Anthony Doane":
            votes_for_rad += 1
        if votes_for_rad > winner:
            winner = votes_for_rad
            winner_name = row[2]
            
        #Calculate percentages of votes for each candidate
        
        percentage_ccs = (votes_for_ccs)/(int(line_count))*100
        percentage_dg = (votes_for_dg)/(int(line_count))*100
        percentage_rad = (votes_for_rad)/(int(line_count))*100
                        
# (4) The winner of the election based on popular vote        
        #if (vote > winning_count):
        #winning_count = votes


# (5) Print the analysis to the terminal 
print(f"Election Results:")
print(f"-----------------------")
print(f"Total number of votes: {line_count}.")
print(f"The candidates were: {Candidate_Ind}.")
print(f"Charles Casper Stockham received {votes_for_ccs} votes, totaling {percentage_ccs} percent of all votes.")
print(f"Diana DeGette received {votes_for_dg} votes, totaling {percentage_dg} percent of all votes.")
print(f"Raymon Anthony Doane received {votes_for_rad} votes, totaling {percentage_rad} percent of all votes.")
print(f"The winner is {winner_name}!")

# print(line_count)
# print(Candidate_Ind)
# print(votes_for_ccs)
# print(votes_for_dg)
# print(votes_for_rad)
# print(percentage_ccs)
# print(percentage_dg)
# print(percentage_rad)
# print(winner)
# print(winner_name)


# (6) AND export a text file with the results
new_csv = os.path.join("..", "Resources", "new.csv")
with open(new_csv, 'w') as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerow([f"Election Results:"])
        csvwriter.writerow(["------------------------"])
        csvwriter.writerow([f"Total number of votes: {line_count}."])
        csvwriter.writerow([f"The candidates were: {Candidate_Ind}."])
        csvwriter.writerow([f"Charles Casper Stockham received {votes_for_ccs} votes, totaling {percentage_ccs} percent of all votes."])
        csvwriter.writerow([f"Diana DeGette received {votes_for_dg} votes, totaling {percentage_dg} percent of all votes."])
        csvwriter.writerow([f"Raymon Anthony Doane received {votes_for_rad} votes, totaling {percentage_rad} percent of all votes."])
        csvwriter.writerow([f"The winner is {winner_name}!"])
