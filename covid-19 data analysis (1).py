#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.getcwd()


# In[2]:


os.listdir('covid datasets')


# In[3]:


# store the data sets into a files
files = os.listdir('covid datasets')
files


# In[4]:


#mutiple datasets over there it means we have to read your data again and again so, 
#create a function (because it makes the task much easier)
#define function
def read_data(path,filename):
    return pd.read_csv(path + '/'+filename)
path = 'covid datasets'
read_data(path,'worldometer_data.csv')
world_data = read_data(path,'worldometer_data.csv')
world_data


# In[5]:


world_data.head()


# In[6]:


day_wise = read_data(path , files[2])
group_data=read_data(path,files[3])


# In[7]:


province_data = read_data(path , files[1])
province_data.shape


# In[8]:


world_data .head()


# In[9]:


#data analysis means get answer our question from the data here the
#statement 1-which country has maximum total cases,death,recovered and active cases ?


# In[10]:


world_data.columns


# In[11]:


#to get a tree map visual
import plotly.express as px


# In[12]:


import plotly.express as px
columns = ['TotalCases','TotalDeaths' ,'TotalRecovered' ,'ActiveCases' ,'TotalTests']
for i in columns:
    fig = px.treemap(world_data.iloc[0:10],values=i,path=['Country/Region'],title='Treemap representation of diff country w.r.t {}'. format(i))
    fig.show ()               


# In[13]:


#statement 2 
#what is the trend of confirmed death, recovered, active case?


# In[14]:


day_wise.head()


# In[15]:


px.line(day_wise, x='Date',y=['Confirmed','Deaths','Recovered','Active'],title ='covid cases w.r.t date',template = 'plotly_dark')


# In[16]:


world_data.head(10)


# In[17]:


#visualise the population to test done ratio


# In[18]:


world_data.head()


# In[ ]:





# In[19]:


#now we going to visualize population to test done ratio these feature is not in the above table so
#we have to create the feature by dividing the populaton by total test done

population_test_ratio = world_data['Population']/world_data['TotalTests'].iloc[0:20]
fig = px.bar(world_data.iloc[0:20],x='Country/Region',y=population_test_ratio[0:20],color ='Country/Region',title='population to test done')
fig.show()


# In[20]:


#20 countries that are badly affected by corona virus
world_data.columns


# In[21]:


px.bar(world_data.iloc[0:20],x='Country/Region',y=['Serious,Critical','TotalDeaths', 'ActiveCases','TotalRecovered'],title='Countries badly affected by corona virus')


# In[22]:


#worst 20 countries having maximum conformed cases
fig = px.bar(world_data.iloc[0:20],y='Country/Region',x='TotalCases',text='TotalCases',color = 'TotalCases')
fig.update_layout(template='plotly_dark',title ='Top 20 countries of total confirmed cases')
fig.show()


# In[23]:


#top 20 countries of maximum total deaths


# In[24]:


fig = px.bar(world_data.iloc[0:20],y='Country/Region',x='TotalDeaths',text='TotalDeaths',color = 'TotalDeaths')
fig.update_layout(template='plotly_dark',title ='Top 20 countries of maximum "Total Deaths"')
fig.show()


# In[25]:


world_data.sort_values('TotalDeaths',ascending=False)


# In[26]:



fig = px.bar(world_data.sort_values('TotalDeaths',ascending=False)[0:20],y='Country/Region',x='TotalDeaths',text='TotalDeaths',color = 'TotalDeaths')
fig.update_layout(template='plotly_dark',title ='Top 20 countries of maximum "Total Deaths"')
fig.show()


# In[27]:


#pie chart representation of stats of worst affected countries
world_data.head()


# In[ ]:





# In[28]:


labels = world_data[0:15]['Country/Region'].values
cases=['TotalCases','TotalDeaths' ,'TotalRecovered' ,'ActiveCases' ]
for i in cases:
    fig= px.pie(world_data[0:15],names=labels,hole=0.3,title='{} recorded w.r.t WHO regio of 15 worst affected countries'.format(i))
    fig.show () 


# In[29]:


#
world_data.head()


# In[32]:


#deaths to confirmed ratio
death_to_totalcases = world_data['TotalDeaths']/world_data['TotalCases']
death_to_totalcases


# In[34]:


px.bar(world_data,x='Country/Region',y=death_to_totalcases,title='death ratio of worst affected countries')


# In[35]:


deaths_to_recovered = world_data['TotalDeaths']/world_data['TotalRecovered']
deaths_to_recovered


# In[36]:


px.bar(world_data,x='Country/Region',y=deaths_to_recovered,title='death to recovered  ratio of worst affected countries')


# In[37]:


group_data=read_data(path,files[3])
group_data


# In[38]:


group_data.head()


# In[39]:


from plotly.subplots import make_subplots  ## for creating subplots in plotly
import plotly.graph_objects as go


# In[43]:


def country_visualization(group_data,country):
    data=group_data[group_data['Country/Region']==country]
    df=data.loc[:,['Date','Confirmed','Deaths','Recovered','Active']]
    fig = make_subplots(rows=1, cols=4,subplot_titles=("Confirmed", "Active", "Recovered",'Deaths'))
    fig.add_trace(
        go.Scatter(name="Confirmed",x=df['Date'],y=df['Confirmed']),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(name="Active",x=df['Date'],y=df['Active']),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(name="Recovered",x=df['Date'],y=df['Recovered']),
        row=1, col=3
    )

    fig.add_trace(
        go.Scatter(name="Deaths",x=df['Date'],y=df['Deaths']),
        row=1, col=4
    )

    fig.update_layout(height=600, width=1000, title_text="Date Vs Recorded Cases of {}".format(country),template="plotly_dark")
    fig.show()


# In[44]:


country_visualization(group_data,'Brazil')


# In[46]:


country_visualization(group_data,'Afghanistan')


# In[ ]:




