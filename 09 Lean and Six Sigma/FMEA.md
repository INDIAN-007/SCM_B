# FMEA — Failure Mode and Effects Analysis

> **Source:** Kuldeepak Ch.6
> **Tags:** #lean #fmea #risk #quality

---

## Definition

FMEA is a **proactive risk-identification methodology** — performed before failures occur to take corrective action in advance and minimise loss.

---

## Types of FMEA

| Type | Scope |
|---|---|
| **PFMEA** (Process FMEA) | Risks in the manufacturing or operational process |
| **DFMEA** (Design FMEA) | Risks in the product design itself |

---

## Three Dimensions — RPN

Each potential failure mode is rated on three factors (scale 1–10 each):

| Dimension | Scale | Description |
|---|---|---|
| **Occurrence (O)** | 1 = Very unlikely → 10 = Almost certain | Probability this failure mode will occur |
| **Severity (S)** | 1 = No impact → 10 = Catastrophic | Impact on customer or process if it occurs |
| **Detection (D)** | 1 = Easily detected → 10 = Cannot be detected | Ability to catch the failure before it reaches customer |

```
RPN (Risk Priority Number) = Occurrence × Severity × Detection
```

**Action priority:** Focus improvement efforts on highest RPN scores first.

---

## FMEA Process Steps

1. List all functions and requirements of the process/design
2. Identify potential failure modes for each function
3. Identify effects of each failure mode
4. Rate O, S, D for each failure mode
5. Calculate RPN = O × S × D
6. Prioritise high-RPN items for action
7. Define recommended actions
8. Assign responsibility and target date
9. Implement and re-assess RPN after improvement

---

## Example (Supply Chain)

| Process Step | Failure Mode | Effect | O | S | D | RPN |
|---|---|---|---|---|---|---|
| Receiving | Wrong item received | Wrong stock dispatched to customer | 4 | 8 | 6 | 192 |
| Picking | Wrong quantity picked | Customer order short | 5 | 7 | 5 | 175 |
| Cold chain | Temperature excursion | Product spoilage / recall | 2 | 10 | 4 | 80 |

*Action: Address "Wrong item received" (RPN 192) first.*

---

## FMEA in Risk Management

FMEA can be applied to **supply chain disruption risk**:
- Failure mode = supplier going bankrupt
- Effect = production stoppage
- O = historical frequency of supplier failures
- S = impact on production output
- D = how quickly you would know (supply chain visibility)

---

## Related Concepts
- [[Six Sigma and DMAIC]]
- [[Poka-Yoke]]
- [[Risk Management in Global SC]]
