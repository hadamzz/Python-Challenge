# Import Modules
from calendar import month
import os
import csv

# Variables and Values
list_months = []
total_months = 0
list_net= []
total_net = 0
list_monthly_change= []
previous_row_change = 0
first_PL_variable = 1
average_change = []
greatest_increase = 0
greatest_decrease = 0
greatest_decrease_month = ""
greatest_increase_month = ""

# Establish path to resouce file
pybank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Read file
with open(pybank_csv) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter= ",")
    csv_header=next(csv_file)
    data_holder=list(csv_reader)


# (1) Determine Total Number of Months
for lines in data_holder:
        
        total_months += 1

        # (2) Determine net total of Profits/Loses for entire sheet
        
        total_net += int(lines[1])

        # (3) Determine changes in Profits/Losses over entire time
        monthly_change = (int(lines[1])-(int(first_PL_variable)))
        first_PL_variable = lines[1]
        list_monthly_change.append(monthly_change)
     
        # # (5) Determine the greatest month-to-month increase
        if monthly_change > greatest_increase:
                greatest_increase = monthly_change
                greatest_increase_month = lines[0]
       

        # # # (6) Determine the greatest month-to-month decrease
        if monthly_change < greatest_decrease:
                greatest_decrease = monthly_change
                greatest_decrease_month = lines[0]

# # (4) Determine average of changes in Profits/Losses over entire time
list_monthly_change.pop(0)
average_change = (sum(list_monthly_change)) / (len(list_monthly_change))
#round it

# # (7) Print the analysis to terminal
print(average_change) 
print(total_months)
print(total_net)
#print(list_monthly_change)
print(greatest_increase)
print(greatest_increase_month)
print(greatest_decrease)
print(greatest_decrease_month)

# # (8) Export a text file with results (see photo for exactly what this should look like)
new_csv = os.path.join("..", "Resources", "new.csv")
with open(new_csv, 'w') as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerow([f"Financial Analysis"])
        csvwriter.writerow(["-------------------"])
        csvwriter.writerow([f"Total: $ {total_net}"])
        csvwriter.writerow(["Average Change: $" + str(average_change)])
        csvwriter.writerow(["Greatest Increase Amount: $" + str(greatest_increase)])
        csvwriter.writerow(["Month of Greatest Increase: " + str(greatest_increase_month)])
        csvwriter.writerow(["Greatest Decrease Amount: $" + str(greatest_decrease)])
        csvwriter.writerow(["Month of Greatest Decrease: " + str(greatest_decrease_month)])
