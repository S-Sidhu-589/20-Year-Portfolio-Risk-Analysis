import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# 1. Setup - 20 Years of Data (2005-2025)
tickers = ["SPY", "AGG"]
weights = np.array([0.6, 0.4])

print("Downloading historical data...")
data = yf.download(tickers, start="2005-01-01", end="2025-01-01", auto_adjust=True)["Close"]
data = data[["SPY", "AGG"]] 

# 2. Rebalancing Logic
portfolio_values = []
current_equity = 1.0
units = (current_equity * weights) / data.iloc[0]

for date, prices in data.iterrows():
    current_value = (units * prices).sum()
    portfolio_values.append(current_value)
    
    # Rebalance every January
    if date.month == 1 and date.day <= 7:
        units = (current_value * weights) / prices

p6040_equity = pd.Series(portfolio_values, index=data.index)
spy_equity = (1 + data["SPY"].pct_change().dropna()).cumprod()

# 3. Performance Stats Function
def get_stats(equity, name):
    rets = equity.pct_change().dropna()
    total_years = len(equity) / 252
    cagr = (equity.iloc[-1] / equity.iloc[0]) ** (1 / total_years) - 1
    mdd = (equity / equity.cummax() - 1).min()
    vol = rets.std() * np.sqrt(252)
    sharpe = (rets.mean() * 252) / vol
    print(f"--- {name} ---")
    print(f"CAGR: {cagr:.2%} | Sharpe: {sharpe:.2f} | Max DD: {mdd:.2%}\n")

get_stats(spy_equity, "100% SPY")
get_stats(p6040_equity, "60/40 Rebalanced")

# 4. Visualization with Solid Colors
plt.figure(figsize=(12, 6))

# Dark Blue and Medium Green as requested
plt.plot(spy_equity, label="100% SPY", color="blue", linewidth=1.5)
plt.plot(p6040_equity, label="60/40 Rebalanced", color="limegreen", linewidth=2)



plt.title("Portfolio Performance: 20-Year Historical Backtest", fontsize=14)
plt.ylabel("Growth of $1")
plt.xlabel("Year")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
