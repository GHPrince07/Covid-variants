import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('covid-variants.csv', index_col='location')

df_1 = df.loc['South Korea']
df_1.set_index(['variant'], inplace=True)
print(df_1.index)

df_alpha = df_1.loc['Alpha', ['date', 'num_sequences']]
df_beta = df_1.loc['Beta', ['date', 'num_sequences']]
df_delta = df_1.loc['Delta', ['date', 'num_sequences']]
df_omicron = df_1.loc['Omicron', ['date', 'num_sequences']]
df_nonwho = df_1.loc['non_who', ['date', 'num_sequences']]

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(1,1,1)

ax.plot(df_alpha['date'], df_alpha['num_sequences'], label='Alpha')
ax.plot(df_beta['date'], df_beta['num_sequences'], label='Beta')
ax.plot(df_delta['date'], df_delta['num_sequences'], label='Delta')
ax.plot(df_omicron['date'], df_omicron['num_sequences'], label='Omicron')
ax.plot(df_nonwho['date'], df_nonwho['num_sequences'], label='non_who')

ax.legend(loc='best')

ax.set_title('Covid-19 variants in South Korea', size=15)

ax.set_xlabel('date', size=12)
ax.set_ylabel('num_sequences', size=12)
ax.set_xticklabels(df_alpha['date'], rotation=90)

plt.show()