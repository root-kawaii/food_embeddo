
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import sys
import matplotlib.pyplot as plt
import seaborn as sns

# df = pd.read_csv(
#     '/Users/root-kawaii/Downloads/archive/RAW_recipes.csv')
# df[['calories', 'total fat (PDV)', 'sugar (PDV)', 'sodium (PDV)', 'protein (PDV)',
#     'saturated fat (PDV)', 'carbohydrates (PDV)']] = df.nutrition.str.split(",", expand=True)
# df['calories'] = df['calories'].apply(lambda x: x.replace('[', ''))
# df['carbohydrates (PDV)'] = df['carbohydrates (PDV)'].apply(
#     lambda x: x.replace(']', ''))
# df[['calories', 'total fat (PDV)', 'sugar (PDV)', 'sodium (PDV)', 'protein (PDV)', 'saturated fat (PDV)', 'carbohydrates (PDV)']] = df[[
#     'calories', 'total fat (PDV)', 'sugar (PDV)', 'sodium (PDV)', 'protein (PDV)', 'saturated fat (PDV)', 'carbohydrates (PDV)']].astype('float')
# df.drop(['id', 'contributor_id', 'submitted',
#         'tags', 'nutrition'], axis=1, inplace=True)

# df['food types'] = np.nan
# df['food types'] = df['food types'].astype('str')


# df['ingredients'] = df['ingredients'].apply(lambda x: x.replace('[', ''))
# df['ingredients'] = df['ingredients'].apply(lambda x: x.replace(']', ''))
# df['ingredients'] = df['ingredients'].apply(lambda x: x.replace('\'', ''))

# df.to_csv('somePP.csv')


df = pd.read_csv('somePP.csv')


ingredient_set = {'salt'}


for i in range(len(df)):
    iter1 = df.iloc[i]['ingredients'].split(',')
    for j in iter1:
        if (j[0] == ' '):
            ingredient_set.add(j[1:])
        else:
            ingredient_set.add(j)
