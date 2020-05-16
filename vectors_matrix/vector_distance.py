import math
import numpy as np
from scipy.spatial import distance


def euclidean_distance(x, y):
    """
    Euclidean distance of 2 vectors
    :param x: vector, list of numbers
    :param y: vector, list of numbers
    """
    if len(x) != len(y):
        raise ValueError('Length of vectors is not the same')
    else:
        t = []
        for i in range(len(x)):
            t.append((x[i]-y[i])**2)
        t = sum(t)
        return np.sqrt(t)
    
    
def manhattan_distance(x, y):
    """
    Manhattan distance of 2 vectors
    :param x: vector, list of numbers
    :param y: vector, list of numbers
    """
    if len(x) != len(y):
        raise ValueError('Length of vectors is not the same')
    else:
        t = []
        for i in range(len(x)):
            t.append(abs(x[i]-y[i]))
        t = sum(t)
        return t


if __name__ == '__main__':
    x = [2, -1, -2]
    y = [0, 2, 4]
    print(f'Euclidean distance between x and y is {euclidean_distance(x, y)}')
    print(f'Manhattan distance between x and y is {manhattan_distance(x, y)}')
    
    # scipy way
    x = np.array(x)
    x = x.reshape(1, x.shape[0])
    y = np.array(y)
    y = y.reshape(1, y.shape[0])
    
    eucl_d = distance.cdist(x, y, metric='euclidean')[0][0]
    manh_d = distance.cdist(x, y, metric='cityblock')[0][0]
    
    print(f'Euclidean distance between x and y is {eucl_d}')
    print(f'Manhattan distance between x and y is {manh_d}')
