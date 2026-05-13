# Time Series Forecasting

> **Source:** Chopra Ch.7
> **Tags:** #forecasting #timeseries #quantitative

---

## What Is a Time Series

A time series is a sequence of demand observations ordered by time. Time series forecasting uses **only the history of demand** — no external causal variables.

---

## Decomposition of Time Series

```
Demand = Level × Trend × Seasonality × Random
```

| Component | Description |
|---|---|
| **Level (L)** | Current baseline demand |
| **Trend (T)** | Persistent upward or downward movement |
| **Seasonality (S)** | Regular pattern repeating over fixed periods (week, month, year) |
| **Random (R)** | Unexplained noise — cannot be forecast |

---

## Methods Summary

### 1. Simple Moving Average (n-period)
```
F(t+1) = [D(t) + D(t-1) + ... + D(t-n+1)] / n
```
- Best for: stable demand with no trend or seasonality
- Lag: slow to adapt to changes

### 2. Weighted Moving Average
```
F(t+1) = w1×D(t) + w2×D(t-1) + ... where Σwi = 1
```
- Gives more recent periods higher weight
- Faster response than simple MA

### 3. Simple Exponential Smoothing
```
F(t+1) = α × D(t) + (1-α) × F(t)
```
- α close to 1 → reacts quickly to changes (more volatile)
- α close to 0 → smooth, slow to respond (better for stable demand)
- Best for: no trend, no seasonality

### 4. Trend-Corrected (Holt's Method)
```
Level:   L(t) = α × D(t) + (1-α) × [L(t-1) + T(t-1)]
Trend:   T(t) = β × [L(t) - L(t-1)] + (1-β) × T(t-1)
Forecast: F(t+m) = L(t) + m × T(t)
```
- Best for: data with a trend but no seasonality

### 5. Winter's Method (Holt-Winters)
Adds seasonal factor S(t) to Holt's method.
- Best for: data with both trend and seasonality

---

## Choosing the Right Method

| Demand Pattern | Method |
|---|---|
| Stable, no trend, no season | Simple Exponential Smoothing |
| Trend, no seasonality | Holt's Method |
| Trend + Seasonality | Winter's Method |
| Highly variable / irregular | Regression or causal methods |

---

## Building in Excel (Chopra approach)

1. Plot demand data to visually identify pattern
2. Test multiple α values — select minimising MAD or MSE
3. Validate out-of-sample (hold back last n periods)
4. Monitor ongoing with tracking signal

---

## Related Concepts
- [[Demand Forecasting Methods]]
- [[Forecast Error Metrics]]
- [[S&OP]]
