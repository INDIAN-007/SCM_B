# Linear Programming for Supply Chain

> **Source:** Chopra Ch.5, Ch.8
> **Tags:** #analytics #lp #optimization #network

---

## When to Use LP in SCM

Linear Programming (LP) optimises a linear objective subject to linear constraints. Key SC applications:

| Application | Objective | Constraints |
|---|---|---|
| **Aggregate Planning** | Minimise total cost | Demand satisfaction, capacity limits |
| **Network Design** | Minimise total SC cost | Plant/DC capacities, customer demand |
| **Transportation** | Minimise freight cost | Supply and demand at each node |
| **Inventory Mix** | Maximise profit | Budget, storage space |

---

## Transportation Problem (Classic LP)

```
Minimise: Σᵢ Σⱼ cᵢⱼ × xᵢⱼ

Subject to:
  Σⱼ xᵢⱼ ≤ Sᵢ   (supply constraint at each origin i)
  Σᵢ xᵢⱼ ≥ Dⱼ   (demand satisfied at each destination j)
  xᵢⱼ ≥ 0

Where:
  cᵢⱼ = unit cost from origin i to destination j
  xᵢⱼ = units shipped from i to j
  Sᵢ  = supply available at origin i
  Dⱼ  = demand at destination j
```

---

## Aggregate Planning LP (Chopra Ch.8)

Variables for each period t:
- Wt = Workforce level
- Ht = Workers hired
- Lt = Workers laid off
- Pt = Production quantity
- It = Inventory at end of period
- St = Stockout (backorder) quantity
- Ct = Subcontracted quantity
- Ot = Overtime hours

Objective: Minimise Σₜ (labour + hiring + layoff + inventory + stockout + subcontracting + overtime costs)

---

## Python: Aggregate Planning with PuLP

```python
from pulp import *

prob = LpProblem("Aggregate_Planning", LpMinimize)

periods = range(1, 13)  # 12 months

# Decision variables
W = LpVariable.dicts("Workforce", periods, lowBound=0)
H = LpVariable.dicts("Hire", periods, lowBound=0)
L = LpVariable.dicts("Layoff", periods, lowBound=0)
P = LpVariable.dicts("Production", periods, lowBound=0)
I = LpVariable.dicts("Inventory", periods, lowBound=0)

# Costs (example values)
cW = 3000   # cost per worker per month
cH = 4000   # hiring cost per worker
cL = 6000   # layoff cost per worker
cI = 100    # inventory holding per unit per month

# Objective
prob += (
    lpSum(cW * W[t] + cH * H[t] + cL * L[t] + cI * I[t] for t in periods)
)

# Constraints (example demand)
demand = {1:1000, 2:1200, 3:1500, 4:1800, 5:2000, 6:1800,
          7:1500, 8:1200, 9:1000, 10:800, 11:1000, 12:1200}

for t in periods:
    # Workforce balance
    if t == 1:
        prob += W[t] == 100 + H[t] - L[t]
    else:
        prob += W[t] == W[t-1] + H[t] - L[t]
    # Inventory balance
    prod_rate = 20  # units per worker per month
    if t == 1:
        prob += I[t] == 2000 + P[t] - demand[t]
    else:
        prob += I[t] == I[t-1] + P[t] - demand[t]
    # Production capacity
    prob += P[t] <= prod_rate * W[t]

prob.solve()
print(f"Total Cost: {value(prob.objective):,.0f}")
```

---

## Transportation Problem Methods (Kuldeepak)

| Method | Description |
|---|---|
| **North West Corner Rule** | Start top-left; allocate to corner; simple but not optimal |
| **Least Cost Method** | Allocate to lowest-cost cell first; better starting solution |
| **Vogel's Approximation** | Uses penalty costs for each row/col; near-optimal starting solution |
| **MODI Method (Optimal)** | Iterative improvement to reach optimal solution |

---

## Related Concepts
- [[Aggregate Planning]]
- [[Distribution Networks]]
- [[Python for SCM.py]]
