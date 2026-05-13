# Safety Stock

> **Source:** Kuldeepak Ch.4 · Chopra Ch.12
> **Tags:** #inventory #safetystock #uncertainty

---

## Definition

Safety stock is **additional inventory beyond cycle stock** held to protect against uncertainty in demand or supply.

Without safety stock, any deviation from average demand or average lead time causes a stockout.

---

## Why Safety Stock is Needed

| Source of Uncertainty | Impact |
|---|---|
| Demand variability | Actual demand exceeds forecast |
| Lead time variability | Supplier delivers later than expected |
| Forecast error | Demand model is wrong |
| Supply disruptions | Supplier failure, port delays, strikes |
| Transportation delays | Route disruptions, weather events |

---

## Safety Stock Formula (Chopra)

### When demand uncertainty only:
```
SS = Z × σ_D × √L

Where:
  Z   = Service level factor
  σ_D = Standard deviation of demand per period
  L   = Lead time in periods
```

### When both demand AND lead time uncertain:
```
SS = Z × √(L × σ_D² + D_avg² × σ_L²)

Where:
  D_avg = Average demand per period
  σ_L   = Standard deviation of lead time
```

### Service Level Factors (Z values)
| Service Level | Z Value |
|---|---|
| 90% | 1.28 |
| 95% | 1.65 |
| 97.5% | 1.96 |
| 99% | 2.33 |
| 99.9% | 3.09 |

---

## Cycle Service Level vs Fill Rate

| Metric | Definition |
|---|---|
| **Cycle Service Level (CSL)** | Probability of NOT stocking out during a replenishment cycle |
| **Product Fill Rate (fr)** | Fraction of demand satisfied from available inventory |
| **Order Fill Rate** | Fraction of orders filled completely from available stock |

Fill rate is generally higher than CSL for the same safety stock level.

---

## Factors Affecting Safety Stock Level (Kuldeepak)

- Lead time variability — more variable → more SS
- Demand variability — more variable → more SS
- Service level target — higher target → more SS
- Review frequency — longer interval → more SS
- Number of SKUs — more SKUs → more total SS (but aggregation can reduce it)

---

## Managerial Levers to Reduce Safety Stock (Chopra)

1. **Reduce demand uncertainty** — improve forecasting, collaborate with customers
2. **Reduce lead time** — work with suppliers, reduce order processing time
3. **Reduce lead time variability** — reliable suppliers, better logistics
4. **Centralise inventory** — pooling effect reduces SS across locations
5. **Use postponement** — delay product differentiation closer to demand point

---

## The Pooling Benefit (Centralisation)

If demand is independently distributed across n locations:
```
Aggregated SS = Z × σ_D × √L × √n

vs.

Decentralised SS = n × Z × σ_D × √L

Saving factor = √n
```

Centralising from 4 warehouses to 1 cuts safety stock by factor of √4 = 2 (50% reduction).

---

## Related Concepts
- [[EOQ]] · [[Reorder Point]]
- [[Types of Inventory]]
- [[Bullwhip Effect]]
- [[Distribution Networks]]
