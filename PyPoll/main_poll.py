import pandas as pd
import csv

polldata_path = "election_data.csv"

election_df = pd.read_csv(polldata_path)
#print(election_df)

voter_count = len(election_df["Voter ID"])
candidates = election_df["Candidate"].unique()

print("Total votes:" + str(voter_count))
print("-------------Candidates running--------------")
print(candidates)

votes = election_df.groupby('Candidate').count()
#print(votes)

#vote % calculations
khan_v = round(int(votes.loc["Khan","Voter ID"])*100/voter_count)
correy_v = round(int(votes.loc["Correy","Voter ID"])*100/voter_count)
li_v = round(int(votes.loc["Li","Voter ID"])*100/voter_count)
otooley_v = round(int(votes.loc["O'Tooley","Voter ID"])*100/voter_count)


print("--------------Vote Percentages---------------")
print("Khan: " + str(khan_v) +"%")
print("Correy: " + str(correy_v) +"%")
print("Li: " + str(li_v) +"%")
print("O'Tooley:" + str(otooley_v) +"%")

if khan_v >= correy_v + li_v + otooley_v:
    print("Khan Wins!")
elif correy_v >= khan_v + li_v + otooley_v:
    print("Correy Wins!")
elif li_v >= khan_v + correy_v + otooley_v:
    print("Li Wins!")
elif otooley_v >= khan_v + correy_v + li_v:
    print("O'Tooley Wins!")
else:
    print("No Majority")





#if election_df["Candidate"] == "Khan":
 #   khan_count = +1
#elif election_df["Candidate"] == "Correy":
 #   correy_count = +1
#elif election_df["Candidate"] == "Li":
 #   li_count = +1
#elif election_df["Candidate"] == "Tooley":
 #   tooley_count = +1

#print(khan_count)


out = open("election_summ.txt","w+")

out.write("Election Results"+"\n----------------------\n")
out.write("Total Votes: " + str(voter_count) +"\n----------------------\n")
out.write("--------------Vote Percentages---------------""\n")
out.write("Khan: " + str(khan_v) +"%""\n")
out.write("Correy: " + str(correy_v) +"%""\n")
out.write("Li: " + str(li_v) +"%""\n")
out.write("O'Tooley:" + str(otooley_v) +"%""\n")
out.write("---------------Winner----------------------""\n")
out.write("Khan is the Winner!")

