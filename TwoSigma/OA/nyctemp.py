'''

2. Daily Temperature By Town
You are given the daily temperature reading of Ptowns and the daily temperature reading of New York City (NYC) for N days. Write a function that returns the answer to the following five questions:
• Q1: The name of the place (either a town or NYC) with the largest variation in the daily temperature. Use the standard deviation to measure the variation.
• Q2: The median daily temperature of NYC when the daily temperature of Town2 is between 90 and 100 degrees (inclusive of 90 and 100). Round your answer to the nearest integer.
• Q3: Fit P simple linear models with intercept using least squares to predict the daily temperature of NYC given each individual town. Find the sum of the absolute values of the regression coefficients (i.e., the slopes or betas), rounded to the nearest integer.
• Q4: For the given data, find the town that is most predictive of the daily temperature of NYC. By most predictive, we mean the town that leads to the lowest mean squared error (MSE) on the given data when fit using a linear model with intercept. 
• Q5: For the given data, find the two towns that are jointly most predictive of the daily temperature of NYC. As before, we mean the two towns that lead to the lowest MSE when fit using a linear model with intercept.
Function Description
Complete the function main() to read the data from stdin and answer the six questions. The input data is in CSV format with a header row indicating the town names; use this header rather than making assumptions about column order. Depending on the language you choose we may provide boilerplate code for reading the data - you are welcome to use this if you wish. You are also welcome to import packages (such as sklearn in Python), as long as they are available in the HackerRank environment.
The function main should return a string with the answer to the six questions below, delimited by a comma. For example, suppose your answers to the five questions are as follows:
• Q1: Town1
• Q2: 95
• Q3: 3
• Q4: Town2
• Q5: Town1 and Town2
You should return "Town 1,95,3,Town2,Town1,Town2".
Constraints
• N> 2 and 4 <P < 60
• There exists at least one data point for Town2 where the highest temperature is between 90 and 100 degrees.
▾ Input Format For Custom Testing
The first line contains a comma separated list of strings corresponding to the name of the towns.
Each subsequent line contains comma separated values corresponding to the temperature of each town.
Example:
Town1, Town2, Town3, Town4, Town5, NYC
70,95,34,46,10,50
65,88,45,24,32,51
87,91,23,35,10,78
67,101,34,55,15,88
'''

import sklearn
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv('test1.csv')
data

def q1(data):
    maxvarplace= data.std().idxmax().strip(' ')
    print("Q1: ", maxvarplace)

def q2(data):
    nyc_temp = data[(data[:, 1] >= 90) & (data[:, 1] <= 100), -1]
    median_temp = np.median(nyc_temp)
    print("Q2:", round(median_temp))
def q3(data):
    regression_coefficients = []

    for i in range(5):
        X = data[:, i].reshape(-1, 1)
        y = data[:, -1]
        model = LinearRegression().fit(X, y)
        regression_coefficients.append(model.coef_[0])

    sum_abs_coefficients = np.sum(np.abs(regression_coefficients))
    print("Q3:", round(sum_abs_coefficients))
