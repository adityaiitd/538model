# C1 v3 market panel, round three (sellers, new buyers, new competitors)

Date of simulation: 24 November 2026. Independent panel; earlier rounds not relied on.

Everything below is a simulated hypothesis. Personas are archetypes, not real people, and no statement here is a real quote, order or commitment.

Evidence labels: [source: URL] = checked this session; [notes] = power_grid.md; [dku] = domain knowledge, unverified; [derived] = arithmetic on the labelled inputs.

Web budget: 8 calls used (4 searches, 4 fetches; 3 fetches failed). Where a source is marked "search summary", only the search-result summary was read, not the page.

## 0. Facts checked before the personas

| Fact | Value | Label |
|---|---|---|
| Solaris / Mobile Energy Rentals, Jul 2024 | $200M ($60M cash + about 16.5M Class B shares). 4.0x run-rate contracted EBITDA of about $50M. Mobile gas turbines, not oilfield recip gensets. Majority of assets already contracted to an AI compute provider. Solaris also committed about $308M for turbines on order through Q3 2025 | [source: https://www.sec.gov/Archives/edgar/data/1697500/000119312524176889/d859401dex991.htm] (search summary of the 8-K) |
| MER operating fleet at signing | about 150 MW, so about $1.3M per MW; about $1.06M per MW including the $308M of orders (478 MW) | [dku] for MW; [derived] |
| Atlas / Moser Energy Systems, Jan 2025 | $220M ($180M cash + $40M stock). About 212 MW. 4.3x 2025 EBITDA. EBITDA margin 50%+. About $1.04M per MW | [source: https://www.sec.gov/Archives/edgar/data/1984060/000110465925006117/tm254438d2_ex99-1.htm] (search summary) |
| Moser unit size | Small wellsite gensets, mostly well under 1 MW each, built in-house | [dku] |
| Kodiak Gas Services / Distributed Power Solutions, Feb 2026 | $675M announced for about 384 MW of Caterpillar recips and turbines; about two-thirds contracted to data centers. About $1.76M per MW. One secondary source gives $587M cash at close | [source: https://markets.financialcontent.com/prnews.pressrelease/article/bizwire-2026-2-5-kodiak-gas-services-to-acquire-distributed-power-solutions] (search summary; page fetch failed) |
| Kodiak data-center contract | 76 MW behind the meter, West Texas, six years | [source: https://www.datacenterdynamics.com/en/news/kodiak-gas-services-to-supply-76mw-of-behind-the-meter-gas-power-to-west-texas-data-center/] (search summary; fetch 403) |
| Firefly Capital / Gravity Power & Rental, Aug 2026 | Financial buyer with no stated power operating history bought a 2,000+ unit gas and diesel rental fleet (13 states, 275+ staff). Terms and MW undisclosed. Piper Sandler advised sellers. Management stayed. Seller "spent months" looking for an owner | [source: https://dealroom.co/news/142932-firefly-capital-acquires-gravity-betting-on-rising-demand-for-onsite-pow/] |
| Other consolidation | Fortress took APR Energy's 850 MW of mobile turbines; Solaris bought Genco Power Solutions (400 MW incremental 2026-2028); Solaris signed a 500 MW ten-year rental starting 2027 | [source: search summaries, https://www.utilitydive.com/news/fortress-behind-the-meter-gas-turbines-support-ai-hyperscalers-data-center/740856/ and https://finance.yahoo.com/sectors/energy/articles/solaris-energy-sei-q1-2026-185558331.html] |
| Incumbent scale | Solaris 3.2 GW contracted, 820 MW earning; VoltaGrid 4.3+ GW contracted through 2028; Liberty 1.2 GW; ProPetro 2.6 GW of equipment secured; capex $1.4-1.5M per MW | [notes] |

Three things follow before any persona speaks.

1. The founder's two reference deals are 2024 and January 2025 prices at 4.0-4.3x EBITDA. The 2026 comparable is about $1.76M per MW. Multiples for data-center-capable fleets are now 7-10x [dku].
2. Neither reference deal was "buy an oilfield fleet and reprice it". MER was already a data-center turbine business with order slots. Moser is small wellsite gensets and Atlas has not turned it into a data-center power business of note [dku].
3. A financial buyer without power history did close a fleet deal in August 2026, so the entry step is possible. What it bought is a small-unit oilfield fleet.

## 1. Owner-operator, private natural-gas generator rental company, about 100 MW

Who: founder-owner, 55-65, Permian and Mid-Continent. About 320 units. Mix [dku]: 55 MW in units below 600 kW (rich-burn wellsite sets), 25 MW in 1.0-1.5 MW high-speed lean-burn units at 480 V, 20 MW in 2.5 MW units bought for e-frac and gas-plant work. About 70 staff, 45 of them field mechanics. Revenue about $34M, EBITDA about $18M [dku], consistent with Moser's 50%+ margin [source above].

Incentives and constraints: most of his net worth is this company. He gets two or three unsolicited calls a month from bankers and funds [dku]. He knows the Kodiak price. He has personally guaranteed his equipment line. He cannot fund medium-voltage switchgear, SCR and a 12-month permit cycle out of cash flow.

Alternatives: (a) sell to a public oilfield-power company for cash plus stock; (b) sell to a rental major; (c) take minority capital; (d) rent his 2.5 MW units to a broker or a neocloud as short-term bridge at $45,000-55,000 per MW-month on 12-24 month terms and keep the company.

Decision: sells, but not to this founder as presented. He will not grant exclusivity to a searcher whose equity is not committed.

Terms he would accept:
- $1.5-1.7M per MW for the 45 MW of units of 1 MW and above; $0.8-1.0M per MW for the 55 MW of small units. Blended ask about $120-130M, or about 7x EBITDA. [dku, anchored on Moser $1.04M (2025) and Kodiak/DPS $1.76M (2026)]
- From a buyer with no committed fund: $3-5M deposit, non-refundable after 30 days, plus a signed equity commitment letter from a named sponsor before the data room opens.
- 20-30% rollover only into a vehicle with a visible exit. He prefers listed stock, because MER's sellers took Solaris shares that multiplied [dku].
- Keeps the yard real estate and leases it back. Two-year employment, then out.

Would he contract with data centers himself: he already does at the edge. About 10-15 MW of his 2.5 MW units sit at a bitcoin site and a small GPU site on 12-month paper [dku]. He will not sign 10-year availability guarantees with liquidated damages; that is why he sells.

What changes his decision: a committed-capital buyer at his ask with a 60-day close gets the deal even against a strategic bidding 5-10% more in stock. An uncommitted buyer does not get a second meeting.

## 2. M&A banker, generator-fleet and behind-the-meter power deals, 2024-2026

Incentives: success fee; runs broad auctions; protects certainty of close.

Who bids [dku]: public oilfield-power companies (Solaris, Atlas, Kodiak, ProPetro, Liberty archetypes); private behind-the-meter platforms and their sponsors; energy private equity funds with existing platforms; infrastructure funds; rental majors; Caterpillar and Cummins dealer rental arms. A typical 2026 process: 40-60 parties contacted, 8-12 indications, 3-5 final bids, 5-7 months from launch to close.

Multiples:
| Period | Data-center-capable fleet (units of 1 MW and above, medium-voltage, contracted) | Small-unit oilfield fleet | Label |
|---|---|---|---|
| 2024 | 4.0x, $1.3M per MW | 3.5-4.5x | [source: MER] |
| Jan 2025 | n/a | 4.3x, $1.04M per MW | [source: Moser] |
| Feb 2026 | $1.76M per MW | 5-6x | [source: Kodiak/DPS]; [dku] |
| Late 2026 | 8-10x, $1.7-2.1M per MW | 5.5-7x, $0.9-1.3M per MW | [dku] |

Targets left [dku]: 10-15 private US natural-gas rental fleets of 50-150 MW. Of these, 3-5 have a meaningful share of units of 1 MW and above, and at least half of those are already sponsor-owned or in a process. Below 50 MW there are perhaps 30-40 owner-operators with wellsite fleets.

Does the outsider win: 
- As an independent sponsor with unfunded equity: screened out after first round in a banked process, or the bid is discounted 10-15% for closing risk.
- With a named infrastructure or private equity fund and an approved equity cheque: credible. Financial buyers win roughly one process in four; they win small-unit fleets the strategics do not want (Firefly/Gravity is that case [source above]) and lose data-center-capable fleets, where strategics pay 15-25% more because they drop the megawatts straight into signed backlog.
- Enterprise sales skill is worth nothing in the auction. Sellers and sponsors price committed capital and an operating chief executive.

His dispute with the brief: $100-300M buys 55-170 MW of the right kind of fleet, or 100-300 MW of the wrong kind. The brief assumes 2024 prices for the right kind.

What changes his view: a sponsor letter naming a fund, an operating partner who has run 200 MW+, and a proprietary (non-auction) relationship with one of the 30-40 small owners.

## 3. Regional dealer for a major engine maker

Incentives: sell allocation to the customers who pay deposits and buy service contracts; protect his own rental power fleet, which competes with his customers [dku].

Change of control [dku]:
- Open purchase orders are assignable only with dealer and manufacturer consent. Consent is normally given when the buyer's credit is better.
- Service agreements and parts discounts (typically 10-15% off list) transfer with consent and re-papering.
- "Slots" as the founder imagines them do not exist for a 100 MW oilfield renter. Allocation follows deposit money and purchase history. This customer has bought 8-15 MW a year.

Allocation he would give this owner:
| Delivery year | What he offers | Terms |
|---|---|---|
| 2027 | 0-10 MW of 2.5 MW gas gensets from cancellations | 30% non-refundable deposit, price at shipment |
| 2028 | 20-40 MW | 20-30% deposit now, escalation clause, no price hold beyond 90 days |
| 2029 | 50-100 MW if deposits and a signed offtake are shown | same |

Lead time for 2.5 MW gas gensets is 60-90 weeks [dku]. Blocks of hundreds of MW and the 10 MW-class engines are sold by the manufacturer's strategic accounts group directly to named programmes (2 GW Nscale, 4 GW Joule, over 1 GW ProPetro [notes]); a regional dealer does not control them.

Decision: sells to the acquired company on those terms. Does not give priority over existing gigawatt accounts. Will quote the same data-center sites himself through his own rental and turnkey power group.

What changes it: a manufacturer-level framework agreement, which needs a deposit in the tens of millions and a contracted site list.

## 4. Field operations veteran who has moved oilfield gensets into data-center service

Experience base: e-frac and gas-processing power, then two compute sites of 20-60 MW.

Duty cycle and suitability [dku]:
- Units below 600 kW: not usable. Too many paralleling points, rich-burn emissions, 480 V only.
- 1.0-1.5 MW high-speed units: usable in a pinch, 30-45 units for a 40 MW site, high mechanic hours.
- 2.5 MW lean-burn units: the workable class. Continuous rating on pipeline gas is fine; step-load acceptance is poor, so a battery sized at 30-50% of load for several minutes is required for GPU load swings.
- So 100 MW of oilfield nameplate yields 20-45 MW that should go to a data centre, and 15-33 firm MW after spares.

Redundancy and availability:
- Single-unit availability 92-96% including planned maintenance. Williams' Socrates South carries 275-285 MW nameplate for 200 MW net [notes], a ratio of about 1.4. Use 1.3-1.4 nameplate MW per firm MW.
- Achieved in the first year of a conversion: 98.5-99.5% at the bus. 99.9% is reachable in year two with N+2, a battery and disciplined maintenance. 99.99% is not reachable on one gas lateral; it needs on-site LNG or diesel dual fuel ($100,000-150,000 per MW) or a grid tie.

Emissions [dku]:
- Oilfield units run under nonroad or temporary-source treatment because they move within 12 months. Parked at a data centre they are stationary sources.
- At 0.5 g/bhp-hr NOx, 100 MW running continuously emits about 590 tons a year [derived: 134,000 bhp x 0.5 g x 8,760 h], which is a major source. SCR at 0.05-0.07 g brings it to 60-80 tons. SCR and oxidation catalyst retrofit: $60,000-110,000 per MW.
- Permit time: 1-3 months under a standard permit or permit-by-rule where the site qualifies; 6-12 months for minor new-source review; 12-18 months if major. Community opposition is now routine.

Retrofit and balance of plant per firm MW: medium-voltage switchgear and step-up transformers, controls, SCR, sound walls, fuel conditioning, battery, civil works: $0.6-0.9M on top of the engines. Medium-voltage switchgear lead time is the gating item at 12-18 months unless bought from stock at a premium.

Crews: 12-18 full-time staff for a 50 MW site on 24-hour cover. Oilfield mechanics convert well; controls and relay technicians and medium-voltage electricians do not exist in an oilfield rental shop and must be hired at 30-40% premiums [notes, section 8, for the premium].

Redeployment speed: units come free in 1-6 months because oilfield rentals are short. First power at a compute site: 4-6 months only where the site already has gas, a permit path and switchgear; otherwise 9-15 months.

Decision: would take the operations job. Would refuse to sign up to 99.9% with liquidated damages in year one, and would refuse 99.99% outright without dual fuel.

## 5. Energy procurement lead, top-five hyperscaler

Constraints: approved-vendor qualification; counterparty credit review; safety record; minimum block 200 MW; 15-year terms; emissions controls; preference to own equipment and buy operations only (Solaris signed a seven-year operations contract for about 400 MW of customer-owned plant [notes]; Energy Vault is selling a 1.25 GW system to a hyperscaler outright [notes]).

Alternatives: Williams, VoltaGrid, Solaris, Liberty, Bloom, utility tariffs, direct engine and turbine frameworks.

Decision: refuses. No purchase order, no deposit.

Price reference: pays incumbents about $32,000-38,000 per MW-month at 500 MW+ on 15-year terms ([derived] from Solaris backlog, about $38,000 [notes]; lower end [dku]). Would not pay $38,000-42,000 to a newcomer; a newcomer comes in below the incumbent, not above.

Reason: a 100 MW mixed oilfield fleet cannot deliver a 200 MW block; no data-centre operating record at scale; the owner is a leveraged single-asset vehicle whose 15-year covenant has no value to his credit team.

What changes it: 100 MW+ operating at a compute site for 12 months at 99.9% measured; parent or sponsor guarantee; then a place on the bid list for sites below 100 MW at or under $36,000.

## 6. Head of infrastructure, neocloud, 150 MW of GPUs on order, no power date

Constraints: GPUs idle cost $350,000-830,000 per MW-month (prior-round figure in the ledger); B-rated; cash tied up in GPU deposits; lender consent needed for any security package.

Alternatives: VoltaGrid and Solaris archetypes (minimum deal 100 MW+, capacity committed through 2028 [notes]); mobile turbine renters; rental majors; brokers; buying engines himself (2028 delivery).

Decision: signs a conditional contract and pays a reservation deposit. This is the one real buyer.

Terms:
- 40-50 MW firm, not 150, because that is what this seller can physically deliver.
- $48,000-52,000 per MW-month, five years plus a three-year extension.
- Reservation deposit $2-3M, refundable if permit or gas is not in hand by a date certain.
- Security: six months of fees by letter of credit, not twelve. Twelve months at $50,000 on 50 MW is $30M he does not have.
- Liquidated damages for late delivery and for availability below 99.9%; step-in rights; delivery within nine months.

Reason: any credible engine owner with crews is worth $50,000 against idle GPUs. He treats the acquired company as a real fleet owner for oilfield work and as a first-timer for data-centre work, and prices that with damages and a short fuse.

What changes it: failure to show 2.5 MW-class units and medium-voltage gear physically available cuts it to an unpaid letter of intent. A competing offer from a public fleet owner at the same date wins even at 10% more.

## 7. Development head, colocation developer, utility date slipped two years

Constraints: tenant lease specifies utility power, so tenant consent is needed; construction lender must approve; wants the bridge gone when the grid arrives.

Alternatives: rental majors and mobile turbine renters on 12-36 month paper; Kodiak-type six-year deals (76 MW, six years [source above]); waiting.

Decision: signs a 36-month bridge with two 12-month extensions for 40-60 MW at $46,000-50,000 per MW-month, three months of security, termination on six months' notice once the utility energises. Refuses five to seven years. Refuses twelve months of security.

Reason: value of a month to a landlord is $150,000-240,000 per MW (ledger), so the price clears. The term does not: he will not pay for power in years four to seven that the utility will supply at a third of the cost.

What changes it: tenant refuses consent (then no deal); a rental major offers the same on a master agreement his contractor already holds (then they win on paper speed).

## 8. Infrastructure lead, sovereign or enterprise AI project, first 50 MW

Constraints: formal tender; three reference sites of similar size; performance bond of 10-20% of contract value; investment-grade or bonded counterparty; if outside North America, 50 Hz equipment and local emissions rules make a US oilfield fleet irrelevant.

Alternatives: engine-maker turnkey with long-term service agreement; Wärtsilä or Jenbacher engineering-procurement-construction; Bloom; Aggreko-type global renter; utility.

Decision: refuses. No deposit.

Reason: cannot pass the tender without data-centre references and bonding; prefers a manufacturer-backed turnkey plant he owns.

What changes it: two operating compute references and a surety bond; then eligible at $40,000-44,000 per MW-month, ten years, US only.

## 9. Corporate development head, public oilfield-services company with a power segment

Incentives: every megawatt acquired drops into signed backlog (Solaris archetype: 3.2 GW contracted against 820 MW earning [notes]). Paper currency. Sellers want his stock.

Response:
- Fleets with units of 1 MW and above: bids $1.8-2.2M per MW, 15-25% above a financial buyer, and is still accretive because the megawatt is worth $456,000+ a year on a ten-year contract from day one [derived from $38,000 x 12].
- Small-unit oilfield fleets: passes, or bids 5-6x. Lets the founder have them.
- After the founder closes: hires the best 10 mechanics; offers to buy the 2.5 MW units out of the fleet; offers to buy the whole company once it holds signed compute contracts, at 8-10x.

What changes it: a fall in his share price that removes the paper advantage; evidence that sub-100 MW sites are too small to bother with (he currently signs 76 MW deals, so they are not).

## 10. Chief commercial officer, large private behind-the-meter provider, multi-gigawatt contracts

Position: 4+ GW contracted through 2028, investment-grade counterparties, $5B debt stack, sponsor equity [notes, VoltaGrid archetype].

Response:
- Does not bid for oilfield fleets except for crews.
- Not threatened below 100 MW per site, but his quotes set the ceiling there.
- Would charter the founder's 2.5 MW units as a subcontractor at $30,000-35,000 per MW-month to cover his own delivery gaps. This makes him a customer.
- Expects supply to loosen in 2028-2029 as Caterpillar, Wärtsilä (+35% by early 2028) and others add capacity [notes], and expects new contracts at $30,000-34,000 per MW-month by 2029 [dku].
- Sees the founder's company at 300 MW as a tuck-in acquisition.

## 11. Head of power division, equipment rental major

Position: national branch network, existing master agreements with general contractors and colocation developers, borrowing at roughly 5.5-6.5% [dku], thousands of MW of mostly diesel plus a growing gas fleet.

Response:
- Competes directly for persona 7's 12-36 month bridge at $45,000-60,000 per MW-month and wins on paper already in place.
- Does not sign 10-15 year availability contracts, so does not compete for the long-term product.
- Bids for the same targets only below 6x; does tuck-ins continuously.
- Would re-rent the founder's units on a sub-hire basis.

## 12. Answers to the specific tests

### Do acquirable fleets still exist, and at what price
Yes, 10-15 at 50-150 MW, but the 3-5 that are data-centre-capable cost $1.7-2.1M per MW and attract strategics. Small-unit fleets cost $0.9-1.3M per MW and are winnable. [dku, anchored on sources above]

### Does the outsider win an auction
Only with committed sponsor equity, and then mainly for fleets the strategics pass on. Odds per process about 25% with a sponsor, about 0-5% without.

### Is the acquired company a credible fleet owner on day one
For oilfield work, yes. For compute: yes to the weak-credit neocloud at a risk-priced contract; conditionally to the colocation developer for a bridge; no to the hyperscaler and the tender-bound buyer.

### Price and term by buyer
| Buyer | Signs? | Price per MW-month | Term | MW |
|---|---|---|---|---|
| Hyperscaler | No | (pays incumbents $32,000-38,000) | 15 years | 0 |
| Neocloud | Conditional contract plus $2-3M deposit | $48,000-52,000 | 5 + 3 years | 40-50 |
| Colocation developer | 36-month bridge | $46,000-50,000 | 3 + 1 + 1 years | 40-60 |
| Sovereign or enterprise | No | (would be $40,000-44,000) | 10 years | 0 |

Total demand that would sign with this company in year one: 80-110 MW. Deliverable from a 100 MW acquired fleet: 15-33 firm MW.

### The repricing arithmetic
Oilfield rental already earns about $25,000-35,000 per nameplate MW-month on rented units [dku]; Moser's implied revenue is at most about $39,000 per nameplate MW-month of fleet [derived: $51M annualised EBITDA at 50%+ margin on 212 MW]. A compute contract at $48,000 per firm MW is about $35,000 per nameplate MW after a 1.35 spares ratio. The uplift is 1.0-1.4 times, not two to three times. The gain is term, utilisation and financeability.

Worked case on the persona 1 fleet: move 40 MW nameplate (30 firm MW) to compute. New revenue 30 x $48,000 x 12 = $17.3M. Oilfield revenue given up, 40 MW x $28,000 x 12 x 75% utilisation = $10.1M. Net uplift about $7M of revenue, about $6M of EBITDA, for $20-27M of retrofit and battery. On a $125M purchase that moves EBITDA from $18M to about $24M. [derived from dku inputs]

### Redeployment speed
4-6 months at a prepared site; 9-15 months otherwise. Gating items: medium-voltage switchgear, air permit, gas lateral.

### Value at scale
Assumptions: $500,000 revenue per firm MW-year (blend of $38,000-50,000), 52-55% EBITDA margin (Solaris segment about 45% with services [notes]; pure rental higher [dku]), 9-11x EBITDA, which matches VoltaGrid at $10B+ on 4.3 GW and $1.1B of 2028 EBITDA, about $2.3M of enterprise value per contracted MW [notes, derived]. Capital $1.9-2.2M per firm MW for growth.

| Contracted and operating | Revenue | EBITDA | Enterprise value | Net debt | Equity value | Cumulative capital |
|---|---|---|---|---|---|---|
| 300 MW | $150M | $80M | $0.7-0.9B | $0.35-0.4B | $0.35-0.5B | $0.6-0.7B |
| 1 GW | $500M | $270M | $2.4-3.0B | $1.3-1.5B | $1.0-1.5B | $2.0-2.2B |
| 3 GW | $1.5B | $0.8B | $7-9B | $4-5B | $3-4.5B | $6-6.5B |

Equity is worth about 1.3-1.7 times what was put in at each stage. A founder holding 5-10% after sponsor dilution has $20-50M at 300 MW and $150-400M at 3 GW.

If fuel is recognised gross, reported revenue per MW rises by about $20,000 per MW-month [derived: $3.50 per MMBtu x 8.5 MMBtu per MWh x 730 h], and $1B of recognised revenue needs about 1.3 GW instead of 2 GW. Value does not change.

### Realistic ceiling
- Base case: 300-600 MW contracted by 2031, sold to a strategic or infrastructure fund for $0.8-1.5B.
- Stretch: 2-3 GW, $7-9B of enterprise value, needing $4-6B of capital raised in competition with platforms that already have it.
- Market bound: if 50 GW of onsite gas runs under service contracts at about $450,000 per MW-year, the whole US market is about $22B of revenue a year [derived from SemiAnalysis volume in notes]. A 10% share is $2.2B of revenue and $12-15B of value. $100B is not available in this business.

### Does anything get harder to compete with as it grows
- Borrowing cost: from 11-12% private credit at 100 MW to 7-8% rated notes or asset-backed debt at 1 GW+ [dku; Solaris is BB- with $1.25B of notes, notes]. This is the main scale effect and incumbents already have it.
- Engine frameworks: 5-10% price and earlier delivery at manufacturer-account scale [dku].
- Mobile spares and overhaul shop shared across sites. Islanded sites cannot share running reserve, so the benefit is small.
- Permitting record and crews: real but hireable.
- Nothing else. No network effect, no proprietary technology, each site is bid separately, customers increasingly own the equipment and buy operations only, and grid arrival ends bridge contracts.

It is a leveraged asset pool with a cost-of-capital scale curve. It is sold in five years; it does not compound on its own.

## 13. Five most damaging objections

1. The fleet the budget can win is the wrong fleet. 55-80% of an oilfield rental fleet is units too small for compute; 100 MW nameplate gives 15-33 firm MW. The right fleets go to strategics at $1.7-2.1M per MW. [dku; Kodiak/DPS source for price]
2. The reference prices are two years stale and the reference deals were different transactions. 4.0-4.3x in 2024-2025 against 7-10x now; MER was already an AI turbine business. [source: MER and Moser 8-Ks; dku for current multiples]
3. No repricing gain of two to three times. Per nameplate MW the uplift is 1.0-1.4 times; about $6M of EBITDA on a $125M purchase. [derived]
4. The founder adds nothing a sponsor needs. Sellers, bankers, dealers and buyers all price committed capital and an operating record. Sales skill is useful only after megawatts exist, and the megawatts available sell themselves to the one buyer type that signs. A sponsor does this through an existing platform or with an operator as chief executive. [dku; Firefly kept Gravity's management, source]
5. Creditworthy buyers still refuse; the signers are a B-rated neocloud and a three-year bridge. Neither supports 40-45% long-dated debt on new-build, and prices are expected to fall to $30,000-34,000 by 2029 as engine supply expands. [notes for capacity additions; dku for price path]

## 14. Numbers in the brief disputed

| Brief | Corrected | Basis |
|---|---|---|
| Solaris bought "a roughly 150 MW rental fleet for about $200M" as an entry template | Correct figures; wrong template. Turbine fleet, mostly contracted to an AI customer, 4.0x, plus $308M of committed orders | [source: MER 8-K] |
| Atlas "about $220M" | Correct; 212 MW of small wellsite gensets at 4.3x; not a compute fleet | [source: Moser 8-K]; [dku] |
| $100-300M buys 50-150 MW with what is needed | Buys 55-170 MW of capable units at $1.7-2.1M per MW, or 100-300 MW of small units of which 20-45% is usable | [source: Kodiak/DPS]; [dku] |
| "Two to three times the oilfield rate" | 1.0-1.4 times per nameplate MW | [derived] |
| Investment-grade buyers at $38,000-42,000 | They refuse this company; they pay incumbents $32,000-38,000 | [notes, derived]; [dku] |
| Sub-investment-grade: five to seven years, 12 months of security | Neocloud: 5 + 3 years, six months. Colocation: three years, three months | panel |
| 99.9% at first | 98.5-99.5% in year one; 99.9% from year two | [dku] |
| 99.99% with a second fuel path | Only with on-site stored fuel or grid tie, $100,000-150,000 per MW | [dku] |
| "$1bn of revenue (about 2 GW) valued at high single-digit to low double-digit billions" | $4.5-6B of enterprise value, $2-3B of equity. The $10B+ comparable has 4.3 GW and about $1.1B of EBITDA | [notes, derived] |
| Dealer relationship carries growth orders for 2028 | 20-40 MW for 2028 on 20-30% deposits; large blocks are sold by the manufacturer directly | [dku] |
| Units move "as contracts roll off" | 4-6 months at a prepared site, 9-15 months otherwise | [dku] |

## 15. Conditions under which each "no" becomes "yes"

- Owner: committed equity letter, $3-5M hard deposit, his price, 60-day close.
- Banker: named sponsor, operating partner with 200 MW+ history, or a proprietary deal.
- Dealer: tens of millions in deposits plus signed offtake; manufacturer-level framework.
- Hyperscaler: 100 MW+ at a compute site for 12 months at measured 99.9%, sponsor guarantee, price at or below $36,000.
- Colocation developer (long term): never for five to seven years; yes to three years with termination on energisation.
- Sovereign or enterprise: two compute references and a surety bond; US only.
- Public oilfield-power company: stops outbidding only if its share price falls or the fleet is small-unit.

## 16. Probabilities

| Event | Estimate | Build-up |
|---|---|---|
| An acquisition closes within 12 months | 18% | Sponsor commits within 5 months about 38%; then a deal signed and closed in the remaining 7 months about 45%; small allowance for a sub-50 MW deal funded by a family office |
| First paid compute delivery within 18 months | 12% | Close within about 14 months about 24%; then delivery within the window about 50%, helped by a roughly one-in-three chance the target already has a few MW at a compute site |
| $1bn of annual recognized revenue within 7 years | 3% | Needs 1.3-2 GW operating and $3-4B of capital. Close at all about 30%; scale to that size about 10% |
