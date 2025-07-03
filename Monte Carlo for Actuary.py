import numpy as np
import matplotlib.pyplot as plt

# Simulation Paramters

num_simulations = 5000
num_policies = 250
average_claim = 1200
std_dev_claim = 400

#Run

total_claims = []
for _ in range(num_simulations):
    claims = np.random.normal(loc=average_claim, scale=std_dev_claim, size=num_policies)
    claims = np.maximum(claims, 0) #Remove any negatives
    total_claims.append(np.sum(claims))

#Analyze

reserve_mean = np.mean(total_claims)
reserve_95 = np.percentile(total_claims, 95) #95% CI

print(f"Expected Reserve: ${reserve_mean:,.2f}")
print(f"95% Confidence Reserve: ${reserve_95:,.2f}")

#Graphs

plt.hist(total_claims, bins=50, color='steelblue', edgecolor='white')
plt.axvline(reserve_mean, color='green', linestyle='dashed', label='Mean')
plt.axvline(reserve_95, color='red', linestyle='dashed', label='95% Reserve')
plt.title("Monte Carlo Simulation of Insurance Claims")
plt.xlabel("Total Claim Amount ($)")
plt.ylabel("Frequency")
plt.legend()
plt.show()