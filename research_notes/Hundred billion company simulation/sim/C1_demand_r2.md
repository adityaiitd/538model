# C1 v2 demand panel, round 2 (simulated, 24 November 2026)

Everything here is a simulated hypothesis. The personas are archetypes. Nothing below is customer validation, and no quote, order or interview is real.

Evidence labels:
- [notes] = the founder's research notes (power_grid.md, ai_compute.md).
- [source: URL] = checked in this session. "snippet" means only the search summary was read, not the page.
- [DK] = domain knowledge, unverified.
- [derived] = my arithmetic on labelled inputs.
- R1 = this panel's round-one transcript, C1_demand_r1.md.

Web checks used this round: 5 of 5 (4 searches, 1 page fetch).

## 0. Result in one paragraph

Demand is now real. The neocloud signs at the asking price and would pay more, and site operations no longer objects. The other six still refuse the startup, mostly in favour of providers that already hold engines and crews. The redesign moved the problem from demand to supply and finance. The startup holds no engines, the "open" non-incumbent capacity is already being bought in 684-1,000 MW lots, the block design does not fit the engines the founder proposes to buy, and the year-four release leaves capital unrecovered on a weak credit. The price of $38,000 is too low for the risk taken; buyers in the target segment would sign at $45,000-50,000.

## 1. Facts checked for this round

| # | Fact | Label |
|---|---|---|
| G1 | HD Hyundai Heavy Industries (Korean marine engine maker) sold 1,000 MW of 9.6 MW HiMSEN gas engines for $673.8M in August 2026 to Corban Energy Group, for data centres of an unnamed major US technology company. In April 2026 it sold about 684 MW of 20 MW-class engines for about $424M to Aperion. No delivery dates or production capacity disclosed. | [source: https://thenextweb.com/news/hd-hyundai-corban-1000mw-engines-ai-data-centres] |
| G2 | Engine-only price implied by G1: $0.62-0.67M per MW. | [derived] |
| G3 | ProPetro's power arm has signed an 80 MW, 10-year contract (May 2025) and a 60 MW hyperscaler contract in the Midwest using gas engines plus a battery (October 2025), both take-or-pay with availability guarantees. | [source: https://www.zacks.com/stock/news/2475083/propetro-s-propwr-wing-lands-first-10-year-80mw-power-deal, snippet]; [source: https://ng.investing.com/news/stock-market-news/propetro-stock-surges-after-securing-60mw-data-center-power-contract-93CH-2166311, snippet] |
| G4 | ProPetro has about 2.6 GW of generation secured against about 510 MW contracted. Capital cost $1.4-1.5M per MW with balance of plant. Payback target four to six years. | [notes] |
| G5 | Conduit Power offers bridge power to a Texas data-centre developer on a five-year initial term. Aggreko, Enchanted Rock and Caterpillar dealers all market bridge power to data centres. | [source: https://utilitydive.com/news/conduit-power-bridge-power-texas-data-center-engie/759759, snippet]; [source: https://www.aggreko.com/en-my/sectors/data-centres/bridging-power-solutions, snippet]; [source: https://www.power-eng.com/gas/power-flexibility-the-key-to-data-center-buildout-enchanted-rock-believes/, snippet] |
| G6 | Behind-the-meter power costs $100-165/MWh all-in (Rabobank); a VoltaGrid deck gives $0.10-0.18/kWh. Bridge duty is typically three to seven years. | [source: https://www.rabobank.com/knowledge/d011524694-the-sprint-data-centers-are-building-a-parallel-energy-system-in-the-us, snippet] |
| G7 | No public per-MW-month price for a short-term gas contract was found. | search result, this round |
| G8 | Wärtsilä orders booked in Q3 2026 deliver in 2028. Wärtsilä and Caterpillar are adding capacity for 2027-2028. GE Vernova order growth slowed in Q3 2026. | [notes] |
| G9 | Liberty expects about $300M of capacity prepayment on a 1.2 GW deal (about $250,000 per MW). Solaris terminations cost 50% of remaining revenue. Solaris Q3 2026: power segment EBITDA $127.0M on 820 MW average earning capacity. | [notes] |
| G10 | Islanded gas for AI is already accepted by large buyers: Energy Vault 1.25 GW off-grid, VoltaGrid 2.3 GW for Oracle. A gas pipeline and air permit stalled Oracle's 2.45 GW New Mexico site. | [notes] |

## 2. Shared arithmetic

All [derived] unless labelled.

| Item | Calculation | Result |
|---|---|---|
| Fee per MW-year | $38,000 x 12 | $456,000 |
| Fee as energy cost at full load | $38,000 / 730 h | $52/MWh |
| All-in with fuel | $52 + 8.8 MMBtu/MWh x $3.50 [DK] | about $83/MWh at full load; about $105 at 70% use |
| Position against market | G6 range $100-165/MWh | At or below the bottom of the range |
| Solaris realized EBITDA per earning MW | $127.0M / 820 MW / 3 months | about $52,000 per MW-month (includes services; order of magnitude) |
| Minimum contracted revenue (release after year four) | 4 years + 12 months of fees | $2.28M per MW; $57M per block |
| Minimum contracted cash margin | 5 years x $250,000-375,000 | $1.25-1.9M per MW |
| Security | 6 x $38,000 | $228,000 per MW; $5.7M per block |
| Damages cap | 3 x $38,000 = $114,000 per MW against about $38M per MW exposed [notes] | 0.3% (was 0.7% in v1) |
| Lease liability, minimum term | $11.4M a year x 5 years at 8% (factor 3.99) | $45.5M per block |
| Installed capacity, N+2, 2.5 MW units | 10 + 2 units = 30 MW for 25 MW net | 20% overbuild |
| Installed capacity, N+2, 9.6 MW units | 3 + 2 units = 48 MW for 25 MW net | 92% overbuild |
| Corrected cost, high-speed units | $1.45M x 1.2, plus battery 20 MWh at about $350/kWh [DK] = $7M if not already inside the $1.45M | $1.75-2.0M per net MW; $44-50M per block |
| Corrected cost, 9.6 MW medium-speed units | 48 MW installed, engine halls and foundations [DK] | $2.3-2.8M per net MW; $58-70M per block |
| Payback at corrected cost | $1.75-2.0M / $250,000-375,000 | 4.7-8 years; firm term is 5 |
| Equipment deposits | $0.65M per MW (G2) x 30 MW = $19.5M; 20-30% deposit [DK] | $3.9-5.9M per block; two blocks take $8-12M |
| NOx, 25 MW with catalytic control | 33,500 bhp x 0.07 g/bhp-h x 8,760 h [DK] | about 23 tons a year; minor source |
| NOx, 150 MW with control | six times the above | about 136 tons a year; above the 100-ton major-source line [DK] |
| Gas demand, 25 MW | 25 x 8.8 x 24 | about 5,300 MMBtu a day |
| Capacity for $1B of revenue | $1B / $456,000 | 2,190 MW; 88 blocks; $3.2B at brief cost, $3.9-4.4B corrected |

## 3. Round-one objections: status

| # | Round-one objection | Status | Reason |
|---|---|---|---|
| 1 | Self-supply costs less than the startup's break-even; the startup controls no scarce input | Partly resolved | Weak-credit mid-size buyers cannot self-supply gas engines, so the self-supply half is gone for the target segment. The second half stands: the startup still holds no fleet, no slots and no crews, and incumbents that do hold them already serve 60-80 MW sites (G3, G4, G5). |
| 2 | Risk transfer is not real; damages cap 0.7% | Partly resolved | The fiction of holding a utility obligation is gone; the startup now really is the supplier. But the cap fell to 0.3%, and the buyer now depends on the startup for all of its power, not for 200 hours a year. |
| 3 | Battery-for-earlier-date unproven; rules weaker than stated | Resolved | No utility dependency remains. It is replaced by a gas and air-permit dependency (new objection N4). |
| 4 | Four hours does not match the exposure | Resolved | Engines run continuously. The replacement risk is fuel supply as a single point of failure (N4, N5). |
| 5 | Credit runs the wrong way; the one signer cannot be financed | Partly resolved | Seven-year term, security and direct agreements make a financeable structure possible. But the firm term is five years, the capital is not recovered inside it at corrected cost, and the recovery relies on reselling used non-incumbent engines into a 2031-32 market. Lenders will price that at 11-14% and 40-50% leverage [DK], which the $38,000 price does not support. |

## 4. New objections created by the redesign

- **N1. No scarce input, and the idea is not private.** Non-incumbent engines are already being bought by funded developers in 684 MW and 1,000 MW lots (G1). A 25 MW buyer with $5-10M sits last in the maker's queue. ProPetro alone has about 2.1 GW secured and uncontracted (G4) and has done 60 and 80 MW deals (G3). Nothing stops it serving these sites.
- **N2. The block does not fit the engines.** Korean and Japanese medium-speed engines come in 5-20 MW units. N+2 on a 25 MW block then means 48-80 MW installed, $2.3-2.8M per net MW. Those engines weigh over 100 tonnes each and need foundations and engine halls [DK]; they are not skid-mounted and not cheaply moved. Redeployment recovers perhaps 55-65% of installed cost, because civil works, gas connection and site electrical stay behind [DK].
- **N3. The year-four release.** Minimum cash margin is $1.25-1.9M per MW against $1.75-2.8M of cost. Releases will cluster around 2031-32, when grid service arrives and engine makers' added capacity is on the market (G8). The residual value is weakest exactly when it is needed.
- **N4. Gas and permits replace the utility.** A gas lateral and meter station take 9-24 months [DK]. An islanded plant with one gas feed fails in a winter gas curtailment. A 25 MW block with catalytic control is a minor air source; 150 MW crosses the major-source line and adds 12-18 months [DK]. New Mexico shows the failure mode (G10). "12-15 months from deposit" holds only at a site that already has gas and a permit.
- **N5. Total dependency at 99.9%.** 99.9% allows 8.8 hours of outage a year; tenants expect 99.99% or better [DK]. Damages are capped at 0.3% of exposed capital. The buyer's own project lenders must accept the operator and the equipment, and a first-time operator with unfamiliar engines does not pass their engineer's review [DK].
- **N6. Capital.** Deposits on two blocks take $8-12M, the whole of the company's funds, before permits, gas studies and engineering.
- **N7. Underpricing.** $38,000 comes from an 11-year average with investment-grade buyers [notes]. For a five-year firm term with B-rated tenants the buyers themselves would pay $45,000-50,000. The founder is giving away the risk premium.

## 5. Personas

### P1. Energy procurement lead, top-five hyperscaler
- **Position:** already outsources gas to third parties on 10-15 year terms [notes] and has accepted Korean engines through a funded developer at 1,000 MW (G1). Not the target of v2.
- **Alternatives:** Solaris, Williams, VoltaGrid, Liberty for large sites; ProPetro for 60-80 MW (G3).
- **Decision: refuses the startup.**
- **Price:** would pay $38,000-42,000 to a provider with a running fleet. Price is not the issue.
- **Reason:** no reason to take a 25 MW block from a first-time operator when fleet owners quote the same size.
- **Would change it:** a first block running 12 months at 99.99%, and a delivery date earlier than any fleet owner can offer.

### P2. Head of power, colocation developer (hyperscaler tenants)
- **Position:** tenant credit is investment grade, so the large providers want this business (Vantage and Liberty, up to 1 GW [notes]).
- **Alternatives:** run a tender among ProPetro, Liberty, Conduit, Enchanted Rock.
- **Decision: refuses a binding contract today.** Would include the startup in a tender.
- **Price and terms if the startup wins on date:** $38,000-42,000, seven years, daily delay damages, evidence of an engine purchase order with delivery slots, air permit and gas agreement in hand before signing.
- **Reason:** the only thing he buys is the date, and the startup cannot yet prove one.
- **Would change it:** engines on order and a permitted site with gas.

### P3. Infrastructure head, neocloud or AI lab
- **Position:** the target buyer. GPUs waiting cost $350,000-830,000 per MW-month (R1). All-in power at $83-105/MWh is trivial against that.
- **Alternatives:** Conduit, ProPetro, Enchanted Rock, Aggreko rental at higher rates; larger peers buy turbines themselves (Crusoe [notes]), small ones cannot.
- **Decision: signs.**
- **Price and terms:** $38,000 as offered, and would pay $45,000-50,000 for delivery inside 12 months. Seven years with the year-four release. Security by letter of credit posted at commercial operation, not at signing. A reservation deposit of about $50,000 per MW in escrow, released against the engine maker's purchase order. Right to walk and recover the deposit if operation slips more than three months. Wants 99.99% and a stated backup-fuel plan.
- **Reason:** speed, no capital of its own for power, and a term that matches its customer contracts.
- **Limit:** a letter of credit of $11.4M per 50 MW uses scarce credit capacity; some in this segment cannot post it [DK, notes on credit].

### P4. Energy manager, fab or electrified industrial plant
- **Fab:** refuses. An islanded engine plant at 99.9% is not acceptable for wafer production [DK].
- **Industrial:** refuses. $83-105/MWh against $50-70/MWh grid power [DK]. Remote loads with no grid (oilfield, midstream) do buy this, from oilfield-service providers at four-year payback (Targa, 230 MW with ProPetro [notes]).
- **Price:** $25,000-30,000 at a remote site, from an incumbent.
- **Would change it:** nothing for a fab.

### P5. CFO, colocation developer
- **Position:** v2 fits better than v1. The term is shorter, the release right exists, and the fee is market for gas.
- **Constraints:** embedded lease, about $45.5M per block [derived]. Security of $5.7M per block uses revolver capacity. The campus lenders' engineer must accept the plant and the operator, because the plant is now the campus's only power [DK].
- **Decision: refuses until the lenders' engineer accepts the operator and equipment.**
- **Price and terms then:** $38,000 as a full tenant pass-through; security by letter of credit that steps down to three months after 24 months of payment; daily delay damages; step-in rights and an option to buy the plant if the provider defaults.
- **Reason:** a dark campus is a loan default; the counterparty risk now runs toward the startup.
- **Would change it:** a named infrastructure fund standing behind performance, and a service agreement from the engine maker with parts held in the US.

### P6. Procurement executive, hyperscaler
- **Decision: refuses.** As end tenant, would sign a standard consent but not a direct agreement that guarantees a landlord's power fees.
- **Reasons:** damages cap 0.3%; first-time operator; qualification takes 6-12 months [DK].
- **Would buy from:** fleet owners with rated debt and operating history (Solaris BB-, VoltaGrid [notes]).
- **Would change it:** two years of operating history and a guarantor.

### P7. VP of critical facilities engineering
- **Position:** islanded gas with a grid-forming battery is an accepted architecture (G10). The concept passes; this specification does not.
- **Objections to the specification:**
  1. 99.9% is one order of magnitude short. Wants 99.99% at the plant bus.
  2. One gas feed. Wants dual fuel, stored fuel or retained diesel sets (about $1M per MW [notes]).
  3. Battery power. 10 MW on a 25 MW block covers a 40% swing. Synchronized AI training loads can swing more [DK]. Wants battery power close to block rating, with less energy.
  4. Engines. Wants one proven model per fleet, with documented running hours on gas at 60 Hz, emissions compliance shown by test, and a US service depot. Refurbished units and mixed makes across blocks are a spares and reliability problem. Fuel cells follow load poorly [DK].
  5. Wants a 72-hour test on a load bank with an AI load profile before acceptance.
- **Decision: refuses the standard block as specified; approves the concept.**
- **Would change it:** the five items above.

### P8. Site operations manager
- **Position:** v2 gives a clean boundary. The provider runs the plant; the site takes power at the medium-voltage bus.
- **Decision: accepts, on terms.** No veto.
- **Terms:** provider's crew on site around the clock, about 8-12 people per block [DK]; written interface and switching procedure; black-start drills; fuel-curtailment plan; provider carries noise and permit compliance.
- **Concern:** the startup has no crews, and skilled electrical labour is short [notes]. Oilfield-service providers have them.

## 6. Verdict table

| Persona | Decision | Price and terms they accept |
|---|---|---|
| P1 hyperscaler energy lead | Refuses startup | $38,000-42,000 from a fleet owner |
| P2 colocation head of power | Refuses binding contract; tender only | $38,000-42,000, seven years, delay damages, engines and permit proven |
| P3 neocloud | Signs | $38,000 (up to $45,000-50,000 for 12-month delivery), seven years, escrowed deposit about $50,000 per MW, security at operation, walk right |
| P4 fab or industrial | Refuses | $25,000-30,000, remote sites, from incumbents |
| P5 colocation CFO | Refuses until lenders' engineer approves | $38,000 as tenant pass-through, stepping security, step-in and purchase option |
| P6 hyperscaler procurement | Refuses | None |
| P7 critical facilities VP | Refuses specification, approves concept | 99.99%, backup fuel, proven engine, larger battery power |
| P8 site operations | Accepts on terms | Provider crew on site around the clock |

## 7. Numbers in the brief the panel disputes

| Brief | Corrected | Basis |
|---|---|---|
| $38,000 per MW-month | $45,000-50,000 for a five-year firm term with weak credit; $38,000 is a long-term investment-grade average | [notes]; G6; Solaris arithmetic; [derived] |
| $1.45M per MW including battery and N+2; $36M per block | $1.75-2.0M with high-speed units ($44-50M); $2.3-2.8M with 9.6 MW units ($58-70M) | G2, G4; [derived]; [DK] |
| Payback four to six years | 4.7-8 years at corrected cost, against a five-year firm term | [derived] |
| Delivery 12-15 months from deposit | Unverified. No delivery date found for any non-incumbent order. 18-30 months for a site without gas and a permit; 12-15 only with both in hand and high-speed or refurbished units | G1, G8; [DK] |
| 99.9% availability | Buyers require 99.99% | [DK] |
| Sites of 25-150 MW are underserved | Sizes are served (60 and 80 MW contracts, five-year bridge terms). What is short is supply for weak credit at investment-grade prices | G3, G5 |
| Skid-mounted and redeployable | True of 2.5 MW high-speed sets, which are the incumbents' sold-out product. Not true of medium-speed engines. Recovery on redeployment 55-65% of installed cost | [DK] |
| 55% debt | 40-50% at 11-14% | [DK]; [notes] on credit |
| Damages cap three months | 0.3% of exposed capital; no buyer treats it as protection | [derived] |
| $5-10M covers deposits on two blocks | Deposits alone are $8-12M | [derived]; [DK] |

## 8. Probabilities (panel's honest estimate)

- **First paid commercial delivery within 18 months, this version: 17%** (v1: 12%). A buyer exists and a 25 MW block is small. The limits are an engine slot, a site with gas and a permit, a crew, and a fund willing to take a first block on B-rated credit.
- **$1 billion of annual recognized revenue within seven years: 3%** (v1: 2%). Needs about 2.2 GW operating and $3.2-4.4B of capital, as a late entrant without equipment, against fleet owners with 2 GW or more of unused secured capacity, in a scarcity that may be peaking.

## 9. What the panel did not establish

- Any public per-MW-month price for a short-term gas contract.
- Delivery times or open capacity at Korean, Japanese or second-tier European engine makers.
- Whether fleet owners are actually declining weak-credit 25-150 MW sites, or pricing them higher.
- All persona decisions are simulated. None is evidence of real demand or real refusal.
