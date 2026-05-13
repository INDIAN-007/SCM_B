# Phoon Huat — Inventory Management Playbook

> **Tags:** #industry #retail #baking #PhoonHuat #Singapore #SCM
> **Applies to:** Phoon Huat outlets, Singapore specialty retail

---

## Business Context

- **Type:** Specialty baking supplies retailer — multi-outlet, Singapore
- **Customer segments:** Home bakers, professional pastry chefs, F&B businesses, hotels
- **Product mix:** ~3,000–5,000 SKUs across perishables, dry goods, equipment, packaging
- **Key seasons:** Christmas, CNY, Hari Raya, Valentine's Day, Mother's Day, Mid-Autumn

---

## Inventory Classification Framework

### Tier 1 — Perishables (Daily/Every-2-Day Control)
| Item Examples | Control Method | Stock Cover | Alert |
|---|---|---|---|
| Butter, cream cheese | FEFO, daily count | 2–4 days | < 1 day = emergency order |
| Fresh cream, eggs | FEFO, daily count | 1–2 days | < 0.5 day = urgent |
| Seasonal fresh fruit (for garnish) | Event-driven order | Day-of | Order per confirmed orders |

### Tier 2 — Dry Ingredients (Weekly Control)
| Item Examples | Control Method | Stock Cover | Reorder Point |
|---|---|---|---|
| Flour, sugar, cocoa powder | EOQ + ROP | 14–21 days | 7 days of stock |
| Baking powder, vanilla extract | Min-max | 21–30 days | 10 days of stock |
| Chocolate chips, nuts | ABC-based | 14–21 days | Based on demand history |

### Tier 3 — Imported Specialty (Monthly Control)
| Item Examples | Lead Time | Stock Cover | Order Cycle |
|---|---|---|---|
| Couverture chocolate (Belgian/French) | 6–8 weeks | 60–90 days | Monthly |
| Specialty food colouring | 4–6 weeks | 45–60 days | Monthly |
| Imported moulds, specialty tools | 4–8 weeks | 90 days | Quarterly |

### Tier 4 — Equipment (Quarterly Review)
| Item Examples | Control Method | Notes |
|---|---|---|
| Stand mixers, ovens, tempering machines | Min = 1 unit display + 1 buffer | Long lead from supplier; order 3 months ahead |
| Hand mixers, piping bags | Min-max | Fast-moving; reorder weekly |

---

## Seasonal Demand Planning Calendar

| Festival | When | Lead Time to Stock | Demand Spike | Key SKUs |
|---|---|---|---|---|
| **Christmas** | Dec 25 | Stock from Nov 1 | 3–5× | Butter, fondant, food colouring, piping bags, cake boards |
| **Chinese New Year** | Jan–Feb | Stock from Dec 15 | 2–4× | Pineapple jam, pandan flavouring, mooncake moulds, gold dust |
| **Valentine's Day** | Feb 14 | Stock from Jan 20 | 2–3× | Chocolate, heart moulds, red colouring, velvet spray |
| **Mother's Day** | May | Stock from Apr 15 | 1.5–2× | Flower moulds, luster dust, fondant, cream |
| **Hari Raya** | Variable | 6 weeks ahead | 1.5–2× | Kueh ingredients, green pandan, coconut cream |
| **Mid-Autumn** | Sep–Oct | Stock from Aug | 1.5–2× | Mooncake moulds, salted egg, lotus paste |

---

## Reorder Formula per SKU

```
Reorder Point (ROP) = Avg Daily Sales × Supplier Lead Time (days) + Safety Stock
Safety Stock = Z × σ_demand × √Lead Time
Order Quantity = EOQ or (Target Stock Cover × Avg Daily Sales) − Current Stock
```

**Example — Belgian Couverture Chocolate (Dark 64%):**
- Avg daily sales: 5 kg
- Lead time: 42 days
- σ_demand: 2 kg/day (high variation during festive)
- Z (95% CSL): 1.65
- Safety Stock = 1.65 × 2 × √42 = 21.4 kg → round to 22 kg
- ROP = 5 × 42 + 22 = **232 kg**
- When stock hits 232 kg, raise PO

---

## Social Media Demand Sensing

**Problem:** When a recipe goes viral on TikTok/Instagram, demand for specific ingredients spikes with 0 warning.

**Approach:**
1. Monitor hashtags: #phoonhuat, #homebaking, #sgbaker, viral recipe keywords
2. If a recipe with a specific ingredient hits 100K+ views → flag to buying team within 24 hours
3. Buying team checks current stock vs estimated demand spike
4. Emergency top-up PO if local supplier available
5. **Tip:** Build relationships with local distributors who can supply within 2–3 days for emergency top-ups

---

## Outlet-Level Demand Variation

Different outlets attract different customer types:
| Outlet Type | Customer Profile | Stock Focus |
|---|---|---|
| **Flagship (large format)** | All segments; highest variety | Full SKU range; large SS |
| **HDB neighborhood** | Home bakers; smaller quantities | Small pack sizes; basics only |
| **Commercial area** | F&B businesses, professional bakers | Bulk packs; professional-grade ingredients |
| **Online** | Nationwide; all segments | Sync with nearest DC stock |

**Policy:** Each outlet has an outlet-specific ranging list; not all SKUs stocked at all outlets.

---

## Dead Stock Management

- **Monthly review:** All SKUs not sold in 30 days flagged
- **Action plan:**
  - Perishables: Mark down immediately; donate to food bank if near expiry
  - Dry goods: Bundle with fast movers in a "Baking Starter Kit" promotion
  - Equipment: Display clearance section; price reduce by 20–30%
  - Imports: Negotiate credit/exchange with supplier for truly dead items

---

## KPI Dashboard for Phoon Huat

| KPI | Formula | Target |
|---|---|---|
| **Perishable Wastage %** | Wastage value / Purchase value × 100 | < 3% |
| **Shelf Availability (A items)** | Time on shelf / Total time × 100 | > 98% |
| **Festive Sell-Through %** | Units sold / Units bought for season × 100 | > 90% |
| **Inventory Turns (dry goods)** | COGS / Avg dry inventory | > 8× |
| **Dead Stock %** | Non-moving value / Total stock × 100 | < 5% |
| **Import Lead Time Compliance** | Orders arriving on time / Total import orders | > 85% |
| **Online-Offline Stock Sync Accuracy** | Matching records / Total SKUs × 100 | > 99% |

---

## Related Concepts
- [[Retail SCM Overview]]
- [[F&B Industry SCM Overview]]
- [[Safety Stock]]
- [[EOQ]]
- [[Demand Forecasting Methods]]
- [[GMROI]]
