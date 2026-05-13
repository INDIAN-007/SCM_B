# Replenishment Models — Q System vs P System

> **Source:** Kuldeepak Ch.4
> **Tags:** #inventory #replenishment #systems

---

## Two Fundamental Approaches

### Q System — Fixed Order Quantity (Continuous Review)
Stocks are replenished with a **fixed quantity** whenever inventory falls to the reorder point.

- **Trigger:** Stock level hits ROP
- **Order Quantity:** Fixed (usually EOQ)
- **Review:** Continuous — must monitor inventory at all times
- **Count method:** Perpetual inventory count

### P System — Periodic Review
Stocks are replenished at **fixed time intervals** with a **variable quantity** to reach a target level.

- **Trigger:** Fixed review period arrives
- **Order Quantity:** Variable — enough to fill up to target stock level
- **Review:** Periodic — only checked at review intervals
- **Count method:** Periodic inventory count

---

## Comparison Table

| Factor | Q System | P System |
|---|---|---|
| Order trigger | Stock hits ROP | Fixed time interval |
| Order timing | Any time | At predefined interval |
| Order quantity | Fixed (constant) | Variable each cycle |
| Inventory size | Lower (less safety stock) | Higher (more safety stock needed) |
| Control method | Perpetual count | Periodic count |
| Record management | Continuous updates | Only at review period |
| IT requirement | Higher (real-time tracking) | Lower |
| Best for | High-value, fast-moving items | Many low-value items |

---

## Safety Stock Requirements

- **Q System:** Safety stock protects only against lead time variability (known order timing)
- **P System:** Safety stock must protect against both lead time and review period variability → higher SS required

```
Q System SS = Z × σ_D × √L
P System SS = Z × σ_D × √(L + T)   where T = review interval
```

---

## When to Use Each

| Situation | Use Q System | Use P System |
|---|---|---|
| High-value items | ✓ | |
| Many low-value items | | ✓ |
| Real-time IT available | ✓ | |
| Coordinated ordering (same supplier) | | ✓ |
| A-class items (ABC) | ✓ | |
| C-class items (ABC) | | ✓ |

---

## Related Concepts
- [[EOQ]]
- [[Safety Stock]]
- [[Reorder Point]]
- [[ABC VED SDE FSN Analysis]]
