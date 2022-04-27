# Stack and Unstack in Pandas

# Tutorial
# In today’s challenge, we will take a look at two more pandas functions that are often used for data wrangling: stack and unstack.

# import pandas as pd

# # we define the dataframe
# df = pd.DataFrame([[25.69, 7692000], [5.084, 268021]],
#             index=['Australia', 'New  Zealand'],
#             columns=['population', 'area'])

# # we apply the function stack()
# stacked = df.stack()

# Observe what happened with our DataFrame. The stack() function stacks both columns into one, and creates something we call a MultiIndex.

# print(stacked.index)

# If you want to learn more, you can find information about the MultiIndex in this article.
# https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html

# The MultiIndex is also the output of the group by method when we use it on more than one column.

# df = pd.DataFrame([["Southern", "Southern","Southern","Southern"], 
#                    ["Austria", "Australia", "New Zealand", "New Zealand"], 
#                    ["Sydney", "Melbourne","Auckland","Wellington"],
#                    [5.312, 5.078,1.463,0.215]],
#                   index=['hemisphere','country', 'city','population'] 
#                   ).transpose()

# grouped = df.groupby(["hemisphere","country"])[["population"]].mean()

# Observe what happened with our DataFrame.

# print(grouped.index)

# Now, we can use the unstack() function to expand the MultiIndex into separate columns.

# grouped.unstack(level=1)
# Play around with the parameter level. We can set it as either 0 or 1. What difference does it make which you choose?

# We can see more examples of stack and unstack here (https://www.w3resource.com/pandas/dataframe/dataframe-stack.php) and
# here (https://www.w3resource.com/pandas/dataframe/dataframe-unstack.php) respectively.

