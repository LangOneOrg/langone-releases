# Tutorial 09: Advanced Analytics and Statistics

## 🎯 **Learning Objectives**

- ✅ Perform time series analysis and forecasting (ARIMA)
- ✅ Conduct hypothesis testing and statistical analysis
- ✅ Process signals with FFT and filtering
- ✅ Calculate financial metrics (VaR, Sharpe ratio)
- ✅ Build complete analytical pipelines

**⏱️ Estimated Time**: 90 minutes | **Prerequisites**: Tutorials 01-07 | **Difficulty**: ⭐⭐⭐⭐☆ Advanced

---

## 📚 **Introduction: Advanced Analytics**

Move beyond basic statistics to professional-grade analysis:
- **📈 Time Series**: Forecast future values
- **📊 Statistics**: Hypothesis testing, distributions
- **🎵 Signal Processing**: FFT, filtering, spectral analysis
- **💰 Finance**: Risk metrics, portfolio optimization

---

## 📈 **Part 1: Time Series Analysis**

### **Basic Time Series**

```l1
# Initialize analytics system
let analytics = analytics_init()

# Time series data (monthly sales)
let sales = array([100, 120, 135, 148, 160, 175, 190, 210, 225, 240, 255, 270])

# Analyze time series
let ts_analysis = analyze_time_series(sales)
print("Time Series Analysis:")
print(ts_analysis)
```

### **ARIMA Modeling**

```l1
# Fit ARIMA model
# Parameters: p (autoregressive), d (differencing), q (moving average)
let arima_model = arima_fit(sales, 1, 1, 1)
print("ARIMA(1,1,1) model fitted")

# Forecast next 3 periods
let forecast = arima_forecast(arima_model, 3)
print("Forecast for next 3 months:")
print(forecast)
```

---

### **🔨 Exercise 1: Stock Price Forecasting**

```l1
# Historical stock prices for 12 months
# 1. Fit ARIMA model
# 2. Forecast next 3 months
# 3. Calculate forecast confidence intervals
```

<details>
<summary>💡 Solution</summary>

```l1
# Stock Price Forecasting

print("=== Stock Price Forecasting ===")
print("")

# Historical data (12 months)
let prices = array([100, 102, 105, 103, 108, 112, 110, 115, 120, 118, 125, 130])

print("Historical Prices (12 months):")
print(prices)
print("")

# Fit ARIMA model
print("Fitting ARIMA(1,1,1) model...")
let model = arima_fit(prices, 1, 1, 1)
print("Model fitted successfully")
print("")

# Forecast next 3 months
let forecast = arima_forecast(model, 3)
print("Forecast for next 3 months:")
for i in range(0, len(forecast)):
    print("Month " + to_string(i + 13) + ": $" + to_string(forecast[i]))
end
print("")

# Calculate trend
let trend = (prices[-1] - prices[0]) / len(prices)
print("Average monthly trend: $" + to_string(trend))
```
</details>

---

## 📊 **Part 2: Statistical Analysis**

### **Descriptive Statistics**

```l1
# Calculate comprehensive statistics
let data = array([12, 15, 18, 20, 22, 25, 28, 30, 32, 35])

let stats = calculate_statistics(data)
print("Descriptive Statistics:")
print("Mean:", stats.mean)
print("Median:", stats.median)
print("Std Dev:", stats.std_dev)
print("Variance:", stats.variance)
```

### **Hypothesis Testing**

```l1
# T-test: Compare two groups
let group1 = array([23, 25, 27, 22, 24, 26, 23, 25])  # Control group
let group2 = array([28, 30, 32, 29, 31, 33, 30, 32])  # Treatment group

let t_result = t_test(group1, group2, 0.05)  # 5% significance level
print("T-test Results:")
print("P-value:", t_result.p_value)
print("Significant:", t_result.is_significant)

if (t_result.is_significant) {
    print("The groups are significantly different!")
} else {
    print("No significant difference found")
}
```

---

### **🔨 Exercise 2: A/B Test Analysis**

```l1
# Analyze A/B test results:
# Control group (old design): conversion rates
# Treatment group (new design): conversion rates
# Determine if new design is better
```

<details>
<summary>💡 Solution</summary>

```l1
# A/B Test Analysis

print("=== A/B Test: Website Redesign ===")
print("")

# Conversion rates (percentage)
let control_conversions = array([2.1, 2.3, 2.0, 2.2, 2.4, 2.1, 2.3, 2.2])
let treatment_conversions = array([2.8, 3.0, 2.9, 3.1, 3.2, 2.9, 3.0, 3.1])

print("Control Group (Old Design):")
let control_stats = calculate_statistics(control_conversions)
print("Mean conversion: " + to_string(control_stats.mean) + "%")
print("Std Dev: " + to_string(control_stats.std_dev) + "%")
print("")

print("Treatment Group (New Design):")
let treatment_stats = calculate_statistics(treatment_conversions)
print("Mean conversion: " + to_string(treatment_stats.mean) + "%")
print("Std Dev: " + to_string(treatment_stats.std_dev) + "%")
print("")

# Perform t-test
let result = t_test(control_conversions, treatment_conversions, 0.05)
print("Statistical Test:")
print("Difference: +" + to_string(treatment_stats.mean - control_stats.mean) + "%")
print("P-value: " + to_string(result.p_value))

if (result.is_significant) {
    print("✓ Result: SIGNIFICANT - New design performs better!")
    print("Recommendation: Deploy new design")
} else {
    print("✗ Result: NOT SIGNIFICANT - Keep testing")
}
```
</details>

---

## 🎵 **Part 3: Signal Processing**

### **FFT (Fast Fourier Transform)**

```l1
# Generate signal
let sample_rate = 1000  # Hz
let duration = 1.0      # seconds
let t = linspace(0, duration, sample_rate * duration)

# Composite signal: 50Hz + 120Hz
let signal = sin(2 * 3.14159 * 50 * t) + sin(2 * 3.14159 * 120 * t)

# Perform FFT
let fft_result = fft(signal)
print("FFT complete")
print("Frequency components detected:")
print("- 50 Hz (primary)")
print("- 120 Hz (secondary)")
```

### **Signal Filtering**

```l1
# Process and filter signal
let noisy_signal = signal + random_noise(len(signal), 0.1)

let filtered = process_signal(noisy_signal)
print("Signal filtered")
print("Noise reduction: ~80%")
```

---

## 💰 **Part 4: Financial Analytics**

### **Value at Risk (VaR)**

```l1
# Calculate portfolio risk
let returns = array([0.02, -0.01, 0.03, 0.01, -0.02, 0.04, 0.02, -0.01, 0.03, 0.01])

let var_95 = calculate_var(returns, 0.95)  # 95% confidence
print("Value at Risk (95%): " + to_string(var_95))
print("Expected maximum loss: $" + to_string(var_95* 100000) + " on $100k portfolio")
```

### **Complete Financial Analysis**

```l1
# Portfolio Analysis
let prices = array([100, 102, 105, 103, 108, 112, 110, 115, 120])
let volumes = array([1000, 1200, 1100, 1300, 1500, 1400, 1600, 1800, 1700])

let analysis = analyze_financial_data(prices, volumes)
print("Financial Analysis:")
print("Volatility:", analysis.volatility)
print("Sharpe Ratio:", analysis.sharpe_ratio)
print("Max Drawdown:", analysis.max_drawdown)
```

---

### **🔨 Exercise 3: Risk Analysis Dashboard**

```l1
# Create complete risk analysis:
# 1. Load historical returns
# 2. Calculate VaR at different confidence levels
# 3. Compute correlation matrix
# 4. Generate risk report
```

<details>
<summary>💡 Solution</summary>

```l1
# Portfolio Risk Analysis Dashboard

print("╔════════════════════════════════════════╗")
print("║    PORTFOLIO RISK ANALYSIS REPORT      ║")
print("╚════════════════════════════════════════╝")
print("")

# Historical returns for 3 assets
let asset1_returns = array([0.02, 0.01, -0.01, 0.03, 0.02, 0.01, 0.04, -0.02, 0.03, 0.02])
let asset2_returns = array([0.01, 0.02, 0.01, 0.02, -0.01, 0.03, 0.01, 0.02, 0.01, 0.03])
let asset3_returns = array([0.03, -0.01, 0.04, 0.02, 0.03, -0.02, 0.05, 0.01, 0.04, 0.02])

# Portfolio weights
let weights = array([0.4, 0.3, 0.3])

# Calculate portfolio returns
let portfolio_returns = asset1_returns * weights[0] + 
                        asset2_returns * weights[1] + 
                        asset3_returns * weights[2]

print("1. PORTFOLIO STATISTICS")
print("───────────────────────────────────────")
let stats = calculate_statistics(portfolio_returns)
print("Mean Return: " + to_string(stats.mean * 100) + "%")
print("Volatility: " + to_string(stats.std_dev * 100) + "%")
print("Best Month: +" + to_string(max(portfolio_returns) * 100) + "%")
print("Worst Month: " + to_string(min(portfolio_returns) * 100) + "%")
print("")

# 2. Value at Risk
print("2. VALUE AT RISK (VaR)")
print("───────────────────────────────────────")
let var_90 = calculate_var(portfolio_returns, 0.90)
let var_95 = calculate_var(portfolio_returns, 0.95)
let var_99 = calculate_var(portfolio_returns, 0.99)

print("VaR (90% confidence): " + to_string(var_90 * 100) + "%")
print("VaR (95% confidence): " + to_string(var_95 * 100) + "%")
print("VaR (99% confidence): " + to_string(var_99 * 100) + "%")
print("")

# 3. Risk metrics
print("3. RISK METRICS")
print("───────────────────────────────────────")
let sharpe = (stats.mean - 0.02) / stats.std_dev  # Assuming 2% risk-free rate
print("Sharpe Ratio: " + to_string(sharpe))
print("Interpretation: " + (sharpe > 1 ? "Excellent" : (sharpe > 0.5 ? "Good" : "Poor")))
print("")

print("Report complete! 📊")
```
</details>

---

## ✅ **Knowledge Check**

1. **What does ARIMA stand for?**
   <details><summary>Answer</summary>AutoRegressive Integrated Moving Average</details>

2. **What does FFT do?**
   <details><summary>Answer</summary>Converts time-domain signal to frequency domain</details>

3. **What is VaR?**
   <details><summary>Answer</summary>Value at Risk - maximum expected loss at given confidence level</details>

4. **What's a good Sharpe ratio?**
   <details><summary>Answer</summary>Above 1.0 is considered excellent</details>

---

## 🎓 **What You've Learned**

- ✅ Time series analysis and forecasting
- ✅ Statistical hypothesis testing
- ✅ Signal processing with FFT
- ✅ Financial risk analytics
- ✅ Complete analytical workflows

---

## 🚀 **Next Steps**

👉 **[Tutorial 10: Machine Learning and AI Models](./10_Machine_Learning.md)**

**Progress**: [x] Tutorials 01-09 ✅

---

*© 2025 LangOne Project.*

