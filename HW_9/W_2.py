# Задача 42: Узнать какая максимальная households в зоне минимального значения population.


import pandas as pd

print('Максимальная households в зоне минимального значения population:')

def main():
    f = pd.read_csv('HW_9\sample_data\california_housing_train.csv')
    print(f[f['population'] == f['population'].min()]['households'].max()

if __name__ == '__main__':
    main()