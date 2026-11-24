# C5 v1, capital and competition panel, round 1

Date of simulation: 24 November 2026. Everything below is a simulated hypothesis by archetype personas. It is not customer, lender or investor validation. No real person was interviewed and no real order exists.

Evidence labels: [notes] = founder's research notes (power_grid.md, ai_compute.md); [brief] = C5_v1.md; [source: URL] = checked in this session; [DK] = domain knowledge, unverified.

Searches used: 7 of 8.

## 0. Facts checked for this panel

- Eaton paid $1.4B for Fibrebond (announced March 2025, closed 1 April 2025). Fibrebond revenue about $378M for the 12 months to February 2025; estimated 2025 adjusted EBITDA $110M. Derived: 12.7x forward EBITDA, 3.7x revenue, EBITDA margin about 29%. [source: https://www.businesswire.com/news/home/20250310706904/en/Eaton-signs-agreement-to-acquire-Fibrebond-Corporation-expanding-reach-into-multi-tenant-data-center-market]
- Powell Industries, fiscal year to 30 September 2026: revenue $1,256M, gross profit $393M (31.3%), SG&A $111.6M, R&D $15.5M (1.2% of revenue), operating income $265M, capex $18.5M (1.5% of revenue), cash and short-term investments $861M, orders $2.6B, backlog $2.7B. [source: https://www.sec.gov/Archives/edgar/data/0000080420/000008042026000139/ex991-powlq4xfy2026earning.htm]
- Vertiv said in May 2025 that its 800 VDC portfolio (centralized rectifiers, DC busway, rack DC-DC converters, DC backup) would be released in H2 2026. No confirmed ship date was found. [source: https://www.vertiv.com/en-us/about/news-and-events/corporate-news/vertiv-accelerates-ai-infrastructure-evolution-in-alignment-with-nvidia-800-vdc-power-architecture-announcement/]
- Nvidia names Eaton, Schneider Electric and Vertiv as data-center power system partners for 800 VDC, and Delta, Flex Power, Lead Wealth, LiteOn and Megmeet as power component suppliers. Delta showed 800 VDC in-row 660 kW power racks at GTC in March 2026. [source: https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories]
- Schneider's prefabricated power modules are 2 to 2.5 MW each; Vertiv's power skids go to 2.5 MW. A SemiAnalysis piece puts Vertiv content at about $3.5M/MW historically, rising toward $7M/MW with modular solutions (vendor content across power and thermal, not a block price). [source: https://newsletter.semianalysis.com/p/the-wild-wild-west-of-lego-datacenters] (read second-hand through search summary)
- Trading multiples, mixed dates and sources, treat as approximate: Vertiv about 6.0x EV/revenue and 24.7x EV/EBITDA (October 2026); Eaton about 27x trailing and about 19x forward EBITDA; nVent about 19x. [source: https://multiples.vc/public-comps/vertiv-valuation-multiples] [source: https://www.alphaspread.com/security/nyse/nvt/relative-valuation/ratio/enterprise-value-to-ebitda]
- No sourced market price per MW for a standalone power block was found. The $1.6M/MW figure stays an assumption.

## 1. Panel's own model

### 1.1 What $1.6M/MW contains

Bought-in content per MW for the stated scope [DK]:

| Item | $k per MW |
|---|---|
| Medium-voltage switchgear and protection | 80-120 |
| Transformer (or rectifier in the DC version) | 60-150 |
| Low-voltage switchboard or 800 VDC distribution and DC protection | 100-180 |
| UPS or battery buffer with power conversion | 350-550 |
| Enclosure, bus, HVAC, fire suppression | 150-250 |
| Controls, wiring, factory labour, test | 100-150 |
| Freight, site commissioning | 30-60 |
| Total cost | 870-1,460 |

Midpoint cost about $1.2M/MW, so gross margin at $1.6M is about 25% before warranty reserve, liquidated damages, expediting and scrap. After those, 15-22%. About 70% of cost is components made by companies that sell a competing block.

Two revenue models exist in this trade [DK]. If the builder buys the gear, revenue is about $1.6M/MW at 15-22% margin. If the customer free-issues the gear under its own frame agreements (normal for hyperscalers), revenue is $0.3-0.6M/MW at 28-35% margin. Fibrebond's 29% EBITDA margin is consistent with the second model plus scarcity pricing; it is not evidence that a full-scope reseller earns 25-30%.

### 1.2 Cash cycle for one 100 MW order ($160M, founder's terms)

Assume cost $120M (25% margin, founder's case).

| Week | Event | Cash | Cumulative |
|---|---|---|---|
| 0 | 30% deposit | +48 | +48 |
| 0-26 | Components, labour, enclosure paid (small buyer gets cash with order or net 30) | -120 | -72 |
| 22-24 | Factory test; 50% invoiced; paid net 45 at about week 29 | +80 | +8 |
| 26 | Ship | | |
| 40-52 | Site acceptance (site readiness, utility energization and inspection decide the date, not the supplier); 20% paid | +32 | +40 |

- Peak cash need: $72M, 45% of order value. At an 18% margin it is $83M (52%).
- Deposit covers 40% of cost in the founder's case, 37% in the panel's.
- The 20% held to site acceptance ($32M) is 80% of the founder's gross profit on the order. Profit is collected last and its date is controlled by the customer's site.
- If the customer requires an advance payment guarantee for the deposit (normal when paying a start-up tens of millions [DK]), the issuing bank takes 100% cash collateral. The deposit is then unusable and peak need is $120-131M, 75-82% of order value.

Steady-state net working capital, panel estimate: inventory and work in progress 24% of revenue, receivables and unbilled 16%, less deposits 13%, less payables 6% = about 21% of revenue. Add 5-10% for supplier deposits on long-lead gear. Total 20-30% of revenue while growing. Cash conversion cycle about 110-130 days. An incumbent with pricing power runs near zero or negative (Powell holds $861M cash on $1.26B revenue [source above]). A start-up does not get those terms.

### 1.3 The 26-week promise against component lead times

15 kV switchgear is 52-80 weeks and data-center-spec medium-voltage gear two to three years at the busiest makers [notes]. A 26-week delivery means buying gear 6 to 12 months before the customer order exists. At 1 GW a year that is $150-300M of non-cancellable supplier commitments and $40-90M of cash deposits with no customer deposit behind them [DK]. This speculative inventory is the largest single risk on the balance sheet.

### 1.4 Liquidated damages and warranty

- Delay damages of 0.5% a week capped at 10% equal $160k/MW. That is 40% of gross profit at a 25% margin and 56% at 18%. The cap is hit after 20 weeks, which is shorter than one missed switchgear slot.
- The buyer's stated loss is $500k/MW a month [brief], about $125k/MW a week. The damages pay $8k/MW a week, 6% of the loss. The clause is too small to protect the buyer and too large for the seller. A rational buyer therefore manages the risk by not single-sourcing from a start-up.
- Five-year warranty: component makers give 12-18 months from shipment [DK]. Years 2 to 5 fall on the builder, including batteries. Reserve 3-4% of revenue [DK]; the brief reserves nothing. One serial defect needing a $50k/MW retrofit across a 1 GW fleet costs $50M.

### 1.5 Two-year pause in AI capital spending

- Data centers are 10-20% of the incumbents' order books; the rest is utilities and industry [notes]. This company is 100% AI data halls.
- Financing is already tight for the customers most likely to buy from a start-up: AI debt issuance fell from $113B in June to $23B in September 2026 and CoreWeave paper yields about 15% [notes]. Bernstein treats about 35% of announced capacity as credible [notes].
- Panel assumption: new orders fall 60-80% for two years; 30-50% of backlog is deferred or terminated for convenience (customer pays cost incurred, forfeits part of deposit) [DK, by analogy with telecom equipment 2001-2003].
- At a 1 GW run rate the company holds $150-300M of supplier commitments, about $290M of working capital, about 800 staff and $115M of annual fixed cost. With revenue at 30% of plan the cash burn is $150-250M a year. It does not survive two years without a recapitalization that wipes out earlier equity.

### 1.6 Price when incumbent capacity arrives in 2028

- About $2B of new North American plant opens in 2027-2028 [notes]. Switchgear is up 50% and breakers 47% since 2021; Eaton Electrical Americas earns a record 29.8% [notes].
- Incumbents earn their margin on components and can sell integration at cost. Solid-state transformer start-ups claim 60-70% of the cost of the equipment they replace [notes].
- Panel estimate: like-for-like block price falls to $1.20-1.35M/MW by 2029 (down 15-25%). A builder that does not make its own gear keeps 12-18% gross margin.

### 1.7 Revenue, margin, capital and value at three scales

| | 100 MW a year | 1 GW a year | 10 GW a year |
|---|---|---|---|
| Net price per MW | $1.45M | $1.30M | $1.10M |
| Revenue | $145M | $1.3B | $11B |
| Gross margin | 8-12% (10%) | 15-22% (18%) | 17-22% as assembler (19%); 28-32% only with own switchgear, rectifiers and breakers |
| Gross profit | $15M | $235M | $2.1B |
| Operating cost | $40M | $115M | $770M |
| EBITDA | -$25M | +$120M (9%) | +$1.3B (12%) |
| Plant and test, cumulative | $50M | $180M | $1.2B |
| Working capital incl. supplier deposits | $45M | $350M | $2.0B |
| Cumulative losses to reach this point | $100M | $200M | $250M |
| Total capital | about $195M | about $730M | about $3.5B |
| Debt a lender would provide | $10-20M | $200-250M | about $1.5B |
| Equity needed | about $180M | about $500M | about $2.0B (partly retained earnings) |
| Rational equity value | $60-150M | $1.0-2.2B, midpoint $1.4B | $13-20B; $26B at boom multiples |

Basis for value: 10-13x EBITDA through the cycle [DK], supported by Fibrebond at 12.7x [source above]; up to 18-20x at today's sector multiples [sources above]. At 1 GW the success case returns about 2.8x on the equity put in. Ten gigawatts a year is 35-50% of plausible world demand (800 VDC adds about 39 GW in total by 2030 [notes]) and is not a credible share for one assembler. Even there the value is $13-20B, because Vertiv's roughly $88B (6.0x of about $14.6B revenue [sources above, notes]) rests on proprietary product and service at 25% operating margin [notes], which an assembler does not have.

### 1.8 Does scale make it more defensible or merely larger?

Merely larger. Scale buys 3-5 points of purchasing leverage, better allocation and qualification slots. It does not create an asset that incumbents lack. Bought-in content stays near 70% of cost, so fixed-cost leverage is small. Working capital, supplier commitments, warranty exposure and cycle risk grow in proportion to revenue. Powell spends 1.2% of revenue on R&D and 1.5% on capex [source above]: this is a shop-capacity and relationship trade, and incumbents own more of both. Defensibility would require owning a component the 800 VDC era needs and incumbents lack (DC protection, rectifier, controls certified into customers' designs) or a service base, and incumbents service their own gear.

## 2. Personas

### Persona 1. Asset-based lender (senior credit officer, commercial finance group)

- Incentives and constraints: paid on losses avoided. Lends against a borrowing base with field exams and appraisals. Credit policy [DK]: 85% of eligible invoiced receivables; 50-65% of appraised liquidation value on raw materials; 0% on work in progress; 0% on custom finished goods until invoiced and accepted; progress billings ineligible; any debtor above 25-35% of the base is capped unless investment grade; foreign debtors ineligible without credit insurance or a letter of credit; receivables under a surety bond are ineligible because the surety ranks first.
- The request: fund inventory and work in progress against deposits and purchase orders.
- Reasons for the answer:
  1. A deposit is a liability to the customer, not collateral. It creates a right of offset, so the lender reserves against it.
  2. A purchase order is not a receivable. Purchase-order finance exists at 1.5-3% a month from specialty lenders [DK], which consumes the gross margin over a 26-week build.
  3. Work in progress is a half-wired enclosure built to one customer's single-line diagram. Liquidation value is the breakers inside it.
  4. The FAT invoice is a milestone billing on goods not yet accepted at site. Ineligible without a no-offset letter from an investment-grade payer.
  5. If the customer takes title to materials as it pays, that conflicts with the lender's lien.
  6. Likely early customers are neoclouds rated around B+ [notes]. Excluded or capped.
  7. On a $160M order the base would support $10-18M against a $72-83M peak need.
- Decision: refuses the facility as requested. No facility before revenue.
- Terms it would accept: after 12 months and at least $50M of delivered, site-accepted revenue: $15-25M revolver; 85% on invoiced receivables from investment-grade debtors with no-offset acknowledgments; 50% of cost on catalogue components (switchgear, breakers, transformers) capped at 40% of the line; nothing on work in progress; reserve equal to deposits held from the same debtor; SOFR + 450-600 bp; minimum liquidity $15M; springing cash dominion; at least $30M of junior capital beneath.
- Evidence that would change the decision: investment-grade payers; contract language giving unconditional milestone payments; appraisal of component inventory; audited warranty history; credit insurance on non-US debtors.

### Persona 2. Partner, industrial private equity (has bought and sold modular power builders)

- Incentives and constraints: five-year hold, 2.5-3x target, leverage 4-5x EBITDA, needs $20M+ of EBITDA to underwrite. Does not fund start-ups.
- Alternatives: buy an existing e-house or skid builder with $100-300M revenue at 9-11x EBITDA [DK], with listings, shop, crews, channel allocations and customer master agreements already in place, then add shifts.
- View of the business:
  - Diligence on these companies shows 60-80% of every order is engineered to the customer's drawing [DK]. "Standard 5 MW block" becomes a configurator at best. Each hyperscaler and large colocation operator has its own single-line.
  - Margins in the 25-30% range occurred in 2024-2026 because shop capacity was scarce. Through the cycle these businesses earn 10-15% EBITDA [DK].
  - Exit is a sale to a strategic at 10-13x. Fibrebond's 12.7x was for a 40-year-old company with multi-tenant data-center relationships [source above].
  - The founder's own factory figure is low. A bay that tests 5 MW at medium voltage needs a 10 MVA+ utility service and load banks, and that service has its own transformer lead time. Panel estimate $45-70M [DK].
- Decision: refuses to invest now.
- Terms it would accept: control buyout at 8-10x trailing EBITDA once EBITDA exceeds $25M, top customer under 40% of revenue, two years of warranty data and no open damages claims. Or structured preferred at 1 GW scale with a 12% coupon and 1.5x liquidation preference.
- Evidence that would change the decision: three customers on multi-year master agreements with take-or-pay volumes; proof that over 70% of bill of materials is common across customers; a component supply agreement with committed allocation.

### Persona 3. Skeptical venture investor (seed and Series A)

- Incentives: needs a credible path to a 50x+ outcome on seed and an asset that grows more valuable per dollar as it scales.
- Arithmetic:
  - Capital to $1B revenue: about $600-730M in total, about $450-500M of it equity (table 1.7).
  - Value at $1B revenue: $1.0-2.2B.
  - Financing path at integrator valuations (1-1.5x forward revenue): seed $5M at $20M post, A $30M at $100M, B $100M at $200M, C $150M at $500M, D $200M at $1.0B, 13% option pool. Founders hold about 11%. With generous rounds (B at $350M, C at $900M, D at $1.6B) about 22%. Founder stake at $1B revenue: 8-22%, worth $100-350M.
  - Seed stake after dilution about 4-5% of $1.4B = about $65M on $5M, 13x, at a probability the investor puts at 5%. Expected multiple about 0.65x.
- Multiples the investor uses: proprietary electrical equipment with service 19-27x EBITDA today and 12-15x through the cycle; modular builders 10-13x; contract assemblers 6-10x EBITDA and 0.3-0.8x revenue [sources above; DK].
- Precedent: no equipment start-up founded since 2019 was found with $100M+ of reported revenue; funded ones took two to four years to first units [notes].
- Decision: refuses seed and Series A as written. Not venture-scale as an assembler.
- Terms it would accept: $3M at $12M post only if the company owns a component: a certified 800 VDC protection or conversion product with 40%+ gross margin that is designed into at least one named buyer's reference design, with the block as the delivery vehicle.
- Evidence that would change the decision: a binding order with a paid, unguaranteed deposit from an investment-grade buyer; a written supply allocation from a breaker maker; bill of materials showing 35%+ gross margin after warranty reserve.

### Persona 4a. Large electrical OEM (strategy head, Americas electrical segment)

- Position: owns breakers, switchgear, UPS and service; has bought an enclosure builder and a solid-state transformer developer; earning record margins with backlog up more than 30% [notes]. Named by Nvidia as an 800 VDC power system partner [source above].
- Will it supply? Yes, through the packager channel, at list lead time (52-80 weeks for 15 kV [notes]) with cash deposits. No allocation priority: own modular lines first, frame-agreement customers second, packagers last. No early access to 800 VDC breakers or protection studies. Outright refusal is unnecessary and invites legal and channel trouble.
- Response in 2027-2028: sell the same block under one warranty and one service contract. When new plants open, price integration at cost to pull through components. Can quote $1.2-1.3M/MW and still earn 25%+ on its own content [DK].
- Decision: competes; does not partner; does not buy.
- Terms it would accept: acquisition at 10-13x EBITDA once the start-up has $50M+ EBITDA or holds a qualified slot at a hyperscaler the OEM lacks.
- Evidence that would change the decision: the start-up owning a certified DC product the OEM does not have.

### Persona 4b. Asian power-electronics maker already qualified for 800 VDC

- Position: ships power shelves, 800 VDC busway and in-row 660 kW power racks; on Nvidia's supplier list [notes; source above]. Makes its own rectifiers and magnetics. Cost base 20-30% below US assemblers before tariffs [DK].
- View: in the DC era the rectifier and protection are the product. The start-up's block is an enclosure around this persona's content.
- Decision: sells rectifier shelves to the start-up as one more channel, net 30 after a credit check, no exclusivity, priced to keep its own 30%+ margin. In parallel it supplies hyperscalers directly and through contract manufacturers.
- Terms it would accept: volume agreement with 12-month rolling forecast, 30% non-cancellable; no most-favoured pricing.
- Evidence that would change the decision: none needed; it gains either way.

### Persona 4c. Established independent skid and e-house builder (owner-operator, $200-400M revenue)

- Position: listed shop, test crews, year-long backlog, channel accounts with the OEMs, free-issue contracts with two or three large operators. More than 80 firms sell prefabricated power [brief].
- Constraint: the same components and the same wiremen. Shop space is cheap and takes 9-12 months to add [DK].
- Response: adds a building and a shift; quotes the same 50 MW at $1.35-1.50M/MW full scope, or $350-500k/MW with customer-furnished gear, 30-40 weeks. Hires the start-up's engineers at a 20% premium.
- Decision: competes on price and track record. Sees no technology gap.
- Evidence that would change the decision: the start-up showing a factory labour content per MW below half of its own.

### Persona 4d. Hyperscaler (director of data-center electrical engineering and sourcing)

- How it buys [DK]: owns the reference design; holds multi-year frame agreements for long-lead gear and free-issues it; uses contract manufacturers and integrators to build to print; supplier qualification takes 12-24 months with factory audits and a financial review; avoids any award above 20-30% of a supplier's revenue; pays on milestones at net 60, no deposit to an unproven vendor unless bank-guaranteed.
- Decision: refuses the standard block and the $1.6M/MW price.
- Terms it would accept: after qualification, a build-to-print pilot purchase order for 5-10 MW in 2028 at an integration fee of $150-350k/MW, gear free-issued, no deposit, 5-10% retention, design owned by the hyperscaler, second source required.
- Reason: its design is the standard. A vendor's standard block removes its ability to dual-source and its control of the protection scheme.
- Evidence that would change the decision: none for the product; for build-to-print, a clean audit and a balance sheet that can absorb a recall.

### Persona 5. Competing start-up (solid-state transformer or DC power, $100M+ raised)

- What it already has: $60-178M raised; power-electronics designs; a factory in build with full-scale production planned for H2 2027; named customers among developers and neoclouds; one of the group is in Nvidia's MGX reference architecture; strategic investors including a breaker maker [notes].
- Weaknesses it admits: no UL-certified data-center unit as of May 2026; shipments in tens of MW; scale adoption not before 2029 [notes].
- View: its unit replaces the transformer, low-voltage switchgear and rectifier in the founder's block, about $0.75M/MW of content [notes]. It ships containerised units itself, so it needs no packager.
- Response: signs non-binding reservations with the same prospects; prices at parity or below using venture money; recruits the founder's power-electronics and certification staff.
- Decision: no partnership. Concedes the founder could ship an AC block before it ships a certified solid-state unit.
- Terms it would accept: all-stock purchase of the team for under $20M if the founder has a listed enclosure and a commissioning crew.
- Evidence that would change the decision: the founder holding a binding 100 MW+ order from one of its target accounts.

### Persona 6. New independent buyer (head of infrastructure, sovereign or enterprise AI project outside the US, first 50 MW)

- Incentives and constraints: first project, personal career risk, public or board-level procurement rules, lenders' technical adviser. Outside the US, UL listing is irrelevant; IEC 61439 and IEC 62271-200 type tests, local grid code and local-language documentation apply [DK]. Buys through an EPC contractor that wraps the risk. Technical advisers usually ask for two or more years of operating references [DK].
- Alternatives: a global OEM's prefabricated power module through the EPC, with one warranty and an in-country service organisation; in the Gulf, India and South-East Asia also Chinese and Taiwanese integrated power modules at 20-30% lower prices [DK].
- Disputes with the brief:
  - Electricians are not the scarce input in most of these markets, so the labour saving is worth little. Willingness to pay is $1.0-1.2M/MW for this scope [DK].
  - The schedule is set by GPU allocation, export licences and grid connection. Realised saving from prefabrication is 2-6 weeks, not 10+ [DK].
  - A 30% deposit to a company with no balance sheet is not approvable without a bank guarantee.
- Decision: refuses a purchase order for 50 MW at $1.6M/MW with 30% deposit. Buys from a global OEM through its EPC.
- Terms it would accept: one 5 MW block (10% of the project) through the EPC at no more than $1.25M/MW; 10-15% advance against a bank guarantee; 10% performance bond; delay damages 1% a week capped at 15-20%; two-year defects period plus five-year warranty backed by a retention bond; IEC type-test certificates; in-country service partner with four-hour response; spares on site.
- Evidence that would change the decision: three operating reference sites totalling 50 MW+ with 12 months of data; an OEM or insurer standing behind the warranty.

## 3. Verdict table

| Persona | Decision | Terms they would accept | Reason |
|---|---|---|---|
| 1 Asset-based lender | Refuses | $15-25M revolver after $50M delivered revenue; 85% on investment-grade invoiced receivables, 50% on catalogue components, 0% on work in progress | Deposits are liabilities and purchase orders are not collateral; base covers $10-18M of a $72-83M peak need |
| 2 Industrial PE | Refuses | Buyout at 8-10x EBITDA above $25M EBITDA | Engineered-to-order shop trade; cheaper to buy an existing builder |
| 3 Venture investor | Refuses | $3M at $12M post if the company owns a certified DC component at 40%+ margin | $450-500M equity for $1.0-2.2B of value; expected seed multiple about 0.65x |
| 4a Large OEM | Supplies at list lead time; competes | Acquires at 10-13x EBITDA above $50M EBITDA | Owns components and service; can sell integration at cost |
| 4b Asian power-electronics maker | Sells components; competes | Rolling forecast, 30% non-cancellable | Rectifier is the product in the DC era |
| 4c Independent builder | Competes | Quotes $1.35-1.50M/MW | Same parts, existing shop, listings and references |
| 4d Hyperscaler | Refuses | Build-to-print pilot 5-10 MW at $150-350k/MW after 12-24 month qualification, no deposit | Its own design is the standard |
| 5 Competing start-up | Competes; no partnership | Team purchase under $20M in stock | Its unit replaces most of the block |
| 6 Non-US first-time buyer | Refuses 50 MW | 5 MW through EPC at $1.25M/MW or less, bank-guaranteed advance | Needs IEC, references and a wrapped warranty; labour is not scarce there |

## 4. Numbers in the brief the panel disputes

| Brief | Panel | Basis |
|---|---|---|
| Gross margin 25-30% at volume | 15-22% as full-scope assembler; 8-12% in the first 100 MW | About 70% bought-in content; warranty and damages unreserved [DK] |
| 100 MW = $160M revenue | $145M net of discounts; $30-60M if gear is customer-furnished | Free-issue practice [DK] |
| Deposits fund the build | Deposit covers 37-40% of cost; peak cash need 45-52% of order value; 75-82% if the deposit is bank-guaranteed | Section 1.2 |
| Delivery in 26 weeks | Only with gear bought 6-12 months before the order | 52-80 week switchgear [notes] |
| First factory $30-40M | $45-70M | Medium-voltage test service and load banks [DK] |
| Commissioned in about 10 days | 3-6 weeks to accepted, with site acceptance payment 14-26 weeks after shipment | Acceptance testing, inspection, utility energization [DK] |
| Vendor lists reopen in 2027-2028 | They reopened in 2025-2026 and the 800 VDC seats are taken | Nvidia partner lists [source above; notes] |
| Incumbent switchgear booked through 2028 helps the entrant | It applies to the entrant's own purchases | [notes] |
| Five-year warranty at no stated cost | 3-4% of revenue | Component warranties of 12-18 months [DK] |
| Target: a new Vertiv | At 10 GW a year, $13-20B | Section 1.7 |

## 5. Probabilities (panel's estimate)

- First paid commercial delivery within 18 months: 30%. An AC block for a developer or neocloud using brokered gear and a field-evaluation label is achievable if seed money is found; an 800 VDC block is under 10%.
- $1B of annual recognized revenue within 7 years: 4%.
