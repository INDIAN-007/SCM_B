# Food & Beverage Industry — SCM Overview

> **Tags:** #industry #food #beverage #FMCG #SCM
> **Applies to:** Hotels, Restaurants, FMCG manufacturers, Cloud Kitchens, Catering

---

## Industry Profile

| Attribute | Characteristic |
|---|---|
| **Demand Pattern** | Seasonal, event-driven, highly variable |
| **Product Nature** | Perishable, shelf-life sensitive |
| **Lead Times** | Short for fresh; longer for packaged/imported |
| **Regulation** | FSSAI (India), FDA (US), SFA (Singapore), HACCP, ISO 22000 |
| **Key Risk** | Spoilage, contamination, cold-chain failure |
| **Top Companies** | Nestlé, ITC, Britannia, Unilever, Amul, McCain |

---

## Core SCM Challenges

| Challenge | Impact |
|---|---|
| Short shelf life | High wastage if over-stocked; stockout if under-stocked |
| Demand volatility | Festivals, weather, trends spike demand unpredictably |
| Cold chain dependency | Any break = product loss + compliance breach |
| Supplier reliability | Fresh produce suppliers are weather-dependent |
| Multi-SKU complexity | Hundreds of variants; each with different ROP |
| Regulatory compliance | Batch tracking, expiry dating mandatory |

---

## Key Methods & Principles

### 1. FEFO — First Expired, First Out
- **Rule:** Always pick item with earliest expiry date first
- **Where:** Refrigerators, dry store, finished goods warehouse
- **Implementation:** Barcode/RFID + WMS enforced picking sequence
- **Tip:** Physically rotate stock on shelves — new stock goes behind old stock

### 2. ABC + VED Analysis
- **ABC:** Classify by consumption value (A = top 70% spend)
- **VED:** Classify by criticality (V = Vital — stockout = operations halt)
- **Combined Matrix:**

| | Vital | Essential | Desirable |
|---|---|---|---|
| **A (High Value)** | Tight control, dual supplier | Review weekly | Monitor monthly |
| **B (Medium Value)** | Review biweekly | Standard ROP | Standard ROP |
| **C (Low Value)** | Bulk buy, safety stock | Periodic review | Periodic review |

### 3. Demand Forecasting for F&B
- **Method:** Decomposition — Trend + Seasonality + Event spikes
- **Tools:** Moving Average (stable items), Exponential Smoothing (trending items)
- **Seasonality factors to build in:**
  - Festive periods (Diwali, CNY, Christmas, Ramadan)
  - Weekend vs weekday patterns
  - Weather impact (ice cream, hot beverages)
- **Tip:** Maintain event calendar in forecasting model — flag known demand spikes 4–6 weeks ahead

### 4. Safety Stock with Shelf-Life Constraint
- Normal SS formula: `SS = Z × σ_demand × √LT`
- **F&B Constraint:** Safety Stock must NOT exceed shelf life turnover window
- Example: If bread shelf life = 3 days, SS should cover max 1.5 days of demand

### 5. Supplier Segmentation
- **Tier 1:** Local fresh produce — daily/EOD delivery, short PO lead time
- **Tier 2:** Packaged/FMCG — weekly order cycle, 3–7 day lead time
- **Tier 3:** Imported specialty — monthly order, long lead time, higher SS needed

### 6. Cold Chain Management
- Temperature zones: Frozen (< -18°C), Chilled (2–8°C), Ambient (15–25°C)
- Key points: Receiving dock check, in-transit monitoring, last-mile verification
- **Tool:** IoT temperature loggers + Control Tower alerts

### 7. Wastage Control Framework
- Track wastage by: Category → SKU → Shift → Cause
- Causes: Over-ordering, FIFO not followed, demand forecast error, storage failure
- Target wastage < 2% for packaged, < 5% for fresh produce

---

## F&B Specific KPIs

| KPI | Formula | Target |
|---|---|---|
| **Food Wastage %** | Wasted qty / Purchased qty × 100 | < 3% |
| **Spoilage Cost** | Value of expired/damaged stock | Minimize |
| **Stock Cover (days)** | Current stock / Avg daily usage | 2–5 days (fresh), 15–30 days (dry) |
| **Cold Chain Compliance %** | Deliveries in-temp / Total deliveries × 100 | > 99% |
| **Supplier On-Time Delivery %** | On-time POs / Total POs × 100 | > 95% |
| **Inventory Accuracy %** | System vs physical match | > 98% |
| **Order Fill Rate** | Lines filled / Lines ordered × 100 | > 97% |

---

## Best Practices & Tips

1. **Daily stock counts** for fresh/perishable items — weekly for dry goods
2. **Par level system** for kitchen: set min/max per item; reorder triggers automatically
3. **Vendor Managed Inventory (VMI)** for high-frequency fresh suppliers — supplier manages replenishment
4. **Menu engineering** drives SCM: reduce SKUs by designing menus around common ingredients
5. **Batch tracking** mandatory — record supplier lot number at receiving for traceability
6. **Demand calendar** — load all events, public holidays, sporting events into forecast system
7. **Cross-utilisation** — buy ingredients usable across multiple dishes to reduce tail SKUs

---

## Indian F&B Companies — Approaches

| Company | SCM Approach |
|---|---|
| **Amul** | Cooperative model; 3.5M farmers → central processing → DCs → retail |
| **ITC (Bingo, Aashirvaad)** | e-Choupal rural procurement network; direct farmer sourcing |
| **Britannia** | Hub-and-spoke DC network; strong distributor management |
| **Zomato/Swiggy (dark kitchens)** | Demand-driven micro-kitchens; real-time inventory from order data |

---

## Related Concepts
- [[FEFO FIFO LIFO]]
- [[Safety Stock]]
- [[ABC VED SDE FSN Analysis]]
- [[Cold Chain (Warehouse Types)]]
- [[Demand Forecasting Methods]]
