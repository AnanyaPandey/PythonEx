# pythonic polynomial regression using sklearn
#SVR
#decisionTree Regression 
#RandomForestRegresion
# All are non linear regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('position_salaries.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 2].values

from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
linreg.fit(X,y)

from sklearn.preprocessing import PolynomialFeatures
polyreg = PolynomialFeatures(degree=3,include_bias=False)
X_poly=polyreg.fit_transform(X) # included polynomial features

linreg2 = LinearRegression()
linreg2.fit(X_poly,y)

plt.scatter(X,y,c='red')
plt.plot(X,linreg.predict(X),c='blue')
plt.title('Comparing regressions')

import statsmodels.formula.api as smf
mod = smf.ols('y ~ X', data=df)
res = mod.fit()
print(res.summary())

                        OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.129
Model:                            OLS   Adj. R-squared:                  0.089
Method:                 Least Squares   F-statistic:                     3.257
Date:                Fri, 29 Apr 2016   Prob (F-statistic):             0.0848
Time:                        20:12:12   Log-Likelihood:                -53.868
No. Observations:                  24   AIC:                             111.7
Df Residuals:                      22   BIC:                             114.1
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
Intercept      0.9909      0.908      1.091      0.287        -0.893     2.875
x              0.3732      0.207      1.805      0.085        -0.056     0.802
==============================================================================
Omnibus:                        3.957   Durbin-Watson:                   0.999
Prob(Omnibus):                  0.138   Jarque-Bera (JB):                1.902
Skew:                           0.380   Prob(JB):                        0.386
Kurtosis:                       1.849   Cond. No.                         8.50
==============================================================================

# to print it in the LATEX format 
#f = open('myreg.tex', 'w')
#f.write(beginningtex)
#f.write(res.summary().as_latex())
#f.write(endtex)
#f.close()