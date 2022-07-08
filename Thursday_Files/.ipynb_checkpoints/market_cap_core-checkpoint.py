# -*- coding: utf-8 -*-
"""
Student Activity: Market Capitalization.

This script showcases the use of Python Dicts to determine the
bank names associated with the corresponding market cap ranges.
"""

# Banks and Market Caps
#-----------------------
# JP Morgan Chase: 327
# Bank of America: 302
# Citigroup: 173
# Wells Fargo: 273
# Goldman Sachs: 87
# Morgan Stanley: 72
# U.S. Bancorp: 83
# TD Bank: 108
# PNC Financial Services: 67
# Capital One: 47
# FNB Corporation: 4
# First Hawaiian Bank: 3
# Ally Financial: 12
# Wachovia: 145
# Republic Bancorp: .97

# @TODO: Initialize a dictionary of banks and market caps (in billions)


banks = {
'JP Morgan Chase': 327,
'Bank of America': 302,
'Citigroup': 173,
'Wells Fargo': 273,
'Goldman Sachs': 87,
'Morgan Stanley': 72,
'U.S. Bancorp': 83,
'TD Bank': 108,
'PNC Financial Services': 67,
'Capital One': 47,
'FNB Corporation' : 4,
'First Hawaiian Bank': 3,
'Ally Financial': 12,
'Wachovia': 145,
'Republic Bancorp': .97}

print(banks)
print()



# @TODO: Change the market cap for 'Citigroup'
banks['Citigroup'] = 170
print(f"The marketcap for Citigroup is: {banks['Citigroup']}")
print()
# @TODO: Add a new bank and market cap pair
banks.update({'American Express': 33})
print(banks)
print()
# @TODO: Remove a bank from the dictionary
banks.pop('Wachovia')
print(banks)

# @TODO: Print the modified dictionary
total_mcap = 0
for i in banks:
    total_mcap += banks[i]
print(total_mcap)