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

def avg_change(profits):
    profit_sum = sum(profits)
    return profit_sum/len(profits)

#print("Average Change: " +str(avg_change(profits)))

    #for i in profits:
        #average_change = (i + (i+1))/2

    #print(average_change)

out = open("budget_summ.txt","w+")

out.write("Total Months: " + str(len(months))+"\n")
out.write("Total Profits: $" + str(sum(profits))+"\n")
out.write("Average Profits: $" + str(avg_change(profits))+"\n")



