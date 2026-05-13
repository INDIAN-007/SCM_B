# Transit Time vs Lead Time

> **Source:** Kuldeepak Ch.2
> **Tags:** #logistics #definitions #timing

---

## Definitions

| Term | Definition |
|---|---|
| **Transit Time** | Time taken to travel from point of origin to point of delivery |
| **Lead Time** | Total time from planning to serve time to customer, including returns |

```
Lead Time = Planning Time + Procurement + Manufacturing + Transit Time + Returns Processing
Transit Time ⊂ Lead Time
```

---

## Transit Time Categories (Kuldeepak)

| Category | Description |
|---|---|
| **Maximum** | Highest time recorded to reach destination |
| **Minimum** | Shortest time recorded |
| **Optimistic** | Best case scenario from historical data |
| **Pessimistic** | Worst case from historical data |
| **Normal** | Averaged scenario from historical data |
| **Optimal** | Best performing scenario from historical data |

---

## Why the Distinction Matters

- Confusing transit time with lead time leads to incorrect safety stock calculations
- Lead time drives the reorder point — using only transit time understates it
- Safety stock must account for **lead time variability**, not just transit variability

---

## Impact on Inventory

```
Reorder Point = (Avg Daily Demand × Lead Time) + Safety Stock
Safety Stock  = Z × σ_demand × √Lead Time
```

Longer and more variable lead time → higher safety stock required → higher holding cost

---

## Related Concepts
- [[Safety Stock]]
- [[Reorder Point]]
- [[Logistics Cost Optimization]]
