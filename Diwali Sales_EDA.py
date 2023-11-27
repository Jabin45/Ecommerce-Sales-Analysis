#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


pip install pandoc


# In[14]:


df = pd.read_csv('Diwali Sales Data.csv', encoding="unicode_escape")
# encoding="unicode_escape" we use the code in order to read the unique characters in the dataset


# In[15]:


df
# to see the whole dataset we can use the file name in which we have stored the data


# In[4]:


df.shape
# we use the above syntax to see the number of rows and columns


# In[5]:


df.head()
# we use the above syntax in order to see the top 5 rows of the data


# In[6]:


df.head(2)
# we can add the number of rows we wanna see in the head()


# In[7]:


df.info()
# we use this syntax to see the columns details and datatype


# In[8]:


# df.drop['Status' , 'unnamed1'], axis=1 , inplace = True)
# # to drop a column 


# In[9]:


df.isnull()
# we use ISNULL to see if there's any null value


# In[10]:


df.isnull().sum()
# to get the count of missing values in each column


# In[11]:


df.dropna(inplace=True)
# to delete the null values from the rows


# In[12]:


df.shape


# In[44]:


df['Amount']=df['Amount'].astype('int')
# to change a column name we use .astype


# In[45]:


df['Amount'].dtypes
# to see if the particular column datatype is changed


# In[46]:


df.columns
# to see the column names


# In[16]:


df.rename(columns={'State':'States'})
# to rename a column we use this syntax


# In[17]:


df.describe()
# to see the numeric value columns count,mean,std etc


# In[18]:


df[['User_ID','Amount']].describe()
# to see a particular columns count,mean,std etc


# # Exploratory Data Analysis 

# ### Gender

# In[49]:


sns.countplot(x='Gender',data=df)
plt.show()


# In[50]:


ax = sns.countplot(x='Gender',data=df)
# creating a barchart without the count 


# In[51]:


# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = df,palette="rainbow",hue="Gender")

for bars in ax.containers:
    ax.bar_label(bars)


# In[52]:


sales_gender = df.groupby('Gender')['Amount'].sum().reset_index()
print(sales_gender)
# to find the sales amount by grouping method with gender


# In[53]:


ax=sns.barplot(x='Gender',y='Amount',data=sales_gender)
for bars in ax.containers:
    ax.bar_label(bars)
# using the above info we made a barplot and adding the count in the label


# ## AGE

# In[54]:


ax=sns.countplot(x='Age Group',hue='Gender',data=df)
for bars in ax.containers:
    ax.bar_label(bars)


# In[55]:


sns.countplot(x='Age Group',hue='Gender',data=df)
plt.show()


# In[56]:


sales_age=df.groupby('Age Group')['Amount'].sum().reset_index()
print(sales_age)


# In[57]:


sns.barplot(x='Age Group',y='Amount',data=sales_age)
plt.show()


# # State

# In[28]:


df


# In[58]:


sales_state=df.groupby('State')['Orders'].sum().reset_index()
plt.figure(figsize=(15,5))
sns.barplot(x='State',y='Orders',data=sales_state,palette='rainbow',hue='Orders')
plt.xticks(rotation=45)
plt.show()


# In[59]:


sales_state=df.groupby('State')['Amount'].sum().reset_index
print(sales_state)


# In[60]:


# States getting highest amount of top 10

sales_state=df.groupby('State')['Amount'].sum().reset_index()
plt.figure(figsize=(15,5))
sns.barplot(x='State',y='Amount',data=sales_state,palette='viridis',hue='Amount')
plt.xticks(rotation=45)
plt.show()


# # Martial Status

# In[61]:


plt.figure(figsize=(6,5))
ax=sns.countplot(data=df,x='Marital_Status')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()


# In[62]:


plt.figure(figsize=(7,4))
ax=sns.barplot(data=df,x='Marital_Status',y='Amount',hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()


# # Occupation

# In[63]:


plt.figure(figsize=(15,5))
ax=sns.countplot(data=df,x='Occupation',palette='viridis',hue='Occupation')
plt.xticks(rotation=45)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()


# In[78]:


sales_state=df.groupby('Occupation')['Amount'].sum().reset_index().sort_values(by='Amount',ascending=False)
print(sales_state)


# In[79]:


plt.figure(figsize=(17,5))
ax=sns.barplot(data=sales_state,x='Occupation',y='Amount',palette='viridis',hue='Occupation')
plt.xticks(rotation=45)
plt.show()


# # Product Category

# In[66]:


plt.figure(figsize=(15,5))
ax=sns.countplot(data=df,x='Product_Category',palette='viridis',hue='Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)
plt.xticks(rotation=45)
plt.show()


# In[67]:


Product_Category_Amount=df.groupby('Product_Category')['Amount'].sum().reset_index().sort_values(by='Amount', ascending=False)
print(Product_Category_Amount)


# In[68]:


plt.figure(figsize=(20,6))


ax=sns.barplot(x='Product_Category',y='Amount',data=Product_Category_Amount,palette='viridis',hue='Product_Category')
plt.xticks(rotation=45)
    
plt.show()


# In[69]:


sales_state=df.groupby('Product_ID')['Orders'].sum().reset_index().sort_values(by='Orders',ascending=False).head(10)
print(sales_state)


# In[70]:


plt.figure(figsize=(13,4))
sns.barplot(x='Product_ID',y='Orders',data=sales_state,palette='viridis',hue='Product_ID')


# In[ ]:




