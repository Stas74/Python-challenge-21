# Descriptive statistics in Pandas

# Pandas https://pandas.pydata.org/

### Tutorial

Part of the job of data scientists and data analysts is to *understand* the data and *extrapolate* certain findings. In most cases, the first step of understanding a numerical data set is to look at the **descriptive statistics**. Descriptive statistics are *brief descriptions that summarize datasets*. There are many great Python libraries we can use to get descriptive statistics from numerical datasets. One such library is **[Pandas](https://pandas.pydata.org/)**. We won't be going too in-depth with Pandas today, just the basics to understand how to use Pandas to get some general descriptive statistics. We will be covering Pandas extensively and going over some of the advanced functions starting on Day 8.

**Pandas** is one of the most widely used Python packages. Pandas can be used when working with large data sets or performing data cleaning, manipulation, and analysis. 

Since the Pandas library is external to base Python, we will need to import it. When importing, we give an alias to Pandas to shorten our code when calling on functions from Pandas. Instead of writing ***pandas.name_of_function()*** we'll be able to write ***pd.name_of_function()***. The alias ***pd*** is standard within the Python community.

```python
import pandas as pd # we must import our external python plugin

list_of_num = [1,2,3,4,5]

series = pd.Series(list_of_num) #converting our list_of_num to a pandas series variable
                                #we need to do this to use some of pandas' useful descriptive statistics functions
    
series.max()    #outputs maximum value in Pandas Series
series.min()    #outputs minimum value in Pandas Series
series.mean()   #outputs average value in Pandas Series
series.median() #outputs median value in Pandas Series
series.mode()   #outputs mode value in Pandas Series
```

To read more on descriptive statistics, read this [article](https://realpython.com/python-statistics/#getting-started-with-python-statistics-libraries).

To learn more about the various Pandas functions, check out the user guide in the [pandas documentation](https://pandas.pydata.org/docs/user_guide/index.html#user-guide).

-------
**Why should I use the documentation?**

On the job as a data scientist or data analyst, more often than not, you may find yourself looking up the documentation of a particular function or plugin you use. Don't worry if there are a few functions you don't know by heart. There are just too many to know! An essential skill is to learn how to navigate documentation and understand how to apply the examples to your work.
