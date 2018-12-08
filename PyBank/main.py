# PyBank
# Analyze financial records using budget_data.csv

# import os and csv modules
import os
import csv
import pandas as pd

# Call budget_data.csv
openPath = os.path.join('..', '..', 'NUCHI201811DATA2', 'Homework', '03-Python', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')
totalMonths = 0
netTotal = 0
budget_df = pd.read_csv(openPath, encoding="ISO-8859-1")

# open budgetData csv
with open(openPath, newline='',encoding="utf8") as budgetData:
    
    # Go past header
    # Separate budgetData file into columns
    next(budgetData)
    reader = csv.reader(budgetData, delimiter=',')

    for row in reader:

        # Count of all months 
        totalMonths += 1
        
        # Cast row[1] as integers and save in variable
        Profits_Losses = int(row[1])

        # Calculate net of profits/losses
        netTotal += Profits_Losses

# Begin calculating monthly change
# Within df, cast 'Profit/Losses' column as numbers
pd.to_numeric(budget_df['Profit/Losses'])

# Create new column for Monthly Change
# Subtract the previous month from the next month revenue
budget_df['Monthly Change'] = (budget_df['Profit/Losses'].shift(-1) - budget_df['Profit/Losses'])

# Shift cells up by one, so monthly change starts with Jan 2010 to Feb 2010
budget_df['Monthly Change'] = budget_df['Monthly Change'].shift(1)

# Average monthly change is the sum of month to month changes
# divided by the length of the df - 1
net_change = budget_df['Monthly Change'].sum()
avg_mnthly_chng = net_change / (len(budget_df)-1)

# Set df index to 'Monthly Change'
budget_df_dateind = budget_df.set_index("Monthly Change")

# Greatest Increase in Profits
max_profit = budget_df["Monthly Change"].max()
max_profit_date = budget_df_dateind.loc[max_profit,"Date"]

# Greatest decrease in Profits
max_loss = budget_df["Monthly Change"].min()
max_loss_date = budget_df_dateind.loc[max_loss, "Date"]


print("Financial Analysis")
print("------------------------------")

print(f"Total Months: {totalMonths}")
print(f"Total Net: {netTotal}")
print(f"Average_change {avg_mnthly_chng}")

print(f"Greateest Increase in Profits: {max_profit_date} (${max_profit})")
print(f"Greatest Decrease in Profits: {max_loss_date} (${max_loss})")

# Create output_pybank.txt file of analysis 
output = open("output_pybank.txt", "w")

analysis = ["Financial Analysis \n", 
    "------------------------------\n", 
    f"Total Months: {totalMonths}\n",
    f"Total Net: {netTotal}\n",
    f"Average_change {avg_mnthly_chng}\n",
    f"Greateest Increase in Profits: {max_profit_date} (${max_profit})\n",
    f"Greatest Decrease in Profits: {max_loss_date} (${max_loss})\n"]

# Write analysis and close file
output.writelines(analysis)
output.close()
   

# Total net amount of "Profit/Losses"

# Average change in "Profit/Losses" between months

# Greatest increase in profits (date and amount)

# Greatest decrease in losses (date and amount)