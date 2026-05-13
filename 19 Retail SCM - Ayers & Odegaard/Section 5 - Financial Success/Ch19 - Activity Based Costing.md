# Ch 19 — Understanding Supply Chain Costs (Activity-Based Costing)

> **Source:** Ayers & Odegaard, Chapter 19
> **Tags:** #retail #ABC-costing #cost-visibility #financial #Ayers

---

## Why Traditional Costing Fails in Supply Chains

Traditional cost accounting allocates overhead by department. It cannot answer:
- What does it cost to serve Customer A vs Customer B?
- What does it cost to stock Product X vs Product Y?
- Where exactly does cost occur across the multi-company SC?

**Result:** Companies make product, customer, and channel decisions based on wrong cost data.

---

## Activity-Based Costing (ABC) — Four Levels

Ayers & Odegaard describe a 4-step ABC implementation for retail SCs:

### Level I-A: Starting Point — Department Costs

| Department | Cost Items |
|---|---|
| Buying | Buyer salaries, travel, sample costs |
| DC/Warehouse | Labour, rent, utilities, equipment depreciation |
| Transportation | Carrier rates, fuel, driver cost |
| IT | System licences, support, development |
| Finance/Admin | Processing cost per PO, per invoice |

### Level II-B: Department Costs with Capital Recovery

Add capital cost (depreciation, cost of capital) to each department:
- `Total Dept Cost = Operating Cost + (Asset Value × Cost of Capital Rate)`
- Ensures decisions reflect true economic cost, not just cash spend

### Level III-C: Multicompany Process Cost

Map costs across company boundaries:
1. **Set process boundaries** — define start and end points (e.g., "order placement to shelf availability")
2. **Document process flow** — every step, who does it, how long it takes
3. **Decide cost categories** — labour, space, equipment, IT, overhead
4. **Assign costs to process steps** — proportion cost by activity driver (time, volume, etc.)
5. **Analyse findings** — where is cost concentrated? Which steps add value?

### Level IV-D: Activity-Based Cost by Product

Calculate fully-loaded cost per product line:
1. Gather product line volume and channel information
2. Adjust unit costs via engineering studies (actual time studies, not estimates)
3. Calculate product line profitability: `Product Margin = Revenue − Full ABC Cost`

---

## Why This Matters for Retail SC Managers

| Old View | ABC View |
|---|---|
| Product A has 40% gross margin — it's profitable | Product A requires 3× the handling; true margin is 12% |
| Customer B is our biggest account | Serving Customer B costs 60% of SC budget; they're barely profitable |
| SKU X is a staple — keep it in range | SKU X turns 1.5× and ties up $50K in inventory; it should be delisted |

---

## Common Retail Cost Categories (Ch 19)

| Cost Category | What It Includes |
|---|---|
| **Cost of Goods** | Product purchase price; import duties; freight-in |
| **Inventory Carrying Cost** | Capital cost, storage, insurance, obsolescence (typically 20–30% of inventory value/year) |
| **Ordering Cost** | PO processing, receiving, accounts payable per order |
| **DC/Warehouse Cost** | Receiving, put-away, picking, packing, dispatch per unit |
| **Transportation Cost** | Inbound (DC to supplier) + outbound (DC to store or customer) per unit |
| **Returns Cost** | Handling, inspection, restock, disposal per return |
| **Technology Cost** | WMS, TMS, ERP cost allocated per unit processed |

---

## Calculating Total SC Cost per Product

```
Total SC Cost (per unit) =
  COGS per unit
+ Inventory carrying cost per unit per year / Annual turns
+ Ordering cost / Annual order quantity
+ DC handling cost per unit
+ Inbound transport cost per unit
+ Outbound transport cost per unit
+ Returns cost × Return rate
+ Technology cost per unit
```

Compare to selling price to get **true product profitability**.

---

## Related Concepts
- [[Total Supply Chain Cost]]
- [[GMROI]]
- [[ABC VED SDE FSN Analysis]]
- [[Inventory Turnover]]
- [[Cash to Cash Cycle]]
