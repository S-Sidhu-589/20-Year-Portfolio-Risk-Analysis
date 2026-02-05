import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# -----------------------------
# 1. PARAMETERS
# -----------------------------
tickers = ["SPY", "AGG"]
weights = np.array([0.6, 0.4])
start_date = "2005-01-01" # 20 years of history
end_date = "2025-01-01"
n_simulations = 10000     # Institutional standard
n_years = 20              # 20-year future look
initial_investment = 10000 

print(f"FETCHING HISTORICAL DATA FOR {tickers}...")

# -----------------------------
# 2. DOWNLOAD & PREP DATA
# -----------------------------
data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)["Close"]
data = data[tickers] # Ensure columns match weights order
returns = data.pct_change().dropna()

# Calculate the historical 60/40 daily returns
portfolio_returns = returns @ weights

print(f"SIMULATING {n_years} YEARS INTO THE FUTURE...")

# -----------------------------
# 3. MONTE CARLO (BOOTSTRAP METHOD)
# -----------------------------
n_days = 252 * n_years
simulated_paths = np.zeros((n_days, n_simulations))

for i in range(n_simulations):
    # Bootstrapping: Sampling from 20 years of REAL market days
    random_samples = np.random.choice(portfolio_returns, size=n_days, replace=True)
    simulated_paths[:, i] = initial_investment * (1 + random_samples).cumprod()

# -----------------------------
# 4. CALCULATE STATS
# -----------------------------
final_values = simulated_paths[-1]
median_final = np.median(final_values)
worst_5pct = np.percentile(final_values, 5)
best_5pct = np.percentile(final_values, 95)
prob_loss = np.mean(final_values < initial_investment)

# -----------------------------
# 5. VISUALIZATION (TWO SUBPLOTS)
# -----------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# --- Plot 1: Future Growth Paths ---
ax1.plot(simulated_paths[:, :100], color="gray", alpha=0.1) # Sample paths
ax1.plot(np.median(simulated_paths, axis=1), color="blue", linewidth=3, label="Median Path")
ax1.plot(np.percentile(simulated_paths, 5, axis=1), color="red", linestyle="--", label="Worst 5% Scenario")
ax1.set_title(f"Monte Carlo: 20-Year Growth Paths of ${initial_investment:,.0f}")
ax1.set_xlabel("Trading Days")
ax1.set_ylabel("Portfolio Value ($)")
ax1.legend()
ax1.grid(True, alpha=0.3)

# --- Plot 2: Terminal Value Histogram (CLEAN BLUE & FIXED SCALE) ---
ax2.hist(final_values, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
ax2.axvline(initial_investment, color='red', linestyle='--', label='Initial Investment')
ax2.axvline(median_final, color='blue', linewidth=2, label=f'Median: ${median_final:,.0f}')

# Set x-axis limit to 250k to remove extreme outliers and improve readability
ax2.set_xlim(0, 250000) 

ax2.set_title("Distribution of Final Values (Year 20)")
ax2.set_xlabel("Ending Dollar Amount ($)")
ax2.set_ylabel("Frequency")
ax2.legend()

plt.tight_layout()
plt.show()

# -----------------------------
# 6. CONSOLE OUTPUT
# -----------------------------
print("-" * 35)
print(f"AUDIT RESULTS AFTER {n_years} YEARS")
print("-" * 35)
print(f"Median Expected Outcome:  ${median_final:,.2f}")
print(f"Worst-Case (5th Pct):     ${worst_5pct:,.2f}")
print(f"Best-Case (95th Pct):      ${best_5pct:,.2f}")
print(f"Probability of Principal Loss: {prob_loss * 100:.2f}%")
print("-" * 35)
