import numpy as np
import pandas as pd


def descriptive_stat(sample):
    """
    Выводит описательную статистику:
    - мат. ожидание
    - дисперсия
    - стандартное отклонение
    - коэффициент вариации
    """
    print('Mean value is ', round(np.mean(sample),2))
    print('Variance is ', round(np.var(sample),2))
    print('St. deviation is ', round(np.std(sample),2))
    print('Variance coef is ', round(np.var(sample)/np.mean(sample),2))
    
    
if __name__ == '__main__':
    # чтение данных
    data = pd.read_csv('data/cars.csv', sep = ';')

    # сравним мощность Ауди и БМВ 

    audi = data[data['Make']=='Audi']['Horsepower'].values
    bmw = data[data['Make']=='BMW']['Horsepower'].values
    
    print('Audi stats: ')
    descriptive_stat(audi)
    
    print('================================')
    
    print('BMW stats: ')
    descriptive_stat(bmw)
