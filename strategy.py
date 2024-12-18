import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

# Step 1: Download VOO data
data = yf.download("VOO", start="2011-01-01", end=datetime.today().strftime('%Y-%m-%d'))['Adj Close']

# Function to calculate RMA (Relative Moving Average)
def calculate_rma(values, length):
    rma = np.zeros_like(values)
    rma[length-1] = np.mean(values[:length])  # Initial RMA value
    for i in range(length, len(values)):
        rma[i] = (rma[i - 1] * (length - 1) + values[i]) / length
    return rma

# Function to calculate RSI with RMA smoothing, based on the Pine Script logic
def calculate_rsi(prices, period=4):
    # Convert to a NumPy array to avoid Series indexing warnings
    prices = prices.values if isinstance(prices, pd.Series) else prices
    
    change = np.diff(prices, prepend=prices[0])  # Price changes
    gain = np.where(change > 0, change, 0)       # Positive changes
    loss = np.where(change < 0, -change, 0)      # Negative changes
    
    avg_gain = calculate_rma(gain, period)       # RMA of gains
    avg_loss = calculate_rma(loss, period)       # RMA of losses
    
    rs = avg_gain / (avg_loss + 1e-10)           # Avoid division by zero
    rsi = np.where(avg_loss == 0, 100, np.where(avg_gain == 0, 0, 100 - (100 / (1 + rs))))
    return rsi


# Function to calculate EMA
def calculate_ema(prices, window):
    ema = np.convolve(prices, np.ones(window) / window, mode='valid')
    ema = np.concatenate((np.full(window - 1, np.nan), ema))
    return ema

# Calculate indicators
rsi = calculate_rsi(data, period=4)
ema20 = calculate_ema(data.values, 20)
ema50 = calculate_ema(data.values, 50)

# Step 2: Define the state signal based on RSI and EMA conditions
state_signal = np.zeros(len(data), dtype=int)  # Initialize with zeros (flat)

# Set the state signal to be long (1) from entry to exit conditions
for i in range(1, len(data)):
    if state_signal[i - 1] == 0:  # If flat
        if rsi[i-1] < 30 and ema20[i-1] > ema50[i-1]:
            state_signal[i] = 1  # Enter long
    elif state_signal[i - 1] == 1:  # If already long
        if rsi[i-1] > 55:
            state_signal[i-1] = 1  # Exit long
            state_signal[i] = 0
        else:
            state_signal[i] = 1  # Stay long

# Step 3: Calculate daily returns and apply state signal
returns = data.pct_change().fillna(0)  # Daily returns
strategy_returns = np.where(state_signal == 1, returns, 0)  # Only apply returns when signal is 1
print(strategy_returns[:1000])
# plt.plot(data.index, strategy_returns)
# plt.show()
# Step 4: Calculate the equity curve
equity_curve = (1 + strategy_returns).cumprod() * 10000  # Starting with $10,000

# Plot the equity curve
plt.plot(data.index, equity_curve, label="Equity Curve")
plt.xlabel("Date")
plt.ylabel("Equity ($)")
plt.title("Equity Curve of RSI/EMA Strategy on VOO")
plt.legend()
plt.show()

# Final output
print(f"Final equity from the strategy: ${equity_curve[-1]:.2f}")
