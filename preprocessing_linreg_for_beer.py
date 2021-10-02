#preprocessing for beer consumption
import sklearn
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

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

y=pd.np.array(ds.iloc[:150,1]).reshape(-1,1)
x=pd.np.array(ds.iloc[:150,6]).reshape(-1,1)
x_train,x_test,y_train,y_test=train_test_split(y,x,test_size=0.2)
reg=LinearRegression()
reg.fit(x_train,y_train)
plt.show()
plt.scatter(y,x)
plt.plot(x_test,reg.predict(x_test),color='Red',linewidth=3)
plt.xlabel('Temperatura Media (C)')
plt.ylabel('Temperatura Minima (C)')
plt.title('Plot for Beer Consumption using Linear Regression')
plt.show()

