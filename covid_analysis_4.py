import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('covid-variants.csv', index_col='location')

df_1 = df.loc['South Korea']

# print(df_1['date'].drop_duplicates())
df_2 = pd.DataFrame({})
df_2['date'] = df_1['date'].drop_duplicates()
# print(df_2)

new_list = []

for date in df_2['date']:
    mark = (df_1['date'] == date)
    df_1_new = df_1[mark]
    num_sequences_sum = df_1_new['num_sequences'].sum()
    new_list.append(num_sequences_sum)

df_2['num_sequences'] = new_list
# print(df_2)

plt.figure(figsize=(10, 10))
sns.regplot(df_2['date'], df_2['num_sequences'])

plt.xticks(rotation='vertical')

plt.title('South Korea Covid Sum')
plt.xlabel('date')
plt.ylabel('num_sequences_sum')
plt.legend(labels=['South Korea'], loc='best')

plt.show()