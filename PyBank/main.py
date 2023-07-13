import os
import csv
months = []
profit_loss = []

currentFilePath = __file__
indexOfLastDirectory = currentFilePath.rfind('\\')
currentDirectory = currentFilePath[0:indexOfLastDirectory]

pybank_budget = os.path.join(currentDirectory,'Resources', 'budget_data.csv')

with open(pybank_budget) as budgetfile:

    # CSV reader specifies delimiter and variable that holds contents
    budgetreader = csv.reader(budgetfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    budget_header = next(budgetreader)
    print(f"CSV Header: {budget_header}")

# For each row in csv file budget_data.csv
    for row in budgetreader:
        # get date from first item in row (column 1)
        date = row[0]
        # get profit/losses from second item in row (column 2)
        profit_losses = int(row[1])

        # Add date to "months" list
        months.append (date)

        # add profit/losses to "profit_loss" list
        profit_loss.append (profit_losses)

    # get total number of rows 
    total_months = len(months)
   
   # get total of all values in profit/losses column
    total_profit_loss = sum(profit_loss)
   
    # declare a new list "total_change"
    total_change = []

    # for 1 to 68 (number of rows in csv)
    for i in range(1, total_months):

        # subtract row i profit/losses value from previous row profit/losses value 
        change = profit_loss[i] - profit_loss[i-1]

        # add answer to "total_change" list
        total_change.append(change)

    average_change = sum(total_change) / (total_months - 1)
    formatted_average_change = format(average_change, ".2f")
    
    # get highest value from "total_change" list ||| NOTE length of "total_change" list is 85 due to index starting at 0 
    # and first row containing titles eg (Date and Profit/Losses)
    max_increase = max(total_change)

    # get index in "total_change" list of highest value (returns value 78 due to 
    # index starting at 0 (79) and title row (80) which is the first value of the calculation)
    max_increase_index = total_change.index(max_increase)

    # get date from "months" list at element index equal to max_increase_index
    max_increase_date = months[int(max_increase_index) + 1]  

    max_decrease = min(total_change)
    max_decrease_index = total_change.index(max_decrease)
    max_decrease_date = months[int(max_decrease_index) + 1]  

    print ("Financial Analysis")
    print ("--------------------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Profit Losses: ${total_profit_loss}")
    print(f"Average Changes: ${formatted_average_change}")
    print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
    print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")

    
    


    