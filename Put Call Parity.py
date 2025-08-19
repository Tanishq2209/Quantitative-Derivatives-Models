# Defining sigmas that contains 500 equally spaced values between 0.01 and 5
sigmas = np.linspace(0.01, 5, 500)

K = 100
def g_call(S):
    return np.maximum(S - K, 0)  

def g_put(S):
    return np.maximum(K - S, 0)  

# Defining call_prices_CRR and put_prices_CRR of length 500
call_prices_CRR = np.zeros(500)
put_prices_CRR = np.zeros(500)

M=100
# Fill the arrays with call and put prices for each sigma
for i in range(len(sigmas)):
    sigma = sigmas[i]
    call_prices_CRR[i] = european_CRR(g_call, S0, T, r, sigma, M)
    put_prices_CRR[i] = european_CRR(g_put, S0, T, r, sigma, M)

print("Last 10 Call Option Prices:", call_prices_CRR[-10:])
print("Last 10 Put Option Prices:", put_prices_CRR[-10:])


# Define no-arbitrage bounds
lower_bound_call = S0 - K * np.exp(-r * T)
upper_bound_call = S0

# Plot call prices vs. volatility
plt.plot(sigmas, call_prices_CRR, label='Call Option Price (CRR)', color='blue')
plt.axhline(lower_bound_call, linestyle='--', color='black', label='Lower Bound')
plt.axhline(upper_bound_call, linestyle='--', color='black', label='Upper Bound')
plt.xlabel('Volatility (σ)')
plt.ylabel('Call Option Price')
plt.title('Call Option Prices vs. Volatility')
plt.legend()
plt.grid(alpha=0.3)
plt.show()



# Define no-arbitrage bounds
lower_bound_put = 0
upper_bound_put = K * np.exp(-r * T)

# Plot put prices vs. volatility
plt.plot(sigmas, put_prices_CRR, label='Put Option Price (CRR)', color='blue')
plt.axhline(lower_bound_put, linestyle='--', color='black', label='Lower Bound')
plt.axhline(upper_bound_put, linestyle='--', color='black', label='Upper Bound')
plt.xlabel('Volatility (σ)')
plt.ylabel('Put Option Price')
plt.title('Put Option Prices vs. Volatility')
plt.legend()
plt.grid(alpha=0.3)
plt.show()



# Verifying the put-call parity by plotting the difference 
put_call_parity_diff = call_prices_CRR - put_prices_CRR - (S0 - K * np.exp(-r * T))

# Plotting put-call parity difference vs. Volatility
plt.plot(sigmas, put_call_parity_diff, color='purple', label='Put-Call Parity Difference')
plt.xlabel('Volatility (σ)')
plt.title('Put-Call Parity Verification')
plt.legend()
plt.grid(alpha=0.3)
plt.show()