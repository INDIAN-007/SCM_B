# Cash-to-Cash (C2C) Cycle

> **Source:** Kuldeepak Ch.1 · Chopra Ch.3
> **Tags:** #kpi #cashflow #working-capital

---

## Definition

C2C measures the amount of time **operating capital is tied up** — from when cash is paid out to when it returns as collected revenue.

A fast (low) C2C = lean and profitable supply chain.
A negative C2C (like Amazon) = company collects from customers before paying suppliers.

---

## Formula

### Kuldeepak Version (Operational)
```
C2C Cycle Time (days) = Materials payment date − Customer order payment date

Interpret: How long does cash stay "out" before it returns?
```

### Chopra Financial Version
```
C2C = DIO + DSO − DPO

DIO = Days Inventory Outstanding = 365 / Inventory Turns
DSO = Days Sales Outstanding     = Accounts Receivable / (Revenue / 365)
DPO = Days Payable Outstanding   = Accounts Payable / (COGS / 365)
```

---

## Example (Amazon 2013)
```
INVT = 7.31 → DIO = 365 / 7.31 = 49.9 days
ART  = 15.62 → DSO = 365 / 15.62 = 23.4 days
APT  = 2.48  → DPO = 365 / 2.48 = 147.2 days

C2C = 49.9 + 23.4 − 147.2 = −73.9 days = −10.53 weeks
```
Amazon holds supplier money for ~10 weeks before paying — funding its own operations.

---

## Industry Benchmarks (Chopra Table 3-3)

| Industry | Avg C2C |
|---|---|
| Consumer Electronics | 9.3 days |
| Automotive | ~50–70 days |
| Medical Devices | >200 days |
| Grocery Retail | Negative to low positive |

---

## Improvement Strategies

| Lever | Effect on C2C |
|---|---|
| Faster inventory turns | Reduce DIO |
| Faster customer collections | Reduce DSO |
| Extend supplier payment terms | Increase DPO |
| Reduce safety stock | Reduce DIO |
| Use consignment inventory | Transfer DIO risk to supplier |

---

## Related Concepts
- [[GMROI]] · [[Inventory Turnover]]
- [[KPI Framework]]
- [[Safety Stock]]
