# -*- coding: utf-8 -*-
"""descriptive.ipynb
# Descriptive statistics
## Library imports
"""

import pandas as pd
from scipy import stats  # A great statistical module from the scipy library

"""## Data import
### Connecting to Google Drive and importing the data
"""

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/sbm-resident-programming-2024/main/Code/Wk1/Data/data.csv')  # Import the csv file

df  # Display the dataframe to the screen

"""### Examining the dataframe object
We investigate the data by looking at the number of subjects (rows) and the number of statistical variable (columns).
"""

df.shape  # Using the .shape property (attribute)

"""We see 200 participants in our study, with data collected for 13 variables.
Let's have a look at all the statistical variables.
"""

df.columns  # Name of each column

"""The data represent a small study on cholesterol values before and after taking either a placebo or an active drug.
Finally, we can view the data types of each variable (column).
"""

df.dtypes  # Pandas data type of each column

"""## Counting
### Frequencies
Counting how many times a sample space element of a categorical variable occurs is a good start.  In our dataframe object, we have a *Group* variable.  Let's first see what the sample space of this variable is.  The `unique` method will return an array of the unqiue elements it finds in a specified column.
"""

df.Group.unique()  # The .unique() method returns the sample space elements of a column (pandas series object)

"""As mentioned, patients received either a placebo (*Control* group) or an active drug (*Active* group).  These two terms are the sample space elemnts of the nominal categorical variable *Group*.
We can now count how many times each of these elements appear in the *Group* column, using the `.value_counts()` method.  This gives us the **frequency** of each value.
"""

df.Group.value_counts()  # Counting the number of times the unique values appear

"""We see that there are 100 participants in each group.  We can express the counts as a fraction, called a **relative frequency**.  Thsi is done by setting the `normalize=` argumen to `True`."""

df.Group.value_counts(normalize=True)  # Expressing the relative frequency

"""As expected, we see each element taking up a half of the total number of participants.  We can multiply this by 100 to get a percentage."""

df.Group.value_counts(normalize=True) * 100  # Expressing the relative frequency as a percentage

"""#### Exercise

The *Smoke* column indicates wheter particpants never smoked (*0*), are smokers (*1*), or have smoked before (*2*).  Calculate the frequency with which each element appears.

#### Solution
"""

df.Smoke.value_counts()
df.Smoke.value_counts(ascending=True, normalize=True) * 100

"""### Grouped frequencies

We can calculate *combined frequencies*.  As an example, consider the number of participants in each group of the study that chose each of the five possible values in the survey question.

We can do this with the pandas `crosstab()` function.
"""

pd.crosstab(df.Survey, df.Group)  # Row and column variable

"""## Measures of central tendency (point estimates)
**Measures of central tendency** or **Point estimates** are single values that are representative of a list of continuous numerical values.  There are a few that we will discuss here.
### Mean (average)
The **mean** or the **average** is more properly known as the **arithmetic mean**.  It is simply the sum of all the continuous numerical variables divided by the number of values.
Let's start learning about the information in our data by asking some questions.
- What is the mean age of all the patients?
A pandas series object has many useful methods that are geared towards summary statistics.  The `.mean()` method calculates the mean.
"""

# Using the .mean() method
df.Age.mean()

"""- What is the mean heart rate of all the patients?"""

# Using alternative column (variable) reference
df['HR'].mean()

"""- What is the mean age of the patients who smoke (indicated as *1* in the *Smoke* column)?

We looked at conditional in the previous notebook, where we selected only certain rows in a pandas series.
"""

# Using a conditional on the Smoke column
df[df.Smoke == 1]['Age'].mean()

"""- What is the mean age of the patients who do not smoke (indicated as *0* in the *Smoke* column)?"""

# Using a conditional on the Smoke column
df[df.Smoke == 0]['Age'].mean()

"""We have learned something usefull with this summary statistic.  The patients who smoke are quite a bit older than those who do not.  Is this a significant difference?  What test can we use to discover this?  What about the third group, the ex-smokers?  All will be revealed.
- What are the mean ages of the patients who smoke compared to those who do not smoke?
We can save a lot of time and typing by calculating the age means for all the smoker groups.
The `.groupby()` method can create groups from the unique elements in a column and then call a method on another column.
"""

# Use the .groupy() method
df.groupby('Smoke')['Age'].mean()

"""By the way, the `.mean()` method has some useful arguments.  We can use `skipna=True` to skip over any missing values (this is the default behaviour of this method).  We can also use `numeric_only=True` if there are data values that were not captured as numbers.
### Geometric mean
The **geometric mean** multiplies all the continous numerical variables and take the *n*-th root of that product, where *n* is the number of values.  At the beginning of this notebook we imported the stats module from the scipy library.  It contains many functions that we will use in the statistical analysis of our data.  The `gmean()` function calculates the geometric mean.  It can take a pandas series as argument.
"""

stats.gmean(df.Age)

"""### Median
The mean makes an assumption of the data values and that is that they should be normally distriuted.  We will learn much more about distributions in the next notebook.  For now, we can view the normal distribution as the familiar bell-shaped curve.
Not all data value for a continuous numerical value follow a nice bell-shaped curve.  We can have quite different *shapes* (distributions) or many outliers (values that are way-off from all the others).  In this case, the mean is not a good representative summary of all the data values.  Here, we rather use the median.
The **median** puts all the values in a sorted order.  If there are an odd number of values, then the median is the middle value.  If there are an even number of values, then the mean of the middle two values as taken.
- What is the median heart rate of patients older than $50$?
"""

# Using the .median() function
df[df.Age > 50]['HR'].median()

"""#### Exercise
Calculate the median age of the participants who smoke (*1*) and have a heart rate of more than 70.
"""

df.columns

"""#### Solution"""

df.loc[(df.Smoke == 1) & (df.HR > 70), 'Age'].median()

"""### Mode
The last measure of central tendency that we will take a look at is the mode.  The **mode** is used for categorical of discrete data types.  It simply return the value(s) that occurs most commonly.  If a single sample space element occurs most commonly, that will be the single mode.  Somethimes more than one sample space element shares the spoils.  This variable is then bimodal.  As you might imagine, there are terms such as tri-modal and multi-modal.
- What is the mode of the smoking variable?
We use the `.value_counts()` method do calculate the frequency.  The `ascending=` argument is set to `False` by default and the `sort=` is set to `True`, such that we get the mode at the top.
"""

df.Smoke.value_counts()

"""## Measures of dispersion (spread)
**Measure of dispersion** give us an indication of how spread out our data is.
### Standard deviation and variance
The **standard deviation** can be understood as the average difference between each continuous numerical data value and the mean of that variable.  Difference infers subtraction.  As some values will be larger than the mean and some smaller, subtraction from the mean will lead to positive numbers and negative numbers. In fact, from the way we calculate the mean, if we sum up all these differences (so as to calculate a mean difference), we will get 0.  To mitigate this, we sqaure all of the differences.  Squaring (multiplying by itself) returns positive values.  Now we can sum all these values and divide by the number of values.  This gives us the **variance**.
Variances are very useful in statistics.  We need to express the spread in the same units as our variable for it to make sense as a summary statistics.  The *age* variable had a unit of years.  What then, is a $\text{years}^2$.  Instead, we take the square root of the variance to get the standard deviation, now expressed in the same units as the variable and a true measure of the average difference between all the values and the mean.
The `.std()` method returns the standard deviation of a series object and the `.var()` method returns the variance.
- What is the standard deviation of the age of patients who smoke vs those who do not smoke?
"""

# Group by the Smoke column
df.groupby('Smoke')['Age'].std()

"""- What is the variance of the age of patients who smoke vs those who do not smoke?"""

df.groupby('Smoke')['Age'].var()

"""### Range
The **range** is the difference between the minimum and the maximum value of a continuous numerical variable.  The `min()` and the `max()` methods for series objects give these values.  Let's see then how old our youngest and oldest participants are.
- What is the minimum age of all the participants?
"""

# Using the .min() functuion
df.Age.min()

"""- What is the maximum age of all the participants?"""

# Using the .max() function
df.Age.max()

"""- What is the range in the age of all the participants?
We simply subtract the minimum value from the maximum value.
"""

# Difference between maximum and minimum ages
df.Age.max() - df.Age.min()

"""### Quantiles
Just as we divided our continuous numerical variables up into two halves for the mean, so we can divide them up into quarters.  In fact, we can divide it up at any percentage level from 0% to 100% (fraction of 0.0 to 1.0).  Here 0% would be the minimum value and 100% would be the maximum value.  Dividing the values up into these bins give us **quantiles**.
We can divide the values up into four bins with three values. These values are the **quartiles**.
The lowest of these three values (the **first quartile**), divide the data into two parts, with a quarter being lower than that value and three-quarters being higher.  The second divide the data values equally (the median or **second quartile**).  The third is a value that has three-quarters of the values less than and a quarter more than it (the **third quartile**).
- What are the quartile values for the age of all the patients?
The `.quantile()` method allows us to choose, as a fraction, any of these cut-off values.  For the quartiles, we create a list `[0.25, 0.5, 0.75]`.
"""

# Specifying the quartiles as fractions
df.Age.quantile([0.25, 0.5, 0.75])

"""- What is the $95$<sup>th</sup> percentile values in age of the patients who smoke vs those that do not?"""

df.groupby('Smoke')['Age'].quantile(0.95)

"""The **interquartile range** is the difference between the third and the first quartile.
- What is the interquartile range of the age of all the patients?
"""

df.Age.quantile(0.75) - df.Age.quantile(0.25)

"""## Conclusion
We now know a lot more about our data.  Be encouraged to learn even more by asking some question about this mock study and see if you can calculate the required value.
"""

