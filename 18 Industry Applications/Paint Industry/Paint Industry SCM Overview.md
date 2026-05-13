# Paint Industry — SCM Overview

> **Tags:** #industry #paint #chemical #manufacturing #SCM
> **Applies to:** Asian Paints, Berger, Nippon, Kansai Nerolac, AkzoNobel

---

## Industry Profile

| Attribute | Characteristic |
|---|---|
| **Product Nature** | Semi-manufactured (tinting at branch) + Finished (ready-mixed) |
| **Demand Pattern** | Seasonal (monsoon = low; post-monsoon = high), project-driven |
| **SKU Complexity** | 10,000+ SKUs per brand (colour × finish × base × pack size) |
| **Distribution** | Plant → Depot → Dealer → Applicator/End customer |
| **Key Challenge** | Colour customisation, demand unpredictability, multi-branch replenishment |
| **Regulation** | VOC limits, hazmat storage norms, REACH (Europe) |
| **Top Companies** | Asian Paints, Berger, Nippon Paint, Kansai Nerolac, Dulux (AkzoNobel) |

---

## Paint Supply Chain Structure

```
Raw Materials          Manufacturing       Distribution         Customer
(Pigments, Resins) → Plant (Base Paint) → Depot → Dealer → Tinting Machine → End User
(Solvents, Fillers)                             ↓
                                           Direct Project Supply
```

**Key insight:** Most paint is sold as BASE + TINTER at dealer point.
The base paint is manufactured; the colour is added at the dealer's tinting machine.
This dramatically reduces finished goods SKUs at the plant level.

---

## Core SCM Challenges

| Challenge | Impact |
|---|---|
| Colour explosion | Thousands of colour combinations; impossible to stock all |
| Seasonal demand swing | Post-monsoon (Oct–Dec) = 40–50% of annual sales |
| Branch-level demand variation | Metro vs rural branches have completely different SKU mix |
| Tinting machine uptime | Machine downtime = zero customised sales |
| Hazmat storage | Solvents and thinners need special storage; compliance required |
| Returns management | Unsold tinted paint cannot be returned — colour-specific |
| Project vs retail demand | Large project orders are lumpy and hard to forecast |

---

## Key Methods & Principles

### 1. Base Paint + Tinter Strategy (Postponement)
- **Concept:** Delay product differentiation as late as possible (Chopra's postponement principle)
- **At plant:** Manufacture only white/neutral base paints (3–5 variants)
- **At dealer:** Add tinter to achieve specific colour on demand
- **Benefit:** Reduces finished goods inventory from 10,000 SKUs → 5 SKUs at plant level
- **Tip:** Only stock top-selling pre-mixed colours; rest are tinted on demand

### 2. Branch-Level Demand Forecasting (100+ Branches)
- **Challenge:** Each branch has a different customer mix, climate, project pipeline
- **Approach:**
  - **Step 1:** Collect branch-level sales history (SKU × branch × month)
  - **Step 2:** Apply time series per SKU per branch (Exponential Smoothing)
  - **Step 3:** Add seasonality index per branch (monsoon timing varies by region)
  - **Step 4:** Add project pipeline input from branch sales team
- **Formula:**
```
Branch Forecast(t) = α × Actual(t-1) + (1-α) × Forecast(t-1)
Adjusted = Branch Forecast(t) × Seasonal Index(t)
```
- **Tip:** Use Weighted Moving Average — give higher weight to recent 3 months

### 3. ABC Analysis at Branch Level
- **Classify per branch:** What sells at an urban showroom ≠ what sells at a rural dealer
- **A items:** Top 20% SKUs = 70–80% of branch revenue → maintain full SS
- **B items:** Next 30% → standard ROP
- **C items:** Remaining 50% → order on demand; don't stock at branch

### 4. Replenishment from Depot to Branch
- **Trigger:** Branch stock falls below ROP → auto-PO raised to depot
- **Depot replenishes from Plant** when depot stock falls below depot ROP
- **Two-echelon inventory model:**
```
Branch ROP = Avg branch demand × Depot lead time + SS
Depot ROP = Sum of branch demands × Plant lead time + Depot SS
```

### 5. Seasonal Stocking Strategy
- **Pre-season build-up:** 6–8 weeks before peak season, build inventory at depots
- **Slow season clearance:** Offer dealer schemes to liquidate inventory before monsoon
- **Monsoon management:** Reduce replenishment; monitor branch stock; avoid expiry of water-based paints

### 6. Hazmat Storage Compliance
- Solvents, thinners, hardeners → classified as flammable/hazmat
- Require: separated storage, fire suppression, ventilation, limited quantity per area
- **Tip:** Keep hazmat items in VED-V category — never let these stock out (safety risk)

### 7. Tinting Machine Management
- Tinting machine = revenue-generating asset at dealer point
- Track: Machine uptime %, tinter cartridge levels, calibration schedule
- **SCM role:** Ensure tinter cartridges replenished before stockout at dealer
- **Approach:** IoT sensors on machines reporting cartridge levels → auto replenishment triggers

---

## Paint Industry Specific KPIs

| KPI | Formula | Target |
|---|---|---|
| **Fill Rate (Branch)** | Lines filled / Lines ordered × 100 | > 96% |
| **Forecast Accuracy** | 1 − (|Forecast − Actual| / Actual) × 100 | > 75% at branch level |
| **Inventory Days at Branch** | Branch stock / Avg daily offtake | 15–25 days |
| **Depot Inventory Days** | Depot stock / Avg daily dispatch | 20–30 days |
| **Tinter Machine Uptime** | Uptime hours / Total hours × 100 | > 97% |
| **Seasonal Stock Build Compliance** | Actual build / Target build × 100 | > 90% |
| **Returns Rate** | Returns value / Sales value × 100 | < 2% |
| **Dead Stock %** | Non-moving stock value / Total stock × 100 | < 5% |

---

## Asian Paints — SCM Approach

| Capability | Detail |
|---|---|
| **Colour technology** | 2000+ colours via tinting machine at 40,000+ dealer points |
| **SAP integration** | Branch orders → depot → plant fully integrated |
| **Demand sensing** | Real-time POS data from dealers feeds forecasting model |
| **Distribution** | 27 manufacturing plants + 350+ depots across India |
| **Project sales** | Dedicated project team handles large B2B orders with separate supply track |
| **Sustainability** | Water-based paint push reduces solvent usage and hazmat risk |

---

## Tips for Paint Industry SCM

1. **Branch sales team input is critical** — they know upcoming project pipeline; include in forecast
2. **Do not apply national seasonality to all branches** — North India vs Kerala have different monsoon timing
3. **Slow-moving colour identification** — run monthly dead stock report per branch; push via dealer schemes
4. **Tinter cartridge as inventory item** — often overlooked; treat it like a critical spare part (VED-V)
5. **Postponement is your friend** — resist pressure to pre-mix colours in bulk; tint at point of sale
6. **Depot as buffer, not stockpile** — depots should carry 20–30 days; not 60+ days
7. **Track return reasons** — wrong colour, damage, excess order; each has a different SCM fix

---

## Related Concepts
- [[Demand Forecasting Methods]]
- [[ABC VED SDE FSN Analysis]]
- [[Safety Stock]]
- [[Replenishment Models Q vs P]]
- [[Bullwhip Effect]]
- [[Distribution Networks]]
