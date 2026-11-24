# C5 delivery panel, round 1: factory-built 5 MW power blocks

Date of simulation: 24 November 2026. Everything below is a simulated hypothesis built from archetypes, not customer or supplier validation. No real person was interviewed.

Evidence labels: [notes] = founder research notes (power_grid.md, physical_production.md). [source: URL] = checked in this session. [DK] = domain knowledge, unverified.

Searches used: 8 of 8 (7 searches, 1 fetch). No source gave a clean $/MW bill of materials, so the BOM below is [DK] and is the weakest part of this assessment.

## Facts checked this session

- Fibrebond: about $378M revenue in the 12 months to 28 Feb 2025; $110M estimated 2025 adjusted EBITDA; Eaton paid $1.4B, closed 1 Apr 2025 [source: https://www.businesswire.com/news/home/20250401369562/en/Eaton-completes-acquisition-of-Fibrebond].
- Lead times, contractor data 2026: 15 kV switchgear 52-80 weeks; 38 kV 78-104 weeks; pad-mount transformers 0-5 MVA 40-65 weeks; small dry-type (0-2 MVA, 480-208 V) 20-32 weeks [source: https://terrapincg.com/news/switchgear-transformer-generator-lead-times-2026]. Data-centre-spec MV gear approaches 2-3 years at the busiest makers [notes].
- Nvidia 800 VDC partners: Eaton, Schneider and Vertiv for data-centre power systems; Delta and Flex for power-system components; full-scale 800 VDC production coincides with Kyber in 2027 [source: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/]. Vertiv's 800 VDC portfolio was scheduled for H2 2026 [source: https://www.vertiv.com/en-emea/about/news-and-events/news-releases/from-vision-to-readiness-vertiv-collaborates-with-nvidia-to-advance-800-vdc-platform-designs-to-power-the-next-generation-of-ai-factories/]. An Eaton executive expected only a few 800 VDC deployments in the following year [source: https://spectrum.ieee.org/data-center-dc].
- 800 VDC safety standards are unfinished: UL is running a gap analysis of 60+ power standards with OCP, ABB and Eaton, and has launched a UL 2877 programme for MV solid-state power units [source: https://www.ul.com/news/building-safety-path-next-generation-data-center-power]. IEEE 1584 does not cover DC arc flash and NFPA 70E has no PPE table for 600-1000 VDC [source: https://eepower.com/industry-articles/powering-ai-safely-in-a-new-era-of-high-voltage-data-centers/].
- UL 891: an Assemblers Programme lets a builder assemble under an OEM's already-tested file; own designs above Annex G limits need a booked third-party high-power lab [source: https://www.ul.com/services/ul-891-general-coverage-program]. No public timeline or price was found.

## What the product physically is (panel's reading)

A 5 MW AC block with N+1 UPS and five minutes of lithium-ion is roughly: 15 kV line-up of 3-5 sections, two or three 2.5-3 MVA transformers, 480 V or 415 V switchgear with 4,000-5,000 A power breakers, 5-6.25 MW of UPS, battery cabinets, relays and controls, HVAC and fire suppression, in a steel building. Weight 80-120 tonnes [DK]. That is not one shippable enclosure. It ships as 3-5 road modules and is rejoined on site. The brief's "one enclosure, 10 days" is wrong on both counts.

## Persona 1. Channel manager, large electrical OEM (MV switchgear, breakers, own skids)

- Incentives: segment operating margin near 30%, backlog up 33% [notes]. Every breaker is worth more inside our own line-up or our own enclosure business than sold loose. My bonus is on margin and on protecting named accounts.
- Alternatives: sell the same breaker to our own skid plant, or to one of several hundred existing panel-builder accounts with 20 years of payment history.
- Decision: **will supply, at the back of the queue, on new-account terms. No allocation.**
- Terms [DK]: complete listed switchgear only, through distribution or the OEM channel. 15 kV metal-clad 60-80 weeks. LV switchgear 45-60 weeks. Loose LV power breakers 30-45 weeks. Price at list times 0.55-0.65 against 0.40-0.45 for large accounts, so the start-up pays 25-40% more than my own skid plant for the same gear. 30% down, credit limit $1-2M, quotes valid 30 days, copper and steel escalators. No licensed-assembler agreement for 6-12 months, and only after a factory audit.
- If the start-up names a hyperscaler end customer that holds a frame agreement with us, I tell my account team, and we quote our own skid to that customer.
- Changes the answer: a three-year take-or-pay volume commitment with 30-50% prepaid capacity reservation; or a top-five buyer formally directing its own allocation to this integrator.

## Persona 2. Sales manager, transformer maker (dry-type and liquid-filled distribution)

- Incentives: fill slots with repeat buyers who forecast accurately. This size class is not in acute shortage: the 2025 distribution deficit was about 10% and brokers deliver standard units in 12-14 months [notes].
- Decision: **yes, will sell. This is the least constrained input.**
- Terms [DK unless marked]: 2.5 MVA liquid-filled 15 kV/480 V, $110-160k, 40-65 weeks [source: Terrapin, above]. 3 MVA cast-coil dry-type, $180-260k, 30-50 weeks. 35% non-refundable deposit to hold a slot, balance before shipment, copper and core-steel index. Standard warranty 12 months from energisation or 18 from shipment. Five-year warranty costs 1-2% per added year.
- 800 VDC variant: a phase-shifting rectifier transformer is a custom design, 50-70 weeks for the first article.
- Changes the answer on lead time: a blanket order of 100+ identical units a year with a 12-week frozen schedule gets 26-30 weeks.

## Persona 3. Operations head, contract manufacturer / enclosure fabricator

- Incentives: keep bays full on cost-plus work without carrying anyone's inventory or warranty. E-house shops are full of data-centre work now [notes: 80+ vendors, Vertiv modular lead times over 12 months].
- Decision: **will sign a build agreement, on consignment and take-or-pay. Will not carry material, design authority, listing or warranty.**
- Terms [DK]: shells in 12-20 weeks. Integration at labour and overhead plus 12-18%, 3-5% handling on consigned gear. NRE $1-2M. Dedicated 100,000 sq ft, 12-month minimum commitment. Ramp to 4-8 blocks a month (240-480 MW a year) after six months.
- The start-up must own: drawings and BOM, all long-lead procurement and the cash for it, the listing file, test procedures, a 5 MW full-load test bay ($5-10M, plus a multi-MW utility service or generators and load banks that I do not have), field commissioning crew, warranty.
- Constraint I cannot fix: wiremen, relay technicians and test engineers. The electrician shortage [notes] follows the work into the factory, at lower wage but the same scarcity for testers.
- Note: large contract manufacturers are also on Nvidia's partner list [source: Nvidia blog, above] and sell their own power modules. Assume anything you show them is seen by a competitor.

## Persona 4. Certification body and local inspector

AC block:
- No single listing covers the block. It is a set of listed parts (LV switchgear UL 1558 or switchboard UL 891, UPS UL 1778, dry transformer UL 1562, battery UL 9540 with 9540A fire test, MV gear tested to IEEE C37.20.2) in a building approved under each state's industrialised-building programme, or field-evaluated per unit [DK].
- Path A, assemble an OEM's listed gear: 3-5 months, $150-400k for file, factory audit and first inspections. Per-unit field evaluation where the inspector asks: $10-30k, 2-4 weeks. State modular approvals: 2-6 months each [DK].
- Path B, own switchgear design: short-circuit and temperature-rise testing at a high-power lab, 9-15 months and $1-2.5M including lab slots and re-tests; first-time failure is common [DK]. Own battery system with 9540A: 9-15 months, $0.5-1.5M [DK].
- Inspector: I accept listed gear with a field-evaluation label. I will ask about NFPA 855 battery siting, working clearances inside the enclosure, and arc-flash labels. Batteries inside the same enclosure as switchgear is the item most likely to be rejected by a fire marshal [DK].
- Utility: no interest in the block if it sits behind the customer's substation. If the MV line-up is the service point, the utility's relay and metering spec applies and adds 3-6 months [DK].
- Hyperscaler qualification, separate from code: 12-24 months of audits, first-article inspection and a pilot of 5-20 MW [DK].

800 VDC variant:
- **Cannot quote a fixed time or cost.** Standards are in gap analysis [source: UL, above]. NEC treatment still needs case-by-case approval, and DC arc-flash methods are unsettled [source: eepower, above].
- Estimate [DK]: 18-30 months and $3-8M if the start-up designs the rectifier; 12-18 months and $1-2M if it integrates someone else's certified rectifier. As of May 2026 no vendor had a UL-certified data-centre SST [notes].

## Persona 5. Veteran executive, established modular power / e-house builder

- Margin: 28-35% is real only on enclosure plus integration scope where the customer free-issues the gear. That is how the Fibrebond numbers ($110M EBITDA on $378M-plus revenue [source: Business Wire, above]) should be read [DK inference]. When the gear runs through your revenue, blended gross margin is 15-22% for an established shop and 5-12% for a start-up in years one to three [DK].
- Revenue per MW: large buyers direct or free-issue the major equipment under their own frame agreements. Then you bill $0.3-0.5M per MW, not $1.6M [DK]. A 100 MW order is $35-60M, or $160M of which $105-125M is pass-through.
- Working capital: 25-35% of revenue for an independent [DK]. Big buyers refuse 30% deposits without an advance-payment bond; expect 10-20% and net 60-90. The last 20% is hostage to the customer's site readiness, often 3-6 months late.
- Warranty: 1.5-3% of revenue mature; 4-6% over the first 100 units [DK]. OEM warranties stop at 12-18 months, so years two to five are yours. One serial defect across 20 blocks is a company-ending retrofit.
- Liquidated damages: hit on about one project in five, 2-5% of contract when hit, mostly negotiated down against customer-caused delay [DK]. At 12-15% real margin a capped 10% claim erases the job. Customers will also call 0.5% a week weak: it is about $35k per MW-month against the $500k per MW-month they lose [notes].
- Engineering repeated: 30-40% of hours on a customer's first project, 10-15% on repeats [DK]. Every hyperscaler has its own topology, voltage, relay brand and monitoring protocol. A fixed catalogue block sells only to neoclouds and smaller colocation firms.
- Site time: set, rejoin, terminate and commission is 4-8 weeks, not 10 days. Notes put field commissioning at 3-8 months as the largest remaining gap [notes].
- Decision: **would not invest; would hire the founder.**

## Persona 6. Surety / insurer

- Request: performance and advance-payment bonds on a $160M supply contract (typically 10-20%, so $16-32M, plus up to $48M for the deposit), delay damages, five-year warranty.
- Decision: **refuse on an unsecured basis.**
- Terms I would write [DK]: bonds against 100% cash or letter-of-credit collateral, or a creditworthy parent indemnity; premium 1-3% a year. Warranty bond limited to 12-24 months. Delay damages are a business risk, not insurable on their own. An insurance-backed five-year warranty needs 12+ months of field reliability data, a third-party engineering report and 1-3% of product price.
- Reason: no net worth, no completed projects, single-product concentration, suppliers who are also competitors. Venture investors do not give indemnities.
- Changes the answer: $50M+ of unencumbered equity on the balance sheet, three completed deliveries, and a contract manufacturer or OEM step-in agreement. Then partial collateral (30-50%).

## Persona 7. Technical lead familiar with Nvidia's 800 VDC reference architecture

- What is specified: 800 VDC bus to the rack, AC-to-DC power racks or sidecars at row level first, then centralised rectifiers and battery racks, then MV-to-800 VDC solid-state transformers; energy storage to smooth GPU load swings; DC protection and grounding scheme [notes; source: Nvidia blog, above].
- Timing: sidecars 2026-2027 with the AC backbone kept; Kyber makes 800 VDC mandatory 2027-2028; centralised rectifiers late 2028-2029; SSTs after 2029 [notes].
- Already qualified: Vertiv, Eaton, Schneider, Delta, Flex, with ABB on protection and DG Matrix as the SST in the MGX reference [source: Nvidia blog; notes]. SST start-ups hold $60-178M each [notes].
- The qualified item is the conversion hardware. A company with no power electronics is not a candidate for the list; it is a buyer from the list.
- "Approved vendor lists reopen in 2027-2028" is wrong in direction. The list for the 800 VDC era was largely set in 2025-2026. In phases 1-2 the AC block upstream barely changes, so nothing reopens there either.
- Decision: **would not sponsor qualification.** Would look again at a working, certified 1 MW-plus rectifier or DC protection product with test data. From a November 2026 start that is 2029 at the earliest.

## Persona 8. Senior power-electronics / switchgear engineer, prospective co-founder

- Position: $250-400k total pay with appreciating stock at an incumbent, and offers from funded SST start-ups [DK].
- Decision: **no at seed. Yes only if three things exist: $50M+ committed, a customer deposit in the bank, and a signed supply or licence agreement for breakers.**
- What breaks, in order:
  1. Breaker and MV gear allocation. The schedule is whatever the slowest competitor-supplier ships.
  2. Cash. Suppliers want 30-50% down and the balance before shipment; the customer's 50% arrives only at factory test.
  3. Heat. Transformers and UPS in a sealed enclosure at 45 C ambient force derating or more HVAC than the layout allows.
  4. Fault duty and arc flash. 65-100 kA bus bracing in a compact enclosure, and battery fire separation.
  5. Customer variation. The "standard" block forks into four variants by the third customer.
  6. Transport. Module splits create field joints, which bring back field labour and commissioning time.
  7. On 800 VDC: DC fault interruption and no settled standard.

## Panel estimates against the founder's numbers

Bill of materials and cost per MW, AC block, N+1 UPS, five minutes of lithium-ion, start-up buying prices [DK; no public source found]:

| Item | $k per MW |
|---|---|
| 15 kV switchgear, relays, instrument transformers | 80-130 |
| Transformers with redundancy | 90-150 |
| LV switchgear or switchboards | 120-200 |
| UPS modules, N+1 | 200-300 |
| Lithium-ion batteries, five minutes | 120-200 |
| Busway, cable, copper, terminations | 60-100 |
| Enclosure, HVAC, fire suppression, lighting | 90-150 |
| Controls, monitoring, metering | 30-60 |
| **Purchased material** | **~1,000-1,250** (range of sums 790-1,290; low ends do not all occur together) |
| Factory labour, test, overhead | 100-150 |
| Freight, rigging, site commissioning | 50-80 |
| Warranty reserve (3-5%) | 50-80 |
| **Total cost of delivery** | **~1,200-1,550** (mid-point about 1,380, a 14% gross margin at $1.6M) |

Cross-check: total electrical content is $3.6-4.8M per MW including generators, rack power and busway [notes], so $1.0-1.25M of material for this scope is consistent.

| Founder number | Panel figure | Basis |
|---|---|---|
| Price $1.6M/MW | $1.4-1.9M/MW for the AC block is a market price, so the price is roughly right. 800 VDC block with rectifier or SST: $2.2-3.0M/MW; at $1.6M it loses money. Where gear is free-issued, billable revenue is $0.3-0.5M/MW. | SST alone $1.0-1.5M/MW [notes]; [DK] |
| Gross margin 25-30% | 5-12% in years one to three; 15-20% at volume with direct OEM terms; 28-35% only on integration-only scope | Persona 5; start-up pays 25-40% more for gear |
| 26 weeks from order | 55-80 weeks for a new buyer of MV and LV gear. 30-40 weeks only with long-lead gear pre-bought 9-12 months ahead at about $1.0M/MW of own cash | Terrapin lead times; [notes] |
| Factory $30-40M | $30-45M is fair for leased, assembly-only, 300-400 MW a year with two test bays. $70-110M with in-house enclosure and bus fabrication. An 800 VDC test bay adds $10-20M | [DK] |
| 10 days on site | 4-8 weeks to set, rejoin and commission; full integrated test follows the hall's schedule | [notes]; [DK] |
| Five-year warranty | Costs 3-5% of revenue and cannot be passed to suppliers after month 12-18 | Personas 2, 5, 6 |
| Not stated: working capital | Peak cash out of $65-90M per 100 MW in build on the founder's own payment terms; $150-250M at a 300 MW a year run-rate with 26-week delivery. On hyperscaler terms, worse | Materials $105-125M plus labour $10-15M paid before the 50% factory-test payment; deposit received $48M |
| Not stated: pre-revenue burn | $20-30M a year, 60-90 staff (15-20 engineers, 40-60 shop, 10-20 field commissioning) | [DK] |
| Not stated: time to first unit | AC block from listed gear: factory test 14-18 months from founding, set by gear lead time. Own switchgear design: 24-30 months. 800 VDC variant: 30-42 months | Personas 1, 4 |

## Full list of inputs, approvals, bottlenecks and failure modes

Material inputs: MV breakers and switchgear; LV power breakers; transformers; UPS modules; lithium-ion cabinets (tariff and foreign-entity exposure [notes]); protective relays; instrument transformers; copper bus and cable (tariff exposure [DK]); enclosure steel; HVAC units; clean-agent fire suppression; controls hardware; for 800 VDC, silicon carbide modules, DC breakers, rectifier transformers.

Approvals: listings for each assembly; factory follow-up inspections; state industrialised-building approvals; engineer-stamped drawings per state; local electrical permit and inspection; fire marshal sign-off on batteries; seismic certification where required ($100-300k [DK]); utility review if at the service point; oversize-load permits per state; customer vendor qualification; arc-flash study.

Bottlenecks, in order: (1) MV and LV switchgear allocation from competitors; (2) working capital; (3) customer qualification time; (4) test and commissioning staff; (5) full-load test power at the factory; (6) 800 VDC standards.

Failure modes: supplier slips and the start-up pays damages it cannot pass back; a customer free-issues gear and revenue falls 70%; a serial defect in the field; a failed short-circuit test adds 6-9 months; a cancelled or deferred order strands pre-bought inventory; incumbent plants opening in 2027-2028 [notes] shorten lead times just as the start-up reaches volume, removing the speed premium.

## Probabilities (panel's honest estimate)

- First paid commercial delivery within 18 months: about 25%. It requires a non-hyperscaler buyer, listed gear from a second-tier or independent builder at 30-40 weeks, and $40M+ raised by early 2027.
- $1 billion of annual recognised revenue within seven years: about 3%.
