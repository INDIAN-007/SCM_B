# Python for Supply Chain Management
# Tags: #analytics #python #scm #data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ── 1. EOQ Calculator ──────────────────────────────────────────────────────────

def eoq(D, S, H):
    """Economic Order Quantity.
    D: Annual demand (units)
    S: Ordering cost per order
    H: Annual holding cost per unit
    """
    return np.sqrt(2 * D * S / H)

def eoq_analysis(D, S, H):
    q = eoq(D, S, H)
    orders_per_year = D / q
    annual_ordering_cost = (D / q) * S
    annual_holding_cost = (q / 2) * H
    total_cost = annual_ordering_cost + annual_holding_cost
    print(f"EOQ: {q:.0f} units")
    print(f"Orders per year: {orders_per_year:.1f}")
    print(f"Annual ordering cost: {annual_ordering_cost:.2f}")
    print(f"Annual holding cost: {annual_holding_cost:.2f}")
    print(f"Total annual cost: {total_cost:.2f}")
    return q

# Example
# eoq_analysis(D=10000, S=500, H=25)


# ── 2. Safety Stock and ROP ────────────────────────────────────────────────────

def safety_stock(service_level, sigma_demand, lead_time, sigma_lead_time=0, avg_demand=0):
    """Calculate safety stock.
    service_level: e.g. 0.95 for 95%
    sigma_demand: std dev of demand per period
    lead_time: average lead time in periods
    sigma_lead_time: std dev of lead time (optional)
    avg_demand: average demand per period (needed if sigma_lead_time > 0)
    """
    z = stats.norm.ppf(service_level)
    if sigma_lead_time > 0:
        ss = z * np.sqrt(lead_time * sigma_demand**2 + avg_demand**2 * sigma_lead_time**2)
    else:
        ss = z * sigma_demand * np.sqrt(lead_time)
    return ss

def reorder_point(avg_demand, lead_time, service_level, sigma_demand, sigma_lead_time=0):
    ss = safety_stock(service_level, sigma_demand, lead_time, sigma_lead_time, avg_demand)
    rop = avg_demand * lead_time + ss
    print(f"Safety Stock: {ss:.0f} units")
    print(f"Reorder Point: {rop:.0f} units")
    return rop

# Example
# reorder_point(avg_demand=50, lead_time=10, service_level=0.95, sigma_demand=8)


# ── 3. ABC Analysis ───────────────────────────────────────────────────────────

def abc_analysis(df, sku_col='sku', revenue_col='annual_revenue'):
    """Classify SKUs into A/B/C based on revenue contribution."""
    df = df.sort_values(revenue_col, ascending=False).copy()
    df['cumulative_revenue'] = df[revenue_col].cumsum()
    df['cumulative_pct'] = df['cumulative_revenue'] / df[revenue_col].sum() * 100
    df['abc_class'] = pd.cut(
        df['cumulative_pct'],
        bins=[0, 80, 95, 100],
        labels=['A', 'B', 'C']
    )
    print(df.groupby('abc_class')[revenue_col].agg(['count', 'sum', 'mean']))
    return df


# ── 4. Demand Forecasting ─────────────────────────────────────────────────────

def exponential_smoothing(demand, alpha):
    """Simple exponential smoothing."""
    forecast = [demand[0]]
    for i in range(1, len(demand)):
        f = alpha * demand[i-1] + (1 - alpha) * forecast[i-1]
        forecast.append(f)
    return forecast

def forecast_errors(actual, forecast):
    errors = np.array(actual) - np.array(forecast)
    mad = np.mean(np.abs(errors))
    mse = np.mean(errors**2)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs(errors) / np.array(actual)) * 100
    return {'MAD': mad, 'MSE': mse, 'RMSE': rmse, 'MAPE': mape}

def find_best_alpha(demand, alphas=None):
    """Find best alpha by minimising MAD."""
    if alphas is None:
        alphas = np.arange(0.1, 1.0, 0.1)
    results = []
    for alpha in alphas:
        f = exponential_smoothing(demand, alpha)
        errors = forecast_errors(demand[1:], f[:-1])
        results.append({'alpha': alpha, **errors})
    df = pd.DataFrame(results)
    best = df.loc[df['MAD'].idxmin()]
    print(f"Best alpha: {best['alpha']:.1f}, MAD: {best['MAD']:.2f}")
    return df


# ── 5. Inventory Turns and KPIs ───────────────────────────────────────────────

def inventory_kpis(cogs, avg_inventory, revenue, ar, ap):
    turns = cogs / avg_inventory
    dio = 365 / turns
    dso = 365 / (revenue / ar)
    dpo = 365 / (cogs / ap)
    c2c = dio + dso - dpo
    print(f"Inventory Turns: {turns:.2f}")
    print(f"DIO: {dio:.1f} days")
    print(f"DSO: {dso:.1f} days")
    print(f"DPO: {dpo:.1f} days")
    print(f"Cash-to-Cash Cycle: {c2c:.1f} days")
    return {'turns': turns, 'dio': dio, 'dso': dso, 'dpo': dpo, 'c2c': c2c}


# ── 6. Bullwhip Effect Simulation ─────────────────────────────────────────────

def bullwhip_simulation(consumer_demand, stages=4, order_up_to_multiplier=1.2):
    """Simulate bullwhip effect across supply chain stages."""
    import random
    demands = {'Consumer': consumer_demand}
    current = consumer_demand.copy()
    for i in range(stages - 1):
        orders = []
        for d in current:
            # Each stage orders more than received (safety stock multiplier)
            order = d * order_up_to_multiplier + random.uniform(-d*0.1, d*0.1)
            orders.append(max(0, order))
        current = orders
        stage_name = ['Retailer', 'Wholesaler', 'Distributor', 'Manufacturer'][i]
        demands[stage_name] = current
    return demands


# ── 7. Network Optimisation (simplified) ──────────────────────────────────────

def transportation_cost_matrix(distances, volumes, cost_per_km_per_unit):
    """Calculate transportation cost matrix."""
    return distances * volumes * cost_per_km_per_unit
