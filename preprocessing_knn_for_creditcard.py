import sklearn
import pandas as pd,numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

knn=KNeighborsClassifier(n_neighbors=10)
#t,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,a=[int(x) for x in input().split(" ")]
df=pd.read_csv('creditcard.csv')
x=df.iloc[:,0].values
y=df.iloc[:,30].values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
knn.fit(x_train,y_train)
#print(knn.predict([[t,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,a]]))

plt.show()
plt.scatter(x,y)
plt.plot(x_test,knn.predict(x_test),color='Red',linewidth=3)
plt.show()
