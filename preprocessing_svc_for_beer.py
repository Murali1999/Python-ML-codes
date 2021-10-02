#preprocessing and plotting using support vector machine for beer consumption data

import sklearn
from sklearn import neighbors
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing
ds=pd.read_csv('Consumo_cerveja.csv')

#preprocessing the data - interpreting NaN and string values
#change NaN values to 0 or drop the values with missing values
ds.update(ds['Data'].dropna())
ds.update(ds['Temperatura Media (C)'].dropna())
ds.update(ds['Temperatura Minima (C)'].dropna())
ds.update(ds['Temperatura Maxima (C)'].dropna())
ds.update(ds['Precipitacao (mm)'].dropna())
ds.update(ds['Final de Semana'].dropna())
ds.update(ds['Consumo de cerveja (litros)'].dropna())

#change string to float;comma to dot to convert to decimal numbers
ds['Temperatura Minima (C)']=ds['Temperatura Minima (C)'].str.replace(",",".").astype(float)
ds['Temperatura Maxima (C)']=ds['Temperatura Maxima (C)'].str.replace(",",".").astype(float)
ds['Temperatura Media (C)']=ds['Temperatura Media (C)'].str.replace(",",".").astype(float)
ds['Precipitacao (mm)']=ds['Precipitacao (mm)'].str.replace(",",".").astype(float)

X=ds.iloc[:100,1:3].values
Y=ds.iloc[:100,-1].values
le=preprocessing.LabelEncoder()
y=le.fit_transform(Y)
C=1.0
knn=neighbors.KNeighborsClassifier()
datx,daty=X.iloc[:,0].values,X.iloc[:,1].values

x_min,x_max=datx.min(),datx.max()
y_min,y_max=daty.min(),daty.max()
h=(x_max/x_min)/100
xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))
plt.subplot(1,1,1)
Z=svc.predict(np.c_[xx.ravel(),yy.ravel()])
Z=Z.reshape(xx.shape)
plt.contourf(xx,yy,Z,cmap=plt.cm.Paired,alpha=0.4)

plt.scatter(datx,daty,c=y,cmap=plt.cm.Paired)
plt.xlabel('Temperature Media (C)')
plt.ylabel('Temperatura Minima (C)')
plt.xlim(xx.min(),xx.max())
plt.title('SVC with rbf kernel for Beer Consumption in Brazil')
plt.show()
