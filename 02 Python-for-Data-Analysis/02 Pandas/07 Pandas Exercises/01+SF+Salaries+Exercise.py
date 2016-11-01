
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[80]:

import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[81]:

sal = pd.read_csv('Salaries.csv')

# In[223]:

pd.concat([sal_jlen, sal_bpay], axis=1).corr('pearson')


# In[225]:

pd.concat([sal_jlen, sal_bpay], axis=1).corr('kendall')# {‘pearson’, ‘kendall’, ‘spearman’}


# In[227]:

pd.concat([sal_jlen, sal_bpay], axis=1).corr('spearman')


# In[230]:

pd_corr_plot=pd.concat([sal_jlen, sal_bpay], axis=1)


# In[245]:

##import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
pd_corr_plot.plot(x='JobTitle', y='BasePay')
##%matplotlib inline


# # Great Job!
