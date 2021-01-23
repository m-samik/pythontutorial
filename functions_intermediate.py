#!/usr/bin/env python
# coding: utf-8

# In[157]:


#Function to accept more than one value at  a time
#"""""" is used to the doc string / documentation of the function.
def mail(*i):
    """Astrix (*) here is used for accepting more than one parameter in our function """
    k=[]
    for j in i:
        k.append(j + "@gmail.com")
    return k


# In[154]:


email_ids=mail("sami","jack","pop")
email_ids


# In[160]:


#Key Value Pair : Keyword Argument in Functions 
#def db (name ="sami") --> Default argument
def db(name,city,country="India"):
    return "Name:"+ name + " City:" + city + " Country:"+ country


# In[162]:


#Defualt Parameter 
db(city="Anantnag",name="Sami")


# In[163]:


#for documentation
mail.__doc__


# In[ ]:


#assining one function to the variable 
k=db


# In[171]:


#Lamba Function
x=lambda i,j : i+j


# In[179]:


x(3,4)


# In[194]:


db=[1,2,3,5,6,5,6,8,8,8,8,7,]
#Filter Function using lamda for filtering the data.
x=list(filter(lambda x: x%2==0 ,db))


# In[195]:


x


# In[ ]:




