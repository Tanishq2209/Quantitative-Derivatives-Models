import numpy as np

class CRRModel:
    def CRR_Stock(self, S0, r, sigma, T, M):
        delta_t = T / M
        beta = (np.exp(-r*delta_t)+np.exp((r+(sigma)**2)*delta_t)) / 2
        u = beta + np.sqrt(beta**2 - 1)
        d = 1 / u

        S = np.empty((M + 1, M + 1))
        for i in range(M + 1):
            for j in range(i + 1):
                S[j, i] = S0 * (u**j) * (d**(i-j))
        return S
  
    def CRR_Option(self, S0, r, sigma, T, M, K, option_type='call', option_style='European'):
        delta_t = T / M
        beta = (np.exp(-r*delta_t)+np.exp((r+(sigma)**2)*delta_t)) / 2
        u = beta + np.sqrt(beta**2 - 1)
        d = 1 / u
        q = (np.exp(r * delta_t) - d) / (u - d)
        
        S = np.zeros((M + 1, M + 1))
        for i in range(M + 1):
            for j in range(i + 1):
                S[j, i] = S0 * (u**j) * (d**(i-j))
        
        V = np.zeros((M + 1, M + 1))
        for j in range(M + 1):
            if option_type == 'call':
                V[j, M] = max(0, S[j, M] - K)
            else:
                V[j, M] = max(0, K - S[j, M])
        
        # Backward induction
        for i in range(M - 1, -1, -1):
            for j in range(i + 1):
                if option_style == 'European':
                    V[j, i] = np.exp(-r * delta_t) * (q * V[j+1, i+1] + (1-q) * V[j, i+1])
                else:  # American
                    if option_type == 'call':
                        exercise = max(0, S[j, i] - K)
                    else:
                        exercise = max(0, K - S[j, i])
                    hold = np.exp(-r * delta_t) * (q * V[j+1, i+1] + (1-q) * V[j, i+1])
                    V[j, i] = max(exercise, hold)
        
        return V
