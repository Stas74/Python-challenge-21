# Advanced Group By Uses in Pandas

# Tutorial
# Within pandas, one of the most essential and useful functions for data analysis is the group by function. 
# During this challenge, we are going to take a look at more complex group by uses.

# You might have noticed that the aggregate functions we used with group by yesterday were always applied to all columns. 
# But what if we wanted to apply different functions to different columns? 
# Do we need to do each column individually? 
# If you think there’s a more efficient way, you’re correct. Pandas has a better way.

# import pandas as pd
# df = pd.read_csv('dubai_properties_data.csv')

# # old way - averages of both columns were computed for each neighborhood
# df.groupby(['neighborhood'])[["price","price_per_sqft"]].mean()

# # new way - using the aggregate function .agg()
# df.groupby(['neighborhood']).agg({'price' : 'mean', 'price_per_sqft' : 'max'})

# We can use the aggregate function .agg() to select the aggregation we want to do for each column. 
# We are using a Python dictionary as a parameter of the .agg() function, 
# where the keys of the dictionary are column names, 
# and the values are functions we want to apply. 
# Furthermore, we can even do two aggregations on one column:
  
#   df.groupby(['neighborhood']).agg({'price' : ['mean','max']})
  
# You can visit the documentation to have more examples of how to use groupby together with the .agg() function.

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.DataFrameGroupBy.aggregate.html?highlight=groupby%20sum

# Challenge

# Using the functions described above, which neighborhood has the biggest difference between maximum and minimum property price?

import pandas as pd
df = pd.read_csv('dubai_properties_data.csv')
# df.head()

group = df.groupby(['neighborhood']).agg({'price' : ['max','min']})
group['dif'] = group['price']['max'] - group['price']['min']
group.sort_values('dif', ascending=False).head()


# SOLUTION

grouped = df.groupby('neighborhood').agg({'price':['min','max']})
grouped.head()

# 	            price
#               min	max
# neighborhood		
# Al Barari	  1307392	4500000
# Al Barsha	  493314	778000
# Al Furjan 	350000	1349999
# Al Kifaf	  1359000	2100000
# Al Quoz	    360000	360000

(grouped.iloc[:,1] - grouped.iloc[:,0]).sort_values(ascending=False).head()

# neighborhood
# Palm Jumeirah               34375112
# Business Bay                30470000
# Jumeirah                    26300000
# Downtown Dubai              18688888
# Jumeirah Beach Residence    14110000
# dtype: int64
