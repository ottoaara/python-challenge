# Homework Module 3 Challenge Aaron Otto 4.15.23
# calling import library
import csv

# setting file path to data source
csvpath = "/Users/aaronotto/Desktop/python-challenge/PyBank/Resources/budget_data.csv"

# setting filepath to utf,opening as csvfile, skipping header and setting comma delim
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)  # skipping header

    # setting variables
    totalmonths = 0
    totalprofit = 0
    avgchange = 0
    totalchange = 0
    prev_month = ''
    prev_value = 0
    count = 0
    highestmonth = ''
    lowesttmonth = ''
    highestvalue = 0 # <> 420
    lowestvalue = 0


    # starting loop for dataset budget_data.csv (csvfile)
    for row in csvreader:
        # Requirement the total number of months included in dataset
        monthname = row[0]
        month = row[0].split('-')[1]
        value = int(row[1])
        totalmonths += 1
        totalprofit += int(row[1])
        # Requirement -the changes in "proffit/loss" over the entire period and then the avg. of those changes
        # for each month compare last month to this current
        if prev_month != '':  # calling out if the prior month not empty
            change = value - prev_value  # change is equal to current month's value minus last's
            totalchange += change  # adding the diff. to the running total of change
            count += 1  # making sure I can count lol. could use totalmonths for this too doing same thing

            # Requirement- the greatest increase in profits(date and amount) over the entire period
            if highestvalue > change: # grabing highest value in column 2 and corresponding month
                highestvalue = highestvalue
                highestmonth = highestmonth
            else:
                highestvalue = change
                highestmonth =monthname
            # Requirement- the greatest decrease in profits(date and amount) over the entire period
            if lowestvalue < change: # grabing lowest value in column 2 and corresponding month
                lowestvalue =lowestvalue
                lowestmonth =lowestmonth
            else:
                lowestvalue = change
                lowestmonth =monthname

        prev_month = month  # setting last month equal to this month after calc
        prev_value = value  # same for value basically these two sets prep for next loop of if

        # I added this in there because I kept getting div zero errors while writing and that become very annoying.
    if count > 0:
        avgchange = totalchange / (count)

#Printing to the terminal
    print("Financial Analysis\n")
    print("--------------------------")
    print(f"Total Months: ",totalmonths)
    print(f"Total: $",totalprofit)
    print(f"Average Change: $",round(avgchange,2))
    print(f"Greatest Increase in Profits:", highestmonth, "($",highestvalue ,")")
    print(f"Greatest Decrease in Profits:", lowesttmonth, "($",lowestvalue ,")")

#printing to text file
with open("/Users/aaronotto/Desktop/python-challenge/PyBank/analysis/analysis.txt", "w") as file:
    print("Financial Analysis\n", file =file)
    print("--------------------------",file =file)
    print(f"Total Months: ", totalmonths,file =file)
    print(f"Total: $", totalprofit,file =file)
    print(f"Average Change: $", round(avgchange, 2),file =file)
    print(f"Greatest Increase in Profits:", highestmonth, "($", highestvalue, ")",file =file)
    print(f"Greatest Decrease in Profits:", lowesttmonth, "($", lowestvalue, ")",file =file)