# Sketching Algorithm for Kendall Tau's Rank Correlation

Kendall’s tau is a measure of rank correlation between two list of rank vectors. This metric can be calculated in `O(n log(n))`, which can be slow when used in pairwise comparisons in tasks like clustering. There is an approximated way to calculate it in constant time, which is described in the work [*"Sketching Algorithms For Approximating Rank Correlations In Collaborative Filtering Systems"*](https://www.microsoft.com/en-us/research/wp-content/uploads/2009/01/SketchKendall2.pdf). I also include a write up in the repo to simplify the descriptions.

## Usage
Just clone the package and put `sketch.py` to your working directory.

    from sketch import KTSketch
    
    x1 = [1,3,2,4,5]
    x2 = [3,2,1,5,4]
    
    epsilon = 0.05     	#accuracy as the abs. error <= epsilon
    CI = 0.95          	#confidence interval as P(abs. error <= epsilon) >= CI
    dimension = 5 		#size of vector
    
    ktsketch = KTSketch(epsilon=epsilon,CI=CI,dim=dimension,seed=0)
    ktsketch.correlation(x1,x2)
