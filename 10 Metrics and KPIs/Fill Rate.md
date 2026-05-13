# Fill Rate

> **Source:** Kuldeepak Ch.4 · Chopra Ch.12
> **Tags:** #kpi #inventory #availability

---

## Definition

Fill rate measures the **fraction of customer demand that is satisfied immediately from available inventory** — without backorders or stockouts.

---

## Types of Fill Rate

| Type | Formula | Description |
|---|---|---|
| **Order Fill Rate** | Orders fully filled / Total orders × 100 | % of orders shipped complete |
| **Line Fill Rate** | Order lines filled / Total lines × 100 | % of individual product lines fulfilled |
| **Unit Fill Rate (Product Fill Rate)** | Units shipped / Units ordered × 100 | % of units delivered |

---

## Fill Rate vs Cycle Service Level

| Metric | Measures | Relationship |
|---|---|---|
| **CSL** | P(no stockout in a replenishment cycle) | Binary — stockout or no stockout |
| **Fill Rate** | Fraction of demand served from stock | Continuous — partial fills counted |

Fill rate is generally **higher** than CSL for the same safety stock level because partial demand is still served even when a stockout occurs.

---

## Fill Rate in Inventory Planning (Chopra)

```
Fill Rate (fr) ≈ 1 − ESC/Q

Where:
  ESC = Expected Shortage per Cycle
  Q   = Order Quantity
```

Increasing safety stock increases fill rate but at diminishing returns.

---

## Target Fill Rates by Industry

| Industry | Typical Target |
|---|---|
| FMCG / Consumer goods | 95–99% |
| Pharmaceutical | 99–99.9% |
| Automotive spare parts | 95–98% |
| MRO / Industrial | 90–96% |

---

## Related Concepts
- [[Safety Stock]]
- [[Perfect Order Rate]]
- [[Inventory KPIs]]
