# Retail & Supermarket — SCM Overview

> **Tags:** #industry #retail #supermarket #FMCG #SCM
> **Applies to:** Phoon Huat, Cold Storage, NTUC FairPrice, Giant, DMart, Big Bazaar

---

## Industry Profile

| Attribute | Characteristic |
|---|---|
| **Product Range** | 5,000 – 50,000+ SKUs (general supermarket); narrower for specialty |
| **Demand Pattern** | Day-of-week, seasonal, promotional, holiday-driven |
| **Replenishment** | Daily (fresh) to weekly/monthly (dry goods, specialty) |
| **Margin Pressure** | Thin margins (1–5% net); inventory efficiency = survival |
| **Key Metrics** | GMROI, Inventory Turns, Shrinkage %, OTD, Shelf Availability |
| **Key Risk** | Stockouts (lost sale), overstocking (markdowns, wastage) |
| **Top Companies** | Walmart, Tesco, Carrefour, NTUC FairPrice, DMart, Reliance Retail |

---

## Retail Supply Chain Structure

```
Supplier → Central Warehouse / DC → Store Backroom → Shelf → Customer
                    ↑                      ↑
             Cross-dock possible      In-store replenishment
```

---

## Core SCM Challenges

| Challenge | Impact |
|---|---|
| SKU proliferation | Too many SKUs → complexity, dead stock, poor turns |
| Promotional demand spikes | 2–5× normal demand during promotions |
| Shrinkage (theft, damage, expiry) | Reduces effective inventory accuracy |
| Last-metre replenishment | Shelf availability ≠ backroom availability |
| Supplier compliance | Late deliveries → empty shelves |
| Seasonal assortment | Festival SKUs need fast in/out cycle |

---

## Key Methods & Principles

### 1. Category Management
- Group SKUs into categories (e.g., Bakery, Dairy, Frozen, Snacks)
- Each category managed as a business unit
- Decisions: Which SKUs to range, how much shelf space, pricing, promotions
- **Tip:** Focus on top 20% SKUs that drive 80% of category revenue; rationalise tail

### 2. Planogram (POG)
- Visual layout of products on shelf
- Optimises: facings per SKU, shelf space allocation, eye-level placement
- **SCM link:** More facings = higher visual inventory = fewer replenishment trips
- **Rule:** High-velocity items get more facings; slow movers get fewer (or delisted)

### 3. Shelf Availability vs Inventory Availability
- **Shelf availability:** % of time product is on shelf for customer to buy
- **Inventory availability:** % of time product is in store (shelf + backroom)
- **Gap = Last-metre problem:** Product in backroom but not on shelf
- **Target:** Shelf availability > 98% for A items
- **Fix:** Automatic replenishment triggers when shelf stock < facing count

### 4. Days of Supply (DOS) Model
- For each SKU, set target DOS at store level
- `DOS = Current Stock / Avg Daily Sales`
- `Order Quantity = (Target DOS × Avg Daily Sales) − Current Stock + SS`
- **Tip:** Set different DOS targets by category: fresh = 1–2 days, dry = 7–14 days

### 5. Demand Forecasting for Retail
- **Baseline:** Moving average / Exponential smoothing on daily sales
- **Promotions:** Add promotional uplift factor (2–5× baseline during promotion)
- **Seasonal:** Multiply by seasonal index (Chinese New Year, Christmas, Diwali)
- **New item:** Use similar item sales as proxy for first 8–12 weeks

### 6. ABC + FSN Analysis
- **ABC by revenue:** Focus control effort on high-revenue SKUs
- **FSN:** Fast/Slow/Non-moving — derange (remove from range) N items quarterly
- **Combined approach:**
  - A+Fast → prime shelf space, full SS, daily replenishment
  - C+Non-moving → clearance, markdown, derange

### 7. Promotional Planning
- **Pre-promotion:** Stock build 2–3 weeks in advance
- **During promotion:** Daily monitoring; emergency replenishment if sell-through faster than forecast
- **Post-promotion:** Manage residual stock; avoid carryover of promotional SKUs
- **Tip:** Negotiate return-to-vendor (RTV) clause for unsold promotional stock

### 8. Cross-Docking for FMCG
- FMCG supplier delivers to DC → sorted by store → dispatched to stores same day
- No storage at DC — direct flow
- Enables daily replenishment to stores without high DC inventory
- **Tip:** Requires supplier delivery time compliance > 95%; build penalty clause in contract

### 9. Vendor-Managed Inventory (VMI)
- Supplier (e.g., P&G, Nestlé) manages replenishment of their own products at your store/DC
- Supplier accesses your POS data → manages orders → ensures availability
- **Benefit:** Reduces your buyer's workload; supplier has better demand visibility
- **Risk:** Supplier may over-stock their products; need KPI governance

---

## Retail / Supermarket KPIs

| KPI | Formula | Target |
|---|---|---|
| **Shelf Availability %** | Time product on shelf / Total time × 100 | > 98% (A items) |
| **Inventory Turns** | COGS / Avg Inventory | 12–25× (grocery), 4–8× (specialty) |
| **GMROI** | Gross Margin / Avg Inventory Cost | > 150% |
| **Shrinkage %** | (Book stock − Physical stock) / Book stock × 100 | < 1% |
| **Days of Supply** | Current stock / Avg daily sales | 3–7d (fresh), 14–30d (dry) |
| **Supplier OTD %** | On-time deliveries / Total deliveries × 100 | > 95% |
| **Dead Stock %** | Non-moving stock value / Total stock × 100 | < 3% |
| **Promo Forecast Accuracy** | 1 − |Forecast − Actual| / Actual | > 70% (promos are hard) |
| **Return Rate %** | Returns / Total sales × 100 | < 1% |

---

## Phoon Huat — Specialty Baking Retail Context

| Aspect | Phoon Huat Specifics |
|---|---|
| **Category** | Baking ingredients, equipment, packaging, decorating supplies |
| **Customer** | Home bakers, professional pastry chefs, bakeries, hotels |
| **Seasonal peaks** | Christmas, CNY, Hari Raya, Valentine's Day, Mother's Day |
| **Product mix** | Perishable (butter, cream, eggs) + Non-perishable (flour, sugar, chocolate) + Equipment |
| **Multi-outlet** | Multiple outlets across Singapore → outlet-level demand variation |
| **Key challenge** | Festive demand spikes (3–5× normal), perishable management, specialty imports |

**Phoon Huat Specific Tips:**
1. **Festive planning calendar** — 6–8 weeks before each major festival, increase orders
2. **Recipe-driven demand** — when a popular recipe goes viral (social media), demand for specific ingredients spikes; monitor social media
3. **Professional vs home baker segment** — professional bakers buy in bulk; home bakers buy small packs; stock both pack sizes of key items
4. **Import lead times** — specialty items from France, Belgium (couverture chocolate) have 6–8 week lead times; order well ahead
5. **Equipment as anchor SKU** — customers come for equipment, then become regular ingredient buyers; always keep flagship equipment in stock
6. **Online + offline** — if they have an online store, sync inventory; avoid overselling online when physical stock is reserved

---

## Tips for Retail Inventory Management

1. **Automate reordering for A items** — reduce buyer time on routine replenishment
2. **Weekly dead stock meetings** — every SKU not sold in 30 days needs a plan (markdown, promotion, return)
3. **Supplier scorecard** — rate each supplier on OTD, fill rate, invoice accuracy; use it in renegotiation
4. **Shrinkage audit** — monthly physical vs system count; investigate gaps immediately
5. **New item process** — every new SKU gets a 90-day trial; if velocity is below threshold, delist
6. **Space productivity** — track sales per linear metre of shelf per category; reallocate space from slow to fast
7. **Cluster stores** — group similar stores and apply same ranging/stocking policy; don't manage each store independently

---

## Related Concepts
- [[ABC VED SDE FSN Analysis]]
- [[Demand Forecasting Methods]]
- [[GMROI]]
- [[Inventory Turnover]]
- [[Cross Docking]]
- [[Bullwhip Effect]]
- [[JIT and Kanban]]
