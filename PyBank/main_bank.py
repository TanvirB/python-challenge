#import pandas as pd
#file = "budget_data.csv"

#df_budget = pd.read_csv("budget_data.csv")

#months = df_budget.count(0)

#print(months)

import os
import csv

budget_file = os.path.join("budget_data.csv")

months = []
profits = []

with open(budget_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))

    print("Total Months: " + str(len(months)))
    print("Total Profits: $"+ str(sum(profits)))


#making a list of all changes - take value of next row, subtract current row, to check for change
change = []
for i in profits:
    change.append((i+1)-i)
print(change) #i's cancel and it keeps showing one, need to fix

#get average change by adding all values, and dividing by # of values.
avg_change = sum(change)/len(change)
print(avg_change)

out = open("budget_summ.txt","w+")
out.write("Total Months: " + str(len(months)) +"\n")
out.write("Total Profits: $" + str(sum(profits)) +"\n")
out.write("Average Profits: $" + str(avg_change) +"\n")



