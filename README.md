# Overview

I am using this free data set found on Kaggle: https://www.kaggle.com/niharika41298/nutrition-details-for-most-common-foods/code. This data includes some nutirional fact 
about common foods found in the standard American Diet.

The purpose for writing this software is to prove my ability to develop software and build an analisys on said data when provided by a thrid party. In paricular, I wanted
to analyze some of the foods we eat on a daily basis and see if we can't make some better choices with our diet.

[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results

Question 1: which foods should I be eating if I want to increase my protein intake and decrease my fat intake?

The dataset was quite large, so I broke it up by category and enabled a user of the program to run the program form the command line, type in the category tey would like to view
and then return results based upon that category. One interesting thing to note is that sea food contained one of the highest Protein to Fat
ratios among all other categories, whereas meat, poultry typically contained more fat. Compare the two tables below:

[](https://github.com/josh-wassum/pandas_project/blob/master/assets/Fat_Protein_Chart.png)

[](assets/MeatPoultryTable.png)

Question 2: what is the fat to protein ratio of these protein rich foods?

The next task was accomplished by using stacked bar charts. I divided the macro nutrients by gram and then stacked them in a bar chart to see what percentage of each gram was occupied by which macro nutrient. The only way to visualize each category is to run the application by view below the seafood chart and the meat, poultry chart.

[](assets/Fat_Protein_Chart.png)

[](assets/meatpoultryChart.png)

Question 3: what is the mean for each Macro by Gram?

The answer to this question is much easier to grasp than the last. The order of macros per gram is Carbs, then Fat, then Protein. From this we can gather that on average there is more fat in the common foods we eat than protein, so we need to make an effort to eat a high protein, low fat diet.

# Development Environment

The software was developed using VS Code as my development environment

I used Python as the base language.
Pandas was used to process the data.
Numpy was used to help format the data.
matplotlib was used to visualize the data using charts.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Geeks For Geeks](https://www.geeksforgeeks.org/)
* [Stack Overflow](https://stackoverflow.com/)
* [matplotlib](https://matplotlib.org/)
* [tutorialspoint](https://www.tutorialspoint.com/)

# Future Work

* Ability to select the which Macros you would like to compare.
* Ability to export charts created directly to a PowerPoint file.
* Create averages for the entire dataset of each Macro.
