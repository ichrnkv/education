# exp size for boolean metrics

from statsmodels.stats.power import zt_ind_solve_power
import scipy.stats as stats

def min_sample_size(bcr, mde, power=0.8, sig_level=0.05):
    """Returns the minimum sample size to set up a split test
    Arguments:
        bcr (float): probability of success for control, sometimes
        referred to as baseline conversion rate
        mde (float): minimum change in measurement between control
        group and test group if alternative hypothesis is true, sometimes
        referred to as minimum detectable effect
        power (float): probability of rejecting the null hypothesis when the
        null hypothesis is false, typically 0.8
        sig_level (float): significance level often denoted as alpha,
        typically 0.05
    Returns:
        min_N: minimum sample size (float)
    References:
        Stanford lecture on sample sizes
        http://statweb.stanford.edu/~susan/courses/s141/hopower.pdf
    """
    # standard normal distribution to determine z-values
    standard_norm = stats.norm(0, 1)

    # find Z_beta from desired power
    Z_beta = standard_norm.ppf(power)

    # find Z_alpha
    Z_alpha = standard_norm.ppf(1-sig_level/2)

    # average of probabilities from both groups
    pooled_prob = (bcr + bcr + mde) / 2

    min_N = (2 * pooled_prob * (1 - pooled_prob) * (Z_beta + Z_alpha)**2 / mde**2)

    return min_N


if __name__ == '__main__':
    print('Sample size for exp: {}'.format(min_sample_size(bcr=0.05, mde=0.01, power=0.99)))
    
    # statsmodels way
    eff_size = 0.01/np.sqrt(0.05*(1-0.05))
    print('Sample size for exp: {}'.format(zt_ind_solve_power(effect_size=eff_size,
                                                              nobs1=None, alpha=0.05, power=0.99, ratio=1.0, alternative='two-sided')))
