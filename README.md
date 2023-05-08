# pands-project

This project concerns the Fisher’s Iris data set. I have researched the data set
and written documentation and code to investigate it. 


The data set contains 3 species of iris:
* setosa
* versicolor
* virginica

![irisx3](https://user-images.githubusercontent.com/123767624/236692889-280b9db3-e557-4c14-bd65-8fb64eb8f002.png)


It contains data for 50 examples of each species including:
* sepal length in cm
* sepal width in cm
* petal length in cm
* petal width in cm




### The dataset is available here:

UC Irvine Machine Learning Repository. Iris data set.
http://archive.ics.uci.edu/ml/datasets/Iris

### Results:

* First my python code outputs the details of the sum, mean and median of the iris data (all 3 species).
  From the information that the program has calculated for us, we can see that there is a quite a difference in size (both length and width) 
  between the petals and the sepals.
* Next the code outputs the minium and maximum value for each species of iris.
  From this information, we can see that in general, the iris virginica species appears to be the largest and 
  the iris setosa and versicolor are closer in size.
* The program then runs two scatter plots which display the petal length/width and also the sepal length/width for each species.
  These scatter plots appear in two separate figures, one is generated first and then the second is generated when the first is closed.
  They provide a good visual of the differences in length/width of these species, with the species diapayed as different coloured dots.
* The next section of code outputs four different histograms which display the different sizes in sepal length, sepal width,
  petal length and petal width, while also displaying the frequency of such on the y axis. This is save to the repository after running as 
  histogram1.png. From this output, we can see for example that the sepal length of all species has the highest frequency at approximately 5.5cm in length.
* Then the code outputs a histogram for each each of the variables of width/lenth for both the sepals and petals of all combined species.
  The two histograms which display sepal data are in green and the two which dispolay petal data are in red. Again these are outpuptting individually and are
  saved as separate .png files once run and each is closed.
  From this data we can see for example in histogram5.png that a petal width of approximatley 0.2cm has the highest frequency with approximatley 33 petals
  displaying this width.
* My code then genrates an image of the 3 species of iris, which also appears at the top of this README file.


### References:

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science., Last accessed 06/05/2023

Santos, Rafael (2019) [http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html], Last accessed 06/05/2023

Data Camp Tutorial [https://www.datacamp.com/tutorial/machine-learning-in-r], Last accessed 06/05/2023

Pedregosa et al.,Scikit-learn: Machine Learning in Python,  JMLR 12, pp. 2825-2830, (2011) [https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html], Last accessed 06/05/2023

Geeksforgeeks [https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/], [https://www.geeksforgeeks.org/add-column-names-to-dataframe-in-pandas/], [https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/], [https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/], [https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/], Last accessed 06/05/2023

Statology [https://www.statology.org/matplotlib-legend-position/#:~:text=To%20change%20the%20position%20of%20a%20legend%20in%20Matplotlib%2C%20you,legend()%20function.&text=The%20default%20location%20is%20%E2%80%9Cbest,avoids%20covering%20any%20data%20points.], Last accessed 06/05/2023

Kumar, Bijay, Python guides [https://pythonguides.com/python-write-variable-to-file/], Last accessed 07/05/2023

Dhanalakshmi Srivani, Karpuram [https://www.analyticsvidhya.com/blog/2022/06/iris-flowers-classification-using-machine-learning/] (used for image of iris'), Last accessed 07/05/2023

Rishi, Rishikesh Kumar, Tutorialspoint [https://www.tutorialspoint.com/how-to-save-a-histogram-plot-in-python#], Last accessed 07/05/2023

Stack overflow [https://stackoverflow.com/questions/50088007/print-specific-rows-and-columns-in-pandas], [https://stackoverflow.com/questions/27405483/how-to-loop-over-grouped-pandas-dataframe], [https://stackoverflow.com/questions/72457668/how-do-i-save-multiple-histograms-to-different-separate-files], Last accessed 08/05/2023
