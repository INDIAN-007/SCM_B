# Reorder Point (ROP)

> **Source:** Kuldeepak Ch.4 · Chopra Ch.12
> **Tags:** #inventory #rop #replenishment

---

## Definition

The Reorder Point is the **inventory level at which a replenishment order must be placed** to avoid a stockout during the lead time.

---

## Formula

```
ROP = (Average Daily Demand × Lead Time in days) + Safety Stock

Or equivalently:
ROP = Expected demand during lead time + Safety stock buffer
```

---

## Example

| Variable | Value |
|---|---|
| Average daily demand | 50 units/day |
| Lead time | 10 days |
| Safety stock | 100 units |

```
ROP = (50 × 10) + 100 = 600 units
```

When inventory falls to 600 units → place replenishment order.

---

## ROP Under Uncertainty

When lead time is fixed but demand is variable:
```
ROP = D_avg × L + Z × σ_D × √L
```

When demand is fixed but lead time is variable:
```
ROP = D × L_avg + Z × D × σ_L
```

When both are variable:
```
ROP = D_avg × L_avg + Z × √(L × σ_D² + D_avg² × σ_L²)
```

---

## Continuous vs Periodic Review

| System | ROP Used? | Description |
|---|---|---|
| **Q System (Continuous)** | Yes — triggers order | Order placed whenever inventory hits ROP; fixed order quantity (EOQ) |
| **P System (Periodic)** | No — time trigger | Order placed at fixed intervals; quantity variable to fill up to target |

---

## Related Concepts
- [[EOQ]]
- [[Safety Stock]]
- [[Replenishment Models Q vs P]]
