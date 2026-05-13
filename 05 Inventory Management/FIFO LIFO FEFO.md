# FIFO / LIFO / FEFO

> **Source:** Kuldeepak Ch.4
> **Tags:** #inventory #dispensing #methods

---

## FIFO — First In, First Out

**Definition:** The oldest stock is picked and shipped first.

**When to use:**
- Products with expiry risk (food, pharma, cosmetics)
- Products that age poorly (fashion, electronics)
- When minimising obsolescence is priority

**Examples:** FMCG, apparel, fresh food, any perishable goods

---

## LIFO — Last In, First Out

**Definition:** The most recently received stock is picked first.

**When to use:**
- Products that appreciate in value over time
- When inflation makes recent stock more expensive (accounting advantage)
- Bulk commodities stored in silos / tanks where physical access is impossible from bottom

**Examples:** Coal (stockpile), wine (vintage appreciation), some raw materials in certain accounting systems

> **Note:** LIFO is not permitted under IFRS (only under US GAAP) for financial reporting.

---

## FEFO — First Expired, First Out

**Definition:** The batch with the earliest expiry date is picked first — regardless of when it was received.

**When to use:**
- Any product with an expiry date
- Particularly critical when batch lead times vary (some batches may have shorter shelf life)
- More precise than FIFO for expiry management

**Examples:** Pharmaceuticals, processed foods, medical devices, vaccines

**LEFO (Last Expired, First Out):** Rarely used — opposite of FEFO; applicable only in very specific scenarios.

---

## Batch Tracking (related concept — Kuldeepak)

Tracks a specific set of products based on:
- Supplier details
- Manufacturing location
- Expiry date
- Production shift

**Benefits:**
- Track expiry dates for FEFO compliance
- Track returns and pinpoint defect sources
- Accurate costing per batch

---

## Implementation Tools

- **Colour-coded stickers** on batches (by month of manufacture) → quick visual FIFO/FEFO
- **WMS batch management** → system enforces FEFO at picking stage
- **Barcode / RFID** → scan to confirm correct batch picked

---

## Related Concepts
- [[ABC VED SDE FSN Analysis]]
- [[Warehouse KPIs]]
- [[Industry 4.0]]
