# C1 v1 delivery panel, round 1 (simulated, 24 November 2026)

Everything below is a simulated hypothesis from archetype personas. It is not customer or supplier validation. No real quotes, orders or people.

Evidence labels: [notes] = power_grid.md. [source: URL] = checked this session. [dk] = domain knowledge, unverified.

Web budget used: 8 of 8 calls. Two White & Case pages returned 403 and one Perkins Coie page redirected, so those facts come from search-result summaries only and are marked "summary".

## 0. What the panel checked on the web

| Fact | Finding | Label |
|---|---|---|
| PJM connect-and-manage | Filed 13 Aug 2026 as Interim Resource Adequacy Service (IRAS), docket ER26-3515. Applies to new loads of 50 MW+ entering service after 1 Jun 2027. PJM dispatch orders the cut ahead of pre-emergency demand response. No cap on hours per event or per year is stated. It is a resource-adequacy tool. Nothing in it ties to earlier transmission energization. | [source: https://powermag.com/pjm-widens-response-to-data-center-load-as-capacity-shortfalls-deepen] |
| FERC ruling on IRAS | Order of 9 Oct 2026 accepted the large-load definition and registry and rejected other parts. A press summary says IRAS itself was rejected and PJM was told to refile. Scope of rejection not confirmed. | [source: https://www.pjm.com/pjmfiles/directory/etariff/FercOrders/9207/20261009-er26-3515-000.pdf, summary]; [source: https://www.publicpower.org/node/31450, summary] |
| Texas SB 6 rule | PUCT Project 58481 final rule filed about 18 Sep 2026. Covers interconnection standards, contributions and security for loads of 75 MW+. Security is set on contracted peak demand, so onsite backup does not reduce it. | [source: https://www.whitecase.com/insight-alert/puct-sets-financial-commitments-data-center-interconnection-governor-pauses-permit, summary] |
| ERCOT curtailment procedures | ERCOT's SB 6 tracker lists operating procedures for curtailing large loads with backup generation covering 50%+ of load as still in progress in October 2026. | [source: https://www.ercot.com/files/docs/2025/09/15/89th-Legislative-Session-PPTX-ERCOT-Status-October-2026-Final-PDF.pdf, summary] |
| PUCT co-location order | 24 Jul 2026 order says emergency curtailment of a co-located data center is not capped by the size of the paired behind-the-meter generator. | [source: https://www.whitecase.com/insight-alert/puct-affirms-curtailment-authority-over-co-located-data-centers-first-net-metering, summary] |
| ERCOT battery revenue | Average battery earned about $24/kW-year annualized in 2026 through 16 Aug, $28 in 2025, $193 in 2023. | [source: https://modoenergy.com/research/ercot-bess-buildout-q3-2026, summary] |

Consequence: of the three legal hooks in the brief, none is a rule in force today that says "accept curtailment, get energized earlier" at 50 MW+. SB 6 imposes curtailment on new large loads as an obligation, not as a trade for speed. PJM's version is not in force and was at least partly rejected. Utility flexible-connection programs are MW-scale pilots [notes].

## 1. Allocation manager, major battery system supplier

Who: allocates 2027 factory slots at a top-three integrator. Paid on margin and on-time delivery, punished for bad debt and for liquidated damages. Fluence's FY2026 gross margin of 2.8% came from delay penalties [notes], so every supplier is now tightening terms.

Constraints: 2027 output is nearly sold at the scale leader [notes]. Compliant North American cell supply is about 100 GWh by end-2027 against 58 GWh of demand in 2027 and 90 GWh in 2028 [notes]. Hyperscalers buy direct: one integrator booked about $550M from a single hyperscaler [notes].

Alternatives: sell the same 200 MWh to an investment-grade utility, a hyperscaler, or an IPP with a 2 GWh frame agreement.

Decision: conditional yes. A 200 MWh order is small (about 0.2% of one leader's nameplate). It gets no priority and no special price.

Terms the persona would accept:

| Item | Scale leader type | Second-tier US-content integrator | Chinese integrator |
|---|---|---|---|
| Price, AC block delivered | $230-270/kWh [dk] | $215-250/kWh ($215 per [notes]) | $115/kWh before tariffs [notes], $150-190 landed [dk] |
| Earliest delivery if ordered Q1 2027 | Q4 2027 to Q2 2028 [dk] | Q4 2027, 9-14 months from notice to proceed [dk] | 6-9 months [dk] |
| Deposit | 10-20% non-refundable at signing, $5-10M [dk] | 10-15% [dk] | 10-30% [dk] |
| Credit support | Letter of credit or cash for 100% of balance; 80-90% paid before delivery [dk] | Same | Same |
| Tax credit | Eligible | Eligible if supplier certifies 60% non-FEOC content for 2027 starts [notes] | Fails FEOC test, no credit [notes]. Likely barred by the customer's security review and by Texas critical-infrastructure law [dk] |
| Delay damages given to buyer | Capped at 10-15% of contract price [dk] | Same | Same |
| Availability guarantee under service contract | 97-98%, damages capped at one year of service fees, about $1.5M [dk] | Same | Same |

Reasons and objections:
- The deposit alone equals the founder's whole $5-10M.
- The supplier will not back the customer uptime guarantee. Its damages cap is about $1.5M a year. The founder's cap is $13.2M. The founder carries the $11.7M gap per block.
- Standby duty at 100% state of charge is outside the normal warranty envelope. LFP warranties commonly limit average resting state of charge [dk]. Expect a warranty amendment and a price adder, or faster fade.
- Grid-forming, islanded operation of GPU load needs application engineering. The supplier quotes it as a paid study (3-4 months) and excludes it from standard performance guarantees.

Changes the decision: investment-grade parent guarantee or funded letter of credit, a 1 GWh+ frame order, or the hyperscaler as buyer of record.

## 2. Engineering and construction contractor, battery plants at data centers

Who: project director at an electrical contractor that has built BESS and data-center substations. Paid on margin and schedule. Will not take interconnection or utility-approval risk.

### Sizing error in the brief
200 MWh nameplate does not deliver 50 MW for four hours at the campus bus in year 10.

| Step | Factor | Label |
|---|---|---|
| Energy to deliver | 200 MWh | brief |
| Retention at year 10, held full in standby | 0.83 | [dk] |
| Availability, about 60 units with one or two out | 0.97 | [dk] |
| Transformer and collection losses | 0.985 | [dk] |
| Beginning-of-life nameplate needed | about 250 MWh | derived |

Alternative: 215 MWh at start plus about 35 MWh of augmentation by year 6.

### Real installed cost, 250 MWh, compliant US supply, islanding-capable, 2027 build

| Item | $/kWh nameplate | $M |
|---|---|---|
| Battery system, AC block | 215-240 [notes]/[dk] | 54-60 |
| Civil, medium-voltage collection, switchgear, protection, controls, microgrid controller, fire protection, commissioning, with data-center labor premium of 30-42% [notes] | 70-90 [dk] | 18-22 |
| Tie-in at campus 34.5 kV bus, grounding, synchronizing | 10-15 [dk] | 2.5-4 |
| Studies, permitting, legal, financing fees, interest during construction, sales tax, builder's risk, 5-8% contingency | 30-45 [dk] | 7.5-11 |
| Total | 325-390 | 81-98 |

Central figure: $90M, which is $360/kWh on nameplate and $450/kWh on the 200 MWh actually guaranteed. The brief says $62M.

The $309/kWh median in [notes] is a front-of-meter grid project and includes projects with cheaper Chinese supply. [notes] gives a $100/kWh premium for compliant US-made systems.

If a high-voltage step-up is needed (campus has no spare medium-voltage position): add $5-8M and the schedule fails outright. Step-up transformers take 144-160+ weeks and high-voltage breakers about 125 weeks [notes].

### Schedule from signed customer contract

| Activity | Months | Label |
|---|---|---|
| Utility restudy and protection requirements (critical path; final design waits on it) | 6-12 | [dk] |
| Battery delivery from notice to proceed | 9-14 | [dk] |
| 38 kV switchgear line-up, if new | 18-24 (78-104 weeks) | [notes] |
| 15 kV switchgear | 12-18 (52-80 weeks) | [notes] |
| Fire authority and customer insurer review (NFPA 855, UL 9540A, hazard analysis, setbacks from data halls) | 3-6 | [dk] |
| Construction | 5-7 | [dk] |
| Commissioning, utility witness tests, islanding tests on live load | 2-3 | [dk] |

Realistic: 16-24 months. Best case 12-14 months, only if the battery slot is reserved before the customer signs, the campus already has spare medium-voltage breaker positions, and the utility restudy is finished. First project: 20-26 months.

Decision: will bid fixed-price for the balance of plant only, at $70-90/kWh, with schedule relief for utility approval, owner-furnished batteries and owner-furnished switchgear. Will not sign a 9-12 month wrap.

Labor: peak 80-120 craft, of which 40-60 electricians, competing with the data hall build on the same site that needs up to 1,500 workers [notes]. Commissioning and protection engineers are the scarcest people; no count exists [notes].

Changes the decision: owner holds equipment slots and a signed utility protection scope before notice to proceed.

## 3a. Director of transmission planning and large-load interconnection, wires utility (ERCOT type)

Who: runs load studies and signs facility agreements. Incentives: reliability record, regulated return on new wires, no reward for speed. Career risk is a large load that trips or forces load shed on residential customers.

Answers to the founder's questions:

- Earlier energization for a battery-backed commitment? Not as a right. Today's sequence is study, ERCOT approval, batch allocation by year for 2028-2032, security of $50,000/MW [notes]. A new request filed now missed the 10 July 2026 Batch Zero cut-off [notes]. Only 5.9 GW of large load was observed energized against a 474 GW queue [notes].
- Under which rule? SB 6 obliges new loads of 75 MW+ to be curtailable in firm load shed. It does not grant earlier service in exchange. The founder's 50 MW block is below the 75 MW threshold. [source: summaries above]; [dk]
- Who signs? The customer of record. The utility will not sign a curtailment agreement with a third-party battery owner. The founder can only indemnify the customer.
- Who controls the breaker? The utility, by remote trip at the point of interconnection, with telemetry. [notes] records one utility calling 100% control of the load-side breaker non-negotiable. The battery therefore sits behind a breaker someone else opens. The campus must island on the battery.
- Charging counts as load. A 50 MW load plus 12.5-25 MW of charging draws 62-75 MW at the meter. Charging will be limited to off-peak windows inside the MW allocation. After a four-hour event the block may not be allowed to recharge before the next day's event.

How long are real events?

| Cause of the delay to firm service | Typical event | Tail | Does 4 h / 200 h a year cover it? |
|---|---|---|---|
| System emergency in summer | 2-8 h, 0-5 a year [dk] | Consecutive days | Mostly |
| System emergency in winter | 8-16 h a day [dk] | About 70 h of load shed in February 2021 in Texas [dk]; about two days of emergency actions in PJM in December 2022 [dk] | No |
| Local transmission constraint until a line or transformer is built (the usual reason firm service slips to 2029-2031) | 6-12 h blocks on peak days [dk] | 200 to 2,000+ h a year, known only after study [dk] | Often no |
| Published program example | Up to 10 h per event, 225 h a year (Idaho Power) [notes] | | No |

Studies: steady-state, short-circuit, dynamic stability, ride-through and oscillation screening. Adding a 50 MW grid-forming inverter plant behind the meter is a material change and triggers a restudy with validated models: 6-12 months [dk]. If the battery exports to earn market revenue, it needs a full generator interconnection study and ERCOT commissioning approvals: 12-24 months [dk].

Decision: refuses the product as described. Will study a customer request for non-firm energization of a stated MW ahead of upgrades.

Terms: utility-owned remote trip and direct load-shed relay; customer pays study and facilities; curtailment hours set by the study, not capped at 200; no export unless separately interconnected; charging schedule in the agreement.

One point in the founder's favor: grid-forming storage that keeps the load from dropping off during voltage dips solves a real stability worry for planners [dk].

Changes the decision: an ERCOT or PUCT rule that allocates earlier MW to loads with a duration-limited curtailment obligation, and one executed precedent at 50 MW+. [notes] found none.

## 3b. Grid operator or state regulator (ERCOT/PUCT, PJM, vertically integrated utility)

ERCOT/PUCT staff type:
- Rule 58481 is final but about security and standards. Curtailment procedures for loads with backup are still being written [source: ERCOT tracker, summary].
- If the battery registers as a market resource to earn revenue, it takes on dispatch obligations in the same scarcity hours the customer needs it. The July 2026 order shows the commission will not let behind-the-meter supply shield a co-located load from emergency curtailment [source: White & Case, summary]. Inference [dk]: a registered battery may be directed to the grid, not the campus.
- Decision: no accelerated path today. Timeline for one: 2027 rulemaking at the earliest.

PJM planning type:
- No non-firm load service is in force. IRAS would start 1 June 2027 at best and was at least partly rejected on 9 October 2026 [source: summaries above].
- As filed, IRAS had no stated hour cap and addressed capacity, not transmission [source: powermag URL above]. Transmission energization dates stay with the transmission owner and the state.
- "Bring your own new capacity" needs new capacity offered into the auction as a price-taker for 10 years [source: powermag URL above]. A battery needs capacity injection rights through the generation queue: 1.5-2+ years [dk]. Four-hour storage accreditation is about 50% [dk].
- Decision: no.

Vertically integrated utility, resource planning type:
- Can do it by special contract with commission approval: 6-12 months [dk]. Precedents are MW-scale [notes].
- Prefers to own the battery in rate base and earn a return, or to have the customer fund it under a bring-your-own-capacity tariff. Sees the founder as taking the utility's margin.
- Decision: conditional yes on a pilot of 10-25 MW, utility dispatches the battery, utility controls the breaker, 10 h per event and 225 h a year as the opening position [notes].

## 4. Veteran battery fleet operator / independent power producer

Who: ran 1 GW+ of storage in ERCOT and PJM. Would be the owner-operator the infrastructure fund hires if the founder cannot do it.

| Topic | Operator's figure | Label |
|---|---|---|
| ERCOT merchant revenue 2026 | about $24/kW-year average, so $1.2M a year for 50 MW unrestricted | [source: Modo, summary] |
| Share capturable while held full for curtailment duty | 20-40%, so $0.25-0.5M a year; company's 70% is $0.2-0.35M | [dk] |
| PJM without injection rights | $0-1M a year (regulation only, small saturated market) | [dk] |
| PJM with injection rights, 2029+ | 50 MW x 50% x $325/MW-day x 365 = $3.0M, but the obligation falls in the same hours as curtailment | derived from [notes] + [dk] |
| Grid revenue as share of the $13.2M fee | 2-4% | derived |
| Calendar fade held at full charge | 1.5-2.5% a year, 80-85% left at year 10 | [dk] |
| Fleet availability | 95-98% | [dk] |
| Fixed operating cost per block | $4-5M a year: service contract $1.5-2M, insurance $0.4-0.8M, property tax $0.5-1M, remote operations $0.5M, standby losses and cooling $0.2-0.3M, augmentation reserve $1M | [dk] |
| First-event risk | 5-15% chance an early islanding transfer fails until controls are tuned | [dk], judgment |

Can one battery do both jobs? Not in any way that matters. Curtailment calls and high prices are the same hours. A battery that discharged for revenue at 5 pm is empty for the 6 pm curtailment. Only products that hold charge near full (regulation around a high setpoint) are compatible, and those markets are thin.

Economics on corrected inputs (derived):
- Net cost $90M less an effective credit of about 25% (30% on about 92% eligible basis, sold at about $0.92 on the dollar [dk]) = about $68M.
- EBITDA $13.2M + $0.3M - $4.5M = about $9M.
- Ten-year unlevered pre-tax return about 6%. The brief's inputs give about 19%.
- Fee needed for a 10% unlevered return: about $26,000-30,000 per MW-month.

Fire: containerized LFP incident rates have fallen, but two large California fires in 2024-2025 reset underwriting [dk]. The battery sits beside $1.5-2.5B of servers per 50 MW [dk]. The customer's property insurer decides siting, not the founder.

Asset when firm service arrives: relocation costs $40-60/kWh and restarts interconnection [dk]. Sale within five years triggers credit recapture [dk]. Merchant value in ERCOT at $24/kW-year does not carry the debt.

Decision: would operate under contract for $0.5-0.8M a year per block. Would not co-invest at $22,000 per MW-month with a 200-hour, four-hour guarantee and a $13.2M damages cap.

Changes the decision: guarantee limited to studied event lengths, customer gensets contractually behind the battery for hour five onward, fee of $28,000+.

## 5. Insurer / performance guarantor

Who: underwriter for energy technology performance cover and surety. Bound by treaty limits, aggregate exposure and loss history.

- Property and operational cover: available at 0.4-0.8% of insured value a year, with UL 9540A test data, spacing and a thermal-runaway sublimit [dk].
- Surety bond for the damages: underwritten on the principal's balance sheet. A startup with $5-10M posts 100% collateral: $13.2M cash or letter of credit per block [dk].
- Performance insurance: the market insures a manufacturer's warranty on degradation and availability. It does not insure a third party's promise that the utility's events stay inside four hours, that the operator kept the battery full, or that an island transfer works [dk].
- Correlation: every block in one grid is called in the same event. A shared firmware fault fails all of them at once. Aggregate exposure is number of blocks times $13.2M. An event limit would be imposed.

Decision: declines the first block. Would quote after 12 months of operating data and at least two successful live events.

Terms then: limit $13.2M, premium 3-6% of limit a year ($0.4-0.8M), 10-20% retention, exclusions for state-of-charge shortfall from market dispatch, cyber, recharge denial by the utility, and events beyond contract length.

Lender view (same desk): 70% non-recourse debt needs an investment-grade offtaker or parent guarantee, a completion guarantee and a supplier wrap. First project gets 50-60% with sponsor support [dk]. The fund becomes the owner and the founder a developer on a $1-3M fee per block [dk].

## 6. Senior power-systems engineer considering the technical co-founder role

Who: 15 years in protection, controls and inverter plant commissioning. Has a secure job with equity at an integrator or utility.

Decision: no at v1.

What breaks first, in order:
1. Utility approval. There is no tariff to sell against. Each deal is a bespoke negotiation plus restudy of 6-12 months. The company controls neither the timeline nor the breaker.
2. Energy, not power. A local transmission constraint or a winter emergency runs past four hours, and recharge is restricted. The guarantee is met on paper while the customer's compute still stops.
3. Islanding 50 MW of GPU load on inverters. Sub-second load swings of tens of MW [notes mention absorbing AI load swings], fault current limited to about 1.1-1.2 times rating [dk], transformer inrush, protection coordination, transfer inside the UPS ride-through window. Solvable, but it is 6-9 months of engineering and testing on the first site.
4. Money. The battery deposit consumes all of the company's capital before a single study is paid for.
5. Copying. Integrators already sell direct to hyperscalers [notes]. Battery racks inside the 800 VDC architecture arrive in 2028-2029 at about $200,000 per MW [notes].

Team needed before first operation: 20-25 people, $6-8M a year [dk]. Protection lead, interconnection and regulatory lead per grid, controls and energy-management software team of 4-6, commissioning lead, project finance lead, two project managers, safety lead, 24/7 operations desk (outsourced).

Would join if: one utility has signed a letter stating MW and months gained and the event hours from its study; an investment-grade customer has signed and funded deposits; the product includes gensets or load shedding for hour five onward; the company is funded at $40M+.

## 7. Delivery promise, part by part

| Promise in brief | Achievable? | What fails | Realistic figure |
|---|---|---|---|
| 9-12 months to operation | No | Utility restudy (6-12 months) stacked before final design; battery slot Q4 2027 at best; 38 kV switchgear 78-104 weeks | 16-24 months; first project 20-26; best case 12-14 with pre-bought slots and spare breaker positions |
| Four-hour coverage, 200 h a year | Partly | Winter emergencies and local transmission constraints run 8-70 h; recharge limited; hours are set by the utility's study | Covers summer peak events only. Needs gensets or load shed behind it |
| 200 MWh block | No | Fade, availability, losses | 250 MWh at start, or 215 MWh plus augmentation |
| $309/kWh, $62M | No | Compliant US supply premium, data-center labor, islanding scope, owner's costs, oversizing | $325-390/kWh nameplate; $81-98M; central $90M |
| 30% tax credit, $43M net | Partly | Only with certified non-FEOC supply at 60% for 2027 starts, prevailing wage rules, eligible-basis exclusions, sale discount | About 25% of total cost; net about $68M |
| Grid revenue on top | No | Same hours as curtailment; ERCOT average $24/kW-year | $0.2-0.5M a year per block to the company |
| Company signs the curtailment obligation | No | Utility contracts with the customer of record and controls the breaker | Indemnity to the customer only |
| 70% non-recourse debt | Not on block one | No operating record, uninsurable guarantee | 50-60% with sponsor support |
| $5-10M covers origination, deposits, studies | No | Battery deposit alone is $5-10M | $25-40M to reach first operation |

## 8. Material inputs and approvals checklist

Inputs: battery slot and deposit; non-FEOC certification; medium-voltage switchgear; pad-mount transformers; grounding transformer; microgrid controller and validated inverter models; fire test data; water supply for fire response; land and setbacks on campus.

Approvals: utility restudy and facility agreement amendment; ERCOT or PJM model acceptance; resource registration if exporting; local fire authority; customer's property insurer; tax credit diligence; lender's independent engineer; state commission approval where a special contract is used.

Failure modes: restudy sets hours above the guarantee; charging window too short; island transfer trips; common firmware fault across blocks; warranty void from standby at full charge; firm service arrives early and the customer pays the 50% termination or disputes it; tax credit recapture on resale; FEOC certification fails audit.

## 9. Probabilities (panel's honest estimate)

- First paid commercial delivery of a 50 MW block within 18 months (by May 2028): 7%.
- $1 billion of annual recognized revenue within 7 years: 1%. It needs about 76 blocks, 3.8 GW and about $6.8B of capital at corrected cost.
