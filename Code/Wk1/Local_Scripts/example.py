import pandas as pd 

df = pd.read_csv('Code/Wk1/Data/cms_hospital_provider_costs/CostReport_2021_Final.csv')

## Print the first 5 rows of the dataframe
print(df.head())

## Create descriptive stats on all numerical values
print(df.describe())

## Create pivot table on the 'Provider Name' and 'Provider City' columns
print(pd.pivot_table(df, index=['Provider Name', 'Provider City']))