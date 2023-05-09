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

# extracting minimum and maximum from a column
# Code Source above and also used: 
# https://stackoverflow.com/questions/27405483/how-to-loop-over-grouped-pandas-dataframe

species_groups = df.groupby('Species')

for species, data in species_groups:
    print(f"Minimum and Maximum values for the {species} species:"
          )
    print(f"Sepal Length: min = {data['SepalLength'].min()}, max = {data['SepalLength'].max()}")
    print(f"Sepal Width: min = {data['SepalWidth'].min()}, max = {data['SepalWidth'].max()}")
    print(f"Petal Length: min = {data['PetalLength'].min()}, max = {data['PetalLength'].max()}")
    print(f"Petal Width: min = {data['PetalWidth'].min()}, max = {data['PetalWidth'].max()}")
    print()

# Code Source:
# https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
# Relationship between the sepal length and sepal width
# Code Source:
# https://www.statology.org/matplotlib-legend-position/#:~:text=To%20change%20the%20position%20of%20
# a%20legend%20in%20Matplotlib%2C%20you,legend()%20function.&text=The%20default%20location%20is%20%E
# 2%80%9Cbest,avoids%20covering%20any%20data%20points.
# Placement of legend

sns.scatterplot(x='PetalLength', y='PetalWidth',
                hue='Species', data=df, )
# Placing Legend inside
plt.legend(loc='lower right')

plt.show()

sns.scatterplot(x='SepalLength', y='SepalWidth',
                hue='Species', data=df, )
plt.legend(loc='lower right')
 
plt.show()

# histograms showing lengths and widths for all species
# Code Source: https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
fig, axes = plt.subplots(2, 2, figsize=(10,10))
 
axes[0,0].set_title("Sepal Length")
axes[0,0].hist(df['SepalLength'], bins=7)
 
axes[0,1].set_title("Sepal Width")
axes[0,1].hist(df['SepalWidth'], bins=5)
 
axes[1,0].set_title("Petal Length")
axes[1,0].hist(df['PetalLength'], bins=6)
 
axes[1,1].set_title("Petal Width")
axes[1,1].hist(df['PetalWidth'], bins=6)

# Save the histogram
# Code Source: https://www.tutorialspoint.com/how-to-save-a-histogram-plot-in-python#
plt.savefig('histogram1.png') 
plt.show()

# Code Source: https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
# Histogram showing sepal length
plt.figure(figsize = (10, 7))
x = df["SepalLength"]
  
plt.hist(x, bins = 20, color = "green")
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_cm")
plt.ylabel("Count")

# Code Source: https://stackoverflow.com/questions/72457668/how-do-i-save-multiple-
# histograms-to-different-separate-files
# Save the histogram
plt.savefig('histogram2.png') 

# Histogram showing sepal width
plt.figure(figsize = (10, 7))
x = df.SepalWidth
  
plt.hist(x, bins = 20, color = "green")
plt.title("Sepal Width in cm")
plt.xlabel("Sepal_Width_cm")
plt.ylabel("Count")

# Save the histogram
plt.savefig('histogram3.png') 

# Histogram showing petal length
plt.figure(figsize = (10, 7))
x = df.PetalLength
  
plt.hist(x, bins = 20, color = "red")
plt.title("Petal Length in cm")
plt.xlabel("Petal_Length_cm")
plt.ylabel("Count")

# Save the histogram
plt.savefig('histogram4.png') 

# Histogram showing petal width
plt.figure(figsize = (10, 7))
x = df.PetalWidth
  
plt.hist(x, bins = 20, color = "red")
plt.title("Petal Width in cm")
plt.xlabel("Petal_Width_cm")
plt.ylabel("Count")

# Save the histogram
plt.savefig('histogram5.png') 

plt.show()

# Code Source: https://www.askpython.com/python/examples/display-images-using-python
# Adding image of iris'
from matplotlib import image as mpimg
 
plt.title("Iris Image")
plt.xlabel("X pixel scaling")
plt.ylabel("Y pixels scaling")
 
image = mpimg.imread("irisx3.png")
plt.imshow(image)
plt.show()

# Code Source: https://www.tutorialspoint.com/How-to-write-multiple-lines-in-text-file-using-Python
# Creating and writing to a file called project.txt
with open("project.txt", "a") as f:
   lines = ["The well-known Fischers Iris data set can display to anyone new to learning code"
    "(such as myself),\n that you can take basically any clean data set and compare every and each variable."
    "You can create histograms and plots to make the data easier to view and compare.\n You can"
    "add images to your code and README files to make it look nicer. You can compare only certain"
    "parts of the data if you so wish.\n This piece of basic code that I have written (and copied"
    "from certain referenced sources) conveys to me that python code can be used for so many purposes."
    "\n I work in the tech field currently, but do not have any ICT degree and am completing this"
    "course so I can expand my knowledge.\n I beleive that by the time I have finished this course"
    "with ATU Galway, I will be able to implement many different programs which will make my tasks"
    "in work,\n (many of which are manual) much smoother and will introduce much less room for human error."
    "\n\n Using the Iris data set as a base, it has shown me that I can take even the most basic of data,"
    "and\n create many different outputs and ways of reading it. I have completed a lot of research on Google"
    "whilst figuring out how to do certain aspects of this project\n and I have found so many useful"
    "websites and platforms that can be used to improve my knowledge even after this course is finished.\n\n"
    "In summary, I have not researched anyone else's analysis of this data set as I did not want to"
    "cloud my own opinion of this data\n when seeing and working with it for the first time. "
    "The code which is present in my project works very well with the iris data set\n and although"
    "basic, the code can be adjusted for more complicated data sets. The outputs could be worked on so"
    "\n that I can produce a histogram/plot/median sum etc. output for each and every variable in the data."
    "I could introduce more complex code which compares\n many different types of variables and output"
    "them in many different formats.\n\n In conclusion, the iris data set has opened my eyes to the"
    "endless possibilities that python coding is capable of and I am excited to leanr more and\n"
    "watch as technology evolves in the future."
   ]
   f.writelines(lines)
# This line closes the "project.txt" file
   f.close()
