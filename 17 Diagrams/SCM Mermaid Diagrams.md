# SCM Mermaid Diagrams

> **Tags:** #diagrams #mermaid #visual

---

## Basic Supply Chain Flow

```mermaid
graph LR
  S[Supplier] -->|Raw Materials| M[Manufacturer]
  M -->|Products| D[Distributor]
  D -->|Bulk| R[Retailer]
  R -->|Units| C[Customer]
  C -.->|Demand Signal| R
  R -.->|Orders| D
  D -.->|Forecast / Orders| M
  M -.->|Purchase Orders| S
```

---

## Three Flows in a Supply Chain

```mermaid
graph TD
  S[Supplier] -->|Product Flow| M[Manufacturer]
  M -->|Product Flow| DC[Distribution Centre]
  DC -->|Product Flow| Retail[Retailer]
  Retail -->|Product Flow| Cust[Customer]
  Cust -->|Fund Flow| Retail
  Retail -->|Fund Flow| DC
  DC -->|Fund Flow| M
  M -->|Fund Flow| S
  Cust -.->|Information Flow| Retail
  Retail -.->|Information Flow| DC
  DC -.->|Information Flow| M
  M -.->|Information Flow| S
```

---

## Decision Phases

```mermaid
graph TD
  A[Strategic Design<br/>3-10 years<br/>Facility location, Network, Capacity] --> B[Planning<br/>Quarter to Year<br/>Markets, Inventory policy, Procurement]
  B --> C[Operational<br/>Daily to Weekly<br/>Individual orders, Scheduling, Picking]
```

---

## 6 Supply Chain Drivers

```mermaid
mindmap
  root((SC Performance))
    Logistical
      Facilities
      Inventory
      Transportation
    Cross-Functional
      Information
      Sourcing
      Pricing
```

---

## Warehouse Material Flow

```mermaid
graph LR
  subgraph I-Flow
    IN1[Inbound Dock] --> ST1[Storage] --> OUT1[Outbound Dock]
  end
  subgraph U-Flow
    IN2[Inbound Dock] --> ST2[Storage]
    ST2 --> OUT2[Outbound Dock]
    IN2 -.->|Short circuit| OUT2
  end
```

---

## EOQ Cost Curve

```mermaid
xychart-beta
  title "EOQ: Total Cost = Ordering Cost + Holding Cost"
  x-axis "Order Quantity" [100, 200, 300, 400, 500, 600, 700]
  y-axis "Annual Cost (₹)" 0 --> 50000
  line [50000, 30000, 25000, 22000, 22000, 23000, 25000]
  line [5000, 10000, 15000, 20000, 25000, 30000, 35000]
```

---

## Bullwhip Effect

```mermaid
graph TD
  C[Consumer: Low Variance] --> R[Retailer: Slightly Amplified]
  R --> W[Wholesaler: More Amplified]
  W --> D[Distributor: High Amplified]
  D --> M[Manufacturer: Extreme Variance]
  style C fill:#90EE90
  style R fill:#ADFF2F
  style W fill:#FFD700
  style D fill:#FF8C00
  style M fill:#FF4500
```

---

## DMAIC Process

```mermaid
graph LR
  D[Define<br/>Problem + VOC] --> M[Measure<br/>Baseline data]
  M --> A[Analyse<br/>Root causes]
  A --> I[Improve<br/>Implement solution]
  I --> C[Control<br/>Sustain gains]
  C -.->|Monitor| D
```

---

## Lean Wastes (TIMWOODS)

```mermaid
pie title 8 Wastes of Lean
  "Transportation" : 12.5
  "Inventory" : 12.5
  "Motion" : 12.5
  "Waiting" : 12.5
  "Overproduction" : 12.5
  "Overprocessing" : 12.5
  "Defects" : 12.5
  "Skills" : 12.5
```

---

## Supply Chain Coordination — Bullwhip Solutions

```mermaid
mindmap
  root((Reduce Bullwhip))
    Information
      Share POS data with suppliers
      Use VMI
      Centralise demand signal
    Orders
      Eliminate batch ordering
      Continuous review systems
      EDI auto-replenishment
    Pricing
      EDLP instead of promotions
      Reduce forward buying incentive
    Allocation
      Base on historical demand not current orders
      Eliminate shortage gaming
```
