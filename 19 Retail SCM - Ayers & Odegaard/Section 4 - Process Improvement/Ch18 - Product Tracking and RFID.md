# Ch 18 — Product Tracking Along Retail Supply Chains

> **Source:** Ayers & Odegaard, Chapter 18
> **Tags:** #retail #RFID #tracking #barcode #technology #Ayers

---

## Evolution of Product Tracking

| Era | Technology | Capability |
|---|---|---|
| **Low-tech retailing** | Manual count, paper records | Store-level only; slow; error-prone |
| **Basic barcode (1D)** | EAN-13, UPC — scan at POS | Item-level identification; inventory management |
| **2D barcode / QR code** | More data; batch/lot info | Supply chain event tracking |
| **RFID** | Radio Frequency Identification | Pallet/case/item level; no line-of-sight needed |
| **RTLS (Real-Time Location System)** | Active RFID + sensors | Real-time location of every item in warehouse/store |
| **IoT + blockchain** | Sensor + distributed ledger | Immutable track-and-trace; provenance verification |

---

## RFID — How It Works

| Component | Role |
|---|---|
| **RFID tag** | Attached to product/pallet/case; stores unique ID + data |
| **RFID reader** | Emits radio waves; reads multiple tags simultaneously (no line-of-sight) |
| **Middleware** | Processes raw RFID data; filters and routes to ERP/WMS |
| **ERP/WMS** | Uses RFID events to update inventory records in real time |

### Passive vs Active RFID

| Type | Power Source | Read Range | Use |
|---|---|---|---|
| **Passive** | Powered by reader signal | 1–5 metres | Item/case tracking in stores and warehouses |
| **Active** | Own battery | Up to 100 metres | High-value assets, vehicles, cold chain monitoring |

---

## Retail Applications of RFID

| Application | Benefit |
|---|---|
| **Receiving at DC** | Auto-receive entire pallets; no manual scan |
| **Put-away verification** | Confirm item placed in correct bin |
| **Inventory cycle counts** | Handheld reader counts shelf in minutes vs hours |
| **Loss prevention / shrinkage** | Detect unpaid items at store exit |
| **Out-of-stock detection** | Reader at shelf edge detects when item is removed |
| **Recall management** | Instantly locate all units of a recalled batch |
| **Cold chain monitoring** | Active RFID with temperature sensor — continuous cold chain log |

---

## Walmart RFID Mandate (Context)

Walmart mandated RFID tagging from top 100 suppliers in 2005:
- **Result:** Dramatic reduction in out-of-stocks on shelves
- **Lesson:** RFID value requires both retailer AND supplier adoption; mandates accelerate adoption

---

## Tracking in Transit

| Method | Description |
|---|---|
| **GPS tracking** | Vehicle location; ETA prediction |
| **Geofencing** | Alert when vehicle enters/exits defined zone |
| **Temperature logging** | Continuous cold chain compliance record |
| **Electronic Proof of Delivery (ePOD)** | Digital signature at delivery; triggers payment |

---

## The Future: RTLS (Real-Time Location System)

A future RTLS system described by Ayers & Odegaard:
- Every item in the warehouse has an active RFID tag
- System knows the exact location of every unit at all times
- Picking is directed by system to nearest available unit
- Inventory accuracy approaches 100% without any manual counting
- Returns are instantly identifiable by location

---

## Related Concepts
- [[Industry 4.0]]
- [[Blockchain in SCM]]
- [[Digital Twins]]
- [[Warehouse KPIs]]
- [[Warehouse Design and Flow]]
