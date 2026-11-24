# C1 v1, capital and competition panel, round 1

Date of simulation: 24 November 2026. Everything below is a simulated hypothesis from archetype personas. It is not customer, lender or investor validation. No real person was interviewed and no quote is real.

Evidence labels: [notes] = founder research notes; [source: URL] = web search this session (snippet level, two page fetches returned 403); [dk] = domain knowledge, unverified; [calc] = my arithmetic on labelled inputs.

Search budget used: 8 of 8.

---

## 0. Panel's own numbers (used by all personas)

### 0.1 Facts checked this session
- A direct precedent exists and it is incumbent-owned. Calibrant (a Macquarie platform) is delivering a 31 MW / 62 MWh battery at Aligned's Hillsboro, Oregon campus so the campus can take utility power years earlier. Portland General Electric can call the battery through its Dispatchable Standby Generation programme. Calibrant builds and operates. Aligned funds it. Planned in service H2 2026; I could not confirm it is operating. [source: https://www.energy-storage.news/turning-data-centres-from-a-potential-liability-to-a-grid-asset-calibrant-on-its-first-of-a-kind-bess-with-aligned/] [source: https://www.macquarie.com/insights/accelerating-data-centre-interconnection-in-power-constrained-high-risk-grid-markets.html]
- ERCOT merchant battery revenue has collapsed. Average battery about $24/kW-year annualised through mid-August 2026; trailing-year base case about $28,800/MW-year; 2025 about $29/kW, 2024 $56/kW, 2023 $193/kW. The figures are not fully consistent across Modo pages. [source: https://modoenergy.com/research/ercot-bess-buildout-q3-2026] [source: https://modoenergy.com/research/ercot-battery-storage-2026-things-to-watch]
- Texas SB 6: large loads of 75 MW+ must accept curtailment in firm load shed, and ERCOT may direct loads with backup generation covering at least half of demand to run it. The PUC published proposed rules around March 2026. I found no confirmation of final adoption and no rule text saying a third-party battery buys earlier energization. [source: https://www.foley.com/insights/publications/2026/03/public-utility-commission-of-texas-issues-proposed-rules-for-large-load-interconn/] [source: https://www.utilitydive.com/news/texas-law-gives-grid-operator-power-to-disconnect-data-centers-during-crisis/751587]
- PJM "connect and manage" was filed on 13 August 2026 as Interim Resource Adequacy Service (docket ER26-3515), with a Bring Your Own New Capacity route. Curtailment hours and duration were not retrievable. FERC outcome not confirmed. [source: https://powermag.com/pjm-widens-response-to-data-center-load-as-capacity-shortfalls-deepen]
- Emerald AI raised $150M at a $1.05B valuation in August 2026, $215M in total, with Nvidia in every round. Its software dispatches batteries and other onsite resources in grid events. Silicon Valley Power runs a programme giving expanded grid access for verified dispatchable flexibility. No contracted MW figure found. [source: https://siliconangle.com/2026/08/25/data-center-power-startup-emerald-ai-raises-150m-at-1-05b-valuation/]
- Battery debt at scale is sized on long tolls with investment-grade utilities, for example GridStor's $220M financing for 400 MWh in Arizona on a 20-year APS toll. No public DSCR, spread or merchant haircut was found. [source: https://www.energy-storage.news/gridstor-closes-us220-million-financing-for-400mwh-arizona-bess/]

### 0.2 Cost and operating assumptions
| Item | Brief | Panel mid | Panel high | Basis |
|---|---|---|---|---|
| Gross installed cost, 50 MW / 200 MWh | $61.8M ($309/kWh) | $68M ($340/kWh) | $78M ($390/kWh) | $309 is a median for front-of-meter projects [notes]. Add grid-forming inverters, tie-in to campus medium-voltage gear, usable-energy overbuild for year-10 capacity, financing fees, interest during construction, reserve account [dk] |
| ITC realised | $18.5M (30% of all cost, at par) | $17.8M | $19.6M | 90-92% of cost eligible, sold by transfer at 93-95 cents [dk]. Requires FEOC-compliant supply, which costs about $100/kWh more at the system level [notes] |
| Net cost | $43.3M | $50.2M | $58.4M | [calc] |
| Operating cost per year | not stated | $3.2M | $3.4M | Service agreement and augmentation, insurance, property tax, remote operations, auxiliary power, letter-of-credit fees. About $65/kW-year [dk] |
| Grid revenue kept by owner | "plus" | $0.3M | $0.3M | $24-29/kW-year average ERCOT battery [source: Modo above]. A behind-the-meter battery that must stay full for curtailments and may not export earns a fraction, about $8-10/kW-year gross, 70% kept [dk, calc] |

### 0.3 Returns, 10-year contract, investment-grade offtaker, pre-tax [calc]
Debt sculpted to 1.30x coverage on contracted fees less operating cost, 6.25% all-in, 9-year amortisation, capped at 75% of net cost. Residual 5% of gross cost.

| Cost case | Price per MW-month | Unlevered IRR | Levered equity IRR | Debt as % of gross cost |
|---|---|---|---|---|
| Brief ($61.8M) | $22,000 | 20.2% | 44-50% | 49-52% |
| Mid ($68M) | $22,000 | 15.1% | 33.8% | 55% |
| High ($78M) | $22,000 | 10.9% | 20.4% | 56% |
| High, non-investment-grade offtaker (8.75%, 1.40x, 7 years) | $22,000 | 10.9% | 12.6% | 44% |
| High, no ITC (FEOC failure) | $22,000 | 4.6% | 2.7% | 60% |
| Brief | $17,000 | 11.2% | 21.2% | 52% |
| Mid | $17,000 | 6.9% | 7.9% | 50% |
| High | $17,000 | 3.3% | 0.3% | 42% |

### 0.4 Clearing price after competition [calc]
- Established developer plus infrastructure fund, $68M cost, 10-15% levered return: $16,900-17,800 per MW-month.
- Hyperscaler self-build, $66M cost, own tax appetite, 5.5-7% cost of capital: $13,800-16,100 per MW-month equivalent.
- Panel view: a 10-year investment-grade contract clears at $16,000-18,000, not $22,000. Non-investment-grade developers and neoclouds would pay $20,000-26,000 but on 3-5 year terms and with weak credit.
- A five-year contract at the high cost case needs $26,000-30,000 for a 14-25% levered return, with a 25% residual assumed.
- The return at the brief's price and cost (20% unlevered, four-year payback) is itself the warning. Batteries are purchasable by anyone. A return that high on a commodity asset is competed away within two or three bid cycles.

---

## Persona 1. Project finance banker / asset-based lender

**Who.** Director, energy project finance, at a bank that lends against battery tolls and data-center offtakes. Also speaks for a private-credit asset-based desk.

**Incentives and constraints.** Credit committee approves on contracted cash flow and counterparty rating, not on asset value. Minimum hold about $50M; deal costs (independent engineer, counsel, insurance and market advisers) $1.5-2.5M per closing [dk]. Career risk sits in first-of-a-kind regulatory structures.

**Asked for.** $43M (70% of $62M) non-recourse.

**Decision: refuses as asked. Counter-offer below.**

Why 70% of gross fails: 70% of $61.8M is $43.3M, which equals 100% of cost after the tax credit. That is zero equity. [calc]

| Term | Investment-grade offtaker (A- or parent guarantee) | BB or unrated offtaker (neocloud, developer) |
|---|---|---|
| Advance | Lesser of 75% of net-of-ITC cost and 1.30x coverage: $32-44M, 50-56% of gross | 55-65% of net cost and 1.40-1.50x: $28-34M, 40-45% of gross |
| Tax credit bridge | 85-90% of signed transfer proceeds, repaid 1-3 months after operation; needs a signed buyer and tax insurance | Same |
| Tenor | Construction plus 9 years, fully amortising one year inside the contract. No balloon | 5-7 years, 50-75% cash sweep |
| Spread | SOFR+250-300 (first-time sponsor premium over the SOFR+225-250 seen on investment-grade compute offtakes [notes]); 2.0-2.5% upfront | SOFR+475-550 (CoreWeave non-investment-grade facilities priced SOFR+450-500 [notes]) |
| Grid revenue | Zero credit in sizing. May flow to equity after reserves | Zero. Swept |
| Reserves | Six months debt service; augmentation reserve | Same plus 6-12 months of fees as offtaker deposit or letter of credit |
| Covenants | Lock-up at 1.15-1.20x, default at 1.05-1.10x. Termination payment at least 110% of debt outstanding at all times, paid to the collateral account. No merchant dispatch that breaches the state-of-charge reserve | Same |

Conditions precedent that the founder does not yet have:
1. Executed, final utility agreement or approved tariff for the flexible connection. A pilot letter is not enough. Change-of-law risk on that programme sits with the offtaker: fees stay payable if the utility withdraws the scheme.
2. Direct agreements giving the lender step-in rights with both the customer and the utility.
3. Fixed-price, date-certain construction contract with delay damages from a creditworthy integrator. Fluence lost its year on exactly these damages [notes], so integrators now price them.
4. Manufacturer service agreement with availability of 97-98% and a capacity guarantee for the loan life. Named back-up operator, because the sponsor has no operating record.
5. Liquidated damages to the customer (cap $13.2M, one year of fees) matched back-to-back by the manufacturer or covered by a sponsor letter of credit. The startup cannot post that letter without cash collateral.

Ticket size: one block is below the bank minimum. First block goes to private credit at SOFR+600-800 and about 50% of net cost, or is all-equity until a three-block warehouse of $120M+ exists. [dk]

**Collateral when firm service arrives.** The lender never lent on the battery. In place, its merchant value in ERCOT is close to nil: $24-29/kW-year of revenue against roughly $65/kW-year of operating cost and a $216/kW-year levelised cost [source: Modo above] [notes] [calc]. All value is the take-or-pay. The 50% termination payment covers the loan in every year (for example $46.2M at end of year 3 against $31M outstanding) [calc]. That protection holds only if the customer is solvent and the termination is for convenience. A termination for provider default pays nothing.

**Loss if the customer defaults at end of year 3** [calc, liquidation values dk]:
| Net liquidation value after removal and recommissioning | Proceeds | Loss on $31.2M (investment-grade sizing) | Loss on $21.6M (non-investment-grade sizing) |
|---|---|---|---|
| $60/kWh | $12M | 62% | 44% |
| $90/kWh | $18M | 42% | 17% |
| $120/kWh | $24M | 23% | 0% |

A foreclosure sale inside five years also triggers recapture of the unvested tax credit, about $8.4M at that point. Equity loses most of its $15-24M. [dk, calc]

**Working capital finding.** The lender funds after equity. Before financial close the company carries, per block: battery reservation deposit of 10-20% of roughly $46M of equipment ($4.6-9.2M), utility study fees and security, engineering and first-of-kind legal ($2-3M). Total $8-13M at risk. The customer prepayment of $3.96M (10% of three years of fees) offsets this only if it is unrestricted, and an investment-grade customer will hold it in escrow or demand a letter of credit against it. Fees then arrive 9-18 months later, billed monthly in arrears. [dk, calc]

**What would change the decision.** Offtaker rated A- or better, or a rated parent guarantee. Executed utility agreement. Three blocks pooled. A sponsor with $50M+ of committed equity and letters of credit.

---

## Persona 2. Partner, infrastructure / private equity fund

**Who.** Partner at a $5-10B energy-transition infrastructure fund that owns a storage developer and a data-center platform.

**Incentives and constraints.** Target net return 9-11% for operating, investment-grade-contracted assets; 13-16% for a new platform carrying regulatory first-of-kind risk. Minimum cheque $75-150M; a $13-19M project equity cheque costs more in diligence than it earns. Investment committee asks first: why not through a platform we already own? [dk]

**Alternatives.** Do the same deal through an established developer. Macquarie already does this through Calibrant [source: energy-storage.news above]. Storage owners with fleets, procurement frame agreements and operating records exist in every large-fund portfolio [dk].

**Decision: refuses the single-block equity. Refuses a startup platform commitment today.**

Terms on which the fund would engage:
- Buy the first two projects at financial close if they have investment-grade or guaranteed offtake and an executed utility agreement. The fund takes 90-100% of project equity.
- Developer gets a fee of 2-3% of cost ($1.5-2.5M per block), an asset-management fee near 1.5-2% of revenue, and a 10-20% promote above a 10-12% hurdle.
- After that, a $150-250M drawdown commitment with exclusivity, a right of first offer on the pipeline, warrants in the parent, board seat, key-person and replace-the-operator rights.

**Return view** [calc]. At the brief's price and cost the model shows 44-50% levered. The fund does not believe a commodity asset holds that. It underwrites $17,000 and $68M: 6.9% unlevered, 7.9% levered. That is below hurdle, so at clearing prices the fund needs either lower cost (a frame agreement the startup does not have) or the higher-priced, weaker-credit customers, where it wants 15%+.

**Contract objection.** A ten-year take-or-pay for a need that lasts two to four years reads to the customer as $47,700 per MW-month if it exits at year 3 (three years of fees plus the 50% payment, $85.8M) [calc]. A sophisticated customer will not sign it. A fund will not underwrite a contract that only an unsophisticated customer signs.

**What would change the decision.** Two signed contracts, one executed utility agreement that names the battery owner as the curtailment counterparty, and a management team with built-and-operated storage megawatts.

---

## Persona 3. Skeptical venture investor

**Who.** General partner at an early-stage fund that has backed asset-heavy energy companies and lost money on two project developers.

**Incentives.** Needs a path to 50x on seed. Fears being the equity that pays for deposits while infrastructure capital takes the asset returns.

**Decision: refuses the $5-10M seed on the brief as written.** Would sign a term sheet for $3-4M at about $15M post-money, tranched, with the second half released on (a) a utility's written confirmation at a named substation that a battery-backed curtailment commitment advances energization by a stated number of months for a stated MW, and (b) a customer letter of intent with a paid, non-refundable study deposit of at least $250,000.

**Venture business or project developer?** Project developer. Evidence:
- $1B of revenue needs 76 blocks (3,790 MW) at $22,000, or 98-104 blocks at $16,000-17,000. Gross capital $4.7-5.9B at the brief's price, $6.1-8.1B at the clearing price. Project equity $0.9-1.7B. [calc]
- The only fast-revenue precedents own scarce megawatts and are debt-funded with billions: VoltaGrid took $5B of debt and $1.575B of equity for 4.3 GW [notes]. $50M buys about 35 MW [notes].
- If funds own 80-90% of project equity, the company's economic share is fees and promote. Per block: about $4M a year of equity cash flow, of which a 15% promote is $0.6M, plus $0.25M management fee and a one-time $2M development fee. At 76 blocks that is roughly $65M a year recurring. "$1B recognised revenue" would be consolidated revenue with $65-100M of income actually attributable to the company. [calc]

**Dilution path** [calc, round sizes dk]:
| Round | Raise | Post-money | Sold | Founders after |
|---|---|---|---|---|
| Seed | $7.5M | $30M | 25% | 75% |
| A (development capital for 3-4 concurrent blocks) | $35M | $140M | 25% | 56% |
| B (deposits and letters of credit for 10+ concurrent blocks at $8-13M each) | $100M | $500M | 20% | 45% |
| C (co-investment to keep a stake in assets) | $250M | $1.5B | 17% | 37% |
| Option pool 15% | | | | about 32% for all founders together |

One lead founder among three ends near 12-16% of a company that itself holds 10-20% of asset economics: a look-through of roughly 3-6% of asset value. If instead the company owns the assets on its own balance sheet it must raise $1B+ of corporate equity and founders finish below 10%.

**Why still not a clear no.** Conditional on success the seed could return 10-15x (about 11% diluted stake in a $1B developer). The probability is the problem: the investor puts under 5% on that outcome.

**What would change the decision.** A proprietary element with software-like margin (utility-certified dispatch and verification that other owners must licence), or signed evidence that utilities assign the curtailment contract to the battery owner and not to the load.

---

## Persona 4. Incumbents

### 4a. Behind-the-meter gas provider (Solaris or VoltaGrid type)
- **Position.** Fleet sold out; backlog of 11-15 years at about $38,000 per MW-month before fuel [notes]. Not threatened in off-grid sites.
- **Response.** No price response needed. Adds batteries to its own package (already paired with grid-forming batteries in the Energy Vault and similar configurations [notes]). Sells "bridge then backup" engines at grid-connected sites for curtailments longer than four hours, which the battery cannot cover. Tells customers the battery product depends on a utility consent that gas does not need.
- **Number the brief gets wrong.** $38,000 buys prime energy capacity. $22,000 buys only curtailment cover; the customer still pays the grid about $40,000 per MW-month for energy at $55/MWh and full load factor [dk, calc]. Like for like: grid plus battery about $62,000; gas capacity plus fuel about $58,000. The battery is not 42% cheaper. It is roughly at par, with the advantage of ending on the grid.
- **What it has.** Equipment allocation, field crews, $850M-$3B credit lines, investment-grade customer contracts [notes].

### 4b. Battery maker or integrator selling direct (Tesla, Fluence, Energy Vault type)
- **Position.** Demand exceeds supply; 2027 Megapack capacity nearly sold out [notes]. Fluence booked about $850M of data-center business by July 2026 and Energy Vault a 1.25 GW campus system [notes].
- **Response.** Sells to the startup at list with a 15-30% deposit and no priority. Gives frame-agreement pricing and earlier slots to hyperscalers and large developers buying in GWh. Offers the same build-own-operate structure through its own financing partners where the customer wants a service contract [dk].
- **Effect.** The startup's cost is the highest in the market and its delivery date the latest. It cannot promise 9-12 months without an allocation. Panel estimate for a first block: 14-20 months from signing. [dk]

### 4c. The utility
- **Vertically integrated states.** Wants the battery in rate base or in a customer-specific large-load tariff where the customer pays and the utility earns its allowed return [dk]. Has no reason to place a third party between itself and the load.
- **ERCOT wires companies.** Cannot own the battery [dk] but will write a technology-neutral rule: the customer of record must drop to its firm level on signal, by any means. The curtailment obligation attaches to the load, not to a battery vendor. Control of the load-side breaker is "non-negotiable" for at least one utility [notes].
- **Decision.** Will not sign a curtailment contract with a startup shell company as principal obligor at 50 MW+. Would accept the startup as the customer's agent, with the customer liable and the utility holding the breaker.
- **Consequence.** "The company signs the curtailment obligation with the utility" is unlikely to be available. If the obligation sits with the customer, the company is a battery lessor and operator, which is the commodity role.

### 4d. Hyperscaler energy team
- **Position.** 5-7% cost of capital, own tax appetite for the credit, GWh-scale frame agreements, in-house engineers. In-rack batteries arrive with the 800 V DC architecture in 2028-2029 at about $200,000 per MW [notes].
- **Decision: refuses at $22,000 for ten years.** Self-build costs $13,800-16,100 per MW-month equivalent [calc]. A ten-year dedicated-asset take-or-pay is an on-balance-sheet lease anyway [dk], so there is no accounting benefit.
- **Would sign.** A 3-5 year service agreement at $14,000-17,000, no prepayment before delivery, purchase option at a declining schedule, damages uncapped or capped at 24 months of fees with a letter of credit behind them, step-in rights. Only where the provider already holds a utility-approved arrangement at that site.
- **Who actually buys from a startup.** Non-investment-grade colocation developers and neoclouds without energy teams. They pay more and are the weakest credits, which is where Persona 1's 40-45% advance and SOFR+475-550 apply.

---

## Persona 5. Aggressive competing startup already in the niche

Two archetypes, both real categories [source: siliconangle and energy-storage.news above]:

**A. Flexible-compute software company** (over $200M raised, chip-vendor backing, live utility programme).
- Has: utility relationships and a running programme; integration with the compute scheduler, which the battery owner cannot reach; demonstrated 25% load reduction for three hours [notes]; capital for several years.
- Does when C1 appears: stays asset-light. Tells utilities and customers that compute flexibility cuts the battery needed by 25-40%, so the firm megawatt costs less than $22,000. Signs integrators and infrastructure funds as battery partners. Seeks to become the utility's verification and dispatch standard, so every battery on a campus runs under its control layer. Would offer C1 a role as one of several financed-battery suppliers under its dispatch.

**B. Onsite battery developer owned by an infrastructure investor** (first project executed with a utility).
- Has: an executed precedent with a utility programme; a parent with an 8-10% cost of equity; procurement and operating staff; a customer-funded option, which is what the first customer chose.
- Does when C1 appears: matches or undercuts to $16,000-18,000, offers customer ownership with a build-and-operate fee, and asks each utility for the same programme terms as Oregon.

**What C1 would control that neither has:** nothing at launch.

---

## Cross-persona findings

**What the company would control that incumbents cannot copy**
- Batteries, inverters, controls, tax credits and project debt: all purchasable. No.
- Utility programmes and tariffs: open to all qualifying customers once written. No.
- The curtailment contract: likely attaches to the load customer. No.
- Operating record as a curtailment counterparty: real but takes 2-3 years and incumbents are already accruing it.
- Only candidate: a site-specific, executed right to earlier non-firm capacity at named substations. That right follows the land and the load, which makes the defensible business a powered-site developer, not a battery owner.

**Where personas disagree**
- Banker: with an A-rated offtaker the contract is financeable in principle at 50-56% of gross cost; coverage at the brief's price is 1.44-2.06x.
- Fund partner: the same coverage proves the price will not hold.
- Venture investor: neither matters to venture returns, because the asset economics go to the banker and the fund.

**Liabilities the brief understates**
- Performance damages cap $13.2M per block, equal to more than a year of project cash flow, needing a letter of credit.
- Utility-side liability if the load does not drop: unknown, unpriced.
- Tax credit recapture and indemnity to the credit buyer for five years.
- Decommissioning and relocation, about $30-50/kWh ($6-10M) [dk].
- Events longer than four hours fall back on the customer, so the customer still needs engines, which weakens the reason to pay.

---

## Disputed numbers
| Brief | Panel | Basis |
|---|---|---|
| $38,000 gas reference shows $22,000 is cheap | Not comparable. Battery fee sits on top of about $40,000 of grid energy. True comparator is self-owned battery at $13,800-16,100 | [calc, dk] |
| $62M per block, $43M after credit | $68-78M gross, $50-58M net | [notes] FEOC premium; [dk] integration, overbuild, financing costs, transfer discount |
| 70% non-recourse debt | 50-56% of gross for investment-grade offtake; 40-45% otherwise. 70% of gross equals 100% of net cost | [calc] |
| Revenue $13.2M "plus grid revenue" | EBITDA $9.8-10.5M after $3.0-3.4M operating cost; grid revenue $0.3-0.5M, 2-4% of revenue, zero for lenders | [source: Modo] [dk] |
| 9-12 months to operation | 14-20 months for a first block | [notes] sold-out supply; [dk] utility agreement |
| $22,000 for 10 years | Clears at $16,000-18,000 for investment-grade 10-year; or $26,000-30,000 on 5 years | [calc] |
| $5-10M covers origination and deposits | One block needs $8-13M at risk before financial close | [dk, calc] |
| 10% prepayment of three years ($3.96M) | Held in escrow or against a letter of credit by any strong customer | [dk] |

## Probabilities
- First paid commercial delivery within 18 months (by May 2028): 10%.
- $1B of annual recognised revenue within 7 years: 1%.
