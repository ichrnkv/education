import numpy as np
from scipy import stats

def t_stat(x, y):
    x_mean, y_mean = np.mean(x), np.mean(y)
    sd1, sd2 = np.std(x), np.std(y)
    n1, n2 = len(x), len(y)
    se = np.sqrt(sd1**2/n1+sd2**2/n2)
    return (x_mean-y_mean)/se


def p_value_t_pair(t_stat, x, y, alternative = 'two-sided'):
    df = len(x)+len(y)-2 # degrees of freedom
    if alternative == 'two-sided':
        return 2*(1-stats.t.cdf(np.abs(t_stat),df))
    if alternative == 'less':
        return stats.t.cdf(t_stat, df)
    if alternative == 'greater':
        return 1 - stats.t.cdf(t_stat, df)

    
if __name__ == '__main__':
    
    h1 = np.random.normal(185, 10, size=10000)
    h2 = np.random.normal(200, 10, size=10000)
    
    t = t_stat(h1, h2)
    p_value = p_value_t_pair(t, h1, h2, alternative='two-sided')
    print('P-value is {}'.format(p_value))
    
    # inbox way
    p_value_ = stats.ttest_ind(h1, h2)[1]
    print('P-value is {}'.format(p_value_))
