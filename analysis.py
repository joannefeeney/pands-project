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
# print the first 10 columns of the specific_data dataframe e.g.
# print(specific_data.head(10))

# Code Source: https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
# calculating sum, mean and mode of a particular column
'''
sum_data1 = df["SepalLength"].sum()
mean_data1 = df["SepalLength"].mean()
median_data1 = df["SepalLength"].median()

print(f"Data for the sepal length of all iris species: \n""Sum:",sum_data1, "\nMean:", mean_data1, "\nMedian:",median_data1, "\n")

sum_data2 = df["SepalWidth"].sum()
mean_data2 = df["SepalWidth"].mean()
median_data2 = df["SepalWidth"].median()

print(f"Data for the sepal width of all iris species: \n""Sum:",sum_data2, "\nMean:", mean_data2, "\nMedian:",median_data2, "\n")

sum_data3 = df["PetalLength"].sum()
mean_data3 = df["PetalLength"].mean()
median_data3 = df["PetalLength"].median()

print(f"Data for the petal length of all iris species: \n""Sum:",sum_data3, "\nMean:", mean_data3, "\nMedian:",median_data3, "\n")

sum_data4 = df["PetalWidth"].sum()
mean_data4 = df["PetalWidth"].mean()
median_data4 = df["PetalWidth"].median()

print(f"Data for the petal width of all iris species: \n""Sum:",sum_data4, "\nMean:", mean_data4, "\nMedian:",median_data4, "\n")
GOOD
'''
'''
# extracting minimum and maximum from a column
# Code Source above and also used: 
# https://stackoverflow.com/questions/27405483/how-to-loop-over-grouped-pandas-dataframe

species_groups = df.groupby('Species')

for species, data in species_groups:
    print(f"Minimum and Maximum values for the {species} species:", "\n")
    print(f"Sepal Length: min = {data['SepalLength'].min()}, max = {data['SepalLength'].max()}")
    print(f"Sepal Width: min = {data['SepalWidth'].min()}, max = {data['SepalWidth'].max()}")
    print(f"Petal Length: min = {data['PetalLength'].min()}, max = {data['PetalLength'].max()}")
    print(f"Petal Width: min = {data['PetalWidth'].min()}, max = {data['PetalWidth'].max()}")
    print()
GOOD
'''
'''
# Code Source:
# https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
# Relationship between the sepal length and sepal width
sns.scatterplot(x='SepalLength', y='SepalWidth',
                hue='Species', data=df, )


# Source Code:
# https://www.statology.org/matplotlib-legend-position/#:~:text=To%20change%20the%20position%20of%20
# a%20legend%20in%20Matplotlib%2C%20you,legend()%20function.&text=The%20default%20location%20is%20%E
# 2%80%9Cbest,avoids%20covering%20any%20data%20points.
# Placement of legend
plt.legend(bbox_to_anchor=(1, 1), loc=1)
 
plt.show()
GOOD
'''
# Relationship between  length and width via scatter plot
sns.scatterplot(x='PetalLength', y='PetalWidth',
                hue='Species', data=df, )
# Placing Legend inside
plt.legend(loc='lower right')

plt.show()

sns.scatterplot(x='SepalLength', y='SepalWidth',
                hue='Species', data=df, )
plt.legend(loc='lower right')
 
plt.show()
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
# Save the histogram e.g.
# plt.savefig('hist.png') 
# Code Source: https://www.tutorialspoint.com/how-to-save-a-histogram-plot-in-python#

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

