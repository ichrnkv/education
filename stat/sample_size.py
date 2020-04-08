import math
 
# confidence intervals: 50%, 68%, 90%, 95%, and 99%
confidence_level_constant = [50,.67], [68,.99], [90,1.64], [95,1.96], [99,2.57]
 

def sample_size(population_size, confidence_level, confidence_interval):
    """
   calculation of sample size
    """
    Z = 0.0
    p = 0.5
    e = confidence_interval/100.0
    N = population_size
    n_0 = 0.0
    n = 0.0

    # calculation of sigma deviation
    for i in confidence_level_constant:
        if i[0] == confidence_level:
            Z = i[1]

    if Z == 0.0:
        return -1

    # sample size calculation
    n_0 = ((Z**2) * p * (1-p)) / (e**2)
    n = n_0 / (1 + ((n_0 - 1) / float(N)) )

    return int(math.ceil(n)) 


def main():
    sample_sz = 0
    population_sz = 60162
    confidence_level = 99.0
    confidence_interval = 5.0
 
    sample_sz = sample_size(population_sz, confidence_level, confidence_interval)
 
    print("Sample size is: %d" % sample_sz)
    
    
if __name__ == '__main__':
    main()
