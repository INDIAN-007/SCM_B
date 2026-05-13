# Demand Forecasting Methods

> **Source:** Kuldeepak Ch.2 · Chopra Ch.7
> **Tags:** #forecasting #demand #planning

---

## Definition (Chopra)

Demand forecasting is the act of predicting future customer demand using historical data, market intelligence, and statistical models. It is the **foundation of all supply chain planning**.

**Key insight:** All supply chain decisions ultimately depend on the forecast — and all forecasts are wrong. The goal is to be **less wrong** and to understand the magnitude of error.

---

## Role in Supply Chain

| Decision | Dependent on Forecast |
|---|---|
| Inventory levels (safety stock, cycle stock) | Yes |
| Production and capacity planning | Yes |
| Procurement quantities | Yes |
| Workforce planning | Yes |
| Transportation capacity booking | Yes |
| Distribution network design | Yes |

---

## Four Components of Demand (Chopra)

1. **Systematic component** — predictable part of demand
   - Level (baseline demand)
   - Trend (sustained increase or decrease)
   - Seasonality (predictable recurring pattern)
2. **Random component** — purely random; cannot be predicted; only its distribution can be characterised

---

## Qualitative Methods (Kuldeepak)

Used when historical data is unavailable or insufficient:

| Method | Description |
|---|---|
| **Delphi Technique** | Expert panel forecasts independently → meets to discuss → iterated until consensus |
| **Market Research** | Survey of target customers / geography; used for new product categories |
| **Sales Force Opinion** | Sales team provides regional demand estimates; aggregated to company forecast |

---

## Quantitative Methods (Kuldeepak)

| Method | Description |
|---|---|
| **Trend Projection / Time Series** | Historical data extrapolated using time series analysis (2–3 years) |
| **Econometric / Regression** | Demand linked to explanatory variables (single or multiple); e.g., ink demand based on pens sold |
| **Barometric Technique** | Uses leading, coincident, and lagging economic indicators; e.g., girls' hostel demand linked to school enrollment |

---

## Time-Series Methods (Chopra Ch.7)

### Moving Average
```
Forecast for t+1 = Avg(Demand for periods t, t-1, ..., t-n+1)
```
Simple to compute; slow to react to trends.

### Weighted Moving Average
More recent periods given higher weights.

### Simple Exponential Smoothing
```
F(t+1) = α × D(t) + (1-α) × F(t)

α = smoothing factor (0 < α < 1)
Higher α = more weight on recent demand
Lower α = smoother forecast (more historical weight)
```

### Trend-Corrected Exponential Smoothing (Holt's Method)
Adds trend adjustment to exponential smoothing — accounts for systematic increase/decrease.

### Winter's Method
Adds seasonality component to Holt's method — handles level + trend + seasonality.

---

## Forecast Characteristics (Chopra)

1. **Forecasts are always wrong** — plan for forecast error
2. **Long-range forecasts are less accurate** than short-range
3. **Aggregate forecasts are more accurate** than individual SKU forecasts (pooling)
4. **The further upstream in the supply chain, the larger the error** (amplified by bullwhip)

---

## Related Concepts
- [[Forecast Error Metrics]]
- [[Time Series Forecasting]]
- [[S&OP]]
- [[Bullwhip Effect]]
- [[Safety Stock]]
