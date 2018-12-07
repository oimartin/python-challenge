# PyBank
# Analyze financial records using budget_data.csv

# import os and csv modules
import os
import csv

# Call budget_data.csv
openPath = os.path.join('..', '..', 'NUCHI201811DATA2', 'Homework', '03-Python', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')

totalMonths = 0
totalNet = 0
profit_loss = [] #back index....
monthlyChange = []
averageprofit_loss = 0


# open budgetData csv
with open(openPath, newline='',encoding="utf8") as budgetData:
    
    # go past header
    next(budgetData)

    # separate budgetData by commas
    reader = csv.reader(budgetData, delimiter=',')

    # loop through
    for row in reader:

        # The total number of months
        # included in the dataset after header
        totalMonths += 1
        
        # calculate total net of profits/losses
        # total net = total net + row[1]
        totalNet += int(row[1])

        # Average change in Profit/Losses between months
        # over entire period
        profit_loss.append(int(row[1]))
        
    # loop through profit_loss list 
    len(profit_loss)

    for month in profit_loss:

        #Feb - Jan etc month to month change
        monthlyChange = 
        # monthlyChange += (next(month) - month[month-1])

print(monthlyChange)

        
        



# print("Total Months: " + str(totalMonths))
# print("Total Net: "+ str(totalNet))




# The total net amount of "Profit/Losses" over
#  the entire period

# The average change in "Profit/Losses" between
#  months over the entire period

# The greatest increase in profits (date and amount)
#  over the entire period

# The greatest decrease in losses (date and amount)
#  over the entire period