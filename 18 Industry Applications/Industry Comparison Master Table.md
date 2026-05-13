# Industry Comparison — SCM Methods Master Table

> **Tags:** #industry #comparison #SCM #overview
> **Purpose:** Quick cross-industry reference for methods, KPIs, and priorities

---

## SCM Method Applicability by Industry

| SCM Method / Principle | Food & Bev | Hotel | Paint | Retail/Supermarket | Pharma | Automotive | E-commerce | Apparel |
|---|---|---|---|---|---|---|---|---|
| **FEFO** | Critical | Critical | N/A | Critical (perishables) | Critical | N/A | Partial | N/A |
| **ABC Analysis** | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **VED Analysis** | Partial | Yes (MRO) | Partial | N/A | Critical | Critical | N/A | N/A |
| **FSN Analysis** | Yes | Yes | Yes | Yes | Yes | Partial | Yes | Yes |
| **EOQ** | Yes | Yes | Yes | Yes | Yes | Yes | Partial | Partial |
| **Safety Stock** | Yes | Yes | Yes (high) | Yes | Very High | Very High | Yes | Yes |
| **Demand Forecasting** | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| **Seasonal Planning** | Yes | Yes | Yes | Yes | Partial | Partial | Yes | Critical |
| **JIT / Kanban** | Partial | Partial | N/A | Partial | N/A | Critical | Partial | Partial |
| **Cross-Docking** | Yes (FMCG) | N/A | Yes (depot) | Yes | Partial | Yes | Yes | Yes |
| **VMI** | Yes | Partial | Yes | Yes | Yes | Yes | Partial | Partial |
| **FMEA** | Yes | Yes | Yes | Partial | Critical | Critical | Partial | Partial |
| **Cold Chain** | Yes | Yes | N/A | Partial | Critical | N/A | N/A | N/A |
| **Postponement** | N/A | N/A | Critical | N/A | N/A | Partial | N/A | Yes |
| **Open-to-Buy** | N/A | N/A | N/A | Yes | N/A | N/A | Partial | Critical |

---

## Key KPI by Industry

| Industry | Primary KPI | Secondary KPI | Risk KPI |
|---|---|---|---|
| **Food & Bev** | Wastage % | Food Cost % | Cold Chain Compliance % |
| **Hotel** | Food Cost % | Stockout Incidents | Spoilage % |
| **Paint** | Forecast Accuracy (branch) | Fill Rate | Dead Stock % |
| **Retail/Supermarket** | Shelf Availability % | Inventory Turns | Shrinkage % |
| **Pharma** | OTIF % | Cold Chain Breach % | Batch Recall Response Time |
| **Automotive** | Line Stoppage Count | Supplier OTD % | Defective PPM |
| **E-commerce** | On-Time Delivery % | Perfect Order Rate | Last-Mile Cost per Order |
| **Apparel** | Sell-Through % | Markdown % | Weeks of Cover |

---

## Lead Time Comparison

| Industry | Typical Replenishment Lead Time | Safety Stock Cover |
|---|---|---|
| Food (fresh) | 0–2 days | 1–3 days |
| Hotel | 1–3 days (local), 30+ days (import) | 2–5 days (fresh), 30d (specialty) |
| Paint | 3–7 days (depot to branch), 30d (plant to depot) | 15–30 days |
| Supermarket | 1–3 days (DC to store) | 3–7 days |
| Pharma | 30–90 days (API), 30–60 days (finished) | 30–60 days |
| Automotive | 1–30 days (local–imported) | 1–60 days (by criticality) |
| E-commerce | Real-time DC to FC | 7–14 days at FC |
| Apparel | 30–120 days (offshore) | 30–60 days |

---

## Demand Forecasting Method by Industry

| Industry | Best Method | Why |
|---|---|---|
| Food (stable items) | Moving Average / Exponential Smoothing | Stable baseline with some seasonality |
| Hotel | Occupancy-linked forecast | Demand is derived from occupancy, not independent |
| Paint (branch) | Exponential Smoothing + Seasonal Index | Per-branch variation; clear seasonality |
| Supermarket | Time Series + Promo uplift factor | Promotions dominate variance |
| Pharma | Stable demand; protocol-driven | Prescription demand is relatively predictable |
| Automotive | MRP (derived from production plan) | Demand is calculated, not forecasted |
| E-commerce | Machine learning on real-time signals | Volume and velocity require ML at scale |
| Apparel | Test-and-repeat; Open-to-Buy | Trend-driven; historical patterns unreliable |

---

## Your Three Projects — Method Matrix

| Method | Hotel Inventory | Asian Paints Branches | Phoon Huat |
|---|---|---|---|
| **FEFO** | Critical (F&B) | N/A | Critical (butter, cream) |
| **PAR Level System** | Critical (housekeeping) | N/A | N/A |
| **ABC Analysis** | Yes — all depts | Yes — per branch | Yes — all SKUs |
| **VED** | Yes — MRO/Engineering | Partial | Partial (import specialty) |
| **EOQ + ROP** | Yes | Yes | Yes |
| **Safety Stock** | Yes | Yes (higher for imports) | Yes (higher for imports) |
| **Seasonal Planning** | Occupancy-linked | Regional monsoon index | Festive calendar |
| **Demand Forecasting** | Occupancy × cover ratio | Exp smoothing × seasonal index | Historical + social media sensing |
| **Dead Stock Management** | Monthly review | Monthly per branch | Monthly; markdown protocol |
| **Supplier Segmentation** | Local vs import tiers | Depot vs direct plant | Local vs import tiers |

---

## Related Concepts
- [[F&B Industry SCM Overview]]
- [[Hotel Inventory Management]]
- [[Paint Industry SCM Overview]]
- [[Retail SCM Overview]]
- [[Phoon Huat Inventory Playbook]]
