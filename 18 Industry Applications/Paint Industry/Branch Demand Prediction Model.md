# Branch Demand Prediction — Paint Industry

> **Tags:** #industry #paint #forecasting #analytics #branches
> **Applies to:** Asian Paints, Berger, Nippon — multi-branch prediction

---

## Problem Statement

Predict monthly demand per SKU per branch across 100+ branches to:
1. Optimise branch-level inventory (right stock, right branch)
2. Plan depot replenishment
3. Identify which SKUs to stock vs order-on-demand per branch

---

## Data Requirements

| Data Element | Source | Frequency |
|---|---|---|
| Branch-level sales history (SKU × branch × month) | ERP/SAP | Monthly |
| Current branch stock levels | WMS | Daily |
| Pending orders (branch POs to depot) | ERP | Real-time |
| Project pipeline per branch | Sales CRM | Monthly |
| Season calendar (monsoon by region) | Historical + Met dept | Annual |
| Dealer sell-out data (if available) | POS integration | Weekly |

---

## Step-by-Step Prediction Approach

### Step 1 — Data Cleaning
- Remove outliers (bulk project orders that skew the average)
- Fill missing months (branch opened mid-year) with category average
- Normalise for branch size / territory coverage

### Step 2 — SKU Classification per Branch
```python
# Classify each SKU at each branch
# A: top 70% of revenue, B: next 20%, C: bottom 10%
branch_sku_df['cumulative_pct'] = branch_sku_df.groupby('branch_id')['revenue'].transform(
    lambda x: x.sort_values(ascending=False).cumsum() / x.sum() * 100
)
branch_sku_df['abc_class'] = pd.cut(branch_sku_df['cumulative_pct'],
    bins=[0, 70, 90, 100], labels=['A', 'B', 'C'])
```

### Step 3 — Forecast per SKU per Branch
```python
# Exponential Smoothing per branch × SKU
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def forecast_branch_sku(series, periods=3, alpha=0.3):
    if len(series) < 4:
        return [series.mean()] * periods  # fallback for new branches
    model = ExponentialSmoothing(series, trend='add', seasonal='add',
                                  seasonal_periods=12)
    fit = model.fit(smoothing_level=alpha)
    return fit.forecast(periods)
```

### Step 4 — Apply Seasonal Index
```python
# Build seasonal index per region
seasonal_index = {
    'North': [0.9, 0.9, 1.0, 1.1, 1.0, 0.7, 0.6, 0.7, 0.8, 1.3, 1.3, 1.1],
    'South': [1.0, 1.0, 1.1, 1.0, 0.9, 1.1, 0.8, 0.8, 1.0, 1.2, 1.1, 0.9],
    'West':  [1.0, 0.9, 1.0, 1.1, 1.0, 0.8, 0.6, 0.7, 0.9, 1.2, 1.3, 1.1],
    'East':  [1.1, 1.0, 1.0, 1.0, 0.9, 0.8, 0.7, 0.8, 1.0, 1.2, 1.1, 1.0],
}
forecast_adjusted = base_forecast × seasonal_index[branch_region][month]
```

### Step 5 — Calculate Replenishment Recommendation
```python
# For each branch × SKU
reorder_point = avg_demand × lead_time_days + safety_stock
recommended_order = max(0, reorder_point + forecast_next_month - current_stock)
```

---

## Output — Branch Replenishment Report

| Branch | SKU | ABC Class | Current Stock | ROP | Forecast (Next Month) | Recommended Order |
|---|---|---|---|---|---|---|
| Mumbai South | INT-EMU-20L-WH | A | 45 | 50 | 120 | 125 |
| Pune East | EXT-WPT-10L-BL | B | 12 | 15 | 35 | 38 |
| Nagpur | INT-EMU-4L-CR | C | 8 | 5 | 10 | 0 (sufficient) |

---

## Segmentation Rules

| Class | Stock Policy | Review Frequency | Source |
|---|---|---|---|
| **A** | Maintain full ROP + SS at branch | Weekly | Depot auto-replenishment |
| **B** | Maintain ROP at branch | Biweekly | Depot replenishment |
| **C** | No branch stock; depot holds buffer | Monthly | Order on customer demand |

---

## Advanced: Cluster Branches by Demand Pattern

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Features: avg monthly demand, seasonality amplitude, growth rate, SKU mix
X = branch_features[['avg_demand', 'seasonality_amp', 'growth_rate', 'sku_diversity']]
X_scaled = StandardScaler().fit_transform(X)
kmeans = KMeans(n_clusters=4, random_state=42)
branch_features['cluster'] = kmeans.fit_predict(X_scaled)
# Apply cluster-level stocking policy
```

**Cluster Types:**
- Cluster 0 — High volume, low seasonal: Metro showrooms → continuous replenishment
- Cluster 1 — High seasonal: Tier-2 cities → pre-season build strategy
- Cluster 2 — Project-driven: Industrial areas → order-to-project model
- Cluster 3 — Low volume: Rural dealers → depot holds, branch orders on demand

---

## Related Concepts
- [[Demand Forecasting Methods]]
- [[Time Series Forecasting]]
- [[Safety Stock]]
- [[ABC VED SDE FSN Analysis]]
- [[Distribution Networks]]
