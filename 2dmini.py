import numpy as np
from scipy.optimize import minimize
def f(x): #define the function to minimize
    return 7*x[0] - 5*np.sin(x[1])
x0 = np.array([0, 0]) #define the starting point for the algo
res = minimize(f, x0) #finds the minimization of the function
print(res) #print the results
