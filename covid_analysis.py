import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('covid-variants.csv', index_col='location')

df_1 = df.loc['Angola']

plt.figure(figsize=(10, 10))
plt.plot(df_1['date'], df_1['num_sequences'])

plt.xticks(rotation='vertical')

plt.title('Angola')
plt.legend(labels=['Angola'], loc='best')

plt.show()