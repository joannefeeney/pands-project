# analysis.py
# Author: Joanne Feeney
# This program outputs a summary of each variable to a single text file
# Saves a histogram of each variable to png files, and  
# Outputs a scatter plot of each pair of variables 

# Code source: https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
# Code source: https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/
# Adding required libraries
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

# Source Code:
# https://www.statology.org/matplotlib-legend-position/#:~:text=To%20change%20the%20position%20of%20
# a%20legend%20in%20Matplotlib%2C%20you,legend()%20function.&text=The%20default%20location%20is%20%E
# 2%80%9Cbest,avoids%20covering%20any%20data%20points.
# Placement of legend
plt.legend(bbox_to_anchor=(1, 1), loc=1)
 
plt.show()
'''
'''
# Relationship between petal length and petal width
sns.scatterplot(x='PetalLength', y='PetalWidth',
                hue='Species', data=df, )
 
# Placing Legend inside
plt.legend(loc='lower right')
 
plt.show()
'''
# Four histograms allow seeing the distribution of data for various columns
'''
fig, axes = plt.subplots(2, 2, figsize=(10,10))
 
axes[0,0].set_title("Sepal Length")
axes[0,0].hist(df['SepalLength'], bins=7)
 
axes[0,1].set_title("Sepal Width")
axes[0,1].hist(df['SepalWidth'], bins=5)
 
axes[1,0].set_title("Petal Length")
axes[1,0].hist(df['PetalLength'], bins=6)
 
axes[1,1].set_title("Petal Width")
axes[1,1].hist(df['PetalWidth'], bins=6)

plt.show()
'''

# Code Source: https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
# Histogram showing sepal length

'''
plt.figure(figsize = (10, 7))
x = df["SepalLength"]
  
plt.hist(x, bins = 20, color = "green")
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_cm")
plt.ylabel("Count")

# Histogram showing sepal width

plt.figure(figsize = (10, 7))
x = df.SepalWidth
  
plt.hist(x, bins = 20, color = "green")
plt.title("Sepal Width in cm")
plt.xlabel("Sepal_Width_cm")
plt.ylabel("Count")

plt.show()
'''

# Code Source: https://pythonguides.com/python-write-variable-to-file/
# Creating and writing to a file called project.txt
# This code creates a set variable named "datasetname" with the value "Iris Dataset"
'''
datasetname = {"Iris Dataset"}
# This line opens a file named "project.txt" in write mode (w)
file = open("project.txt", "w")
# This line uses string formatting to write the "datasetname" variable and its value to the file
file.write("%s = %s\n" %("datasetname",datasetname))
# This line closes the "project.txt" file
file.close()
'''
# Code Source: https://www.askpython.com/python/examples/display-images-using-python
# Adding image of iris'
'''
from matplotlib import image as mpimg
 
plt.title("Iris Image")
plt.xlabel("X pixel scaling")
plt.ylabel("Y pixels scaling")
 
image = mpimg.imread("irisx3.png")
plt.imshow(image)
plt.show()
'''

