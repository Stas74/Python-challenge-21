# Group By in Pandas

# Tutorial

# Within Pandas, one of the most essential and useful functions for data analysis is the group by function.

# Group by does one thing: it groups the dataset according to a categorical column or columns. 
# However, the grouping function can't stand on its own. 
# The user needs to apply a specific aggregate function to the dataset after using group by. 
# Check the example below.

# import pandas as pd

# df = pd.read_csv('dubai_properties_data.csv', index_col = 0)

# df.groupby(['quality']).mean()

# In the above code, we grouped the dataset by the quality column, 
# then used the mean() aggregate function to see the average of ALL numerical columns for each year. 
# However, we don’t have to use the sum() function with group by. 
# We can easily use other aggregate functions, such as sum(), min(), max()....

# Below is a list of aggregate functions we can use on our group by`s.

# count() – Number of non-null observations
# sum() – Sum of values
# mean() – Mean of values
# median() – Arithmetic median of values
# min() – Minimum
# max() – Maximum
# mode() – Mode
# std() – Standard deviation
# var() – Variance
# size() - Number of rows

# We can specify the columns we want to group by:

# df.groupby(['quality'])[['price','size_in_sqft','no_of_bedrooms']].mean()

# Try this line of code below and see what it does:

# df.groupby(['view_of_landmark','view_of_water'])[['price','no_of_bedrooms']].mean()

Before you continue to the challenge, play around with the group by function a bit. You can read more on the function in this article.
https://realpython.com/pandas-groupby/

To learn more about the various pandas functions, check out the user guide in the pandas documentation.
https://pandas.pydata.org/docs/user_guide/index.html#user-guide

  
# Challenge

# Which neighborhood has the highest average property price and the highest size_in_sqft?

import pandas as pd
df = pd.read_csv('dubai_properties_data.csv')
# df.groupby(['quality'])[['price','size_in_sqft','no_of_bedrooms']].mean()
# df.groupby(['view_of_landmark','view_of_water'])[['price','no_of_bedrooms']].mean()

df.head()
# price
# size_in_sqft

fin = df.groupby(['neighborhood'])[['price']].mean()
print((fin.sort_values(by='price', ascending=False)).head(1))

#                       price
# neighborhood               
# Palm Jumeirah  4.379435e+06

size = df.groupby(['neighborhood'])[['size_in_sqft']].mean()
print((size.sort_values(by='size_in_sqft', ascending=False)).head(1))

#                      size_in_sqft
# neighborhood                     
# Dubai Festival City        2778.4
