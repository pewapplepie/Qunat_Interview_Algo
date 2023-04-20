'''
3. Daily Temperature by Town Bonus Question
Question 3 is a bonus question and will not be scored. The parameters and data set remain the same from Question 2. Please finish Questions 1 and 2 before attempting Question 3.
You are given the daily temperature reading of Ptowns and the daily temperature reading of New York City (NYC) for N days. For the given data, write a function that returns a set of five towns that are jointly as predictive as possible of the daily temperate of NYC. Note that the exact solution to this problem requires an exhaustive search that can be computationally challenging. We expect you to write an approximate solution that is as fast, or maybe faster, than your solution to Question 2.
Function Description
Complete the function main() to read the data from stdin and answer the question. The input data is in CSV format with a header row indicating the town names; use this header rather than making assumptions about column order. Depending on the language you choose we may provide boilerplate code for reading the data - you are welcome to use this if you wish. You are also welcome to import packages (such as sklearn in Python), as long as they are available in the HackerRank environment.
The function main should return a string with the name of the five towns. For example, a valid output is "Town1,Town2,Town3,Town4,Town5". We will use the name of the towns you provide to compute the R2 for each test case.
Constraints
• N >5 and 4 <P <60
▾ Input Format For Custom Testing
The first line contains a comma separated list of strings corresponding to the name of the towns.
Each subsequent line contains comma separated values corresponding to the temperature of each town.
Example:
Town1, Town2, Town3, Town4, Town5, Town6, NYC
34,32,53,5,10,29,40
86,91,24,10,12,50,45
56,78,90,23,23,45,23
23,92,45,44,55,67,34
12,99,23,34,64,56,35
22,102,11,23,45,65,43
'''


def find_five_most_predictive_towns(df):
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # Fit the LassoCV model
    lasso = LassoCV(normalize=True, max_iter=10000, tol=0.001, cv=5)
    lasso.fit(X, y)
    
    # Get the 5 most important features (towns)
    coef_abs = np.abs(lasso.coef_)
    town_indices = np.argpartition(coef_abs, -5)[-5:]
    town_names = df.columns[town_indices]

    return ','.join(town_names)