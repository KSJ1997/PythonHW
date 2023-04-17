# Задание 44
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one_hot вид.

import random
import numpy as np
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})
lst = pd.DataFrame({'whoAmI': data['whoAmI'].unique()})

for i, integer_encoded in enumerate(lst['whoAmI']):
    data[integer_encoded] = np.where(data['whoAmI'] == integer_encoded, 0, 1)

print(data.head(5))