import pandas as pd
import numpy as np
import math
import os
import sys

desired_occupation = sys.argv[1]
state_of_residence = sys.argv[2]

occupation_data = pd.read_csv("occupation_data.csv")
university_data = pd.read_csv("university_data.csv")

idx = (occupation_data["MedianWeeklySalary"] == "-")
occupation_data.loc[idx, "MedianWeeklySalary"] = np.nan
occupation_data["MedianWeeklySalary"] = occupation_data["MedianWeeklySalary"].astype(float)

university_data["OutCost"] = university_data["OutCost"].astype(float)
university_data["InCost"] = university_data["InCost"].astype(float)

idx = occupation_data["OccupationTitle"] == desired_occupation
weekly = occupation_data[idx]

yearly = weekly["MedianWeeklySalary"].astype(int)*52
monthly_contribution = (yearly.array[0]/12)*.1

#brute force! sim the months till balance is 0
#I have no idea how finances work
def sim_payoff(tuit, mon_con):
    total_tuit = tuit*4
    total_months = 0
    while True:
        interest = total_tuit * (.0481/12)
        for i in range(12):
            total_tuit += interest
            total_tuit -= max(mon_con, interest+20)
            total_months += 1
            if total_tuit < 0:
                return total_months/12

university_data["TimeToPayOff"] = university_data["OutCost"].apply(sim_payoff, args=[monthly_contribution])

university_data = university_data.sort_values(by="TimeToPayOff")
res = university_data.head(20)

res.to_json("result.json")