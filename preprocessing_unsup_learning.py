import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

dataset=pd.read_csv('store_data.csv')
print(dataset)
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary,columns=te.columns_)
df.columns.values[0] = 'aa' #rename column with null header
set(df['aa'])
set(df['a'])
print(df)

print(apriori(df, min_support=0.00004, use_colnames=True,))
frequent_itemsets = apriori(df, min_support=0.00004, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
print(frequent_itemsets)
print(frequent_itemsets[ (frequent_itemsets['length'] == 2) & (frequent_itemsets['support'] >= 0.0004) ])
df['support'].max()

