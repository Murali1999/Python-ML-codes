import sklearn
from sklearn import neighbors
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

ds=pd.read_csv('Housing_data.csv')
x=pd.np.array(ds['lotsize']).reshape(-1,1)
y=pd.np.array(ds['price']).reshape(-1,1)
knn=neighbors.KNeighborsClassifier()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
C=1
knn.fit(x_train,y_train)
plt.show()
plt.scatter(x,y)
plt.plot(x_test,knn.predict(x_test),color='Red',linewidth=3)
plt.xlabel('lot size')
plt.ylabel('price')
plt.title('Plot for housing data using KNN')
plt.show()
