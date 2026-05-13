# Economic Order Quantity (EOQ)

> **Source:** Kuldeepak Ch.4 · Chopra Ch.11
> **Tags:** #inventory #eoq #formula #optimization

---

## Definition

EOQ is the order quantity that **minimises total inventory cost** — balancing ordering cost against holding cost.

As order quantity rises → ordering frequency and ordering cost fall, but holding cost rises.
EOQ finds the optimal midpoint.

---

## Formula

```
EOQ = √(2 × D × S / H)

Where:
  D = Annual demand (units)
  S = Ordering cost per order (fixed cost per order placed)
  H = Annual holding cost per unit
      = Unit cost × Holding cost rate (e.g. 25% of unit cost)
```

---

## Step-by-Step (Kuldeepak Method)

```
Step A: No. of Orders per Year = D / Q
Step B: Annual Ordering Cost   = (D / Q) × S
Step C: Holding Cost per unit  = Carrying rate × Unit cost
Step D: Avg Annual Holding Cost = (Q / 2) × H
Step E: Total Annual Cost (TC) = Annual Ordering Cost + Annual Holding Cost

Minimise TC by setting dTC/dQ = 0 → gives EOQ formula
```

---

## Example Calculation

| Variable | Value |
|---|---|
| Annual Demand (D) | 10,000 units |
| Ordering Cost (S) | ₹500 per order |
| Unit Cost | ₹100 |
| Holding Rate | 25% of unit cost |
| H | ₹25 per unit per year |

```
EOQ = √(2 × 10,000 × 500 / 25) = √400,000 = 632 units
No. of Orders = 10,000 / 632 ≈ 15.8 orders per year
Order Cycle = 365 / 15.8 ≈ 23 days
```

---

## Assumptions (and Limitations)

| Assumption | Real-World Limitation |
|---|---|
| Constant demand | Demand is rarely constant — seasonality, trends |
| Constant lead time | Supplier delays and disruptions occur |
| Instantaneous replenishment | Lead time > 0 in practice |
| No quantity discounts | Suppliers often offer volume discounts |
| Single product | Multi-product orders require aggregate EOQ |
| No stockouts allowed | Stockouts happen; safety stock handles this |

> **Author's Tip (Kuldeepak):** EOQ does not consider variability in holding or ordering cost — this makes it less relevant where seasonality or demand skewness brings cost variability.

---

## Extensions to EOQ

| Extension | Situation |
|---|---|
| **EOQ with Quantity Discounts** | Unit price changes at different volume thresholds |
| **EOQ with Planned Shortages** | Allow stockouts with back-ordering |
| **Production Order Quantity (POQ)** | Gradual replenishment (production rate > demand rate) |
| **Periodic Review (P system)** | Fixed review interval instead of fixed order quantity |

---

## Related Concepts
- [[Safety Stock]]
- [[Reorder Point]]
- [[Replenishment Models Q vs P]]
- [[Inventory KPIs]]
