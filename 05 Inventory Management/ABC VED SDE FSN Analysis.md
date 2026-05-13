# ABC / VED / SDE / FSN Analysis

> **Source:** Kuldeepak Ch.4
> **Tags:** #inventory #analysis #classification

---

## ABC Analysis — Always Better Control

Derived from Pareto's 80/20 principle. Classifies inventory by **value / revenue contribution**.

| Class | % of Items | % of Revenue | Control Level |
|---|---|---|---|
| **A — Critical** | 20% | 80% | Tight, high frequency review, strict control |
| **B — Medium** | 30% | 15% | Moderate review, periodic reporting |
| **C — Trivial Many** | 50% | 5% | Loose control, simple rules, minimal oversight |

### Application
- **Class A:** Daily monitoring, dedicated buyer, tight safety stock management
- **Class B:** Weekly monitoring, standard procedures
- **Class C:** Bulk orders, simple min-max rules

---

## VED Analysis — Vital, Essential, Desirable

**Qualitative** analysis, primarily used for **spare parts** based on operational criticality (not value).

| Category | Description | Example |
|---|---|---|
| **V — Vital** | Without it, operations stop | Compressor seal on production line |
| **E — Essential** | Operations impacted but not stopped | Conveyor belt drive motor |
| **D — Desirable** | Comfortable to have but not critical | Office printer cartridge |

**VED is independent of cost** — a cheap but vital part gets more attention than an expensive desirable part.

---

## SDE Analysis — Scarce, Difficult, Easy

Classifies inventory by **procurement difficulty / availability**.

| Category | Description |
|---|---|
| **S — Scarce** | Very limited availability; long lead times; import-dependent |
| **D — Difficult** | Available but requires effort; moderate lead time |
| **E — Easy** | Readily available from multiple sources; short lead time |

**Used for:** Imported items, rare spares, raw materials with supply risk.

---

## FSN Analysis — Fast, Slow, Non-moving

Classifies by **movement velocity** — helps reduce dead stock and free working capital.

| Category | Description | Action |
|---|---|---|
| **F — Fast Moving** | High demand, frequent replenishment | Ensure availability; short reorder cycle |
| **S — Slow Moving** | Low demand, infrequent movement | Reduce safety stock; periodic review |
| **N — Non-Moving** | No demand in defined period | Liquidate, scrap, or return to supplier |

**Used when:** Large stockholding facilities with capital blockage due to slow / non-moving inventory.

---

## Combined Analysis — ABC × VED Matrix

| | V (Vital) | E (Essential) | D (Desirable) |
|---|---|---|---|
| **A (High Value)** | Critical — tightest control | High control | Moderate |
| **B (Medium Value)** | High control | Standard | Lower |
| **C (Low Value)** | High control (don't stockout) | Standard | Simple rules |

---

## Related Concepts
- [[Types of Inventory]]
- [[EOQ]] · [[Safety Stock]]
- [[Inventory KPIs]]
