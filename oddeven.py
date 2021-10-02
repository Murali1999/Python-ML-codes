#insert odd and even values in the table

import pandas as pd
af=pd.DataFrame()
lia,lib=[],[]

a = int(input("Enter number - "))
print(a)

for i in range(a):
    if(i%2==0):
        lia.append(i)
    elif(i%2==1):
        lib.append(i)
else:
    print("out of range")

af=pd.DataFrame({'a':lia,'b':lib})
print(af)

df=af.to_csv("c:/Users/Public/col2.csv")
print("File saved as .csv file")
