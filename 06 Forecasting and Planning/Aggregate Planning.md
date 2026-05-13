# Aggregate Planning

> **Source:** Chopra Ch.8
> **Tags:** #planning #aggregate #production #capacity

---

## Definition

Aggregate planning determines **medium-term production, staffing, and inventory levels** to meet expected demand at minimum cost — typically over a 3–18 month horizon.

"Aggregate" because decisions are made at the product family level, not individual SKU.

---

## The Basic Tradeoffs (Chopra)

To respond to demand variation, firms choose between:

| Option | Description | Cost |
|---|---|---|
| **Chase strategy** | Adjust production to match demand (hire/fire, overtime) | Low inventory, high labour flexibility cost |
| **Level strategy** | Constant production rate; use inventory to buffer | Stable workforce, but higher holding cost |
| **Flexible strategy** | Mix of both | Balance of costs |

---

## Cost Components in Aggregate Planning

| Cost | Description |
|---|---|
| Regular-time labour | Standard workforce salary during normal hours |
| Overtime labour | Premium pay for hours beyond standard |
| Hiring and layoff | Recruitment, training, severance |
| Inventory holding | Cost to hold unsold production |
| Stockout / Backorder | Cost of unmet demand (lost sales or delayed delivery) |
| Subcontracting | Cost to outsource production when demand exceeds capacity |

---

## Aggregate Planning Using Linear Programming

Objective: Minimise total cost subject to:
- Demand must be met each period (or backlogged at a cost)
- Workforce cannot exceed maximum capacity
- Inventory cannot go below safety stock
- Inventory balance: Inventory(t) = Inventory(t-1) + Production(t) - Demand(t)

---

## Aggregate Plan → Master Production Schedule

```
Aggregate Plan (Product Family Level)
        ↓
Master Production Schedule (Individual Product Level)
        ↓
Material Requirements Plan (MRP — Component Level)
        ↓
Purchase Orders + Work Orders (Execution)
```

---

## Related Concepts
- [[S&OP]]
- [[Demand Forecasting Methods]]
- [[Capacity Planning]]
- [[EOQ]]
