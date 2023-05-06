# analysis.py
# Author: Joanne Feeney
# This program outputs a summary of each variable to a single text file
# Saves a histogram of each variable to png files, and  
# Outputs a scatter plot of each pair of variables 
# Performs any other analysis you think is appropriate  

# Code source: https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
# Code source: https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 

df = pd.read_csv("irisdata.csv")

# adding column name to the respective columns
# Code source:
# https://www.geeksforgeeks.org/add-column-names-to-dataframe-in-pandas/
df.columns =['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']

# setosa data 
# print(data[0:49])

# versicolor data 
# print(data[50:99])

# verginica data 
# print(data[100:151])

# you can also save it in a variable for further use in analysis
# sliced_data=data[50:99]
# print(sliced_data)

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
# extracting minimum and maximum from a column e.g.
# min_data=data["SepalLength"].min()
# max_data=data["SepalLength"].max()
# print("Minimum:",min_data, "\nMaximum:", max_data)

# Code Source:
# https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
# Relationship between the sepal length and sepal width
'''
sns.scatterplot(x='SepalLength', y='SepalWidth',
                hue='Species', data=df, )
# Placement of legend
# Source Code:
# https://www.statology.org/matplotlib-legend-position/#:~:text=To%20change%20the%20position%20of%20
# a%20legend%20in%20Matplotlib%2C%20you,legend()%20function.&text=The%20default%20location%20is%20%E
# 2%80%9Cbest,avoids%20covering%20any%20data%20points.
plt.legend(bbox_to_anchor=(1, 1), loc=1)
 
plt.show()
'''
# Relationship between petal length and petal width
sns.scatterplot(x='PetalLength', y='PetalWidth',
                hue='Species', data=df, )
 
# Placing Legend inside
plt.legend(loc='lower right')
 
plt.show()