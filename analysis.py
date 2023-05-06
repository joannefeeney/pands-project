# analysis.py
# Author: Joanne Feeney
# This program outputs a summary of each variable to a single text file
# Saves a histogram of each variable to png files, and  
# Outputs a scatter plot of each pair of variables 
# Performs any other analysis you think is appropriate  

# Code source: https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
import pandas as pd

data = pd.read_csv("irisdata.csv")

# setosa data 
# print(data[0:49])

# versicolor data 
# print(data[50:99])

# verginica data 
# print(data[100:151])

# you can also save it in a variable for further use in analysis
# sliced_data=data[50:99]
# print(sliced_data)

# adding column name to the respective columns
# Code source:
# https://www.geeksforgeeks.org/add-column-names-to-dataframe-in-pandas/
data.columns =['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidthth', 'Species']


# displaying only certain columns
# save it in a another variable named "specific_data" e.g.
# specific_data=data[["SepalLength","Species"]]
# data[["column_name1","column_name2","column_name3"]]
# now we will print the first 10 columns of the specific_data dataframe e.g.
# print(specific_data.head(10))

# calculating sum, mean and mode of a particular column
# data["column_name"].sum()
''' 
sum_data = data["SepalLength"].sum()
mean_data = data["SepalLength"].mean()
median_data = data["SepalLength"].median()

print(f"Data for the length of all iris species: \n""Sum:",sum_data, "\nMean:", mean_data, "\nMedian:",median_data)
'''

