#preprocessig using polynomial regression for housing data
import pandas as pd,numpy as np,sklearn
data=pd.read_csv('Housing_Data.csv')
ip=np.array(data.loc[:,'lotsize'][:30]).reshape(-1,1)
op=np.array(data.loc[:,'price'][:30]).reshape(-1,1)
##ip=np.array([1,3,3,4,4,6,5,7]).reshape(-1,1)
##op=np.array([2,2,2,5,3,7,8,9]).reshape(-1,1)
from sklearn.model_selection import train_test_split
xtr,xte,ytr,yte=train_test_split(ip,op,test_size=0.2)

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly=PolynomialFeatures(degree=4)
l=poly.fit_transform(xtr)
poly.fit(l,ytr)
lr=LinearRegression()
lr.fit(l,ytr)

#print(lr.predict([[4000]]))
import matplotlib.pyplot as plt

plt.scatter(ip,op,color='blue')
plt.plot(xte,lr.predict(poly.fit_transform(xte)),color='red',linewidth=3)
plt.title('Housing price prediction')
plt.xlabel('lotsize')
plt.ylabel('price')
plt.show()
