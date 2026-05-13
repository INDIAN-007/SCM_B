# Automotive & Manufacturing — SCM Overview

> **Tags:** #industry #automotive #manufacturing #MRP #SCM

---

## Industry Profile

| Attribute | Characteristic |
|---|---|
| **Product Nature** | Complex BOM (Bill of Materials); thousands of components per vehicle |
| **Demand Pattern** | Derived demand (vehicle sales drive parts demand) |
| **Production Type** | Mixed MTO + MTS (variants are MTO; standard models are MTS) |
| **Key Methodology** | MRP (Material Requirements Planning), JIT, Kanban, Lean |
| **Key Risk** | Single-source components, supply disruption halts assembly line |
| **Companies** | Toyota, Maruti Suzuki, Tata Motors, Hyundai, Mahindra |

---

## Core Methods

| Method | Application |
|---|---|
| **MRP / MRP-II / ERP** | Explode BOM → calculate component requirements → generate purchase orders |
| **JIT + Kanban** | Parts delivered to assembly line exactly when needed; no WIP buildup |
| **Supplier Tiering** | Tier 1 directly supplies OEM; Tier 2 supplies Tier 1; etc. |
| **Single-piece flow** | Eliminate batch processing; move one unit at a time through production |
| **SMED** | Reduce changeover time; enable smaller batch sizes; more flexibility |
| **FMEA** | Risk-score every component and process; prevent failures before they happen |
| **Safety Stock by criticality** | Critical path components carry higher SS; commodity parts carry minimal |

---

## Automotive-Specific Concepts

### Bill of Materials (BOM)
- BOM = full list of all components, sub-assemblies, and raw materials needed to build one vehicle
- **Multi-level BOM:** Vehicle → Sub-assembly → Component → Raw material
- **Key SCM use:** Feed BOM into MRP system → generate component requirements based on production plan

### Takt Time
- `Takt Time = Available production time / Customer demand rate`
- Sets the rhythm of production; all upstream supply must match Takt Time
- **Example:** If 480 min/day available, demand = 240 units/day → Takt = 2 min/unit
- Every supply chain activity must be designed to feed at this rate

### Milk Run Logistics
- Instead of each supplier delivering separately, a truck runs a circuit collecting from multiple suppliers and delivering to the plant
- **Benefit:** Frequent small deliveries; lower inventory at plant; reduces truck idle time
- **Used by:** Toyota, Maruti Suzuki for local supplier clusters

---

## Automotive KPIs

| KPI | Target |
|---|---|
| Line Stoppage due to parts shortage | 0 incidents |
| Supplier On-Time Delivery | > 99% |
| Defective Parts PPM (parts per million) | < 50 PPM |
| Inventory Days (WIP) | < 1 day (JIT target) |
| BOM Accuracy | > 99.9% |

---

## Tips

1. **Never single-source a critical component** — always qualify a second supplier for long-lead, sole-source parts
2. **Supply chain visibility** — map your Tier 2 and Tier 3 suppliers; disruptions often originate there
3. **Buffer stock for single-source parts** — even JIT plants carry 30–60 days for sole-source critical components
4. **Quality at source** — defect escaping to assembly line costs 10× more than catching at supplier's end
5. **Supplier development** — invest in improving supplier quality and delivery capability; your chain is only as strong as your weakest Tier 1

---

## Related Concepts
- [[JIT and Kanban]]
- [[Lean Philosophy]]
- [[FMEA]]
- [[Make vs Buy Decision]]
- [[Risk Management in Global SC]]
