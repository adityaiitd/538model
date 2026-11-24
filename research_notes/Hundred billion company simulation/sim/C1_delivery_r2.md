# C1 v2 delivery panel, round 2 (simulated, 24 November 2026)

Everything below is a simulated hypothesis from archetype personas. It is not supplier, regulator or customer validation. No real quotes, orders or people.

Evidence labels: [notes] = power_grid.md. [source: URL] = checked this session. "summary" = taken from a search-result summary, page not opened. [dk] = domain knowledge, unverified.

Web budget used: 5 of 5.

## 0. What the panel checked on the web

| Fact | Finding | Label |
|---|---|---|
| Korean maker capacity | HD Hyundai Heavy signed 684 MW (April 2026, KRW 627.1B) and 1,000 MW (9 Aug 2026, $673.8M) of 9.6 MW HiMSEN medium-speed gas sets for US data centers. That is about $650-675 per kW for generating sets alone at gigawatt scale (derived). No delivery schedule published. | [source: https://www.datacenterdynamics.com/en/news/hyundai-heavy-industries-signs-1gw-natural-gas-engine-supply-deal-with-unnamed-us-data-center-developer/, summary]; [source: https://www.asiae.co.kr/en/article/2026042214542984228, summary] |
| Other non-incumbents | Everllence (formerly MAN Energy Solutions): 480 MW, 24 engines, for an off-grid US data center. Bergen Engines: about 750 MW to Crusoe. | [source: https://www.datacenterdynamics.com/en/news/everllence-to-supply-480mw-of-gas-engines-to-data-center-developer-in-us/, summary]; [source: https://www.powermag.com/engine-power-plants-surge-as-data-centers-drive-unprecedented-demand/, summary] |
| Incumbent lead times | INNIO 450 MW Jenbacher J624 order (September 2026) delivers by 2028. Cummins deliveries scheduled 2026-2030. Trade press gives generator lead times of two years, some near three. Enverus says engines can be online within 24 months of order. | [source: https://pgjonline.com/news/2026/september/innio-secures-450-mw-order-to-power-next-generation-data-centers, summary]; [source: https://www.powermag.com/data-centers-are-turning-to-gas-generators-for-prime-power-to-eliminate-long-lead-times-for-grid-connections/, summary] |
| Texas air permits | Governor ordered the state air agency on 21 Sep 2026 to pause permit issuance for data-center projects until ERCOT finishes a review, expected mid-December 2026. The pause covers fully islanded sites. Effect on standard permits is unclear. Six self-powered campuses totalling 8.7 GW are waiting. | [source: https://www.bracewell.com/resources/governor-abbott-orders-tceq-to-pause-all-permit-issuance-for-data-center-projects/, summary]; [source: https://fourweekmba.com/ai-texas-freeze-hits-air-permits-for-8-7gw-of-ai-campuses/, summary] |
| Texas permit route | Behind-the-meter plants mostly use the standard permit for electric generating facilities (gas-engine version effective 30 Jan 2025), with no public notice. One registration carried a NOx limit of 50 tons a year and drew a notice of intent to sue from an environmental group. | [source: https://acoel.org/blog/the-great-power-secession-texas-air-permitting-and-the-data-center-boom/, summary]; [source: https://environmentalintegrity.org/wp-content/uploads/2026/07/2026-07-22-Vantage-Voltagrid-NOI_final.pdf, summary] |
| Gas laterals | One data-center lateral in New Mexico slipped to 2027. One developer's proposed lateral sites had no firm interconnection timeline in August 2026. Pipelines are themselves building onsite power. | [source: https://sourcenm.com/2026/08/17/proposed-gas-pipeline-for-project-jupiter-data-center-delayed-to-2027-filings-show/, summary]; [source: https://blockspace.media/insight/cipher-gas-laterals-25gw-hpc/, summary] |

Not found: any published price for refurbished gas gensets, any delivery date for the Korean orders, typical meter-station lead times. Those figures below are [dk].

Consequence for the founder's central assumption: the "makers with open capacity" have already sold about 2.9 GW to gigawatt buyers in 2026. They are not an untouched pool. A 25 MW order queues behind those.

## 1. Allocation manager, incumbent high-speed gas engine maker

Who: allocates factory slots and dealer quotas. Rewarded for multi-year frame agreements and service attach. Backlog at one incumbent is $78B, and capacity is the pacing factor [notes].

Decision: refuses a direct sale. Refers the founder to the dealer queue.

Terms through the dealer: delivery H2 2028 for orders placed now (orders this autumn deliver "by 2028" [source: pgjonline, summary]); $800-1,000 per kW for a packaged 2.5-4.5 MW set with exhaust treatment [dk]; 20-30% deposit [dk]; no slot held without a frame order of 200 MW+ or a named investment-grade end user [dk].

Reason: frameworks of 1.25 GW and 2 GW [notes] take the slots. Oilfield-service fleets already hold 2.6 GW of secured units [notes].

Changes the decision: a 250 MW+ frame order with a funded parent.

## 2. Export sales director, Korean or Japanese medium-speed gas engine maker

Who: sells 5-10 MW engines, mostly marine and island power. Wants US reference plants. Risk: warranty cost in a market with no service base, and buyer default.

Decision: conditional yes.

Terms:

| Item | Figure | Label |
|---|---|---|
| Price, small order | $750-900 per kW ex-works, against $650-675 at 1 GW | [dk]; [source: summaries above] |
| US tariff on Korean or Japanese machinery | about 15% | [dk] |
| Ex-works delivery | 10-14 months from deposit | [dk] |
| Sea freight, port, inland heavy haul (100-150 t per engine) | 2-3 months | [dk] |
| Payment | 20-30% deposit, confirmed letter of credit for 100% before shipment | [dk] |
| Service | Parts depot and field engineers from the home country for the first two years; long-term service agreement with availability damages capped at one year of service fees | [dk] |

Problems the director states plainly:
- Unit size. The standard set is 9.6 MW. A 25 MW block at N+2 needs three running and two spare: 48 MW installed for 25 MW sold. With 5.5 MW units it is seven sets, 38.5 MW.
- These are not skid-mounted. They need concrete foundations, an engine hall or heavy enclosures, stacks and radiator fields. Moving one costs 20-30% of installed cost [dk].
- No US plant of this make is operating yet. A lender's engineer will ask for one.
- US emissions packaging (catalytic reduction and oxidation catalyst), UL-listed switchgear and 60 Hz alternators are bought separately.

Deposit to commercial operation: 18-24 months. The brief says 12-15 months to delivery and implies operation soon after.

Changes the decision: nothing needed to sell. To back a 99.9% guarantee: a 200 MW+ fleet that justifies a US service base.

## 3. Dealer, refurbished gensets and aeroderivatives

Who: buys from oilfield, cogeneration, landfill and failed crypto sites. Sells for cash.

Decision: yes, as-is, where-is.

Terms:

| Item | Figure | Label |
|---|---|---|
| Used 2-2.5 MW high-speed gas sets | $600-1,000 per kW, lots of 2-10 units, mixed hours and vintages | [dk] |
| Refurbished aeroderivatives | about $1.3M per MW; well-kept used $1.5-1.7M per MW | [notes] |
| Lead time | 1-4 months for stock units; 12-18 months for refurbished aeroderivatives | [dk]; [notes] for summer-2027 delivery on an April 2026 order |
| Payment | 30-50% deposit, balance before shipment | [dk] |
| Warranty | 90 days to 12 months on workmanship; no performance or availability guarantee | [dk] |

Problems:
- European cogeneration units are 50 Hz. Most cannot be used at 60 Hz without derating or a new alternator [dk].
- Older engines may not meet current federal engine standards or state control requirements without retrofit and stack tests [dk].
- Aeroderivatives are 22-50 MW each. N+2 on a 25 MW block means three units, 66-150 MW installed. They also need 400-700 psig gas and burn about 20% more fuel per MWh than engines [dk].
- The good lots went in 2024-2026. Refurbishers sold 21 and 13 units at a time to large buyers [notes].

Changes the decision: none. The dealer does not care who buys.

## 4. State air-permitting authority

Who: permit section manager. Bound by federal thresholds, state control rules and, in Texas, the governor's order.

Emission arithmetic for one 25 MW block (derived, [dk] inputs): 27 MW average output is about 36,200 brake horsepower.
- NOx without catalytic reduction at 0.5 g/bhp-h: about 175 short tons a year.
- NOx with catalytic reduction at 0.05-0.07 g/bhp-h: about 18-25 tons a year.
- Formaldehyde with oxidation catalyst: about 8-16 tons a year, against a 10-ton threshold for a major source of a single hazardous pollutant.

Thresholds [dk]: Title V at 100 tons a year; federal major-source review at 250 tons a year in attainment areas; 25-50 tons in serious ozone non-attainment areas such as Dallas-Fort Worth and Houston. All blocks on one site are added together.

Timelines:

| Case | Time to authorization | Label |
|---|---|---|
| Texas standard permit, 25 MW with catalytic reduction | 1-4 months in normal times; paused since 21 Sep 2026 | [dk]; [source: Bracewell, summary] |
| Other states, minor or synthetic-minor permit | 6-12 months | [dk] |
| 150 MW site with catalytic reduction on every unit (110-150 tons NOx) | Synthetic minor, 6-12 months, plus Title V application after start-up | [dk] |
| Any site over 250 tons, or in non-attainment | 12-24 months | [dk] |

Decision: conditional yes for 25 MW with catalytic reduction and oxidation catalysts on every unit, enforceable limits and one-hour NO2 modeling. No date can be given in Texas while the pause holds.

Reasons and objections:
- One-hour NO2 modeling often fails for short stacks on containerized units [dk]. Taller stacks or more spacing follow.
- Splitting a campus into several "minor" plants invites citizen suits [source: EIP notice, summary].
- Refurbished units without certification need stack tests before operation.
- Catalytic reduction adds $80-150 per kW and urea cost [dk].

Changes the decision: lifting of the Texas pause; certified new engines with vendor emission guarantees.

## 5. Gas pipeline or local distribution company interconnect manager

Who: manages taps, meter stations and capacity requests. Protects existing firm shippers and winter reliability.

Load: 25 MW at about 8,300 Btu/kWh is about 5,000 MMBtu a day (4.8 MMcf a day). 150 MW is about 30,000 MMBtu a day (derived, [dk]).

Decision: conditional yes on a transmission pipeline; often no on a distribution system.

Terms:

| Item | Figure | Label |
|---|---|---|
| Tap and meter station, customer-paid in advance | $1.5-4M | [dk] |
| Time from signed interconnect agreement | 9-15 months | [dk] |
| Lateral | $2-4M per mile; 6-18 months for right-of-way | [dk] |
| Firm transport | Only where capacity exists; expansions take 2-4 years | [dk] |
| Credit | 3-12 months of demand charges as collateral from a non-rated shipper | [dk] |
| Distribution utility service at this volume | Usually interruptible on peak winter days | [dk] |

Reasons and objections:
- 99.9% availability means 8.76 hours of outage a year. One winter gas curtailment uses several years of allowance. Lean-burn gas engines have no second fuel.
- The pipeline's own affiliates build onsite power for large buyers [notes]. Best taps go to them first.
- Laterals slip: one slid to 2027, others have no dates [source: summaries above].

Changes the decision: site within one mile of a transmission line with unsubscribed capacity; customer-funded facilities; posted collateral.

## 6. Construction contractor (kept from round one)

Decision: bids balance of plant only. Refuses a 12-15 month wrap.

Schedule from deposit:

| Route | Months to operation | Critical path | Label |
|---|---|---|---|
| Used high-speed sets in hand, site near gas, permit outside Texas pause | 12-16 | Gas meter station 9-15; 15 kV paralleling switchgear 52-80 weeks [notes] | [dk] |
| New high-speed sets from incumbent dealer | 20-26 | Engine slot | [dk] |
| New medium-speed sets from Korea or Japan | 18-24 | Engines, foundations, hall, commissioning | [dk] |

Installed cost per MW sold (25 MW block, N+2):

| Item | High-speed route | Medium-speed route | Label |
|---|---|---|---|
| Installed generation needed | 33 MW | 38.5-48 MW | derived |
| Generation plant at $1.2-1.5M per installed MW | $40-50M | $46-69M | [notes] for $1.4-1.5M; [dk] |
| Battery, 10 MW / 20 MWh grid-forming | $9-12M | $9-12M | [dk] |
| Gas tap, meter station, short lateral | $2-5M | $2-5M | [dk] |
| Permits, engineering, financing, contingency | $4-6M | $5-7M | [dk] |
| Total | $55-73M | $62-93M | derived |
| Per MW sold | $2.2-2.9M | $2.5-3.7M | derived |

Central figure: $2.4M per MW sold, $60M per block. The brief says $1.45M and $36M.

Why the gap: the $1.4-1.5M in [notes] is a fleet figure without a battery and without small-block redundancy. One real 200 MW plant carries 275-285 MW of nameplate [notes], a 40% overbuild. At 25 MW with N+2 the overbuild is 30-90%.

## 7. Engine fleet operator (kept; now an oilfield-power type)

Operating cost per 25 MW islanded block, fuel excluded:

| Item | $M a year | Label |
|---|---|---|
| Engine service agreement and overhaul reserve, about $10 per MWh on 186 GWh | 1.9 | [dk] |
| On-site crew, 8-12 people at about $150,000 loaded | 1.2-1.8 | [dk] |
| Insurance, including machinery breakdown | 0.4-0.7 | [dk] |
| Property tax | 0.4-0.8 | [dk] |
| Urea, lube oil, catalysts | 0.3-0.4 | [dk] |
| Battery service, remote monitoring, site overhead | 0.4-0.6 | [dk] |
| Total | 4.6-6.2 | derived |

That is $185,000-250,000 per MW-year. Cash margin is $205,000-270,000 per MW-year, or $5.1-6.8M per block. The brief says $6.3-9.4M.

Payback on $60M: 9-12 years. A seven-year contract returns $36-48M of margin. With a four-year exit and 12 months of fees: $32-39M. The asset must be worth 35-45% of cost at release for capital to be returned at all.

Redeployment: demobilize and remobilize costs $100,000-200,000 per MW and 4-8 idle months for containerized sets [dk]. Each new site needs a new air permit and gas tap.

Would the operator serve these sites itself? Yes, with existing units, at $45,000-70,000 per MW-month for three-to-five-year terms to weak credits [dk]. The founder's $38,000 is not the constraint. Equipment and capital are.

Decision: would not co-invest. Would sell operations and maintenance at $50,000-70,000 per MW-year.

## 8. Insurer and lender desk (kept)

- Damages cap is now three months of fees, $2.85M per block. That is bondable with 50-100% collateral [dk]. This part of round one is fixed.
- Property and machinery breakdown: 0.6-1.2% of insured value for known makes; mixed refurbished fleets get double the rate or a breakdown exclusion; unproven-design clauses for makes with no US operating record [dk].
- 99.9% islanded on a single gas feed: gas interruption must be excluded, or the guarantee is not insurable.
- Tenant credit insurance on a B-rated neocloud: 12-month tenor, 2-4% of insured receivables, limited capacity [dk].
- Lender: this is asset-based lending. Advance rate 50-65% of orderly liquidation value [dk]. That value is 60-75% of cost for containerized incumbent sets and 30-40% for foundation-mounted non-incumbent engines [dk]. Debt is therefore 20-45% of cost at 10-13%, not 55% [dk].

Decision: insures property. Declines to cover fuel-caused downtime. Lends 20-45%.

## 9. Regulator (kept)

- A fully islanded plant needs no grid interconnection study. Round-one objections 1 and 2 are answered on that point.
- The Texas pause shows the state can still gate islanded power through air permits [source: Bracewell, summary].
- Selling electricity to another party behind the meter is restricted in many states with franchised utilities [dk]. The contract must be an equipment lease with the customer buying the gas. The "private utility for compute" step needs franchise law to change.
- When grid service arrives in Texas, backup generation covering 50%+ of demand must be disclosed and can be directed by ERCOT in emergencies [round-one source, summary].

Decision: no approval needed from the utility commission for an islanded lease in Texas. Outcome in franchised states is case by case, 6-12 months of legal risk [dk].

## 10. Senior power-systems engineer (kept)

Decision: conditional yes. No at $5-10M of funding.

What breaks first:
1. Capital and equipment. Deposits, letters of credit and an 18-24 month team cost several times the stated funds.
2. Fuel. One pipeline, no second fuel, 8.76 hours a year of allowance.
3. Load transients. Lean-burn engines accept 10-25% load steps [dk]. A 25 MW training cluster can swing 30-60% in under a second [dk]. A 10 MW battery inverter is marginal; 15-25 MW is safer. Load oscillation can also excite generator shaft modes [dk].
4. Tenant default with engines bolted to foundations.
5. Texas permit pause.

Team before first operation: 30-40 people, $8-12M a year [dk].

Would join if: $40M+ raised, containerized sets from a known maker under contract, site outside the Texas pause with a signed gas interconnect.

## 11. Capital to reach one operating block

| Use | $M | Label |
|---|---|---|
| Engine deposits and progress payments before a fund will close | 6-12 | [dk] |
| Battery and switchgear deposits | 2-3 | [dk] |
| Gas tap and meter station, paid in advance | 1.5-4 | [dk] |
| Permits, engineering, legal | 1.5-2.5 | [dk] |
| Team for 18-24 months | 14-22 | [dk] |
| Customer security shortfall and working capital | 3-5 | [dk] |
| Total if a fund finances construction at close | 30-45 | derived |
| Total if the fund buys only at operation | 60-75 | derived |

The brief says $5-10M covers the first two blocks.

## 12. Round-one objections, status

| Round-one objection | Status | Reason |
|---|---|---|
| 1. No rule grants earlier energization | Resolved, with a new dependency | Islanding removes the grid rule. Air permit and gas tap replace it; Texas has paused permits for islanded data-center power. |
| 2. Utility holds the breaker and contracts only with the customer | Resolved | No utility obligation. Residual: third-party power sale law in franchised states. |
| 3. Four hours does not cover real events | Resolved for duration | Engines run continuously. New exposure: single gas feed against 99.9%. |
| 4. Cost understated ($90M against $62M) | Unresolved | Same error again: $60M per block against $36M. |
| 5. Guarantee unbacked; deposit consumes the capital | Partly resolved | Damages cap is small and bondable. Capital gap is wider: $30-45M against $5-10M. Non-incumbent and refurbished suppliers cannot back 99.9%. |

## 13. Probabilities (panel's honest estimate)

- First paid commercial delivery of a 25 MW block within 18 months (by May 2028): 12%. Only the used high-speed route can make the date.
- $1 billion of annual recognized revenue within 7 years: 2%. It needs about 88 blocks, 2.2 GW sold and about $5.3B of capital at corrected cost, leased to weak credits.
