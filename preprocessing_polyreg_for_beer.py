#preprocessig using polynomial regression for housing data
import pandas as pd,numpy as np,sklearn
from sklearn import preprocessing
ds=pd.read_csv('Consumo_cerveja.csv')
ds.update(ds['Data'].dropna())
ds.update(ds['Temperatura Media (C)'].dropna())
ds.update(ds['Temperatura Minima (C)'].dropna())
ds.update(ds['Temperatura Maxima (C)'].dropna())
ds.update(ds['Precipitacao (mm)'].dropna())
ds.update(ds['Final de Semana'].dropna())
ds.update(ds['Consumo de cerveja (litros)'].dropna())

ds['Temperatura Minima (C)']=ds['Temperatura Minima (C)'].str.replace(",",".").astype(float)
ds['Temperatura Maxima (C)']=ds['Temperatura Maxima (C)'].str.replace(",",".").astype(float)
ds['Temperatura Media (C)']=ds['Temperatura Media (C)'].str.replace(",",".").astype(float)
ds['Precipitacao (mm)']=ds['Precipitacao (mm)'].str.replace(",",".").astype(float)

x=np.array(ds.iloc[:100,1]).reshape(-1,1)
Y=np.array(ds.iloc[:100,-1]).reshape(-1,1)
le=preprocessing.LabelEncoder()
y=le.fit_transform(Y)
from sklearn.model_selection import train_test_split
xtr,xte,ytr,yte=train_test_split(x,y,test_size=0.2)
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly=PolynomialFeatures(degree=4)
l=poly.fit_transform(xtr)
poly.fit(l,ytr)
lr=LinearRegression()
lr.fit(l,ytr)

#print(lr.predict([[4000]]))
import matplotlib.pyplot as plt

plt.scatter(x,y,color='blue')
plt.plot(xte,lr.predict(poly.fit_transform(xte)),color='red',linewidth=3)
plt.title('Polynomial regression for Beer Consumption')
plt.xlabel('Temperatura Media (C)')
plt.ylabel('Temperatura Minima (C)')
plt.show()
