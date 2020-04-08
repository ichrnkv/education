# estimation of Bernoulli distribution differences

import numpy as np
from scipy import stats


def confidence_interval_95(focus, control):
    n_focus = len(focus)
    n_control = len(control)
    p_focus = sum(focus)/n_focus
    p_control = sum(control)/n_control
    
    lower = p_focus - p_control - np.sqrt(p_control*(1-p_control)/n_control + p_focus*(1-p_focus)/n_focus)
    upper = p_focus - p_control + np.sqrt(p_control*(1-p_control)/n_control + p_focus*(1-p_focus)/n_focus)
    return [round(lower, 4), round(upper, 4)]

def z_stat_bernoulli(focus, control):
    
    n_focus = len(focus)
    n_control = len(control)
    p_focus = sum(focus)/n_focus
    p_control = sum(control)/n_control
    
    P = (p_focus*n_focus + p_control*n_control)/(n_focus + n_control)
    z_stat = (p_focus - p_control)/np.sqrt(P*(1 - P)*(1/n_focus + 1/n_control))
    return z_stat

    
def p_value_z(z_stat, alternative = 'two-sided'):

    if alternative == 'two-sided':
        return 2 * (1 - stats.norm.cdf(np.abs(z_stat)))
    
    if alternative == 'less':
        return stats.norm.cdf(z_stat)

    if alternative == 'greater':
        return 1 - stats.norm.cdf(z_stat)
    
    
if __name__ == '__main__':
    z_stat = z_stat_bernoulli(focus, control)
    print('Сonfidence interval of the conversion difference is {}'.format(confidence_interval_95(focus, control)))
    print('P-value is %.5f' %(p_value_z(z_stat)))
