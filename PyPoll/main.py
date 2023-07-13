import os
import csv

currentFilePath = __file__
indexOfLastDirectory = currentFilePath.rfind('\\')
currentDirectory = currentFilePath[0:indexOfLastDirectory]

pypoll_election = os.path.join(currentDirectory,'Resources', 'election_data.csv')

with open(pypoll_election) as electionfile:

    # CSV reader specifies delimiter and variable that holds contents
    electionreader = csv.reader(electionfile, delimiter=',')
    print(electionreader)

    # Read the header row first (skip this step if there is no header)
    election_header = next(electionreader)
    print(f"CSV Header: {election_header}")

    data = list(electionreader)
    row_count = len(data)
    print(row_count)

    candilist = list()
    tally = list()
    for i in range (0,row_count):
        candidate = data[i][2]
        tally.append(candidate)
        if candidate not in candilist: 
            candilist.append(candidate)
    candicount = len(candilist)
    print(candicount)
    
    votes = list()
    percentage = list()
    for j in range (0,candicount):
        name = candilist[j]
        votes.append(tally.count(name))
        vprct = votes[j]/row_count
        percentage.append(vprct) 
        formatted_percentage = ["{:.3%}".format(p) for p in percentage]
    print(formatted_percentage)
    winner_index = votes.index(max(votes))    
    winner_name = candilist[int(votes.index(max(votes)))]
    print(winner_name)

    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    for k in range (0,candicount): 
        print(f"{candilist[k]}: {formatted_percentage[k]} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {winner_name}")
    print("----------------------------")



    print("Election Results", file=open("analysis/PyPoll.txt", "a"))
    print("----------------------------", file=open("analysis/PyPoll.txt", "a"))
    print(f"Total Votes: {row_count:,}", file=open("analysis/PyPoll.txt", "a"))
    print("----------------------------", file=open("analysis/PyPoll.txt", "a"))
    for k in range (0,candicount): 
        print(f"{candilist[k]}: {percentage[k]:.3%} ({votes[k]:,})", file=open("analysis/PyPoll.txt", "a"))
    print("----------------------------", file=open("analysis/PyPoll.txt", "a"))
    print(f"Winner: {candilist[winner_index]}", file=open("analysis/PyPoll.txt", "a"))
    print("----------------------------", file=open("analysis/PyPoll.txt", "a"))


