## import packages
import pandas as pd
import numpy as np
import datetime as dt
import uuid

## load data into python
df = pd.read_csv('data/School_Learning_Modalities.csv')

## columns/rows
df.shape

## column names
list(df)

## clean column names
# remove whitespace and special characters
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')

# change to lowercase
df.columns = df.columns.str.lower()

###rename week for date

df = df.rename(columns={'week':'date'})

## list datatypes
df.dtypes


## datetime
dates = df.select_dtypes(include=['object']).columns

df['date'] = pd.to_datetime(df['date'])


##drop duplicates
df.drop_duplicates()

## count missing values
df.isnull().sum()

## replace missing values with nan
df.replace(to_replace='', value=np.nan, inplace=True)
df.replace(to_replace=' ', value=np.nan, inplace=True)

##drop rows with missing values
df.dropna(inplace=True)

## create new column called modality_inperson

df['modality_inperson'] = np.where(df['learning_modality'] == 'In Person', True, False)

df.dtypes


## save clean version 
df.to_csv('data/School_Learning_Modalities_Clean.csv')