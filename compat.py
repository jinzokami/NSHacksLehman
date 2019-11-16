import os
import math
import pandas as pd
import numpy as np

university_data = pd.read_csv("university_data.csv")
occupation_data = pd.read_csv("occupation_data.csv")

print(university_data.head())
print(occupation_data.head())