from scipy import stats
from itertools import combinations
import random


def get_random_example(X, n):
    """Gets random example from X with size of n"""
    idx = [random.randrange(0, len(X), 1) for i in range(n)]
    return [X[i] for i in idx]

def get_multiple_examples(X, m, n):
    """Gets N of random examples with size of n"""
    examples = list()
    for item in range(m):
        examples.append(get_random_example(X,n))
    return examples

def t_stat(x, y):
    x_mean, y_mean = np.mean(x), np.mean(y)
    sd1, sd2 = np.std(x), np.std(y)
    n1, n2 = len(x), len(y)
    se = np.sqrt(sd1**2/n1+sd2**2/n2)
    return (x_mean-y_mean)/se


def p_value_t_pair(t_stat, x, y, alternative='two-sided'):
    df = len(x)+len(y)-2 # degrees of freedom
    if alternative == 'two-sided':
        return 2*(1-stats.t.cdf(np.abs(t_stat),df))
    if alternative == 'less':
        return stats.t.cdf(t_stat, df)
    if alternative == 'greater':
        return 1 - stats.t.cdf(t_stat, df)
    
    
def false_alarm(X, m, n, alpha=0.5):
    samples = [get_multiple_examples(X, m, n) for i in range(1000)]
    pairs = [list(combinations(x, 2)) for x in samples]
    
    p_stats = []
    for subset in pairs:
        subset_stat = []
        for pair in subset:
            t = t_stat(pair[0], pair[1])
            p_val = p_value_t_pair(t, pair[0], pair[1], alternative='two-sided')
            subset_stat.append(p_val)
        p_stats.append(subset_stat)
        print('{} pairs passed'.format(idx+1), end='\r')
    return p_stats

if __name__ == '__main__':
    
    # generate big sample from normal distibution
    r = np.random.normal(0,1,5000)
    p_stats = false_alarm(r, 20, 30)
    p_results = [1 if any(x < 0.05 for x in item) else 0 for item in p_stats]
    print('Part of false alarmed is %.4f' % (sum(p_results)/len(p_results)))
