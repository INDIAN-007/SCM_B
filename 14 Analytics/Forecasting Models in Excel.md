# Forecasting Models in Excel

> **Source:** Chopra Ch.7
> **Tags:** #analytics #excel #forecasting

---

## Setting Up a Forecasting Workbook

### Data Structure
```
| Period | Month | Actual Demand | Forecast | Error | |Abs Error| |
|--------|-------|--------------|----------|-------|----------|
| 1 | Jan-24 | 1200 | 1200 | 0 | 0 |
| 2 | Feb-24 | 1350 | 1200 | -150 | 150 |
```

---

## Simple Exponential Smoothing in Excel

Cell references (Column E = Forecast):
```
E2 = D2                          (initialise with actual demand)
E3 = $B$1 * D2 + (1-$B$1) * E2  ($B$1 = alpha parameter)
E4 = $B$1 * D3 + (1-$B$1) * E3
...copy down
```

Error metrics in summary row:
```
MAD  = AVERAGE(ABS(D3:D50 - E3:E50))   {Ctrl+Shift+Enter as array formula}
MSE  = SUMPRODUCT((D3:D50-E3:E50)^2)/COUNT(D3:D50)
MAPE = AVERAGE(ABS((D3:D50-E3:E50)/D3:D50))*100
```

---

## Finding Optimal Alpha with Solver

1. Set MAD cell as **Objective** (minimise)
2. Set alpha cell as **Variable** (0.01 to 0.99)
3. Add constraint: 0 ≤ alpha ≤ 1
4. Run Solver → optimal alpha found automatically

---

## Seasonal Index Calculation

```
1. Calculate average demand per period across years
2. Calculate overall average
3. Seasonal Index = Period Average / Overall Average
4. Deseasonalise: Actual / Seasonal Index
5. Forecast deseasonalised → reseasonalise: × Seasonal Index
```

---

## Forecast Error Tracking with Control Chart

```
Tracking Signal = Cumulative Error / MAD
Plot in Excel; add control lines at +4 and -4
```

If tracking signal exceeds ±4 → model is biased → recalibrate.

---

## Related Concepts
- [[Time Series Forecasting]]
- [[Forecast Error Metrics]]
- [[S&OP]]
