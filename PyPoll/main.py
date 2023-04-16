# Module 3 Challenge PyPoll assignment Aaron Otto
import csv # loading csv libraries
# setting file path to data payload
csvpath = "/Users/aaronotto/Desktop/python-challenge/PyPoll/Resources/election_data.csv"
#opening the data file and using reader
with open(csvpath, mode='r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader) # skipping first ro

    # Requirements- The total number of votes cast
    votecount = 0 # setting votcount to zero
    pollData = {} # initializing dict
    candidateVotes = {} # initializing dict
    # this is looping through the dataset basically putting the data set into a dict called pollData
    for row in csvreader:
        pollData[row[0]] = {"county": row[1], "candidate": row[2]}
        votecount += 1  # counting number of ballots ie votes cast.
        if row[2] in candidateVotes:
            candidateVotes[row[2]] += 1  # If the last row in the dataset is truthy (which it is by default) +1
        else:
            candidateVotes[row[2]] = 1  # else set to = 1 this won't happen until end of dataset becasue truthy

    # Calculate percentage of votes received by each candidate by using a dictionary called candidate%
    candidatePercentages = {} #initilaze the dict
    for candidate, votes in candidateVotes.items():  # starting loop using two columns watched a
        # youtube on this was stuck for a day on this part.  put the video in slack hope it helps folsk.
        candidatePercentages[candidate] = round((votes / votecount) * 100, 3)

        # Requirement - get the winner of the electiono based on popular vote.
        winner = max(candidateVotes, key=candidateVotes.get) # googled this one allows you to query a dict w/ key .get

    # Requirements- A complete list of candidates who received votes

    #Requirements -prints results to terminal
    print("Election Results \n")
    print("------------------------------------------")
    print(f"\nTotal number of votes cast:", votecount)
    print("\n------------------------------------------\n")
    for candidate, votes in candidateVotes.items(): # using list function so I can call items
        percentage = candidatePercentages[candidate]
        print(f"{candidate}: {percentage}% ({votes})")
    print("\n------------------------------------------\n")
    print(f"Winner:", winner)
    print("\n------------------------------------------\n")


#     # Requirements-printing to text file
    with open("/Users/aaronotto/Desktop/python-challenge/PyPoll/analysis/analysis.txt", "w") as file:
        print("Election Results \n",file =file)
        print("------------------------------------------",file =file)
        print(f"\nTotal number of votes cast:", votecount, file =file)
        print("\n------------------------------------------\n",file =file)
        for candidate, votes in candidateVotes.items():
              percentage = candidatePercentages[candidate]
              print(f"{candidate}: {percentage}% ({votes})",file =file)
        print("\n------------------------------------------\n",file =file)
        print(f"Winner:", winner, file =file)
        print("\n------------------------------------------\n",file =file)
