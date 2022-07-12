import numpy

import numpy_financial as npf

interest_rate = .1
cash_flows = [-1000, 400, 400, 400, 400]

net_present_value = npf.npv(interest_rate, cash_flows)
print(f'NPV = {net_present_value}')