import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('covid-variants.csv', index_col='location')
# print(df)
# print(df.location.drop_duplicates())
# mask1 = (df['location'] =='Angola')
# mask2 = (df['location'] =='Argentina')
# df_1 = df[mask1]
# df_2 = df[mask2]
# print(df_1)
# print()
# print(df_2)
df_1 = df.loc['Angola']

plt.figure(figsize=(10, 10))
plt.plot(df_1['date'], df_1['num_sequences'])

plt.xticks(rotation='vertical')

plt.title('Angola')
plt.legend(labels=['Angola'], loc='best')

plt.show()