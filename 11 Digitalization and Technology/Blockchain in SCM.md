# Blockchain in Supply Chain

> **Source:** Kuldeepak Ch.5
> **Tags:** #technology #blockchain #traceability

---

## What Is Blockchain?

Blockchain is a **distributed digital ledger** stored in cryptographic strings (blocks) across a peer-to-peer network of computers (nodes).

Key properties:
- **Distributed** — no single owner; copies held across all nodes
- **Immutable** — once written, cannot be altered (consensus algorithm)
- **Verified** — digital signatures and keys authenticate every entry
- **Transparent** — all authorised parties can view the chain

---

## How Blocks Form a Chain

```
Block 1: [Hash of Block 0 | Transaction Data | Timestamp | New Hash]
Block 2: [Hash of Block 1 | Transaction Data | Timestamp | New Hash]
Block 3: [Hash of Block 2 | Transaction Data | Timestamp | New Hash]
```

Any tampering with Block 2 changes its hash → breaks the chain → detected by consensus.

---

## Supply Chain Applications

| Use Case | Description |
|---|---|
| **Shipment tracking** | Digital approval and tracking of shipments — accessible to customs, port authority, consignor, consignee, agents |
| **Pharmaceutical traceability** | Track high-value medicines from manufacturer to patient — includes payment verification |
| **Food safety** | Trace farm-to-fork in seconds; identify contamination source |
| **Anti-counterfeiting** | Verify product authenticity at every SC stage |
| **Smart contracts** | Auto-trigger payment when delivery is confirmed on-chain |
| **Supplier compliance** | Immutable record of certifications, audits, ESG data |

---

## Benefits

| Benefit | Description |
|---|---|
| **Transparency** | All parties see the same version of truth |
| **Traceability** | Full history of product movement and custody |
| **Trust** | No intermediary needed to verify — the chain is the proof |
| **Speed** | Eliminates paper-based documentation delays |
| **Security** | Cryptographic protection; no single point of failure |

---

## Challenges

- High energy consumption (proof-of-work consensus)
- Integration with legacy ERP/WMS systems
- Requires all SC partners to participate and adopt
- Governance questions — who manages the network?

---

## Related Concepts
- [[Industry 4.0]]
- [[Control Towers]]
- [[Information Driver]]
