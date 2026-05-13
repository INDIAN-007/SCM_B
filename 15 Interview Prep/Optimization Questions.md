# Optimisation Interview Questions

> **Tags:** #interview #optimization #analytics

---

## EOQ Calculation

**Q: Annual demand = 5,000 units. Ordering cost = ₹1,000. Unit cost = ₹200. Holding rate = 20%. Calculate EOQ and annual cost.**

```
H = 200 × 20% = ₹40/unit/year
EOQ = √(2 × 5000 × 1000 / 40) = √250,000 = 500 units
Orders per year = 5000 / 500 = 10 orders
Annual ordering cost = 10 × 1000 = ₹10,000
Annual holding cost = (500/2) × 40 = ₹10,000
Total cost = ₹20,000
```
*At EOQ, ordering cost always equals holding cost.*

---

## Safety Stock Calculation

**Q: Daily demand = 100 units, std dev = 20 units. Lead time = 5 days. Service level = 95%. Calculate safety stock and ROP.**

```
Z (95%) = 1.65
Safety Stock = 1.65 × 20 × √5 = 1.65 × 20 × 2.236 = 73.8 ≈ 74 units
ROP = (100 × 5) + 74 = 574 units
```

---

## C2C Calculation

**Q: COGS = ₹120M. Revenue = ₹200M. AR = ₹25M. AP = ₹30M. Avg Inventory = ₹20M. Calculate C2C.**

```
Inventory Turns = 120 / 20 = 6 → DIO = 365 / 6 = 60.8 days
ART = 200 / 25 = 8 → DSO = 365 / 8 = 45.6 days
APT = 120 / 30 = 4 → DPO = 365 / 4 = 91.3 days
C2C = 60.8 + 45.6 − 91.3 = 15.1 days
```

---

## GMROI

**Q: SKU A: Gross Profit = ₹50,000. Opening stock = ₹80,000. Closing stock = ₹60,000. Calculate GMROI.**

```
Avg Inventory = (80,000 + 60,000) / 2 = ₹70,000
GMROI = 50,000 / 70,000 × 100 = 71.4%

Interpretation: For every ₹100 invested in inventory, ₹71.4 of gross profit is generated.
Target: >100% is good; industry leaders achieve 150-200%+
```

---

## Bullwhip Quantification

**Q: Consumer demand σ = 10 units. 3 stages in SC. Each stage orders based on 2-period MA. What is the bullwhip ratio?**

With n-period moving average and L stages:
- Bullwhip factor per stage = 1 + 2L/n (approximate)
- Each stage amplifies upstream variance
- 3 stages can amplify variability 3–8x in practice

---

## Transportation Problem (Mini)

**Q: 2 plants (supply: 500, 400). 3 customers (demand: 300, 350, 250). Cost matrix provided. Minimise transport cost.**

Apply:
1. Vogel's Approximation Method for initial feasible solution
2. MODI method to check optimality and improve
3. Or use LP / solver directly

---

## Related Concepts
- [[EOQ]] · [[Safety Stock]] · [[Reorder Point]]
- [[Cash to Cash Cycle]] · [[GMROI]]
- [[Linear Programming for SCM]]
