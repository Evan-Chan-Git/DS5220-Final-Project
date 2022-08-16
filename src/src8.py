import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error

df = pd.read_csv('https://raw.githubusercontent.com/Evan-Chan-NEU/DS5220-Final-Project/main/Project%20Dataset/Stores.csv')

X=df[["Daily_Customer_Count", "Items_Available"]]
y=df[["Store_Sales"]]

# divide into train and test spits
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# fit linear regression model
lr=LinearRegression()
lr.fit(X_train,y_train)
pred = lr.predict(X_test)

# assess whether model explains data using r2
r2=(r2_score(y_test,pred))
#print(r2*100)

# assess whether model holds using the absolute error
error = mean_absolute_error(y_test, pred)
#print(error)
