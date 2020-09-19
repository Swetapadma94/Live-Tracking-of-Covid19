#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

df = pd.read_json('https://www.mohfw.gov.in/data/datanew.json')
df


# In[3]:


df=df.iloc[:-1,1:]


# In[4]:


df


# In[6]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
total_states=np.arange(len(df['state_name']))


# In[7]:


total_states


# In[9]:


df['active']


# In[11]:


max(df['positive'])


# # Total Positive Cases Based On States In India

# In[14]:


from matplotlib.pyplot import figure
figure(num=None, figsize=(9, 6), dpi=80, facecolor='w', edgecolor='k')
plt.barh(total_states,df['positive'], align='center', alpha=0.5,  
                 color=(1,0,0),  
                 edgecolor=(0.5,0.2,0.8))
    
plt.yticks(total_states, df['state_name'])  
plt.xlim(1,max(df['positive'])+300) 
plt.xlabel('Positive Number of Cases')  
plt.title('Corona Virus Cases')  
plt.show()


# In[ ]:





# In[17]:


from matplotlib.pyplot import figure
figure(num=None, figsize=(9, 6), dpi=80, facecolor='w', edgecolor='k')
plt.barh(total_states,df['active'], align='center', alpha=0.5,  
                 color=(0,1,0),  
                 edgecolor=(0.5,0.2,0.8))
    
plt.yticks(total_states, df['state_name'])  
plt.xlim(1,max(df['active'])+100) 
plt.xlabel('Active Number of Cases')  
plt.title('Corona Virus Cases')  
plt.show()


# In[20]:


from matplotlib.pyplot import figure
figure(num=None, figsize=(9, 6), dpi=80, facecolor='w', edgecolor='k')
plt.barh(total_states,df['death'], align='center', alpha=0.5,  
                 color=(0,0,1),  
                 edgecolor=(0.5,0.2,0.8))
    
plt.yticks(total_states, df['state_name'])  
plt.xlim(1,max(df['death'])+100) 
plt.xlabel('death Number of Cases')  
plt.title('Corona Virus Cases')  
plt.show()


# # Stack All the columns in the bar chart

# In[21]:



df.columns


# In[22]:



df=df.set_index('state_name',drop=True)


# In[23]:


df


# In[24]:



### Plotting Based on Stacking
df.plot.barh(stacked=True,figsize=(10,10))


# In[25]:


df1=df.iloc[:,1:3]
df1.plot.barh(color={"cured": "red", "positive": "green"},figsize=(10,10))


# In[30]:


df1=df.iloc[:,1:4]
df1.plot.barh(color={"cured": "red", "positive": "green","death":"blue"},figsize=(10,10))


# In[ ]:




