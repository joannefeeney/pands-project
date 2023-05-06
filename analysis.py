# analysis.py
# Author: Joanne Feeney
# This program outputs a summary of each variable to a single text file
# Saves a histogram of each variable to png files, and  
# Outputs a scatter plot of each pair of variables 
# Performs any other analysis you think is appropriate  

# Opening and reading the dataset
# https://www.w3schools.com/python/python_file_open.asp
f = open("iris.data", "r")
# print(f.read())

# Code source: Pedregosa et al.
import matplotlib.pyplot as plt
import numpy as np

# import the data set
iris = f
X = iris.data[:, :2]  # we only take the first two features
y = iris.target

x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor="k")
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

plt.show()