import numpy as np
from scipy.stats import norm

class BlackScholesModel:
    def european_BS(t, St, K, T, r, sigma, option='call'):
         d1 = ((np.log(St / K) + (r + 0.5 * sigma**2) * (T - t))) / (sigma * np.sqrt(T - t))
         d2 = d1 - sigma * np.sqrt(T - t)
    
         if option=='call':
              return St * norm.cdf(d1) - K * np.exp(-r * (T - t)) * norm.cdf(d2)
         elif option=='put':
              return K * np.exp(-r * (T - t)) * norm.cdf(-d2) - St * norm.cdf(-d1)
         else:
              raise ValueError("Option type must be either call or put")

