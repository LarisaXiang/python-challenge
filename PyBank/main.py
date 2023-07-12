import os
import csv
months = []
profit_loss = []

pybank_budget = os.path.join('Resources', 'budget_data.csv')

with open(pybank_budget) as budgetfile:

    # CSV reader specifies delimiter and variable that holds contents
    budgetreader = csv.reader(budgetfile, delimiter=',')

    print(budgetreader)

    # Read the header row first (skip this step if there is no header)
    budget_header = next(budgetreader)
    print(f"CSV Header: {budget_header}")

    for row in budgetreader:
        date = row[1]
        profit_losses = int(row[1])

        months.append (date)
        profit_loss.append (profit_losses)

    total_months = len(months)
    print(total_months)
    total_profit_loss = sum(profit_loss)
    print(total_profit_loss)
    
    total_change = 0
    for i in range(1, total_months):
        change = profit_loss[i] - profit_loss[i-1]
        total_change += change

    average_change = total_change / (total_months - 1)
    formatted_average_change = format(average_change, ".2f")
    print(formatted_average_change)
