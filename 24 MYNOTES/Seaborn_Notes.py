conta install seaborn
pip install seaborn


to see the distribution of the object

import seaborn as sns
%matplotlib inline

tips = sns.load_dataset('tips')
tips.head()

good for one variable 
sns.dist(tips['total'])
# histogram and density estimation
sns.dist(tips['total'],bins=30)




joint plot  = for bivariate and allow to join the dist plot

sns.joint(x,y,data=dataset)


sns.jointplot(x='total_bill',y='tip',data=tips)

sns.jointplot(x='total_bill',y='tip',data=tips, kind = 'hex')
sns.jointplot(x='total_bill',y='tip',data=tips, kind = 'reg')
sns.jointplot(x='total_bill',y='tip',data=tips, kind = 'kde')

pairwise relationship for numerical columns  and categorical columns
do the joint plot for every possible combinations

sns.pairplot(tips)
sns.pairplot(tips, hue = 'categoricalcolumname') # hue will colour charsts based on the categories
sns.pairplot(tips, hue = 'categoricalcolumname', pallete = 'bright')

#Rugplot goes handy with KDE (distplot)
sns.rugplot(tips['total_bill']) # rugplot draws a small vertical line for each observation 

KDE = kernel density estimation
sns.kdeplot(tips['total_bill'])

==============================================================================================

Categorical Plots 
===================
import numpy as np
usually categories referenced to another categorical or continuous variable 

#this is visualization of a groupby 
sns.barplot(x='sex',y='total_bill',data=tips) # by default it will tell MEAN of both 
sns.barplot(x='sex',y='total_bill',data=tips, estimator = np.std #std ) #standard deviation #somefunction

barplot where sestimator is counting the number 
sns.countplot(x='sex',data=tips) # it will count the no of male and female 

# Box whisker plot 
sns.boxplot(x='day',y='total',data=tips)
x = categorical 
y = continous

sns.boxplot(x='day',y='total',data=tips, hue = 'smoker')
# splitted by another category 


#similar to box also shows distribution
sns.violinplot(x='day',y='total_bill',data=tips)

#distribution shown on sides

sns.violinplot(x='day',y='total_bill',data=tips, hue = 'sex')
sns.violinplot(x='day',y='total_bill',data=tips, hue = 'sex', split=True)

#scatterplot based on categories
sns.stripplot(x='day',y='total_bill',data=tips)
sns.stripplot(x='day',y='total_bill',data=tips, jitter=True) # add stacking details shows density better

sns.stripplot(x='day',y='total_bill',data=tips, hue = 'sex', jitter=True)

sns.swarmplot(x='day',y='total_bill',data=tips) # show points

# mixing this with violinplot
sns.violinplot(x='day',y='total_bill',data=tips)
sns.swarmplot(x='day',y='total_bill',data=tips, color='black') # show points

# Factor plot 

sns.factorplot(x='day',y='total_bill', data=tips, kind='bar')


==============================================================================================

Matrixplots 
HEatmaps

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')


