from scipy import stats

def MSbg(*args):
    """Межгруповой средний квадрат"""
    groups = [x for x in args]
    m = len(groups)
    mean = np.mean([item for sublist in groups for item in sublist])
    ssb = 0
    for item in groups:
        ssb +=len(item)*(np.mean(item)-mean)**2
   
    return ssb/(m-1)


def MSwg(*args):
    """Внутригрупповой средний квадрат"""
    groups = [x for x in args]
    N = len([item for sublist in groups for item in sublist])
    m = len(groups)
    ssw = 0
    for sublist in groups:
        sublist_mean = np.mean(sublist)
        for item in sublist:
            ssw+=(item-sublist_mean)**2
            
    return ssw/(N-m)

def f_stat(*args):
    return MSbg(*args)/MSwg(*args)

def p_value_f(f, N, m):
    df1 = m-1 #кол-во степеней свободы 1 (m-1)
    df2 = N-m #кол-во степеней свободы 2 (N-m)
    return 1 - stats.f.cdf(f, df1, df2)


if __name__ == '__main__':
    x, y, x = [2, 2, 3, 9], [1, 4, 9, 8], [4, 12, 0, 9]
    f = f_stat(x, y, z)
    p_value = p_value_f(f, 12, 4)
    print('P-value is: %.4f' % p_value)
    print(p_value)
