# C5 v1 demand panel, round 1: factory-built 5 MW power blocks

Date of simulation: 24 November 2026. Everything below is a simulated hypothesis built from the research notes, eight web checks and domain knowledge. It is not customer validation. No real person or order is quoted.

Evidence labels: [notes] = the founder's research notes; [source: URL] = checked in this session; [DK] = domain knowledge, unverified.

Web checks used: 8 of 8.
- S1: https://newsletter.semianalysis.com/p/the-wild-wild-west-of-lego-datacenters (fetched, first 100k characters)
- S2: https://flex.com/resources/understanding-the-medium-voltage-bottleneck-in-ai-expansion (fetched)
- S3: https://blogs.nvidia.com/blog/dsx-ready/ (fetched)
- S4: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/ (search snippet only)
- S5: https://www.vertiv.com/en-us/insights/articles/educational-articles/powering-the-future-of-ai-factories-vertivs-role-in-the-800-vdc-ecosystem/ (search snippet only)
- S6: https://newsletter.semianalysis.com/p/datacenter-anatomy-part-1-electrical (fetched; cost table is paywalled)
- Two further searches (per-MW cost breakdown; hyperscaler qualification timing) returned no usable primary figure. Per-MW prices by scope and qualification durations below are therefore [DK].

---

## 0. Shared facts the personas rely on

### 0.1 What equivalent scope costs today (per MW of block nameplate)

Scope as in the brief: medium-voltage switchgear section, transformer, low-voltage switchgear or DC distribution, UPS or rectifier with battery, protection and controls, enclosure. Excludes utility substation, generators, busway in the hall, rack power shelves.

| Buyer | Stick-built (equipment + field labor and materials) | Prefabricated skid or e-house, bought today | Label |
|---|---|---|---|
| Top-five hyperscaler, frame pricing | $1.0-1.3M | $0.9-1.2M turnkey; or $0.15-0.30M integration fee with the gear free-issued by the owner | [DK] |
| Wholesale colo | $1.2-1.6M | $1.3-1.7M | [DK] |
| Neocloud, spot buyer | $1.4-1.9M | $1.5-2.0M | [DK] |

Cross-checks that are sourced:
- Moving the power scope into a factory is about 5% cheaper per MW than field build; Schneider's own paper says module hardware costs about 40% more than traditional, but net first cost is 13% lower after labor. [source: S1]
- Whole-hall modular $13.5M/MW against $14.6M/MW stick-built. [notes]
- Total electrical content is $3.6-4.8M/MW across architectures (this includes generators, power racks and everything else). [notes]
- So the block is roughly 11-12% of build cost and about a third of the electrical content, not "45-70%". (Arithmetic: $1.6M / $13.5-14.6M.)

Redundancy matters. The brief prices "one megawatt of conditioned power delivered to the data hall". Buyers size by IT load with redundancy: 4-to-make-3 block redundant needs 1.33 MW nameplate per IT MW, 2N needs 2.0. At $1.6M per nameplate MW the buyer's cost is $2.1M (4N3R) to $3.2M (2N) per IT MW. [DK] Every persona asked which basis the price is on. The brief does not say.

### 0.2 Lead times actually obtained from incumbents

| Item | Hyperscaler under frame agreement | Colo | Neocloud, spot | Label |
|---|---|---|---|---|
| 15 kV switchgear | 30-45 weeks call-off against reserved slots forecast 2-3 years ahead | 52-80 weeks | 52-80 weeks, up to 2-3 years for data-center spec at the busiest makers | hyperscaler [DK]; others [notes] |
| 38 kV switchgear | reserved | 78-104 weeks | 78-104 weeks | [notes] |
| Switchgear and transformers, general | - | 12-18 months | 12-18 months | [source: S1] |
| Vertiv modular power | - | over 12 months | over 12 months | [source: S1] |
| Conventional on-site MV infrastructure | - | 18-36 months | 18-36 months | [source: S2] |
| Customisation penalty | - | about +8 weeks | about +8 weeks | [source: S1] |
| Large-frame LV power breakers | allocated | 30-50 weeks | 30-50 weeks, on allocation | [DK] |

Implication for the brief: a start-up that buys its breakers, switchgear and transformers from these makers cannot promise 26 weeks from order unless it has already paid for slots or stock 12-18 months earlier, or the buyer free-issues the gear. No persona believed the 26-week figure for a first order.

### 0.3 Value of speed

- $500k per MW per month is the owner-operator figure. For a wholesale colo it is about $190k per MW per month. [source: S1]
- Modular power cuts the power fit-out from about 5.5 months to about 2.5 months. Commissioning to IT-ready still takes 3-8 months and is the largest remaining gap. [source: S1; notes]
- The brief's liquidated damages: 0.5% a week = $8k/MW/week, capped at $160k/MW. An owner-operator loses about $115k/MW/week ($500k / 4.33). The cap equals 1.4 weeks of the owner-operator's loss, or 3.6 weeks of a colo's. (Arithmetic.)

### 0.4 Who already sells this

- Flex (Anord Mardix power pods, Crown Technical MV e-houses), Schneider (EcoStruxure Pod, Easy Modular), Vertiv (MegaMod, OneCore 12.5 MW pods, SmartRun), Delta, Eaton (Fibrebond), plus integrators and contractors: Comfort Systems, Sterling, Cupertino Electric, PCX, Infra Partners, Faith Technologies. AWS builds its own "Houdini" skids, each removing more than 50,000 electrician hours. Crusoe builds 1 MW units in its own factory. Hut 8 bought Vertiv OneCore for a 704 MW lease. [source: S1; S2]
- EPG (Singapore) reports more than 200 MW of prefabricated modules delivered in 2025 and about $200M raised in 2026. [source: search snippet, law360.com/real-estate-authority/articles/2434569, not opened]

### 0.5 800 V DC

- Nvidia's named data-center power system partners are Eaton, Schneider and Vertiv, with Delta and Flex Power for components. Transition "starting in 2027". [source: S4, snippet]
- Vertiv's 800 V DC portfolio is scheduled for commercial availability in H2 2026. [source: S5, snippet]
- Nvidia's DSX Ready qualification launched with two categories and three names each: batteries (Hitachi Energy, LG Energy Solution, Tesla), CDUs (LG, LiquidStack, Vertiv). Switchgear and 800 V DC power are not yet covered; more categories "over time". [source: S3]
- Phase 1 (2026-2027) keeps the AC backbone; centralised rectifiers arrive late 2028-2029; solid-state transformers after 2029, none UL certified for data centers as of May 2026. [notes]
- Read-across: the design changes, but the lists are being refilled with the same incumbents plus power-electronics specialists. The founder's block has no power-conversion technology of its own; the rectifier or solid-state transformer is someone else's product.

---

## 1. Vice president, data center design and construction, top-five hyperscaler

Who: owns the reference design and the delivery schedule for several GW a year.

Incentives and constraints: schedule certainty across a fleet, identical halls, career risk concentrated in a late or failed energisation. Bound to the company reference design, the approved vendor list and frame agreements that reserve factory slots at the large electrical OEMs. [DK]

Alternatives: (a) frame OEMs delivering integrated skids; (b) in-house or captive skid programmes (AWS Houdini, about 25 weeks to first server room) [source: S1]; (c) qualified build-to-print integrators working with owner-furnished gear.

Decision: REFUSES. No purchase order, no deposit, no frame agreement.

Price or terms they would entertain later: build-to-print integration of the hyperscaler's own design with free-issued equipment at $0.15-0.30M/MW [DK]; or turnkey at no more than $1.0-1.2M per nameplate MW, open book [DK]. Never a 30% deposit; milestone payments against bonded progress.

Reasons:
1. They do not buy a vendor's "standard block". They buy their own design built by others. Customisation demanded: effectively 100% (voltage, redundancy topology, breaker make, relay settings, monitoring protocol, enclosure dimensions). [DK]
2. Speed is not the gap for them. Frame slots already give 30-45 week call-off [DK], and their bottleneck is grid power (3-7 years) [notes], not skid assembly.
3. A start-up consuming the same OEM breakers adds a margin layer and no capacity.
4. Would not switch for speed alone: a start-up's promised 26 weeks carries no fleet evidence, and one failed energisation costs more than the months saved.
5. 800 V DC: they co-wrote the OCP paper with Nvidia [notes] and are developing it with frame vendors. New-architecture RFIs go to existing frame holders first. A newcomer gets a pilot only if it brings conversion technology the incumbents lack.

Would change the decision: 500 MW or more installed at named operators with 12 months of field data; demonstrated own supply of long-lead components (not resale of the frame vendors' gear); willingness to build to print.

---

## 2. Head of construction, wholesale colocation developer

Who: delivers 50-300 MW campuses, mostly pre-leased to hyperscalers and large AI tenants.

Incentives and constraints: rent commencement dates in the lease with tenant penalties; a guaranteed maximum price with the general contractor; lender covenants; the tenant approves the basis of design on build-to-suit halls. [DK]

Alternatives: Schneider, Eaton (Fibrebond), Vertiv, Flex power modules; e-houses from established integrators; the electrical contractor's own prefab shop.

What they pay today: $1.2-1.6M/MW stick-built, $1.3-1.7M prefabricated. [DK] Lead times: 52-80 weeks for 15 kV gear [notes], more than 12 months for Vertiv modular [source: S1].

Decision: REFUSES for any hall on a lease-critical path. Would issue no order today.

Terms they would accept later: one 5 MW block on a speculative or late phase as an alternate, at no more than $1.3M per nameplate MW, 10% deposit against a bank guarantee, after a witnessed factory test of a UL-listed first unit and written tenant acceptance.

Reasons:
1. Their value of a month is about $190k/MW, not $500k [source: S1]. A three-month saving is worth about $0.57M/MW, and only if the power fit-out is the critical path. Usually the critical path is utility power and long-lead gear.
2. The 26-week promise is not credible against 52-80 week switchgear [notes]. If the start-up misses, the capped damages ($160k/MW) cover 3.6 weeks of lost rent.
3. Would switch for speed, but only for proven speed. An unproven promise is worth zero in a lease schedule.
4. Customisation: 30-50% of the block varies by site and tenant (utility voltage 12.47/13.8/24.9/34.5 kV, fault duty, 4N3R or 2N, tenant monitoring standard). [DK]
5. 800 V DC: tenants dictate. They will follow whatever vendor the tenant and Nvidia name.

Would change the decision: three or more blocks running at another operator for six months; tenant sign-off in writing; component allocation letters from the breaker and transformer makers; a bonded delivery date.

---

## 3. Infrastructure lead, neocloud building 100-300 MW fast

Who: must energise capacity against GPU delivery dates and take-or-pay customer contracts.

Incentives and constraints: every month late is roughly $500k/MW of lost contribution [notes; S1]. Thin balance sheet, debt-funded, lenders' technical adviser reviews major equipment. Little in-house engineering, so they prefer a vendor design. No frame agreements, so they sit at the back of the incumbent queue; OEMs allocate capacity to larger projects first. [source: S1]

Alternatives: Vertiv OneCore (as Hut 8 did), Schneider or Flex pods at 12 months plus [source: S1]; regional integrators; brokers charging 12-15% markup for faster gear [notes]; buying an integrator outright as Crusoe did [notes].

What they pay today: $1.5-2.0M/MW prefabricated at spot. [DK]

Decision: SIGNS A CONDITIONAL PURCHASE ORDER FOR 10 MW (two blocks), not 100 MW. REFUSES the 30% cash deposit and refuses a multi-year agreement.

Terms: $1.6M per nameplate MW accepted, provided UPS and battery are inside that price. 10% deposit held in escrow, released only against proof that long-lead components are bought. 60% at factory test, 30% at site acceptance. Delivery firm at 26-30 weeks with a right to cancel and recover the deposit if the factory test slips by more than six weeks. Damages 1% a week capped at 20%. Order value $16M; cash at risk $1.6M.

Reasons:
1. The only persona for whom speed alone is a sufficient reason. If the block truly arrives 6 months before a Vertiv pod, it is worth about $3M/MW to them, twice its price.
2. Still places the main 100-300 MW order with an incumbent or an established integrator, because a start-up's failure would breach customer contracts. The start-up gets a hedge slot.
3. Lowest customisation demand: will take a standard block if it matches the Nvidia reference design and the local utility voltage (two or three variants). [DK]
4. 800 V DC: will buy whatever is on Nvidia's qualified list. Today that list favours Eaton, Schneider, Vertiv, Delta. [source: S3, S4]

Would change the decision to a 100 MW order: two blocks delivered on time and commissioned; Nvidia qualification; a delivery bond from a rated surety.

Risk the founder should price: this buyer's own credit. Neocloud orders are cancelled when financing or power slips (Crusoe paused 1.8 GW in Wyoming, Nebius lost a schedule in New Jersey). [notes]

---

## 4. Preconstruction director, general or electrical contractor placing the orders

Who: prices the job, writes the purchase orders for switchgear and skids, carries the schedule and the bond.

Incentives and constraints: margin is earned on self-performed labor and on equipment mark-up; liable under a guaranteed maximum price and liquidated damages to the owner; surety limits; buys what the specification names, or an "or equal" accepted by the engineer and owner. Large electrical contractors run their own prefabrication shops (Cupertino Electric, Faith Technologies and others are listed as skid suppliers). [source: S1]

Alternatives: buy gear through an OEM distributor and assemble skids in their own shop; buy an OEM pod.

Decision: REFUSES to place the order on their own account. Would process it only as an owner-nominated supplier with the owner carrying delivery and performance risk in writing.

Terms: no deposit from the contractor's cash; pay-when-paid; supply bond or parent guarantee for 100% of the order; the start-up accepts flow-down of the prime contract's damages; clear demarcation of who terminates and tests field cables.

Reasons:
1. The block removes $0.3-0.5M/MW of the contractor's own scope [DK]. In a labor-short market they will give that up, but to their own prefab shop first.
2. A start-up supplier worth 10-15% of contract value with a 10% damages cap is unbondable risk for them.
3. Union jurisdiction: some IBEW locals contest factory-wired assemblies built by non-signatory shops. Site acceptance can turn on where and by whom the block was wired. [DK]
4. The claimed 85% cut in electrician hours applies inside the module. Medium-voltage cable pulls, terminations, grounding and feeders into the hall stay on site; total on-site hours fall about 63%. [source: S1]
5. Customisation: none of their own; they pass through the owner's.

Would change the decision: named in the owner's specification; UL listing file in hand; bonded; delivered price at or below their own shop cost of roughly $1.2-1.4M/MW [DK].

---

## 5. Chief financial officer, colocation developer

Who: signs payments, owns the lender relationship and the construction loan or securitisation.

Incentives and constraints: loan agreements require an independent engineer's report; major equipment must be from suppliers the engineer accepts as proven; advance payments above a threshold need security; warranties must be assignable to lenders. [DK]

Decision: REFUSES the 30% deposit and REFUSES to rely on a five-year start-up warranty.

Terms they would accept: at most 10% down, against a standby letter of credit from an investment-grade bank or escrow; 5-10% retention for 12-24 months; OEM component warranties passed through and assignable; the start-up's own warranty backed by escrow, insurance or a warranty bond; step-in rights to drawings and the factory if the start-up fails.

Reasons:
1. On a 100 MW order the deposit is $48M unsecured to a company with no revenue. On a 10 MW pilot it is $4.8M. Neither clears a credit committee without security. A start-up must cash-collateralise a letter of credit, which defeats the deposit's purpose.
2. A five-year warranty is worth the warrantor's balance sheet. Lender's engineer will mark it at zero.
3. Supplier failure mid-build is a covenant event. Katerra raised over $2B and still failed. [notes]
4. The damages cap ($160k/MW) is below one month of lost rent ($190k/MW). [source: S1 for the rent figure]
5. Paying a premium for speed is acceptable; paying it before proof is not.

Would change the decision: lender's engineer letter accepting the product; a rated surety or bank standing behind deposit and warranty; an equity sponsor or strategic parent guaranteeing performance.

---

## 6. Procurement executive, top-five hyperscaler

Who: runs supplier qualification, commercial terms and second sourcing for electrical equipment.

Incentives and constraints: measured on supply assurance and cost per MW. Rules of thumb: audited financials, supplier revenue concentration below roughly 25-30% from one buyer, ISO 9001, safety record, factory audit, first-article inspection, type-test reports, pilot, then frame agreement. [DK]

Decision: REFUSES. Will accept a registration and an RFI response; no commercial commitment.

Time for a start-up with no installed base to reach the approved list: 18-30 months from first contact to a volume order at a hyperscaler; 6-12 months at a colo; 1-3 months at a neocloud. [DK; no primary source found in two searches]

Terms once qualified: open-book cost-plus, integrator gross margin held to roughly 12-18% [DK]; payment 60-90 days after milestone; no deposits; damages uncapped or capped far above 10%; right to audit sub-tier suppliers; right to direct component allocation.

Reasons:
1. Second sourcing is real, but the second and third sources being added are established manufacturers with their own factories and components: the Korean makers expanding in the US (LS Electric switchgear revenue +120%, Hyosung, HD Hyundai) and contract manufacturers such as Flex. [notes; source: S1, S2]
2. The start-up's bill of materials is the frame vendors' own breakers and transformers. Procurement can already direct that allocation to a qualified integrator. The start-up adds no supply.
3. Financial health test fails on day one: no revenue, one product, and a single 100 MW order would exceed its entire turnover.
4. 800 V DC does trigger new sourcing events in 2027-2028. They reopen the specification, not the supplier base. Invitations go to frame holders and to firms with conversion technology (Delta, the solid-state transformer makers with ABB or Eaton behind them). [notes]
5. A 25-30% gross margin on resold components will not survive an open-book negotiation.

Would change the decision: two years of audited revenue above $100M; a factory that passes audit; proprietary supply of at least one constrained component; a pilot block with 12 months of clean operating data.

---

## 7. Electrical engineer of record

Who: seals the design; personally liable for code compliance.

Constraints: National Electrical Code and the local authority having jurisdiction; equipment must be listed or field-evaluated by a recognised lab. Relevant listings: UL 891 or UL 1558 for low-voltage assemblies, IEEE C37.20.2 and C37.20.7 for medium-voltage and arc-resistant gear [source: S2 for C37.20.7], UL 1778 for UPS, UL 9540 with UL 9540A fire testing and NFPA 855 for batteries, UL 2755 or state industrialised-building approval for the enclosure. [DK]

Decision: REFUSES to name the block as basis of design. Would list it as an alternate subject to full submittal review once it is listed.

Reasons:
1. No listing, no seal. First-unit listing of an integrated assembly takes 6-12 months and each variant (voltage class, fault rating, topology) needs its own evaluation. [DK]
2. Battery in the same shippable enclosure as medium-voltage switchgear is a fire-code and separation problem; many owners require a separate battery room or container. [DK]
3. Selective coordination and arc-flash results depend on the site's fault current and the upstream utility protection. A "standard" block needs site-specific relay settings, a coordination study and incident-energy labels every time. That is engineering per project. [DK]
4. Serviceability: working clearances, breaker rack-out space, maintenance bypass and infrared access inside a transportable enclosure are where prefabricated designs most often fail review. [DK]
5. 800 V DC: product standards and calculation methods are immature (IEEE 1584 arc-flash method covers AC; no data-center solid-state transformer was UL certified as of May 2026 [notes]). The engineer will follow the OCP specification and listed equipment from makers who did the type tests, which a start-up integrator cannot fund quickly.
6. Customisation the engineer imposes: voltage, fault duty, grounding scheme, redundancy topology, monitoring points, seismic and climate ratings. Expect 8-12 variants before the block is "standard" for the US market. [DK]

Would change the decision: complete listing file; published short-circuit and coordination data; a third-party arc-flash report; a successful inspection by two or three large authorities (for example in Virginia, Texas, Arizona).

---

## 8. Commissioning agent

Who: independent agent who signs the acceptance the owner and lender rely on. Not a buyer; decision is accept or reject.

Decision: REJECTS "commissioned in about 10 days". Would accept the block itself in 3-4 weeks and the hall in a further 2-4 weeks of integrated testing, for a mature product. First units from a new maker: plan 30-50% longer. [DK]

Reasons:
1. A factory test does not survive shipping untested. Site work still includes torque checks, insulation and cable tests on field terminations, relay setting verification, battery discharge test, transfer sequences with generators, monitoring point-to-point checks and load-bank heat runs. [DK]
2. Sourced benchmark: modular power takes the fit-out from 5.5 to 2.5 months; commissioning to IT-ready remains 3-8 months. Nobody reports 10 days. [source: S1; notes]
3. The honest comparison is about 10-12 weeks saved on fit-out, not 12 weeks compressed into 10 days.
4. Would require: witnessed factory test at full load, complete as-built drawings and settings files before shipment, and the maker's engineers on site through integrated testing.

Would change the view: test records from ten or more installed blocks showing site acceptance inside three weeks with a short defect list.

---

## 9. Answers to the specific tests

1. Price paid today for equivalent scope: $0.9-1.3M/MW (hyperscaler), $1.2-1.7M (colo), $1.4-2.0M (neocloud), per nameplate MW [DK]. Factory build is about 5% cheaper than field build on first cost [source: S1]. $1.6M is saleable only to non-frame buyers, and only on a nameplate basis.
2. Incumbent lead times: 12-18 months for switchgear and transformers, over 12 months for Vertiv modular [source: S1]; 52-80 weeks at 15 kV [notes]; hyperscalers with reserved slots get roughly 30-45 weeks [DK].
3. Approved vendor list for a start-up with no installed base: 18-30 months at a hyperscaler, 6-12 at a colo (plus tenant and lender's engineer), 1-3 at a neocloud [DK].
4. Switch for speed alone: neocloud yes, in pilot size. Colo only for proven speed. Hyperscaler no. Contractor no.
5. 800 V DC reopening lists: the specification reopens, the supplier base mostly does not. Nvidia's named partners and its first qualification lists are incumbents [source: S3, S4]. Entry is through conversion technology, which this brief does not include.
6. Customisation: hyperscaler about 100% (build to print); colo 30-50%; neocloud 2-3 variants; engineer of record forces 8-12 variants nationally [DK]. This is engineered-to-order with a common platform, not a single product.

## 10. Numbers in the brief the panel disputes

| Brief | Panel's figure | Basis |
|---|---|---|
| $1.6M/MW | $0.9-1.3M for hyperscalers, $1.2-1.7M colo, $1.4-2.0M neocloud; state nameplate or IT basis | [DK]; factory build about 5% cheaper than field [S1] |
| 26 weeks from order | 50-70 weeks for first orders unless stock is pre-bought or gear is free-issued | 52-80 week switchgear [notes]; 12-18 months [S1] |
| Commissioned in 10 days against 12+ weeks | Fit-out 5.5 to 2.5 months; commissioning still 3-8 months; block acceptance 3-4 weeks | [S1]; [DK] |
| $500k per MW per month for all buyers | $500k owner-operator, $190k wholesale colo | [S1] |
| Electrical is 45-70% of build cost | The block is about 11-12% of build cost | $1.6M / $13.5-14.6M [notes] |
| Electrician hours cut 85% | True inside modules; on-site hours fall about 63%; site cabling remains | [S1] |
| Gross margin 25-30% | 12-18% as an integrator of bought-in gear under open-book terms | [DK]; Eaton's 29.8% is earned on its own components [notes] |
| Damages cap 10% is meaningful | Equals 1.4 weeks of an owner-operator's loss | arithmetic from [S1] |
| 100 MW first order, $160M | First orders 5-10 MW, $8-16M | panel decisions |
| Factory $30-40M is the capital need | Add $60-100M of component working capital per 100 MW in build, since deposits fall to about 10% | [DK] |
| 800 V DC reopens vendor lists | Lists refill with Eaton, Schneider, Vertiv, Delta and conversion specialists | [S3, S4, S5; notes] |
| Switchgear booked through 2028 | "At some suppliers"; survey average 44 weeks; and the same queue binds the founder | [notes] |

## 11. Overall panel view

Not plainly unworkable as a regional skid integrator: more than 80 firms do it and neoclouds will give pilot orders. Unworkable on the brief's own terms. A start-up reselling competitors' long-lead components cannot hold 26 weeks, cannot collect 30% unsecured deposits, cannot keep a 25-30% margin under open-book buyers, and gains no entry from 800 V DC without conversion technology. When the new incumbent plants open in 2027-2028 [notes], the speed premium that justifies the one "yes" narrows at the moment the start-up reaches volume.

Panel probabilities:
- First paid commercial delivery within 18 months: 25%. One neocloud pilot is winnable; the binding risks are component lead time and listing.
- $1 billion of annual recognised revenue within seven years: 3%. That is 625 MW a year at the brief's price, from a firm with no component supply, against Vertiv, Schneider, Eaton-Fibrebond, Flex and funded prefab entrants. No equipment start-up founded since 2019 has yet reported $100M of revenue. [notes]
