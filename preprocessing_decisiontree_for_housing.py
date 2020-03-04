import sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
ds=pd.read_csv('Housing_data.csv')
dtc=DecisionTreeClassifier()

x=pd.np.array(ds['lotsize']).reshape(-1,1)
Y=pd.np.array(ds['price']).reshape(-1,1)
le=preprocessing.LabelEncoder()
y=le.fit_transform(Y)
C=1.0
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)
dtc.fit(x,y)

plt.show()
plt.scatter(x,y,c=y,cmap=plt.cm.Paired)
#plt.plot(x_test,dtc.predict(x_test),color='Red',linewidth=3)
plt.xlabel('Temperature Media (C)')
plt.ylabel('Temperatura Minima (C)')
plt.title('Decision Tree for Housing data')
plt.show()
