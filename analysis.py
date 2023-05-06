# analysis.py
# Author: Joanne Feeney
# This program outputs a summary of each variable to a single text file
# Saves a histogram of each variable to png files, and  
# Outputs a scatter plot of each pair of variables 
# Performs any other analysis you think is appropriate  

# Code source: https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
import pandas as pd

data = pd.read_csv("irisdata.csv")

#setosa data 
# print(data[0:49])

#versicolor data 
# print(data[50:99])

#verginica data 
# print(data[100:151])

# you can also save it in a variable for further use in analysis
sliced_data=data[50:99]
print(sliced_data)