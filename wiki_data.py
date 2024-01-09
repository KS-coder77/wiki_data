#!/usr/bin/env python
# coding: utf-8

# In[46]:


#import libs 

import pandas as pd

import plotly as py
import plotly.graph_objs as go 


# In[2]:


filepath = r"C:\Users\krupa\OneDrive\Documents\Krups coding\Data analysis\wiki data\Country_data.csv"

data = pd.read_csv(filepath)
data.head()
    


# In[6]:


# info about dataset 
#stats
data.describe()


# In[8]:


data.info()


# In[10]:


data.shape


# In[ ]:


#the dataset consists of 19 columns and 142 rows. 16 out of the 19 columns have float data types and 3 columns have string object data types.


# In[ ]:


#the dataset consists of some interesting information. Before we dive in, let's check for any inconsistencies and missing values.


# In[13]:


#locate any missing vals
print('missing values (%) per column: \n', 100*data.isnull().mean())


# In[ ]:


#Most of the missing values are within the GDP forecast columns. The column with the most missing values is the IMF Forecast GDP (Nominal). 


# In[15]:


#non-numerical data columns
non_numeric_data = list(data.select_dtypes(exclude = ('int', 'float')).columns)
print(f'Columns without numeric data: {", ".join(non_numeric_data)}.')


# In[34]:


#check for any duplications 
print('Duplication overall: ', 100*(len(data)-len(data.drop_duplicates()))/len(data))
print('Duplication in Country column: ', 100*(len(data['Country'])-len(data['Country'].drop_duplicates()))/len(data['Country']))


# In[35]:


#There are no overall duplicates or duplicates in any of the country names. We can expect there to be duplicates in the region and sub-region columns.


# In[48]:


#Let's see how the data is split geographically 
continents_df = data['UN Continental Region'].value_counts().to_frame().reset_index().rename(columns = {'index':'UN Continental Region', 'UN Continental Region':'Quantity'})
continents_df


# In[49]:


trace1 = go.Pie(labels=continents_df['UN Continental Region'], values = continents_df['Quantity'],
               title = 'Data split by Continents',
               )


# In[50]:


fig=go.Figure(trace1)
fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




