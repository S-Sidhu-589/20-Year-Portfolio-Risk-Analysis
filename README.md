# 20-Year Portfolio Risk Audit: Findings and Projections

This project evaluates the historical performance and future risk characteristics of a 60/40 Balanced Portfolio (60% Stocks, 40% Bonds) compared to a 100% Equity benchmark (S&P 500). The analysis utilizes 20 years of historical data to assess risk-adjusted returns and drawdown mitigation.

### Top-Line Results: 2005 - 2025

| Metric | 100% SPY (Stocks) | 60/40 Strategy | Performance Lead |
| :--- | :--- | :--- | :--- |
| **Annual Return (CAGR)** | 10.38% | 7.68% | 100% SPY |
| **Sharpe Ratio (Efficiency)** | 0.61 | **0.72** | **60/40** |
| **Max Drawdown** | -55.19% | **-34.33%** | **60/40** |

---

## Major Findings

The audit of the 2005–2025 period confirms that the 60/40 portfolio provided significant downside protection during major market contractions.

* **Drawdown Mitigation:** The 60/40 portfolio reduced the maximum drawdown by 20.86 percentage points compared to the S&P 500. This demonstrates the effectiveness of bond allocations in preserving capital during systemic market stress.
* **Risk-Adjusted Performance:** With a Sharpe Ratio of 0.72, the 60/40 strategy proved more efficient than the equity benchmark (0.61), delivering higher returns per unit of volatility.
* **Rebalancing Impact:** Implementing an annual rebalancing schedule maintained the target risk profile and ensured the portfolio did not become over-leveraged toward equities during extended bull markets.

![Equity Curves](Equity%20Curves.png)

---

## Future Risk Projections (Monte Carlo)

A 10,000-iteration simulation was ran to project the growth of a $10,000 investment over a 20-year future market.

* **Median Expected Outcome:** $45,255.57 (A 4.5x multiple on initial investment).
* **Worst-Case Scenario (5th Percentile):** $19,268.14 (Capital remains preserved at nearly 2x the initial principal even in adverse conditions).
* **Probability of Principal Loss:** 0.18%. The statistical likelihood of the portfolio ending below the initial $10,000 investment after 20 years is negligible.

### Monte Carlo: Simulated Growth Paths
![Monte Carlo Paths](Monte%20Carlo.png)

### Histogram: Final Value Distribution
![Histogram](Final%20Distribution%20Histogram.png)

---

## Project Components

* **equity-curve.py**: Conducts historical backtesting from 2005 to 2025 using an annual rebalancing logic.
* **monte_carlo.py**: Runs a 10,000-iteration simulation based on historical daily return distributions to forecast terminal wealth.

## Tools & Libraries
* **Python 3.x**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **YFinance**
