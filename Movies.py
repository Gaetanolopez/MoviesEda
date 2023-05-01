#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Importing the required packages here

import numpy as np
import pandas as pd
import seaborn as sns
import ast, json

from datetime import datetime
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[6]:


#### load the movie dataset and create their dataframes

movies= pd.read_csv("movies.csv")
movies.columns


# In[7]:


movies.isna().sum()


# In[8]:


movies.shape


# In[9]:


movies.drop("keywords",axis=1,inplace=True)
movies.drop("homepage",axis=1,inplace=True)
movies.drop("status",axis=1,inplace=True)
movies.drop("tagline",axis=1,inplace=True)
movies.drop("original_language",axis=1,inplace=True)
movies.drop("overview",axis=1,inplace=True)
movies.drop("production_companies",axis=1,inplace=True)
movies.drop("original_title",axis=1,inplace=True)


# #### Remove any duplicate rows

# In[10]:


movies.drop_duplicates(subset="budget",keep="first",inplace=True)
len(movies)
movies.shape


# In[11]:



indexValue = movies[ (movies['budget'] == 0) | (movies['revenue'] == 0) ].index
movies.drop(indexValue , inplace=True)
movies.shape


# In[12]:


movies.shape


# In[13]:


# Change the release_date column to DateTime column
movies["release_date"] = pd.to_datetime(movies['release_date'], format='%Y-%m-%d')
# Extract the release year from every release date ?


# In[14]:


movies["budget"]=np.dtype("int64").type(movies["budget"])
movies["revenue"]=np.dtype("int64").type(movies["revenue"])


# In[15]:


def parse_col_json(column, key):
    """
    Args:
        column: string
            name of the column to be processed.
        key: string
            name of the dictionary key which needs to be extracted
    """
    for index,i in zip(movies.index,movies[column].apply(json.loads)):
        list1=[]
        for j in range(len(i)):
            list1.append((i[j][key]))# the key 'name' contains the name of the genre
        movies.loc[index,column]=str(list1)
    
parse_col_json('genres', 'name')
parse_col_json('spoken_languages', 'name')

parse_col_json('production_countries', 'name')

movies.head()


# In[16]:


len(movies)


# In[17]:


expensive=movies[["budget","revenue","title"]].sort_values(by="budget",ascending=False).head(5)
cheapest=movies[["budget","revenue","title"]].sort_values(by="budget",ascending=True).head(5)


# In[18]:


expensive


# In[19]:


sns.barplot(x="budget", y="revenue",data=expensive, hue="title")


# In[20]:


# the 5 most expensive movies are Pirates of the Caribbean: On Stranger Tides,Pirates of the Caribbean: At World's End,
#Avengers: Age of Ultron,Superman Returns and John Carter


# In[21]:


cheapest


# In[22]:


sns.barplot(x="budget", y="revenue",data=cheapest, hue="title")


# In[23]:


# we notice that if we consider the cheapest movies, only Modern Times was able to generate revenue even without spending money.
# regarding the expensivest movie, every movie was able to generate profit.So is worth so invest money in the movie because it will generate more profit


# In[24]:


movies["profit"]=movies["revenue"] - movies["budget"]


# In[25]:


profitable=movies[["profit","title"]].sort_values(by="profit",ascending=False).head(5)


# In[26]:


sns.barplot(x="profit", y="title",data=profitable)


# In[27]:


#The 5 top profitable movies are: Avatar, Titanic,Jurassic World, Furious 7 and The avengers


# In[ ]:





# In[28]:


less_profitable=movies[["profit","title","budget"]].sort_values(by="profit",ascending=True).head(5)


# In[29]:


sns.barplot(x="profit", y="title",data=less_profitable)


# In[30]:


# The movie that generates more profit is Avatar and the one that generate less profit was The Lone Ranger(it lost money)


# In[31]:


popular=movies[["popularity","title"]].sort_values(by="popularity",ascending=False).head(20)


# In[32]:


sns.barplot(x="popularity", y="title",data=popular)


# In[33]:


# The most popularity movie was Minions


# In[34]:


movies[movies["vote_average"]>7]





# In[35]:


movies[["profit","release_date","title"]].sort_values(by="profit",ascending=False).head(1)





# In[36]:


# the most profitable movie was made in 2009


# In[37]:


fig = plt.figure(figsize=(20,10))
movies.groupby("genres")["genres"].count().sort_values(ascending=False).head(20).plot(kind="bar")


# In[38]:


# the most successful genre was Drama because as we see in this bar graph, the majority of movies are related to this genre


# In[39]:


movies.isna().sum()


# In[40]:


movies.columns


# In[41]:


fig = plt.figure(figsize=(20,10))
movies.groupby("spoken_languages")["spoken_languages"].count().sort_values(ascending=False).head(20).plot(kind="bar")


# In[42]:


# almost every movie is spoken only in English


# In[43]:


fig = plt.figure(figsize=(20,10))
movies.groupby("title")["runtime"].max().sort_values(ascending=False).head(20).plot(kind="bar")


# In[44]:


# the longest movie is Cleopatra with a runtime of 250 minutes


# In[45]:


movies["production_countries"].value_counts().sort_values(ascending=False)


# In[46]:


movies.groupby("production_countries")["production_countries"].count().sort_values(ascending=False).head(20).plot(kind="bar")


# In[47]:


# the majority of movies were were producted in United Stated


# In[48]:


sns.lineplot(data=movies,x=movies["profit"],y=movies["popularity"])  
plt.show()


# In[49]:


# interesting to notice that the movies that were more popular didn`t make more profit


# In[50]:


movies[["budget","vote_average","title","vote_count"]].sort_values(by="vote_count",ascending=False)

