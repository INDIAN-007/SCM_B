# Forecast Error Metrics

> **Source:** Chopra Ch.7
> **Tags:** #forecasting #error #metrics #accuracy

---

## Why Measure Forecast Error

- Forecast error drives safety stock requirements
- Tracking error identifies when a model needs updating
- Error metrics allow comparison between forecasting approaches

---

## Key Metrics

### MAD — Mean Absolute Deviation
```
MAD = Σ|Actual(t) - Forecast(t)| / n
```
- Most intuitive; same units as demand
- Does not penalise large errors proportionally

### MSE — Mean Squared Error
```
MSE = Σ[Actual(t) - Forecast(t)]² / n
```
- Penalises large errors heavily
- Useful when large errors are especially costly

### RMSE — Root Mean Squared Error
```
RMSE = √MSE
```
- Same units as demand; more interpretable than MSE
- Still penalises large errors more than MAD

### MAPE — Mean Absolute Percentage Error
```
MAPE = Σ(|Actual - Forecast| / Actual) / n × 100
```
- Scale-independent — enables comparison across products and periods
- Problematic when actual demand is near zero

---

## Bias — Systematic Error

```
Forecast Bias = Σ(Forecast - Actual) / n
```
- Positive bias → consistently over-forecasting (excess inventory)
- Negative bias → consistently under-forecasting (stockouts)
- Good forecast has bias near zero

---

## Tracking Signal

```
Tracking Signal = Cumulative Forecast Error / MAD
```
- If |Tracking Signal| > 4–6 → model is biased, needs recalibration
- Used to monitor ongoing forecast quality in real time

---

## Relationship Between MAD and σ (Standard Deviation)

```
σ ≈ 1.25 × MAD   (for normally distributed errors)
```

This relationship allows safety stock calculation from MAD:
```
Safety Stock = Z × σ_D × √L ≈ Z × 1.25 × MAD × √L
```

---

## Related Concepts
- [[Demand Forecasting Methods]]
- [[Time Series Forecasting]]
- [[Safety Stock]]
