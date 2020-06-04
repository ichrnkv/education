# http://www.nickart.spb.ru/clause/text_17.php
# https://paperity.org/p/87955319/sample-size-determination

import numpy as np
from statsmodels.stats.power import tt_ind_solve_power


def get_min_sample_size_for_non_binomial_metrics(sd, mde, C=10.51):
    """
    Sample size for non binomial metrics expetiment
    :param sd: standart deviation
    :param mde: minimum detectable effect
    :param C: C
    """
    n = 1 + (2 * C) * ((sd / mde) ** 2)
    return n
    
    
if __name__ == '__main__':
    # minimum detectable effect
    mde = 1

    # some random values for example
    values = np.random.randint(10, 20, 100)

    # nobs - sa,ple size for one group
    nobs = get_min_sample_size_for_non_binomial_metrics(sd=np.std(values), mde=mde, C=10.51)
    print(int(nobs))
    
    # statsmodels way
    eff_size = mde/np.std(values) # normalized effect size
    nobs = tt_ind_solve_power(effect_size=eff_size, nobs1=None, alpha=0.05, power=0.9, ratio=1.0, alternative='two-sided')
    print(int(nobs))
