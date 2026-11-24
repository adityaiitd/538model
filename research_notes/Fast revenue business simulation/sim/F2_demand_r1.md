# F2 v1 demand panel, round 1: bridge fuel for onsite power, delivered by truck

Date of simulation: 24 November 2026. Everything below is a simulated hypothesis from archetype personas. It is not customer validation. No real person was interviewed and no real order exists.

Evidence labels:
- [notes] = the research notes `fuel_equipment_leasing.md` Part A or `power_grid.md` sections 2-3. "Derived" means my arithmetic on figures in the notes.
- [source: URL] = a page opened or searched during this panel.
- [domain knowledge, unverified] = my own knowledge of how these organisations work, or a panel estimate. Not checked.

Web budget used: 4 searches, 2 fetches. They confirmed the Hexagon order and Superior's capital plan and found nothing new on trailer prices, lead times or rival haulers.

## Result in one paragraph

Nobody signs the contract as offered. Three personas make counter-offers that a founder could turn into revenue: the neocloud's head of infrastructure (a 12-month conditional contract with the advance held in escrow), the power provider (an overflow purchase order with no commitment) and the oilfield operator (spot work). The willingness to pay for trucked gas is real: the fuel premium is about 6-7% of a neocloud's revenue. The founder's problem is not price. It is that a first-time supplier has no equipment on the day the buyer needs a date, and the time to get equipment is about as long as the bridge it is meant to fill.

## Shared arithmetic used by all personas

| Item | Brief | Panel figure | Basis |
|---|---|---|---|
| Burn, 35 MW engines at full load | 7,500 MMBtu/day | 7,440 MMBtu/day | 8.853 MMBtu/MWh [notes] |
| Realistic load factor during a bridge | 100% implied | 65-80% | Site is ramping; engines run N+1 [domain knowledge, unverified] |
| Loads per day, 35 MW | 17 | 19-20 at full load | About 88% of a trailer is usable before pressure is too low [domain knowledge, unverified; the notes found no published figure] |
| Charge above commodity | $11-12 | $8.50-10.00 | Certarus's direct delivery margin is $8.51; the other $3.80 of its $12.31 is rentals, standby and take-or-pay fees across a mostly oilfield book [notes]. The 135 MW contract works out at $11.5-14.3 all-in including commodity [notes, derived], so the adder there is about $8.5-11.5 |
| Revenue per 35 MW block | $40M/yr | $24-32M/yr | 7,440 x 365 x 65-80% x ($3 commodity + $9.50-10.50) [derived] |
| Trailers per block | 45-60 | 65-85 | Certarus ratio is 1.48 trailers per MW = 52 [notes, derived]; add 48 hours of parked storage for winter that site operations will demand (35 trailers, partly overlapping the rotation) [domain knowledge, unverified] |
| Capital per block | $35-45M | $45-55M | Trailers $32-42M at the brief's unverified $0.5M, hub compression $8-12M, site pressure-reduction $2-3M |
| EBITDA margin | 28% | 10-20% | Certarus earns 28% with 25 hubs and 919 trailers, and its cost rose to $8.13/MMBtu on third-party drivers [notes]. Stabilis guides to "high teens" [notes]. Single-hub new entrant cost about $6.50-8.00/MMBtu [domain knowledge, unverified] |
| EBITDA per block | about $11M | $4-6M (new entrant); $8.5-11M at Certarus's $4.18/MMBtu | [notes, derived] |
| Payback on a block | not stated | 4-5 years at Certarus economics; 8+ years at new-entrant economics | Against contracts of 12-30 months |

Neocloud value of time, used by personas 2 and 5: 50 MW of engines carries about 38-40 MW of computing load. At roughly $10-12M of revenue per MW-year that is $33-39M of revenue a month [domain knowledge, unverified]. The fuel premium at 75% load is about $10 x 7,965 MMBtu x 30 days = $2.4M a month [derived]. So the premium is 6-7% of revenue. Price is not the obstacle.

## How many sites are waiting on gas, and for how long

- No published count exists [notes]. Sized evidence: RBC counts about 7 GW of onsite gas generation under construction and over 57 GW with equipment orders; Cleanview counts about 2 GW online at four projects [notes].
- Disclosed trucked-gas demand: about 250 MW across three Certarus contracts, plus one Stabilis contract of about $100M a year, plus Oracle sites in Utah and Texas. Certarus has seven data center contracts; five of them total only about $50M, so most are short commissioning jobs [notes].
- Panel estimate: 10-20 US sites over 20 MW will be taking trucked gas at any time during 2027, 400-900 MW in total, with a median bridge of 6-12 months and a tail of 18-30 months where land rights are contested. At about $0.9M of fuel revenue per MW-year [notes, derived] that is a $350-800M a year market, of which about $270M a year is already contracted to Certarus and Stabilis for 2027 [domain knowledge, unverified; built from the notes].
- What they pay today and to whom: Certarus blended $14.78 delivered [notes]; the 135 MW contract $11.5-14.3 all-in [notes, derived]; Stabilis sells LNG to a temporary-power provider, not to the data center [notes]; VoltaGrid hauled its own gas for Oracle in Texas [notes].
- What happens as laterals complete: each contract ends. A lateral costs roughly $60-120M once; trucking a 135 MW site costs about $103M a year more than pipeline gas [notes, derived]. Every buyer below asked for the right to stop paying when the pipe is live. Superior's own management says its contracts "don't fully eliminate redeployment risk" [notes].

---

## Persona 1. Chief commercial officer, behind-the-meter power provider (engines arriving before the gas lateral)

**Who.** Sells power under 5-15 year take-or-pay contracts with availability guarantees. Typically grew out of oilfield services and already runs gas logistics, or has a hauler on a master agreement [notes: VoltaGrid hauled its own gas; Stabilis's buyer was a temporary-power provider]. Some peers started as compressed-gas fuelling businesses for frac fleets [domain knowledge, unverified].

**Incentives and constraints.** Paid on megawatts energised on the contract date. Its customer contract carries liquidated damages for missed availability, so fuel failure is its own loss. It has a BB-type balance sheet and equipment lenders [notes], so it can buy trailers itself.

**Alternatives.** Certarus under a master agreement; its own trailers and a contracted hazmat carrier; Stabilis LNG; a regional hauler it has used at well sites.

**Decision.** Refuses the take-or-pay contract and the advance. Issues a non-exclusive overflow purchase order: commodity plus $8.50-9.00 per MMBtu, six months, 20-30% of site burn, 30 days' notice, no advance, no minimum beyond the month.

**Reasons.**
- It will not hand the primary fuel path, on which its own damages depend, to a supplier with no deliveries.
- It will not fund a supplier's fleet when it can finance its own trailers at a lower cost of capital.
- A second source is worth something to it, because Certarus's fleet is committed to the 135 MW contract through mid-2027 [notes], so it will pay for spare capacity but only at a discount.

**What would change it.** Ninety days of clean deliveries at one of its sites, a price at least 10% under the incumbent, and trailers the founder already holds. Then: primary supply on one site of 25-50 MW, 12 months, take-or-pay at 60% of nominal, still no advance.

## Persona 2. Head of infrastructure, neocloud (50 MW site, engines on order, gas interconnect quoted at 12 months)

**Who.** Owns the energisation date. GPUs are financed at 10-15% [notes] and depreciate whether or not they run.

**Incentives and constraints.** Every month of delay costs about $33-39M of revenue against $2.4M of fuel premium. Has no vendor list of its own for fuel and a small team. Needs the CFO and procurement to countersign.

**Alternatives.** Certarus (first call); Stabilis LNG; ask the engine or power provider to bundle fuel; wait for the pipe; rent dual-fuel or diesel units for commissioning only.

**Decision.** Refuses the contract as offered. Signs a counter-offer if the founder can meet the conditions: commodity plus $10.00-10.50 per MMBtu, 12 months, take-or-pay at 70% of nominal volume (about 5,200 MMBtu a day for a 35 MW first phase), the advance paid into escrow and released against delivery of titled equipment, and a right to terminate at no cost if first gas is more than 30 days after first engine fire.

**Reasons.**
- This persona is buying a date. The founder today has no trailers, no hub and no drivers, so cannot sell a date.
- Engines arrive in roughly 6-9 months. New trailers and a compression hub take an estimated 9-12 months for a new buyer [domain knowledge, unverified; Hexagon's lead time for a new customer is not published, per notes]. If the founder orders at signing, first gas lands at about the same time as the pipeline.
- Will pay $1-2 more than Certarus for a firm earlier date. Will not pay anything for a later one.

**What would change it.** Evidence of title to at least 40 trailers and a commissioned hub 60 days before first fire, plus written confirmation that Certarus cannot meet the date. With both, signs within two weeks.

## Persona 3. Head of power, colocation developer (tenant start date fixed)

**Who.** Builds to a signed lease with a hyperscale or frontier-lab tenant. The lease carries rent abatement for late delivery and a tenant termination right after a long-stop date [domain knowledge, unverified].

**Incentives and constraints.** Power is usually passed through to the tenant at cost [domain knowledge, unverified]. At about $131/MWh [notes] against a budget near $50-70, the tenant must consent or the developer absorbs about $2-3M a month per 35 MW. The tenant has approval rights over critical suppliers. The developer's lenders review material contracts.

**Alternatives.** Certarus; Stabilis; the pipeline company's own temporary supply offer (Kinder Morgan markets portable LNG for start-up [notes]); negotiate a later start date with the tenant.

**Decision.** Refuses. Would place a second-source order for no more than 25% of volume after 90 days of incident-free deliveries elsewhere.

**Reasons.**
- The tenant and the lender both have to approve the supplier. Neither approves a company with no operating history as sole fuel source.
- The developer cannot commit to a 12-30 month take-or-pay that outlasts the lateral, because the tenant will stop reimbursing the premium the day pipeline gas flows.

**What would change it.** The tenant names the founder as acceptable in writing, or the founder is a subcontractor under a hauler already approved.

## Persona 4. Energy procurement lead, top-five hyperscaler (remote campus)

**Who.** Buys power for gigawatt campuses. Already has Certarus-type suppliers on contract: Certarus's named customers are hyperscale operators [notes].

**Incentives and constraints.** Career risk sits entirely on the downside: a fuel incident at a flagship site is a board-level event (Oracle's shares fell 5.5% on the trucked-gas story alone [notes]). Supplier onboarding needs three years of safety statistics, audited financials and a credit review [domain knowledge, unverified]. Sites are 100-2,450 MW; trucking tops out near 100-150 MW per site [notes].

**Alternatives.** Certarus, Stabilis, the integrated power provider, the pipeline company. The hyperscaler can also pay to accelerate the lateral, which at $60-120M is cheaper than a year of trucking [notes, derived].

**Decision.** Refuses. No purchase order, no advance, no pilot at an owned campus.

**Reasons.**
- A first-time hazardous-materials supplier fails vendor qualification before price is discussed.
- It will never prepay a start-up; it expects suppliers to finance themselves and post security.
- It regards trucked gas as an embarrassment to be ended, not a category to develop.

**What would change it.** The founder appears as a named subcontractor under an approved prime, or owns an operator with a multi-year record. Even then the hyperscaler contracts with the prime.

## Persona 5. Chief financial officer, the same neocloud

**Who.** Manages covenants on GPU debt with minimum coverage of 1.15-1.3x and a three-month payment reserve [notes].

**Incentives and constraints.** Accepts the fuel price: at $131/MWh [notes] fuel is 6-7% of revenue during the bridge. Objects to two things: unsecured cash out, and fixed payments after the pipe arrives.

**The numbers the CFO ran.**
- Advance at 12% of an 18-month, 50 MW contract of about $57M: $6.8M, unsecured, to a company with no assets.
- Take-or-pay tail if the pipeline arrives six months early: 6 x $2.4M = about $14M paid for gas not taken.
- Lender view: a fixed obligation to an unrated counterparty is added to debt service in the coverage test.

**Decision.** Refuses the advance as offered and refuses a take-or-pay longer than the lateral's contractual in-service date. Approves the head of infrastructure's counter-offer with these changes: deposit of no more than 5% of contract value, held in escrow or backed by a letter of credit or a first lien on the trailers; take-or-pay falls away when the pipeline is in service, against an exit fee of three months of the fixed adder (about $7M at most, stepping down monthly).

**Reasons.**
- The Stabilis precedent does not transfer. Stabilis is listed, has made more than 55,000 deliveries and owns liquefaction plants [notes]. Its customer was advancing cash to a going concern.
- If the supplier fails, the neocloud loses the deposit and the date.

**What would change it.** A lien on equipment already delivered, or a credible parent or bank guarantee. With either, pays 10-12%.

## Persona 6. Procurement and safety lead (qualifying a first-time hazardous-materials supplier)

**Who.** Runs supplier qualification for the neocloud or the developer. Signs off before any truck enters the site.

**Requirements that apply here.**
- Carrier with a satisfactory federal safety rating and a hazardous materials safety permit, which applies to bulk methane loads [domain knowledge, unverified]. A new carrier has no rating history.
- Federal minimum of $5M financial responsibility for bulk compressed gas [domain knowledge, unverified]; this buyer asks for $25M of excess liability, pollution cover, and additional-insured status. A hyperscaler asks for $50M.
- Three years of loss runs and incident rates. A new company has none.
- Cylinder approvals or special permits for composite trailers, a security plan, and state licensing in states such as Texas [notes].
- Emergency response plan agreed with the local fire authority; on-site storage under the applicable fire codes [notes].
- Step-in rights: the buyer can take over the trailers and hire another carrier if deliveries stop.

**Decision.** Refuses to qualify the founder as sole supplier. Will qualify as a secondary supplier after a site audit, if the driving is done by an established permitted carrier and the founder's own people are limited to hub and decant operations.

**Reasons.** The site has no other fuel path. One supplier with no history is a single point of failure that no safety lead will sign for. Insurance for a start-up hauling bulk gas will be expensive or unavailable at the limits asked.

**What would change it.** The founder buys or partners with an operator that has three or more years of clean record, and that operator is the contracting party.

## Persona 7. Plant operations manager at the site

**Who.** Runs the engine plant. Not a buyer, but can veto.

**What the offer means on the ground at 35 MW.**
- 19-20 loads a day, so about 38-40 truck movements, one every 36 minutes around the clock.
- Each trailer lasts about 1.3 hours at full burn (about 400 usable MMBtu against 310 MMBtu an hour) [derived; usable share unverified].
- Needs at least six decant bays (two feeding, two staged, two swapping), two independent pressure-reduction trains with heaters because expanding gas chills, and a hard-surfaced loop road.
- Winter: wants 48 hours of fuel parked on site, about 35 trailers, because one closed highway otherwise stops the plant. The brief's 45-60 trailers do not cover rotation plus that reserve.
- Fuel quality: lean-burn engines need a stable heating value and a methane number above roughly 70-80 [domain knowledge, unverified]. Pipeline-tap gas is acceptable; field gas or mixed sources are not without testing. Compressor oil carry-over and liquids must be filtered at the decant skid.
- Low-pressure trips when a trailer runs down are the most common cause of engine trips at trucked sites [domain knowledge, unverified].

**Decision.** Accepts trucked gas technically, with conditions: 48 hours of on-site storage, a spare pressure-reduction train, the supplier's technician on site every shift, live telemetry on trailer pressure, and gas analysis per hub.

**Effect on the founder.** These conditions raise the fleet to 65-85 trailers and add $2-3M of site equipment per block.

**What would change it.** Nothing needs to change; these are standing terms. A battery that rides through a trailer swap would let the manager relax the staging requirement.

## Persona 8. Oil and gas operator, and an industrial plant, that already buy trucked gas

**Who.** A Permian or Appalachian operator displacing diesel on drilling rigs and frac fleets, and an off-pipeline industrial plant in the Northeast.

**What they pay and to whom.**
- Operator: about $9-11 per MMBtu delivered, commodity included, from Certarus or a regional hauler, by the pad or by the month [domain knowledge, unverified]. Wellsite pricing fell through 2025 and into 2026 [notes]. The benchmark is diesel at roughly $25-29 per MMBtu [domain knowledge, unverified], so the saving is large and the buyer captures most of it.
- Industrial plant: commodity plus $6-9 on a one-to-three year contract from a regional incumbent [domain knowledge, unverified]. Utilities also buy winter standby, which fell in early 2026 [notes].

**Decision.**
- Operator: issues spot purchase orders at $9-11 delivered all-in, 30-90 days, no take-or-pay, no advance, after a master service agreement and safety prequalification. Will switch supplier for a 10-15% discount.
- Industrial plant: refuses to switch from its incumbent mid-contract; would bid the founder at renewal.

**Reasons.**
- There is business for an idle fleet, and it is fragmented [notes]. It is where Certarus still earns most of its volume [notes].
- It pays about 60-70% of data center revenue per MMBtu and carries no commitment. Certarus's fleet average is about 108 MMBtu per trailer per day, a quarter of a load [notes, derived].
- When data center bridges end, Certarus's roughly 1,000 trailers return to this market too, and prices fall again.

**What would change it.** A hub within 100 miles of the operator's acreage. Without one, the founder's fleet cannot serve the work at any price.

---

## Answers to the founder's listed weak points

| Question | Panel answer |
|---|---|
| Can a new buyer get equipment in under 12 months? | Unverified. Hexagon's record order from Certarus delivers mostly over the 12 months from Q3 2026 with an option to 2028 [notes; source: https://hexagonagility.com/news/record-data-center-demand-mobile-pipeline]. No lead time for a new customer is published. Buyers assumed 9-12 months and judged the offer on that basis. |
| Will a customer give a first-time operator the contract? | No as sole supplier (personas 3, 4, 6). Yes as a conditional supplier where the incumbent cannot meet the date (persona 2), or as overflow (persona 1). |
| What stops Certarus and Stabilis taking every contract? | Only capacity. Superior's capital spending stays elevated through mid-2027 [source: https://quartr.com/events/superior-plus-corp-spb-q3-2026_ofx60syO], which means its new trailers are spoken for until then. That is the founder's window and it closes as the Hexagon order delivers. |
| What is the fleet worth when pipelines catch up? | Oilfield and industrial work at about 60-70% of the revenue per MMBtu, short commitments, and only near a hub (persona 8). |
| Permanent backup fuel | No named contract exists [notes]. Backup is an LNG storage product, about 180,000 gallons for 48 hours at 35 MW [domain knowledge, unverified], not a use for compressed-gas trailers. No persona offered to pay for it. |

## Five most damaging objections

1. **The equipment lead time is as long as the bridge.** A 12-month lateral quote minus 9-12 months to get trailers and a hub leaves 0-9 months of paid deliveries, unless the founder buys $45-55M of equipment before any contract. [domain knowledge, unverified; notes]
2. **Payback is longer than the contract.** A block earns $4-6M of EBITDA a year as a new entrant, $8.5-11M at Certarus's economics, on $45-55M. Contracts run 12-30 months and every buyer wants out when the pipe is live. [notes, derived]
3. **No buyer advances cash to an operator with no history.** Without the 12% advance and with lenders at 40-50% rather than 60%, equity per block is $20-30M, above the founder's starting capital. [notes; domain knowledge, unverified]
4. **The buyers supply themselves or already have a supplier.** Power providers haul their own gas; hyperscalers use Certarus. The contestable segment is neoclouds and smaller developers, the weakest credits. [notes]
5. **The follow-on products do not exist yet.** No named site holds permanent backup fuel, and the fallback market pays less with no commitment. [notes]

## Numbers in the brief that the panel disputes

| Brief | Corrected | Basis |
|---|---|---|
| $11-12 above commodity | $8.50-10.00 | Certarus direct margin $8.51; 135 MW contract arithmetic [notes] |
| $40M a year per 35 MW block | $24-32M | 65-80% load factor and the lower adder [derived] |
| 17 loads a day | 19-20 | Usable share of a trailer [domain knowledge, unverified] |
| 45-60 trailers | 65-85 | Rotation plus 48 hours of parked storage [domain knowledge, unverified] |
| $35-45M per block | $45-55M | Above |
| 12% customer advance | 0-5%, escrowed or secured | Personas 1-5 |
| 60% equipment debt | 40-50% at 11-14% | Short contract, weak-credit offtaker [notes on lender terms; domain knowledge, unverified] |
| $10-15M equity per block | $20-30M | Above |
| 28% EBITDA margin | 10-20% | Single hub, third-party drivers [notes; domain knowledge, unverified] |
| Take-or-pay 12-30 months | 12 months effective, ending at pipeline in-service with a three-month exit fee | Personas 2, 3, 5 |
| "Trailers move to the next site" | 3-6 idle months per move | A new hub, tap and permits are needed within 100 miles of the next site [domain knowledge, unverified] |

## Conditions under which each "no" becomes a "yes" (their terms)

- Persona 1: 90 days of clean overflow deliveries, a price 10% under the incumbent, equipment already held. Then primary supply on one 25-50 MW site for 12 months at 60% take-or-pay, no advance.
- Personas 2 and 5: title to at least 40 trailers and a commissioned hub 60 days before first engine fire; proof the incumbent cannot meet the date; deposit secured by lien, letter of credit or guarantee. Then signs at commodity plus $10.00-10.50 and pays up to 10-12% in advance.
- Persona 3: written tenant approval of the supplier, or the founder as subcontractor to an approved hauler.
- Personas 4 and 6: the contracting party is an operator with three or more years of loss runs, a satisfactory federal safety rating and $25-50M of excess cover. In practice the founder would have to buy one.
- Persona 7: already a conditional yes.
- Persona 8: master service agreement, safety prequalification, a hub within 100 miles, 10-15% discount.

## The four numbers

| Measure | Panel estimate |
|---|---|
| Probability of a first paid delivery to a power site within 9 months | 20% (about 40% if oilfield or subcontract hauling with leased trailers counts) |
| Probability of $40M of gross recognised revenue in a trailing twelve months by month 18 | 4% |
| Probability of $100M by month 36 | 6% |
| Year five if it works | Revenue $120-150M across four to five blocks; gross margin after commodity and delivery cost 25-30%; EBITDA about 20% ($25-30M); enterprise value at 6-8x (Superior paid 8.5x for Certarus [notes]) $150-240M; equity after debt $70-170M |

Revenue type: contracted but short. Each contract lasts 12-30 months and ends when a pipeline arrives. It is not recurring. Revenue must be re-won site by site, and about 20% of it is commodity passed through at no margin.

## Sources opened during this panel

- [Hexagon Agility release on the record order](https://hexagonagility.com/news/record-data-center-demand-mobile-pipeline): $100M order, option of $25M to 2028, over 2,250 modules in operation; no unit count, price or lead time.
- [Pipeline & Gas Journal, July 2026](https://pgjonline.com/news/2026/july/hexagon-agility-lands-100-million-certarus-order-for-mobile-pipeline-modules): same order.
- [Quartr summary of Superior Plus Q3 2026](https://quartr.com/events/superior-plus-corp-spb-q3-2026_ofx60syO): capital spending of about $230M in 2026, elevated through mid-2027, higher cash flow expected by Q4 2027; Certarus EBITDA growth about 5%. Machine-written summary; verify against the filing.
- Searches for data center contracts at NG Advantage, Xpress Natural Gas, Kinetrex and CNG Delivery, and for in-house gas hauling at VoltaGrid, Solaris and Liberty, returned nothing usable. Absence of results is not proof of absence.
