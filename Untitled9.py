#!/usr/bin/env python
# coding: utf-8

# In[13]:


# checking working directory
import os
import pandas as pd

current_directory = os.getcwd()
print(current_directory)


# In[14]:


# change working directory
new_directory_path = r'C:\Users\sanja'
os.chdir(new_directory_path)


# In[15]:


updated_dir = os.getcwd()
print(updated_dir)


# In[20]:


file_path = r"C:\Users\sanja\Week13Assignment.txt"

try: 
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except IOError:
    print("An error occured while reading the file.")


# In[22]:


# average age of patients
df = pd.read_csv(file_path)


# In[23]:


print(df)


# In[24]:


print (df.columns)


# In[25]:


# average age
average_age = df[' Age'].mean()
print(average_age)


# In[27]:


# 6number of male and female patients
male = (df[' Gender'] == ' Male').sum()
female = (df[' Gender'] == ' Female').sum()
print(f"The number of male patients is {male} and the number of female patients is {female}.")


# In[28]:


# get the highest blood pressure
max_bp = max(df[' BloodPressure'])
print(f"The highest blood pressure is {max_bp}.")


# In[31]:


# get the lowest blood pressure
min_bp = min(df[' BloodPressure'])
print(f"The lowest blood pressyre is {min_bp}.")


# In[32]:


# average temperature
average_temp = df[' Temperature'].mean()
print(f"The average temperature is {average_temp}.")

