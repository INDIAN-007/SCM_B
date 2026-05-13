# Poka-Yoke — Error Proofing

> **Source:** Kuldeepak Ch.6
> **Tags:** #lean #pokayoke #quality #errorproofing

---

## Definition

Poka-Yoke (Japanese: "avoid inadvertent mistakes") is a technique for **designing processes that prevent errors from occurring** or immediately detect and signal them.

Developed as part of the Toyota Production System.

---

## Three Strategies

### 1. Shut-Out Strategy
The process is designed so the error **cannot physically occur**.

Example: Machine with safety sensor — if body part touches the danger zone, machine automatically shuts off.

### 2. Control Strategy
The process **stops if a mistake is made** — cannot continue without correction.

Example:
- DIY furniture with numbered steps and notches — if assembled wrong, next piece won't fit
- PIN pad that locks after 3 wrong entries

### 3. Attention Strategy
The process **warns the operator** before or as an error is about to happen.

Example: Warning lights, colour-coded zones, floor markings indicating maximum reach.

---

## Supply Chain / Warehouse Examples (Kuldeepak)

| Example | Strategy |
|---|---|
| Barcode / RFID on each lot at origin — prevents wrong routing or wrong delivery | Control |
| Vehicle inspection checklist before dispatch — prevents damaged goods | Control |
| Auto-shut nozzles at fuel pumps — prevents overfilling | Shut-out |
| Colour-coded stickers by batch/month — enforces FIFO/FEFO visually | Attention |
| Rack limit switches with continuous noise until gate closed — prevents falls | Shut-out |
| WMS system requiring scan confirmation before pick completion | Control |

---

## Design Principles

1. **Simple** — should not require specialised knowledge to operate
2. **Inexpensive** — low cost to implement widely
3. **Immediate** — detects error at the point of creation, not downstream
4. **100% inspection** — checks every unit, not a sample

---

## Related Concepts
- [[Kaizen and Continuous Improvement]]
- [[FMEA]]
- [[Six Sigma and DMAIC]]
