from scipy import stats
import numpy as np
import pandas as pd


def bucketing(df, n=100):
    """
    Splits data into buckets
    """
    # buckets = np.zeros(n)
    buckets = pd.DataFrame()
    for i in range(int(df.shape[0]/n)):
        sample = df.sample(n)
        sample['cohort'] = i
        buckets = pd.concat([buckets, sample])
        df.drop(sample.index)
    return buckets

if __name__ == '__main__':
    
    # generate data
    r = stats.expon.rvs(size=1000000)
    df = pd.DataFrame(r, columns=['value'])
    bucketed_df = bucketing(df, n=1000)
    buckets = bucketed_df.groupby('cohort')['value'].agg(np.mean)
    print('P-value is %4f:' %stats.shapiro(buckets)[1])
    
