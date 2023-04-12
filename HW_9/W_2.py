# Задача 42: Узнать какая максимальная households в зоне минимального значения population.


import pandas as pd

print('Максимальная households в зоне минимального значения population:')

def main():
    file = pd.read_csv('HW_9\sample_data\california_housing_train.csv')
    print(file[file['population'] == file['population'].min()]
          ['households'].max())

if __name__ == '__main__':
    main()