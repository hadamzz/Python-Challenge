# Import Modules
import os
import csv

from numpy import int0

# Variables and Values
voter_ids= []
votes_cast = []
votes_cast= 0
candidates = []
votes_per_candidate = []
percentage_per_candidate= []
most_votes = []
counties = []
line_count = 0


# Establish path to resouce file
pypoll_csv = os.path.join('Resources', 'election_data.csv')

# Read file
with open(pypoll_csv) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter= ",")
    csv_header=next(csv_file)

#Make lists for column data
    for row in csv_reader:
        voter_id=row[0]
        county=row[1]
        candidate=row[2]
        voter_ids.append(voter_id)
        counties.append(county)
        candidates.append(candidate)

# (1) Total number of votes cast

        line_count = len(voter_id)
print(line_count)

# (2) A complete list of candidates who received votes


# (3) The percentage of votes each candidate won
#Dictionary?

# (4) The winner of the election vased on popular vote

# (5) Print the analysis to the terminal
# print(f'{votes_cast} votes were cast')
# print(f"")

# (6) AND export a text file with the results

