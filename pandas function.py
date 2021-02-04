#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# # series

# In[2]:


a=[1,2,3,"as"]
print(a)


# In[6]:


s=pd.Series(a)
s


# In[7]:


s2=pd.Series([1,2,3,4])
print(s2)


# In[8]:


s3=pd.Series([1,2,3,4],index=["a","b","c","d"])
s3


# In[9]:


s4=pd.Series([1,2,3,4],index=["a","b","c","d"],dtype=float)
s4


# In[10]:


s5=pd.Series(0.5)
s5


# In[11]:


s6=pd.Series(0.5,index=[1,2,3])
s6


# In[13]:


dict=pd.Series({"a":1,"b":2})
dict


# In[18]:


s4["a"]


# In[19]:


s4[0:2]


# In[20]:


max(s4)


# In[21]:


min(s4)


# In[26]:


s6=s4[s4>2]


# In[25]:


s3+s4


# In[27]:


s3+s6


# # Data frame

# In[30]:


s_pd=pd.DataFrame()
print(s_pd)


# In[31]:


l=["a","b","c"]
l


# In[33]:


df1=pd.DataFrame(l)
df1


# In[35]:


ls=[[1,2,3],[4,5,6],[4,5,7]]
ls
df2=pd.DataFrame(ls)
df2


# In[36]:


dict1={"id":[1,2,3]}
dict1
df3=pd.DataFrame(dict1)
df3


# In[37]:


dict2={"id":[1,2,3], "sn":[4,5,6]}
dict2


# In[38]:


df4=pd.DataFrame(dict2)
df4


# In[41]:


ld=[{"a":1,"b":2},{"a":3,"b":4}]
df5=pd.DataFrame(ld)
df5


# In[43]:


lde=[{"a":1,"b":2,"c":5},{"a":3,"b":4}]
df6=pd.DataFrame(lde)
df6


# In[44]:


dr_sr={"id":pd.Series([1,2,3]), "sn":pd.Series([11,12,13])}
dr_sr
df7=pd.DataFrame(dr_sr)
df7


# # Csv file read

# In[47]:


df8=pd.read_csv("F:\\Data\\50_Startups.csv")
df8


# In[49]:


df8.columns


# In[50]:


df8=pd.read_csv("F:\\Data\\50_Startups.csv",nrows=1)
df8


# In[58]:


df8=pd.read_csv("F:\\Data\\50_Startups.csv",usecols=[2])


# In[56]:


df8=pd.read_csv("F:\\Data\\50_Startups.csv", usecols=[0,3])


# In[59]:


df8=pd.read_csv("F:\\Data\\50_Startups.csv", skiprows=1)
df8


# In[61]:


df8=pd.read_csv("F:\\Data\\50_Startups.csv", skiprows=[2,4])
df8


# In[3]:


df8=pd.read_csv("F:\\Data\\50_Startups.csv", index_col="State" )
df8


# In[5]:


df8=pd.read_csv("F:\\Data\\50_Startups.csv", index_col=3 )
df8


# In[8]:


df8=pd.read_csv("F:\\Data\\50_Startups.csv" ,header=1)
df8


# In[9]:


df8=pd.read_csv("F:\\Data\\50_Startups.csv", header=None )


# In[12]:


df8=pd.read_csv("F:\\Data\\50_Startups.csv",header=None, prefix="col")
df8


# In[16]:


df8=pd.read_csv("F:\\Data\\50_Startups.csv", names=["a","b","c","d","e"] )
df8


# In[17]:


df8.head()


# In[18]:


df8.tail()


# In[ ]:




