# Hotel Inventory Management — SCM Application

> **Tags:** #industry #hotel #hospitality #inventory #SCM
> **Applies to:** Hotels, Resorts, Banquet Halls, Club Houses

---

## Industry Profile

| Attribute | Characteristic |
|---|---|
| **Demand Driver** | Occupancy rate, events, season, day-of-week |
| **Departments** | F&B, Housekeeping, Maintenance, Front Office, Spa |
| **Inventory Types** | Perishables, Linen, Chemicals, Engineering spares, Stationery |
| **Key Challenge** | Multi-department inventory with different demand patterns |
| **Regulation** | FSSAI, fire safety, OSHA for chemicals |

---

## Department-wise Inventory Categories

| Department | Key Items | Classification | Method |
|---|---|---|---|
| **Kitchen / F&B** | Fresh produce, proteins, dry goods, beverages | Perishable + Non-perishable | FEFO, daily count |
| **Housekeeping** | Linen, toiletries, cleaning chemicals | Non-perishable + consumable | PAR level, weekly count |
| **Engineering** | Spare parts, tools, lubricants | MRO (Maintenance, Repair, Operations) | VED + EOQ |
| **Front Office** | Stationery, key cards, printing supplies | Low-value consumables | Min-Max system |
| **Banquet** | Crockery, cutlery, disposables, decor | Reusable + consumable | Event-driven ordering |

---

## PAR Level System (Hotel Standard)

**PAR = Periodic Automatic Replenishment**

- **PAR Level** = quantity needed for one service cycle (1 day or 1 shift)
- **On-hand PAR** = quantity physically in the department
- **Reorder trigger:** When stock < PAR × Safety factor

**Example (Housekeeping):**
- Hotel has 200 rooms
- Each room needs 2 bath towels per day → PAR = 400 towels
- With 3-day laundry cycle → Stock needed = 400 × 3 = 1,200 towels
- Safety buffer (10%) → Order trigger at 1,320 towels

---

## Occupancy-Based Demand Forecasting

- **Step 1:** Get occupancy forecast from front office (7-day rolling)
- **Step 2:** Apply cover ratios: rooms → expected F&B covers → ingredient demand
- **Step 3:** Add event load (banquets, weddings, conferences)
- **Formula:**
```
Expected ingredient usage = Forecasted covers × Recipe standard qty per cover
```
- **Tip:** Maintain standardised recipes in the system — every dish has fixed ingredient quantities

---

## Inventory Control Methods by Category

### Fresh Produce (Daily Control)
- Order = (Forecasted covers × recipe qty) + SS − current stock
- Delivery: Daily from local vendors
- Count: Storekeeper + Chef cross-count at receiving
- FEFO enforced at all points

### Linen (Weekly Control)
- PAR-based: Count on hand vs PAR → raise laundry/purchase requisition
- Discard rate tracked: linen discards per 1000 occupied room nights
- Target: < 5% linen discard rate

### Engineering Spares (VED-based)
- **Vital:** AC compressors, boiler parts, lift parts — keep safety stock, dual supplier
- **Essential:** Plumbing, electrical — standard stock, EOQ-based
- **Desirable:** Minor spares — order as needed

---

## Hotel SCM KPIs

| KPI | Formula | Target |
|---|---|---|
| **Food Cost %** | Food cost / Food revenue × 100 | 28–35% |
| **Beverage Cost %** | Bev cost / Bev revenue × 100 | 18–24% |
| **Spoilage %** | Spoiled value / Total purchased × 100 | < 3% |
| **Linen Discard Rate** | Discards / (1000 occupied room nights) | < 5 |
| **Stockout Incidents** | Count of stockouts per month | 0 (vital items) |
| **Supplier OTD %** | On-time deliveries / Total deliveries × 100 | > 95% |
| **Inventory Days Cover** | Stock on hand / Avg daily usage | Fresh: 1–3d; Dry: 15–30d |
| **Purchasing Cost % of Revenue** | Total purchasing / Total revenue × 100 | < 30% |

---

## Tips for Hotel Inventory Management

1. **Centralise the store** — all items go through central receiving; no direct department purchasing
2. **Recipes in system** — standard recipe card for every menu item drives automatic material requirement
3. **Weekly food cost meeting** — Kitchen head + Purchasing + F&B Controller review actual vs budget
4. **Market list system** — Chef raises daily market list by 8pm for next-day delivery
5. **Buffet vs A-la-carte** — buffet is harder to forecast; use historical consumption per head ratio
6. **Vendor consolidation** — fewer vendors = better pricing, better reliability
7. **Slow-mover clearance** — monthly review; push slow items into staff meals or daily specials
8. **Event BOM (Bill of Materials)** — for every banquet event, raise a material requirement sheet 72 hours ahead

---

## Related Concepts
- [[F&B Industry SCM Overview]]
- [[FEFO FIFO LIFO]]
- [[Safety Stock]]
- [[Reorder Point]]
- [[Warehouse KPIs]]
