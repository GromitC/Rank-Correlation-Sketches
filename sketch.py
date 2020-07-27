import math
import numpy as np
import itertools

#Condensed index to indices from https://stackoverflow.com/a/36867493
def calc_row_idx(k, n):
    return int(math.ceil((1/2.) * (- (-8*k + 4 *n**2 -4*n - 7)**0.5 + 2*n -1) - 1))

def elem_in_i_rows(i, n):
    return i * (n - 1 - i) + (i*(i + 1))//2

def calc_col_idx(k, i, n):
    return int(n - elem_in_i_rows(i + 1, n) + k)

def condensed_to_square(k, n):
    i = calc_row_idx(k, n)
    j = calc_col_idx(k, i, n)
    return [i, j]

class KTSketch():
    def __init__(self,epsilon=0.05,CI=0.95,dim=1000,seed=0):
        
        assert 0 < epsilon <= 1, "epsilon should be in the range of (0,1]"
        assert 0 <= CI < 1, "CI should be in the range of [0,1)"
        
        np.random.seed(seed)
        self.nTrials = math.ceil(2 * np.log( 2 / (1 - CI) ) / (epsilon * epsilon))
        idx = np.random.randint(dim * (dim - 1) / 2, size=self.nTrials)
        self.dim = dim
        self.sketch = np.array([condensed_to_square(i,dim) for i in idx])
        
    def correlation(self,a,b):
        
        a = np.array(a)
        b = np.array(b)
        
        assert a.shape == b.shape, "dimension of two arrays should be equal"
        assert a.shape[0] == self.dim, "dimension not equal to initialization"
        
        i = self.sketch[:,0]
        j = self.sketch[:,1]
        concordant_pairs = np.sum(np.sign(a[i] - a[j]) * np.sign(b[i] - b[j]) > 0)
        p_c = concordant_pairs / self.nTrials
        
        return 2 * p_c - 1
        
        