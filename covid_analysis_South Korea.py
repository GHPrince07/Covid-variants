import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('covid-variants.csv', index_col='location')

df_1 = df.loc['South Korea']
df_1.set_index(['variant'], inplace=True)
# print(df_1.index)

df_alpha = df_1.loc['Alpha', ['date', 'num_sequences']]
df_omicron = df_1.loc['Omicron', ['date', 'num_sequences']]

fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.plot(df_alpha['date'], df_alpha['num_sequences'])
ax2.plot(df_omicron['date'], df_omicron['num_sequences'])

ax1.legend(loc='best')
ax2.legend(loc='best')

ax1.set_title('Alpha', size=15)
ax2.set_title('Omicron', size=15)

ax1.set_xticklabels(df_alpha['date'], rotation=90)
ax2.set_xticklabels(df_omicron['date'], rotation=90)

plt.show()