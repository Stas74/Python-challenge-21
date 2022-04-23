# Data Filtering in Pandas

# Tutorial

# Data in this tutorial are the results of a chemical analysis of wines grown in the same region in Italy 
# but derived from three different cultivars.
# The analysis determined the quantities of 13 constituents found in each of the three types of wines.

# import pandas as pd
# df = pd.read_csv('wine.csv')

# df.head()

#   Class	Alcohol	Malic acid	Ash	  Alcalinity of ash	Magnesium	Total phenols	Flavanoids	Nonflavanoid phenols	Proanthocyanins	Color intensity	Hue	  OD280/OD315 of diluted wines	Proline
# 0	  1	  14.23      	1.71	  2.43	15.6	              127    	2.80	          3.06        	0.28              	2.29	              5.64     	1.04	    3.92	                     1065
# 1	  1 	13.20     	1.78	  2.14	11.2	              100	    2.65	          2.76	        0.26              	1.28	              4.38	    1.05	    3.40	                     1050
# 2	  1	  13.16	      2.36	  2.67	18.6	              101	    2.80	          3.24         	0.30              	2.81               	5.68	    1.03	    3.17	                     1185
# 3	  1	  14.37	      1.95	  2.50	16.8	              113   	3.85          	3.49        	0.24               	2.18	              7.80    	0.86    	3.45	                     1480
# 4	  1 	13.24	      2.59  	2.87	21.0	              118	    2.80	          2.69	        0.39              	1.82              	4.32    	1.04	    2.93	                      735 

# An important concept in data analysis that you should become familiar with is data filtering. We can think about filtering as a two step process. 
# The first step is creating a boolean condition that works as a filter, and the second step is passing the data through the filter.

# #Example - Loading Data
# user_filter = pd.read_csv('wine.csv')
# df.head()

# #Step 1: Create filter
# user_filter = df['Alcohol'] >= 14

# #Step 2: Feed the filter to the original DataFrame and store the result in a new variable
# filtered_df = df[user_filter]

# #Step 3: Display Variable
# filtered_df

# Try the code above and see how it plays out. 
# When you create a filter, observe the change in the number of rows between the old filtered DataFrame and the new one.

# We can combine step 1 and 2 into one step:

# # Step 1 and 2
# filtered_df_2 = df[df['Alcohol'] >= 14]
# Compare the two filtered DataFrames to see that they are the same. We can use the Python function len() to see how many rows the DataFrame has.

# print(len(user_filter))
# print(len(filtered_df))
# print(len(filtered_df) == len(filtered_df_2))

# To learn more about filtering in pandas, read this article.
# https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/

# To learn more about the various pandas functions, check out the user guide in the pandas documentation.
# https://pandas.pydata.org/docs/user_guide/index.html#user-guide
  
# filtered_df_2 = df[df['Alcohol'] < 13]
# filtered_df_2.head()

#   Class	Alcohol	Malic acid	Ash	  Alcalinity of ash	Magnesium	Total phenols	Flavanoids	Nonflavanoid phenols	Proanthocyanins	Color intensity	Hue	OD280/OD315 of diluted wines	Proline
# 21	1	  12.93  	3.80	      2.65	18.6	102	2.41	2.41	0.25	1.98	4.50	1.03	3.52	770
# 23	1 	12.85	  1.60	      2.52	17.8	95	2.48	2.37	0.26	1.46	3.93	1.09	3.63	1015
# 59	2	  12.37	  0.94      	1.36	10.6	88	1.98	0.57	0.28	0.42	1.95	1.05	1.82	520
# 60	2	  12.33	  1.10	      2.28	16.0	101	2.05	1.09	0.63	0.41	3.27	1.25	1.67	680
# 61	2	  12.64	  1.36	      2.02	16.8	100	2.02	1.41	0.53	0.62	5.75	0.98	1.59	450

# Challenge

# Answer the following questions using the data:

# How many Italian wines have a lower percentage of alcohol than 13%
# How many wines are there in class 3?

import pandas as pd
df = pd.read_csv('wine.csv')
df.head()

# Stretch Questions

# How many wines have a level of magnesium between 90 and 100?
# How many wines have a level of magnesium higher than 90, and a percentage of alcohol lower than 13.5%?
