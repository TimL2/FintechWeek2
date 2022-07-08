# -*- coding: utf-8 -*-
"""
Student Do: Trading Log.

This script demonstrates how to perform basic analysis of trading profits/losses
over the course of a month (20 business days).
"""

# @TODO: Initialize the metric variables

Total_Days = 0
Profitible_Days = 0
Unprofitible_Days = 0
Max_Gain = 0
Max_Loss = 0
Total = 0
Average = 0

# @TODO: Initialize lists to hold profitable and unprofitable day profits/losses

Profit_list = []
Unprofit_list = []


# List of trading profits/losses
trading_pnl = [ -224,  352, 252, 354, -544,
                -650,   56, 123, -43,  254,
                 325, -123,  47, 321,  123,
                 133, -151, 613, 232, -311 ]

# @TODO: Iterate over each element of the list

#for pl in trading_pnl:
#    print(pl)

    # @TODO: Cumulatively sum up the total and count
for pl in trading_pnl:
    Total += pl
    Total_Days += 1

print(Total)
print(Total_Days)
    
    # @TODO: Write logic to determine minimum and maximum values
for pl in trading_pnl:
    if Max_Loss ==0:
        Max_Loss = pl
    elif pl < Max_Loss:
        Max_Loss = pl
    if pl > Max_Gain:
        Max_Gain = pl

print(Max_Loss)
print(Max_Gain)


    # @TODO: Write logic to determine profitable vs. unprofitable days
for pl in trading_pnl:
    if pl > 0:
        Profit_list.append(pl)
    elif pl <0:
        Unprofit_list.append(pl)

print(Profit_list)
print(Unprofit_list)


# @TODO: Calculate the average
Average = round(Total / Total_Days,2)

# @TODO: Calculate count metrics
for pl in trading_pnl:
    if pl > 0:
        Profitible_Days += 1
    elif pl <0:
        Unprofitible_Days += 1

# @TODO: Calculate percentage metrics



# @TODO: Print out the summary statistics

