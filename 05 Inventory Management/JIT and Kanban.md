# JIT and Kanban

> **Source:** Kuldeepak Ch.4 & Ch.6
> **Tags:** #inventory #jit #kanban #lean

---

## Just-In-Time (JIT)

### Philosophy
JIT is a philosophy — conceptualised and adopted by **Toyota Production Systems** — to make materials available exactly at the time of requirement. No earlier, no later.

**Core principle:** Eliminate inventory as waste. Inventory is a symptom of poor SC coordination.

### Goals
- Reduce inventory holding cost
- Improve working capital flows
- Eliminate dead stock and obsolescence
- Force quality improvement (no buffer to hide defects)

### Requirements for JIT
- Reliable, responsive suppliers with short lead times
- High forecast accuracy (or true demand pull)
- Disciplined production scheduling
- Strong supplier relationships
- Robust transportation network

### JIT in Distribution (Kuldeepak)
- **Drop shipping:** No inventory held by seller — order forwarded to supplier who ships directly to customer
- **Consignment Inventory:** Supplier retains ownership until goods are sold; consignee pays only on sale

---

## Kanban

### Definition
Kanban (Japanese: "visual card / signboard / billboard") is a **scheduling system** that supports JIT. Physical or digital cards signal when material is needed — ensuring proper visibility at each processing point.

### How It Works
```
Production Point ← Kanban Card (signal to replenish) ← Upstream Process
                → Material Replenished →
```

- When a production station consumes its inventory → triggers a Kanban card
- Upstream process (supplier or prior production stage) produces/delivers exactly what was consumed
- Nothing is produced without a Kanban signal → pure pull system

### Types of Kanban
| Type | Description |
|---|---|
| **Production Kanban** | Authorises production of a specific quantity |
| **Withdrawal Kanban** | Authorises movement of material from upstream to downstream |
| **Supplier Kanban** | Sent to external suppliers to trigger delivery |

### Kanban Beyond Manufacturing
Kuldeepak uses Kanban for project tracking (e.g., warehouse site selection):
```
Backlog → In Progress → Review → Done
```
Similar to modern Agile / Scrum boards.

---

## JIT vs Traditional Inventory

| Dimension | Traditional | JIT |
|---|---|---|
| Inventory philosophy | Buffer against uncertainty | Eliminate waste |
| Stock levels | High safety stock | Near-zero buffer |
| Supplier relationship | Transactional | Long-term partnership |
| Quality focus | Inspect after production | Build quality in (Jidoka) |
| Production | Push (forecast-based) | Pull (demand-based) |

---

## Related Concepts
- [[Lean Philosophy]]
- [[TIMWOODS - 8 Wastes]]
- [[Safety Stock]]
- [[Push vs Pull Systems]]
