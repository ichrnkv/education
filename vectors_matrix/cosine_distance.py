import numpy as np
from scipy.spatial import distance

def cosine_distance(x, y):
    """
    Cosine distance between x and y
    :param x: vector, numpy array
    :param y: vector, numpy array
    """
    
    norm_x = np.sqrt(np.sum(x*x))
    norm_y = np.sqrt(np.sum(y*y))
    
    return 1-(np.dot(x, y))/(norm_x*norm_y)
    
    
if __name__ == '__main__':
    x = np.array([2, -1, -2])
    y = np.array([0, 2, 4])
    print(f'Cosine distance between x and y is {cosine_distance(x, y)}')
    
    # scipy way
    print(f'Cosine distance between x and y is {distance.cosine(x, y)}')
    
