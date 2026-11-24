# C1 v1 demand panel, round 1 (simulated, 24 November 2026)

Everything here is a simulated hypothesis. The personas are archetypes. Nothing below is customer validation, and no quote, order or interview is real.

Evidence labels:
- [notes] = the founder's research notes (power_grid.md, ai_compute.md).
- [source: URL] = checked in this session. "snippet" means only the search summary was read, not the page.
- [DK] = domain knowledge, unverified.
- [derived] = my arithmetic on labelled inputs.

Web checks used: 8 of 8 (6 searches, 2 page fetches).

## 0. Result in one paragraph

Seven of eight personas refuse. The neocloud signs, but only a conditional five-year contract with fees starting at energization, and that contract cannot carry the 70% non-recourse debt the plan depends on. The offer fails on three points. Buyers with credit can own the same battery for about half the fee. The startup cannot actually take the curtailment risk off the customer. And nobody has yet shown that a battery buys an earlier energization date at 50 MW or more.

## 1. Facts checked for this panel

| # | Fact | Label |
|---|---|---|
| F1 | FERC rejected PJM's curtailment plan (Interim Resource Adequacy Service) and its bring-your-own-capacity rules around 9 Oct 2026. It approved only a registry of loads of 50 MW or more. FERC suggested PJM look at a voluntary non-firm transmission service. No current PJM route to early connection through curtailment is described. | [source: https://www.latitudemedia.com/news/ferc-rejected-pjms-data-center-curtailment-plan-whats-next-for-byoc/] |
| F2 | PJM, MISO, NYISO and others refiled large-load reforms on 13-16 Nov 2026. MISO and NYISO propose non-firm or flexible classes. Outcomes unknown. | [notes] |
| F3 | Texas SB 6 covers sites above 75 MW. Customers must disclose backup generation able to serve at least 50% of demand. In energy emergencies ERCOT may direct them to run that backup or curtail. The interconnection rule (16 TAC 25.194) was published as a draft in March 2026. I could not confirm final adoption or any battery-specific text. | [source: https://perkinscoie.com/insights/update/sb-6-implementation-shaping-data-center-future-texas, snippet]; [source: https://www.foley.com/insights/publications/2026/03/public-utility-commission-of-texas-issues-proposed-rules-for-large-load-interconn/, snippet] |
| F4 | EPA's 2025 interpretation lets emergency engines run up to 50 hours a year in non-emergency conditions under a financial arrangement, when dispatched by the balancing authority or distribution operator and other conditions are met. Hours run under DOE emergency orders do not count toward the 50. The guidance is non-binding. | [source: https://www.epa.gov/newsreleases/epa-issues-clarification-help-power-data-centers-ensure-us-ai-capital-world, snippet]; [source: https://www.kirkland.com/publications/kirkland-alert/2025/05/new-epa-guidance-clarifies-when-data-centers-and-other-operators-may-utilize-emergency-backup, snippet] |
| F5 | The one executed precedent found: Aligned, Portland General Electric and Calibrant (Macquarie-backed), Hillsboro, Oregon. Battery about 30 MW / 60 MWh, two-hour, completion 2027. Each PGE study is "bespoke" and takes four to six months. Ownership and price not disclosed. | [source: https://pv-magazine-usa.com/2026/03/18/how-on-site-batteries-are-fast-tracking-data-center-grid-connections/] |
| F6 | Google had written about 1 GW of demand response into long-term contracts with five US utilities by March 2026, and says this helps new sites connect sooner. | [source: https://www.verdantix.com/insights/blog/data-centre-load-flexibility-is-becoming-the-new-currency-for-quicker-grid-access, snippet; attribution to this page is my best guess from the result list] |
| F7 | Published value of one month of delay: about $237,000 per MW (60 MW example, $14.2M per month), about $196,000 per MW for a colocation operator (Accenture, $235M a year per 100 MW), about $150,000 per MW (Occam's Edge), and about $833,000 per MW for an AI model provider (Accenture, over $1B a year per 100 MW). Shell cost $11.3M per MW (JLL). | [source: https://kaizen.com/us/insights-us/america-data-center-missing-dates/, snippet]; [source: https://www.accenture.com/content/dam/accenture/final/accenture-com/document-fy26/q4/Accenture-Data-Centre-PoV-2026-v5.pdf, snippet]; [source: https://occamedge.substack.com/p/confronting-the-datacenter-delay, snippet]; per-MW figures [derived] |
| F8 | Utilities want hard control of the load-side breaker (Silicon Valley Power: "non-negotiable"). Flexible-connection programs "have started with MW-scale loads". No GW-scale early energization on a flexibility commitment was found. Idaho Power requires up to 10 hours per event and 225 hours a year. | [notes] |
| F9 | Four-hour battery levelized fixed cost: $216/kW-yr with tax credits, $337/kW-yr without (E3). Median capex $309/kWh. US-made battery systems cost about $100/kWh more than Chinese. Tesla 2027 capacity nearly sold out. Fluence had about $850M of data-center orders by July 2026, $550M from one hyperscaler. | [notes] |
| F10 | AI workload flexibility demonstrated at 25% for three hours (Emerald AI), up to 40% (EPRI). Backup gensets cost about $1M per MW and some AI builds skip them. Abilene implies about $38M of capital per MW of IT load. | [notes] |
| F11 | Credit: CoreWeave rated B+, bonds traded near 15% in October 2026. AI-related debt issuance fell from $113B (June) to $23B (September). Hyperscaler bonds priced at 5.6-7.5%. | [notes] |

## 2. Shared arithmetic

All [derived] from the brief and the facts above unless labelled otherwise.

| Item | Calculation | Result |
|---|---|---|
| Fee per MW-year | $22,000 x 12 | $264,000 |
| Fee as energy adder at 100% load factor | $264,000 / 8,760 h | $30/MWh |
| Prepayment | 10% x 36 months x $22,000 | $79,200 per MW; $3.96M per 50 MW block |
| Cost of a three-year bridge under the 10-year take-or-pay | 3 years of fees + 50% of 7 years = 6.5 years x $264,000 | $1.72M per MW |
| Cost of buying the battery | Brief: $1.24M per MW; less 30% credit | $0.87M per MW, and the buyer keeps the asset |
| Buyer's own cost, investment-grade, 6% money | $0.87M over 10 years (factor 7.36) = $118,000 a year, plus about $25,000 a year O&M and augmentation [DK] | $11,900 per MW-month; $9,500 on a 15-year life |
| Buyer's own cost at E3's assumptions | $216/kW-yr [notes] | $18,000 per MW-month |
| Startup's break-even fee, brief's capex | $43M at about 10% blended cost of capital over 10 years (factor 6.14) = $7.0M, plus about $1.5M O&M, insurance, land, operations [DK] | $8.5M a year = $14,200 per MW-month |
| Startup's break-even fee, corrected capex (section 4) | $54.6M net: $8.9M + $1.8M | $17,800 per MW-month |
| Liquidated damages cap | 12 x $22,000 = $264,000 per MW, against about $38M per MW of campus capital [notes] | 0.7% of the capital exposed |
| Lease liability if the contract is an embedded lease | $13.2M a year for 10 years at 8% (factor 6.71) | $88.6M per block, against a $62M asset |
| Colocation carry cost of a month's delay when the shell is already built | $11.3M per MW x 8% / 12 | $75,000 per MW-month |
| Capacity needed for $1B of revenue | $1B / $264,000 | 3,790 firm MW, about 15 GWh, about $4.7B of capex |

The central gap: an investment-grade buyer's own cost is $10,000-12,000 per MW-month and the startup's break-even is $14,000-18,000. No price clears both.

## 3. Personas

### P1. Energy procurement lead, top-five hyperscaler

- **Who:** runs a team that buys power, storage and flexibility contracts at GW scale. Investment grade. Borrows at about 5.6-7.5% [notes].
- **Incentives and constraints:** measured on MW energized per year and cost per MW. Owns the utility relationships. Free cash flow is negative in some quarters [notes], so off-balance-sheet structures have some appeal, but a battery is about 3% of campus capital ($1.24M against about $38M per MW) [derived].
- **Alternatives already in hand:**
  - Buys batteries direct. A hyperscaler placed about $550M with Fluence [notes].
  - Workload curtailment of 25-40% [notes], and demand response written into utility contracts (F6).
  - Existing diesel fleet under emergency rules (F3, F4).
  - Third-party gas on 10-15 year terms [notes]. This is outsourced because the provider controls scarce engines, fuel, permits and crews. A battery provider controls nothing scarce. The brief's own selling point, that batteries can be bought in under a year, is the reason no intermediary is needed.
  - Waiting. A portfolio of sites means no single site is critical.
- **Decision: refuses.** No purchase order, no prepayment.
- **Price:** would lease only at or below own cost: $11,000-12,000 per MW-month, three to five years, purchase option at depreciated book value, 100% of grid revenue kept. That is below the startup's break-even.
- **Reasons:**
  1. $22,000 is about twice own cost.
  2. A three-year bridge costs $1.72M per MW against $0.87M to own.
  3. The utility agreement stays with the customer of record [DK]. A third party in the middle adds a failure point and removes nothing.
  4. The value of an earlier month accrues to whoever negotiated the utility deal, and this team does that itself.
- **Is "one month earlier" real for them:** yes in principle (up to about $833,000 per MW-month of revenue for a model provider, F7). They pay away none of it to a vendor who did not cause the acceleration.
- **Evidence that would change it:** the startup holds, in its own name, an executed utility agreement with a dated earlier energization at a specific site the hyperscaler wants, plus a firm 2027 battery allocation. Then it is selling a powered site sooner, and the hyperscaler would pay a one-off development fee and buy the asset at commercial operation.

### P2. Head of power, wholesale colocation developer

- **Who:** delivers powered shells to hyperscaler tenants. Sub-investment-grade, project-financed.
- **Incentives and constraints:** lease delivery dates carry delay credits and tenant termination rights [DK]. The tenant's design standard and service-level terms define what counts as acceptable utility service. Cannot change the electrical topology or the service class without tenant consent [DK].
- **Alternatives:**
  - Put the battery in the project budget through the EPC contractor and an OEM service agreement, funded by the construction loan.
  - Buy from a provider with a balance sheet and a precedent: Calibrant with Macquarie backing (F5).
  - Negotiate the flexible connection directly, as Aligned did with PGE (F5).
  - Existing gensets for emergency events (F3, F4).
  - Sequence the build to the firm date. If the shell is not yet built, delay costs little.
- **Decision: refuses today.** Offers a non-binding letter of intent with no money.
- **Price they would sign at:** $14,000-16,000 per MW-month, five-year term, buyout option, fees starting only at energization, and only with two documents in hand: the utility's written earlier date tied to the battery, and the tenant's written acceptance of non-firm service inside the lease's power-availability definition.
- **Reasons:**
  1. The tenant decides, and the tenant is P1, P6 and P7.
  2. The value of a month for a colocation developer is $75,000 (carry) to $150,000-240,000 (lease revenue) per MW, not $500,000 (F7, section 2). Where the lease runs 15 years from commencement, an earlier start mostly shifts the revenue stream; the gain is carry and avoided delay credits [DK].
  3. Ten years of take-or-pay for a bridge that the brief says ends in 2029-2031.
- **Share of the gain they would pay away:** 15-25% of realized gain, after the fact. On 12 months gained at $175,000, that is $0.3-0.5M per MW in total, about $14,000 per MW-month over three years [derived].
- **Evidence that would change it:** one operating reference at 30 MW or more where the utility's letter names the battery as the reason for the earlier date, and a tenant that has accepted it.

### P3. Infrastructure head, neocloud or AI lab

- **Who:** 100-500 MW sites, many in Texas. Weak credit (B+ class, paper near 15%) [notes]. Speed decides the job.
- **Incentives and constraints:** GPUs that arrive before power lose roughly $350,000-500,000 per MW-month in depreciation alone (about $25-30M of chips per MW over five to six years) [derived, DK]. For this buyer the brief's $500,000 is about right. Customer contracts run three to five years [DK]. Cannot fund a 1,200 MWh battery purchase itself.
- **Alternatives:**
  - Off-grid gas with batteries, already common in Texas (Energy Vault 1.25 GW) [notes]. Engines ordered now arrive in 2028 [brief].
  - Workload curtailment during firm load shed, which SB 6 requires anyway (F3).
  - No gensets at all; some builds skip them [notes].
  - Calibrant, Energy Vault or an OEM with vendor finance.
- **Decision: signs, conditionally.** Signs a five-year contract at $20,000-22,000 per MW-month. Pays a $1M refundable study deposit now. Puts the rest of the prepayment in escrow, released only when the utility or ERCOT issues a written earlier energization date. Fees start at energization.
- **What they refuse:** the 10-year term, the 50% termination payment, any unsecured prepayment, and the four-hour limit without a stated plan for longer events.
- **Reasons:** price is not the problem. Third-party ownership suits a buyer that cannot borrow. A 300 MW site needs six blocks, 1,200 MWh, about $370M [derived], in a year when Tesla is nearly sold out [notes].
- **The catch for the founder:** lenders will not put 70% non-recourse debt on a five-year contract with a B+ counterparty [DK, consistent with notes on credit]. The one persona that says yes cannot be financed as planned.
- **Open regulatory question:** ERCOT's batch study gives year-by-year MW allocations for 2028-2032 [notes]. Nothing found says a battery earns an earlier allocation. Texas also paused new data-center interconnections in summer 2026 [notes].
- **Evidence that would change it to an unconditional yes:** an ERCOT or utility document that grants earlier MW against a battery-backed commitment; a customer contract long enough to match the term.

### P4. Energy manager, semiconductor fab or electrified industrial plant

- **Who:** buys firm power for a process plant.
- **Incentives and constraints:**
  - Fab: a voltage sag of milliseconds scraps wafers. Firm dual-feed service and a dedicated substation are negotiated at site selection, three to five years ahead, often with state support [DK]. Non-firm service is not acceptable.
  - Industrial plant: power is $50-70/MWh of cost [DK]. The fee adds $30/MWh [derived].
- **Alternatives:** interruptible tariffs that pay the plant to curtail; arc furnaces and electrolysers shed load routinely [DK]. Existing uninterruptible supplies on critical tools. Waiting, since the plant schedule was set around the firm date.
- **Decision: refuses.**
- **Price:** nothing above about $5,000 per MW-month, and only for a plant that is already built and stranded.
- **Reasons:** a month earlier is worth perhaps $10,000-30,000 per MW in contribution margin [DK], a twentieth of the brief's figure. Industrial loads get paid for flexibility; they do not pay to hide it.
- **Evidence that would change it:** none at this price. This segment is not a market for this product.

### P5. CFO, colocation developer

- **Who:** owns capital allocation, lender relations and accounting.
- **Constraints:**
  - Accounting: a dedicated battery on the developer's site, whose output it takes and directs, likely contains an embedded lease under ASC 842 [DK]. Liability about $88.6M per block for a $62M asset [derived].
  - Covenants: project credit agreements limit additional debt and liens and require lender consent to material project documents. A third-party asset on site needs a site lease, access rights and the lenders' engineer's sign-off [DK].
  - Coverage: the fee is operating cost that cuts debt-service coverage unless the tenant reimburses it. Hyperscaler leases pass power through at cost, so a new charge needs tenant consent [DK].
- **Alternatives:** capitalize the battery in the project. $62M gross, about $45M after selling the tax credit at 90-95 cents [DK], at about 7.5% over 10 years is about $6.5M a year against a $13.2M fee [derived].
- **Decision: refuses.** No prepayment.
- **Price and terms they would sign:** at most $13,000 per MW-month; five years; termination payment on a declining schedule tied to the unamortized asset, not 50% of remaining fees; prepayment only against a letter of credit or in escrow; full tenant pass-through; lender consent obtained by the vendor.
- **Reasons:** paying 6.5 years of fees for a three-year need; an unsecured $3.96M prepayment to a company with $5-10M; a liability larger than the asset.
- **Evidence that would change it:** tenant agrees in the lease to reimburse the fee for the full term, which makes it the tenant's credit and the tenant's decision.

### P6. Procurement executive, hyperscaler

- **Who:** runs vendor qualification and contract terms.
- **Rules they apply [DK]:** audited financials, usually three years; liability insurance of $100M or more; parent guarantee or performance bond; cybersecurity review of any system that takes a utility dispatch signal; safety record; no unsecured prepayments; critical-supplier limits. Qualification of a new critical-infrastructure vendor takes 6-12 months and starts with a pilot at a non-critical site.
- **Counterparty analysis:** the obligor is a single-asset vehicle, 70% lender-funded and non-recourse, sponsored by a company with $5-10M. Damages are capped at 0.7% of the capital exposed [derived]. On default the lenders, not the startup, control the asset.
- **Would they accept a startup holding the utility curtailment obligation:** no. The obligation sits in the utility's tariff or service agreement with the customer of record [DK]. If the battery fails, the utility opens the breaker (F8) and the hyperscaler's load goes dark. The startup can be an agent. It cannot be the obligor in any way that protects the customer.
- **Decision: refuses.** No price cures it.
- **Would buy instead from:** the battery maker with a long-term service agreement (Tesla, Fluence), or an infrastructure fund platform with a balance sheet (Macquarie-backed Calibrant, F5).
- **Evidence that would change it:** an investment-grade guarantor behind the 10-year obligation; damages cap raised to cover replacement power and tenant credits; two years of operating history; step-in and purchase rights at a fixed schedule.

### P7. VP of critical facilities engineering

- **Who:** owns the electrical design standard and tenant uptime terms.
- **Technical position:**
  1. **Mode matters.** If "curtailment" means holding net import at the meter below a limit while staying connected, the battery discharges in parallel with the grid and the UPS never notices. That is acceptable. If the utility opens the breaker (F8), the battery must form the grid for a 50 MW AI load that swings tens of percent in under a second [DK], the UPS sees a transition, and gensets must synchronize to an inverter-formed bus. That needs a full failure-mode study and a staged test.
  2. **Four hours is not backup.** After four hours the battery is empty and the gensets run. So the battery removes no genset from the design. Gensets cover long events; the battery covers only the short, frequent, non-emergency calls that emergency-permitted engines may not serve beyond 50 hours a year (F4). That is its real niche: roughly 150 hours a year of non-emergency curtailment, with no engine start.
  3. **Recharge.** The campus is non-firm because the grid lacks headroom. Recharging 200 MWh while serving 50 MW needs up to twice the import. Back-to-back events on consecutive peak days, or a multi-day winter emergency of the 2021 Texas kind [DK], defeat a four-hour block. Idaho Power's tariff asks for 10 hours per event (F8).
  4. **Energy margin.** A 200 MWh nameplate does not deliver 50 MW for four hours after losses, reserve and ten years of fade. It needs 20-25% more energy or scheduled augmentation [DK].
  5. **Siting and approvals.** Fire code separation, large-scale fire test data, insurer approval, protection coordination and short-circuit studies [DK]. The battery must sit on its own medium-voltage bus, isolable from the critical path.
  6. **Double use.** A battery held full for curtailment cannot also sell the same energy. Grid stress is when both are called.
- **Decision: refuses to approve the standard block as a substitute for firm service or for gensets.** Would approve a 10-20 MW pilot, upstream, in grid-parallel mode, with gensets kept at full redundancy.
- **Price view:** worth what it saves in engine permitting and runtime, perhaps $6,000-10,000 per MW-month [DK], not $22,000.
- **Evidence that would change it:** 12 months of operation at 30 MW or more under real AI load with at least ten utility-called events; a written utility definition of compliance (averaging window, notice time, maximum event length); six-hour or longer energy at guarantee.

### P8. Site operations manager

- **Who:** runs the campus 24/7 and answers the utility's control room.
- **Concerns:**
  1. **One chain of command.** During an event the dispatch signal goes to the startup's controls, but the utility's operator calls the site, and the site is accountable [DK]. A remote startup operating switchgear inside the fence breaks lockout and switching authority rules.
  2. **The fallback is the site's job.** At hour three someone decides to start engines or shed load. That needs live state of charge in the site's own power monitoring system, a local override and a written trigger (for example, start gensets at 40% charge).
  3. **Staffing.** Events come at 3 a.m. and in storms. The vendor needs a technician on site within 30 minutes, around the clock. Skilled electrical labor is already short [notes].
  4. **Fire response.** A battery fire plan with the local fire department, and clear responsibility for it.
  5. **No engines, no fallback.** At sites that skipped gensets [notes], an event past four hours means shedding compute. Operations needs that sequence agreed with the tenant in advance.
- **Decision: refuses to hand over control during an event.** Holds an effective veto, not a budget.
- **Terms they would accept:** site retains switching authority and override; vendor supplies telemetry, a staffed operations centre and a 30-minute on-site response; joint drills each quarter; the utility's contact of record is the site.
- **Evidence that would change it:** a run-book proven in drills and at least one real event at another site.

## 4. Numbers in the brief the panel disputes

| Brief | Panel's corrected value | Basis |
|---|---|---|
| A month earlier is worth $500,000 per MW | $75,000 (colocation carry) to $150,000-240,000 (colocation lease revenue); $350,000-830,000 only for an operator with GPUs waiting; $10,000-30,000 for industrial loads | F7; [derived]; [DK] |
| Reference price is gas at $38,000 per MW-month | Wrong comparator. Gas supplies energy all year; the battery covers at most 200 hours. The notes call the $38,000 an order-of-magnitude figure. The right comparator is the buyer's own battery: $10,000-12,000 (investment grade) to $18,000 (E3) per MW-month | [notes]; [derived] |
| $1.24M per firm MW; $62M per block | $1.5-1.7M per firm MW; $75-85M per block, after 20-25% extra energy, grid-forming inverters, medium-voltage tie-in and fire separation. The $309/kWh median may not fully include the $100/kWh premium for compliant US supply | [DK]; [notes] |
| $43M after tax credit | About $45M on the brief's capex, because a startup must sell the credit at 90-95 cents; $53-60M on corrected capex. Credit depends on meeting the 55-60% non-FEOC threshold | [DK]; [notes] |
| Grid revenue when idle | Close to zero bankable. The battery must stay charged for curtailment, the two calls coincide, and exporting needs a generator interconnection, which is the same queue. Texas merchant battery revenue has fallen to perhaps $20-50/kW-yr [DK]. PJM capacity ($119/kW-yr [notes]) needs capacity interconnection rights and a four-hour accreditation near half [DK] | [DK]; [notes] |
| Guarantee of four hours per event, 200 hours a year | The one tariff quoted in the notes asks for 10 hours per event and 225 hours a year. Emergency events run for days | [notes]; [DK] |
| Delivery in 9-12 months | 15-24 months: Tesla 2027 nearly sold out; utility study four to six months and bespoke; step-up transformers and switchgear have their own lead times; the only precedent was announced in 2025 and completes in 2027 | [notes]; F5 |
| "PJM connect-and-manage" as an enabling rule | FERC rejected it around 9 October 2026. A refiling is pending | F1, F2 |
| "Texas SB 6" as an early-energization route | SB 6 imposes curtailment and backup deployment on all loads above 75 MW. Nothing found says it trades a battery for an earlier date | F3 |
| "The company signs the curtailment obligation with the utility" | The obligation stays with the customer of record. The startup's damages cap is 0.7% of the capital exposed | [DK]; [derived] |
| 70% non-recourse debt | Achievable only with an investment-grade payer. With the buyers who say yes, expect 40-50% at higher rates | [DK]; [notes] on credit |

## 5. Five most damaging objections, most lethal first

1. **Self-supply costs less than the startup's break-even.** Own cost $10,000-12,000 per MW-month; startup break-even $14,000-18,000; price $22,000. A three-year bridge under the 10-year contract costs $1.72M per MW against $0.87M to own the asset. The startup controls no scarce input. [derived from notes]
2. **The risk transfer is not real.** The utility's obligation and the breaker stay with the customer. Damages are capped at 0.7% of exposed capital. The buyer pays for a transfer it does not get. [notes on breaker control; DK; derived]
3. **The causal claim is unproven and the rules cited are weaker than stated.** FERC rejected PJM's plan in October 2026. SB 6 is an obligation, not a fast lane, and it points at existing gensets. The only precedent is 30 MW, two-hour, bespoke. Where the delay is a missing substation or transformer, a battery does nothing. [F1, F3, F5; notes]
4. **Four hours does not match the exposure, so cheaper tools still have to be there.** Tariffs ask for 10 hours; emergencies run for days; recharge needs headroom the site lacks. Gensets and 25-40% workload curtailment remain necessary and already cover emergency events at almost no added cost. [notes; F4; DK]
5. **Credit runs the wrong way on both sides.** Buyers with credit refuse. The buyer who signs is B+ and wants five years. Procurement will not accept a $5-10M startup vehicle as a 10-year counterparty or prepay it unsecured. Funded competitors exist: Calibrant with Macquarie, Tesla, Fluence, Energy Vault, and gas providers that bundle batteries. [notes; F5; DK]

## 6. Conditions under which each "no" becomes a "yes" (their terms)

| Persona | Condition |
|---|---|
| P1 hyperscaler energy lead | Startup arrives holding an executed utility agreement with a dated earlier energization at a site the hyperscaler wants, plus a firm battery allocation. Hyperscaler pays a development fee and buys the asset at commercial operation. Or a lease at $11,000-12,000 with purchase option |
| P2 colocation head of power | Utility's written earlier date tied to the battery, and tenant's written acceptance. Then $14,000-16,000, five years, buyout option, fees from energization |
| P3 neocloud | Already a conditional yes. Unconditional when the utility or ERCOT issues the earlier date in writing and the term matches its customer contract |
| P4 fab or industrial | None at this price. Under $5,000 for an already-built, stranded plant |
| P5 colocation CFO | Tenant reimburses the fee in the lease for the full term. At most $13,000, five years, declining termination schedule, secured prepayment, lender consent delivered by vendor |
| P6 hyperscaler procurement | Investment-grade guarantor on the 10-year obligation, higher damages cap, two years of operating history, step-in and purchase rights |
| P7 critical facilities VP | Twelve months of operation at 30 MW or more under AI load with ten or more real events; utility's written compliance definition; six hours or more of guaranteed energy; gensets retained |
| P8 site operations | Site keeps switching authority and override; vendor provides telemetry, staffed operations centre, 30-minute response and quarterly drills |

## 7. Probabilities (panel's honest estimate)

- **First paid commercial delivery within 18 months, this version (50 MW block, these terms): 12%.** About 20% if a 10-30 MW paid pilot counts. Basis: the funded precedent took roughly two years from announcement to completion at 30 MW (F5); 2027 battery supply is tight [notes]; the only willing buyer is conditional and hard to finance.
- **$1 billion of annual recognized revenue within seven years: 2%.** Basis: needs about 3.8 GW of firm capacity and $4.7B of capex at the brief's price, or about 5.5 GW at the $15,000 buyers would sign [derived]; the product is a bridge that the brief itself says expires in 2029-2031; self-supply and funded competitors take the creditworthy accounts.

## 8. What the panel did not establish

- Whether Texas has adopted final SB 6 rules, and whether they give batteries any credit toward earlier energization. Searches returned only the March 2026 draft.
- The price and ownership in the Aligned/Calibrant deal.
- Actual curtailment hours per year under any executed flexible-connection agreement.
- Current Texas merchant battery revenue; the figure used is unverified domain knowledge.
- All persona decisions are simulated. None is evidence of real demand or real refusal.
