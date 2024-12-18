# mrld-VOO

Welcome to the Mean Reversion Long Daily strategy for VOO #mrld-VOO repository! This is an open-source trading strategy designed to identify profitable opportunities in the market using a combination of the Relative Strength Index (RSI) and Exponential Moving Averages (EMA). The strategy is applied to the VOO ETF and can be automated on platforms like Alpaca.

---

## Strategy Overview

### Key Indicators
1. **Relative Strength Index (RSI)**
   - A momentum oscillator that measures the speed and change of price movements.
   - Smoothed using the Relative Moving Average (RMA) for accurate signals.

2. **Exponential Moving Averages (EMA)**
   - EMA20 (20-day EMA) and EMA50 (50-day EMA) are used to identify trends and entry/exit points.

### Signal Logic
- **Long Entry:** RSI < 30 and EMA20 > EMA50.
- **Exit Long:** RSI > 55.
- **Flat:** Default state when no conditions are met.

### Backtesting and Performance
- Daily returns are calculated based on the state signal.
- An equity curve is generated to visualize the strategy's performance starting with $10,000.

---

## Installation and Usage

### Prerequisites
Ensure you have the following Python libraries installed:
- `numpy`
- `pandas`
- `yfinance`
- `matplotlib`

Install missing dependencies with:
```bash
pip install numpy pandas yfinance matplotlib
```

### Running the Strategy
1. Clone the repository:
   ```bash
   git clone https://github.com/LibreTrading/mrld-VOO.git
   cd mrld-VOO
   ```

2. Run the Python script:
   ```bash
   python mrld_voo_strategy.py
   ```

The script will:
- Download historical price data for VOO.
- Calculate RSI, EMA20, EMA50, and the state signal.
- Generate a plot of the equity curve and other relevant metrics.

---

## Features
- **Indicator Calculation:** Calculates RSI using RMA smoothing and EMA trends.
- **Signal Logic:** Implements logic for entry and exit based on market conditions.
- **Visualization:** Plots RSI, EMA trends, state signals, and the equity curve.
- **Performance Metrics:** Calculates and displays final equity after backtesting.

---

## Contributions
We welcome contributions from the community! Feel free to:
- Open issues for bugs or feature requests.
- Submit pull requests to improve the strategy or code quality.

---

## Support
If you need help automating this strategy, reach out to our friends at [Plutarco](https://plutarco.tech) or visit [LibreTrading.org](https://libretrading.org) for more resources.

---

## License
This project is open-source under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Donations
Support the LibreTrading community by contributing to the project. Every donation helps us continue to develop and share open-source trading tools.

Thank you for being part of the LibreTrading community!
