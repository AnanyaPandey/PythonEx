# Analysis
 
 
Who is more likely to commit suicide(Male or Female)
Which Age segment is most susceptible to suicide
What is the global trend of suicide throughout the years in the data. 
Developed countries vs Non Developed Countries(Need to tag all countries as Developed and Non Developed)

replacing NA with 0
df['suicides_no'].fillna(value=0,inplace=True)

#Suicide rate by country for top 15 countries
df.groupby('country)['suicide_no').sum().head(15)

#staringa nd ending year 
print(min(df.year))
print(max(df.year))


#Who is more likely to commit suicide(Male or Female)
df.groupby('sex')['suicide_no'].sum()
df.groupby('sex')['suicide_no'].sum().plot.bar(figsize=(10,7),title = "Male V/s Female Suicide Overall comparison from 1978 to 2015")

#Which Age segment is most susceptible to suicide

df['age'].unique()
df.groupby('age')['suicide_no'].sum().sort_index().plot.bar(figsize=(10,7), title = "Age wise Suicide comparison")

#What is the global trend of suicide throughout the years in the data.
df.groupby('year')['suicide_no'].sum().plot.line(figsize = (10,7), title = "Suicide global trend")


import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks", color_codes=True)


Groupby !
# If reset_index is not used the grouped column is returned as index or hierarchical index if multiple columns are selected.
df.groupby(['ID','Year']).mean().reset_index()
df.groupby(data['column']).function().reset_index()

#two categorical columns are grouped
df.groupby(['country','sex'])['suicides_no'].sum().reset_index().head()
