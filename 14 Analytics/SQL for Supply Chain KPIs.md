# SQL for Supply Chain KPIs

> **Tags:** #analytics #sql #kpi #data

---

## Inventory KPIs

```sql
-- Inventory Turns
SELECT
    sku,
    product_name,
    SUM(cogs) AS total_cogs,
    AVG(inventory_value) AS avg_inventory,
    ROUND(SUM(cogs) / NULLIF(AVG(inventory_value), 0), 2) AS inventory_turns
FROM inventory_metrics
GROUP BY sku, product_name
ORDER BY inventory_turns DESC;

-- Days Inventory Outstanding
SELECT
    sku,
    ROUND(365.0 / NULLIF(inventory_turns, 0), 1) AS days_inventory_outstanding
FROM (
    SELECT sku, SUM(cogs) / NULLIF(AVG(inventory_value), 0) AS inventory_turns
    FROM inventory_metrics GROUP BY sku
) t;

-- ABC Classification
SELECT
    sku,
    revenue,
    SUM(revenue) OVER (ORDER BY revenue DESC) AS cumulative_revenue,
    SUM(revenue) OVER () AS total_revenue,
    ROUND(100.0 * SUM(revenue) OVER (ORDER BY revenue DESC) / SUM(revenue) OVER (), 1) AS cum_pct,
    CASE
        WHEN 100.0 * SUM(revenue) OVER (ORDER BY revenue DESC) / SUM(revenue) OVER () <= 80 THEN 'A'
        WHEN 100.0 * SUM(revenue) OVER (ORDER BY revenue DESC) / SUM(revenue) OVER () <= 95 THEN 'B'
        ELSE 'C'
    END AS abc_class
FROM sku_revenue
ORDER BY revenue DESC;
```

---

## Order Fulfilment KPIs

```sql
-- Fill Rate
SELECT
    DATE_TRUNC('month', order_date) AS month,
    ROUND(100.0 * SUM(shipped_qty) / NULLIF(SUM(ordered_qty), 0), 2) AS fill_rate_pct
FROM orders
GROUP BY 1
ORDER BY 1;

-- Perfect Order Rate
SELECT
    ROUND(100.0 * SUM(CASE WHEN on_time = 1
                            AND in_full = 1
                            AND no_damage = 1
                            AND correct_invoice = 1
                       THEN 1 ELSE 0 END) / COUNT(*), 2) AS perfect_order_rate_pct
FROM shipments;

-- On-Time Delivery
SELECT
    carrier,
    COUNT(*) AS total_shipments,
    SUM(CASE WHEN actual_delivery <= promised_delivery THEN 1 ELSE 0 END) AS on_time,
    ROUND(100.0 * SUM(CASE WHEN actual_delivery <= promised_delivery THEN 1 ELSE 0 END) / COUNT(*), 2) AS otd_pct
FROM deliveries
GROUP BY carrier
ORDER BY otd_pct DESC;
```

---

## Financial KPIs

```sql
-- Cash-to-Cash Cycle
SELECT
    ROUND(365.0 / NULLIF(inventory_turns, 0), 1) AS DIO,
    ROUND(365.0 / NULLIF(ar_turns, 0), 1) AS DSO,
    ROUND(365.0 / NULLIF(ap_turns, 0), 1) AS DPO,
    ROUND(
        365.0 / NULLIF(inventory_turns, 0)
        + 365.0 / NULLIF(ar_turns, 0)
        - 365.0 / NULLIF(ap_turns, 0), 1
    ) AS c2c_days
FROM financial_metrics
WHERE period = '2024-Q4';

-- GMROI by SKU
SELECT
    sku,
    product_name,
    SUM(gross_profit) AS total_gross_profit,
    AVG((opening_stock + closing_stock) / 2.0) AS avg_inventory_value,
    ROUND(100.0 * SUM(gross_profit) / NULLIF(AVG((opening_stock + closing_stock) / 2.0), 0), 1) AS gmroi
FROM sku_financials
GROUP BY sku, product_name
ORDER BY gmroi DESC;

-- Turn-Earn Index
SELECT
    sku,
    inventory_turns,
    gross_margin_pct,
    ROUND(inventory_turns * gross_margin_pct * 100, 1) AS turn_earn_index
FROM sku_metrics
ORDER BY turn_earn_index DESC;
```

---

## Warehouse KPIs

```sql
-- Picking Accuracy by Shift
SELECT
    shift,
    picker_id,
    COUNT(*) AS total_picks,
    SUM(CASE WHEN pick_correct = 1 THEN 1 ELSE 0 END) AS correct_picks,
    ROUND(100.0 * SUM(CASE WHEN pick_correct = 1 THEN 1 ELSE 0 END) / COUNT(*), 2) AS accuracy_pct
FROM pick_transactions
WHERE pick_date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY shift, picker_id
ORDER BY accuracy_pct ASC;

-- Space Utilisation
SELECT
    zone,
    SUM(occupied_cubic_ft) AS used_volume,
    SUM(total_cubic_ft) AS total_volume,
    ROUND(100.0 * SUM(occupied_cubic_ft) / SUM(total_cubic_ft), 1) AS utilisation_pct
FROM warehouse_locations
GROUP BY zone;
```

---

## Forecasting Error

```sql
-- MAD and MAPE by SKU
SELECT
    sku,
    COUNT(*) AS periods,
    ROUND(AVG(ABS(actual_demand - forecast_demand)), 1) AS mad,
    ROUND(AVG(POWER(actual_demand - forecast_demand, 2)), 1) AS mse,
    ROUND(SQRT(AVG(POWER(actual_demand - forecast_demand, 2))), 1) AS rmse,
    ROUND(100.0 * AVG(ABS(actual_demand - forecast_demand) / NULLIF(actual_demand, 0)), 1) AS mape
FROM demand_forecasts
GROUP BY sku
ORDER BY mape DESC;
```
