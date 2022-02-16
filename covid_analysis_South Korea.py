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

new_list = []
for date in df_2['date']:
    if int(date[0:4]) == 2020:
        a = 0
    elif int(date[0:4]) == 2021:
        a = 365
    b = int(date[5:7])
    c = int(date[8:])
    new_date = a + b*30 + c
    # print(new_date)
    new_list.append(new_date)

df_2['date'] = new_list

plt.figure(figsize=(10, 10))
sns.regplot(x='date', y='num_sequences', data=df_2)
plt.show()