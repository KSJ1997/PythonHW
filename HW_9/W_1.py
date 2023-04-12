# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).


import pandas as pd

print('Средняя стоимость дома, где кол-во людей от 0 до 500 (population):')

def main():
    file = pd.read_csv('HW_9\sample_data\california_housing_train.csv')
    print(file[file['population'] <= 500]['median_house_value'].median())


if __name__ == '__main__':
    main()