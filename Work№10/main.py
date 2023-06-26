import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

def one_hot_encoding(data):
    unique_values = list(set(data['whoAmI']))
    for value in unique_values:
        data[value] = (data['whoAmI'] == value).astype(int)
    data.drop('whoAmI', axis=1, inplace=True)
    return data

result = one_hot_encoding(data)
print(result.head())
