# Quick Reference Formulas

> **Tags:** #formulas #math #quickref

---

## Inventory
```
EOQ = √(2 × D × S / H)
  D = Annual demand quantity
  S = Ordering cost per order
  H = Annual holding cost per unit

Safety Stock = Z × σ_demand × √Lead Time
  Z: 1.28 → 90% | 1.65 → 95% | 1.96 → 97.5% | 2.33 → 99%

Reorder Point (ROP) = (Avg Daily Demand × Lead Time in days) + Safety Stock

Cycle Inventory = Q / 2   (average on-hand between orders)

Inventory Turns = COGS / Avg Inventory

Days Inventory Outstanding (DIO) = 365 / Inventory Turns
```

## Financial KPIs
```
Cash-to-Cash (C2C) = DIO + DSO − DPO
  DIO = Days Inventory Outstanding
  DSO = Days Sales Outstanding
  DPO = Days Payable Outstanding

GMROI = Gross Profit / [(Opening Stock + Closing Stock)/2] × 100

Turn-Earn Index = Inventory Turns × Gross Profit % × 100

Total SC Cost (TSCC) = Material + Manpower + Inv. Holding + Logistics + Overheads

ROA = Net Income / Total Assets
ROE = Net Income / Shareholder Equity
Profit Margin = Net Income / Revenue
Asset Turnover = Revenue / Total Assets

Accounts Payable Turnover (APT) = COGS / Accounts Payable
```

## Logistics
```
Perfect Order Rate = (Total Orders − Erratic Orders) / Total Orders × 100

On-Time Delivery % = On-Time Shipments / Total Shipments × 100

Vehicle Capacity Utilization = Actual Load / Rated Capacity × 100

Cost-to-Sales Ratio = Transport Cost / Net Sales × 100

Supply Chain Cycle Time = Sum of longest lead times across each stage
```

## Warehouse
```
Picking Accuracy % = Correctly Picked Lines / Total Picked Lines × 100
Putaway Accuracy % = Correctly Placed Items / Total Items × 100
Storage Space Utilization = Volume Used / Total Storage Volume × 100
Units Handled per Hour = Total Units / Manhours
Non-Storage Area % = Non-Storage Space / Total Space × 100
```

## Forecasting Error
```
MAD  = Σ|Actual − Forecast| / n
MSE  = Σ(Actual − Forecast)² / n
RMSE = √MSE
MAPE = (Σ|Actual − Forecast| / Actual) / n × 100
```

## Lean / Six Sigma
```
Takt Time = Total Available Time / Customer Demand per Period
DPMO     = (Defects / (Units × Opportunities)) × 1,000,000
RPN      = Occurrence × Severity × Detection   (each 1–10 scale)
6σ level = 3.4 DPMO
```
