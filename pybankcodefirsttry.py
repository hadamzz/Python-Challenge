# Import Libraries
import os
import csv

# Variables and Values
list_months = []
total_months = 0
list_net= []
total_net = 0
list_monthly_change= []
previous_row_change = 0
# current_row = 0
# next_row = 0
first_PL_variable = 1
average_change = []
greatest_increase = []
greatest_decrease = []
# greatest_decrease_date = 0
# greatest_increase_date = 0

# Establish path to resouce file
pybank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Read file
with open(pybank_csv) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter= ",")
    csv_header=next(csv_file)
    data_holder = list(csv_reader)
    print(data_holder)

# (1) Determine Total Number of Months
for lines in data_holder:

#print(lines)
        # total_months += 1
        #print(total_months)

        # (2) Determine net total of Profits/Loses for entire sheet
        #print(lines[1])
        total_net += int(lines[1])
        print(total_net)
       

        # (3) Determine changes in Profits/Losses over entire time
        list_monthly_change = (int(lines[1])-(int(first_PL_variable)))
        first_PL_variable = lines[1]
        print(list_monthly_change)
     
        # # (4) Determine average of changes in Profits/Losses over entire time
        average_change = total_net/total_months
        print(average_change)
       

# # (5) Determine the greatest month-to-month increase
# Calculate the greatest increase
# if list_monthly_change > greatest_increase[1]:
# greatest_increase[0] = row[0]
# greatest_increase[1] = net_change

        greatest_increase = max(list_monthly_change)
        print(greatest_increase)
       


# # (6) Determine the greatest month-to-month decrease
        greatest_decrease = max(list_monthly_change)
        print (greatest_decrease)

# # (7) Print the analysis to terminal
        # print(total_net)
        # print(average_change)
        # print(greatest_increase)
        # print(greatest_decrease)



# # (8) Export a text file with results (see photo for exactly what this should look like)
# with open(pybank_csv, 'w') as csvwriter:
#         csvwriter.writerow("Financial Analysis")
#         csvwriter.writerow("-------------------")
#         csvwriter.writerow("Total: $" + str(total_net))
#         csvwriter.writerow("Average Change: " + str(average_change))
#         csvwriter.writerow("Greatest Increase: " + str(greatest_increase))
#         csvwriter.writerow("Greatest Decrease: " + str(greatest_decrease)) 