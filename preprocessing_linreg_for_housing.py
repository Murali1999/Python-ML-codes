#preprocessing for housing data
import sklearn
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

ds=pd.read_csv('Housing_data.csv')
y=pd.np.array(ds['lotsize']).reshape(-1,1)
x=pd.np.array(ds['price']).reshape(-1,1)
x_train,x_test,y_train,y_test=train_test_split(y,x,test_size=0.2)
reg=LinearRegression()
reg.fit(x_train,y_train)
plt.show()
plt.scatter(y,x)
plt.plot(x_test,reg.predict(x_test),color='Red',linewidth=3)
plt.xlabel('lot size')
plt.ylabel('price')
plt.title('Plot for housing data using Linear Regression')
plt.show()

