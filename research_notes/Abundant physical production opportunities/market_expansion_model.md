# Market-expansion model: one method applied to 19 physical-production candidates (as of 24 Nov 2026)

Reader notes
- Purpose: apply one method to every candidate so they can be compared on the same scale, and step each through 2027-2032 against incumbent, Chinese, regulatory, buyer, complement and cycle responses. This note does not re-research the sectors. It uses the nine first-round files, cited by short tag: HIST (historical_analogs_framework.md), SKEP (skeptic_red_team.md), ENER (energy_grid_hardware.md), AVIA (aviation_space.md), DEFN (defense_maritime_heavy.md), MED (medical_biopharma_hardware.md), ROBO (robots_industrial_machinery.md), CONS (consumer_goods.md), HOUS (housing_buildings.md). Each cited finding gives the file tag and the original source link carried in that file.
- Labels on every number: [M] measured (filings, regulator or trade-body data, reported actuals); [SE] sourced estimate (third-party estimate, forecast, company claim, or a search-summary figure as carried in the first-round notes); [D] derived (my arithmetic on cited figures); [A] my own assumption where no source exists, with basis and a wide range. Every model output is [D] built on a mix of [M], [SE] and [A] inputs. None of the outputs is a fact or a forecast by any third party.
- New fetches for this note (WebSearch was not used): Howmet 2025 revenue (Wikipedia citing the 10-K), US total vehicle sales 2025 (FRED TOTALSA), US total solar installed 2025 (SEIA table on Wikipedia). Fetches that failed and left a labelled estimate in place: SEIA residential data (HTTP 403), a cabinet-market anchor (MasterBrand page had no data), Trench Group revenue (not in the Utility Dive article).
- Arithmetic was run in a script at /tmp/claude-0/-home-user-538model/51eae3c5-b49f-5736-a923-fe31660ffdf0/scratchpad/mem/model.py (Monte Carlo: 20,000 draws per candidate, seed 538 plus the candidate number). All inputs and formulas are restated below, so every deterministic output can be reproduced by hand.
- What the model leaves out: (1) firm-level execution risk (yield, cash, team); the SKEP base rates on capital tiers should be applied on top; (2) margins and profit; outputs are revenue only; (3) share gains from being cheaper than rivals (firm-level elasticity), which is why entrant share is a uniform assumption; (4) interactions between candidates (C4 parts feed C18 drones; C1 parts feed C17 turbines).

## 1. Direct answers to the four key questions

### Takeaway
Existing shortage at today's prices is about $154B a year across all 19 rows [D], but 84% of it sits in three reference rows a new entrant cannot reach by 2032 (airliners, gas turbines, naval ships). Among the shortlisted candidates the near-certain pools are metal parts (about $8.8B a year, open to about 2033), data-center power blocks (about $6B, closing about 2030) and rocket motors and interceptors (about $4B, to about 2031). Under conservative elasticities no candidate reaches a 10x market on price alone: unit gains are 1.0-1.7x, and ten candidates lose revenue when price falls. A 2027-funded entrant reaches volume after most shortage windows have narrowed, so the model's base-case 2032 revenue is $50-300M for the best candidates on $160-770M of capital, or $0.2-0.45 of risk-adjusted revenue per dollar.

### Cited Findings
- Airliner backlog was 16,402 aircraft at end-October 2026, about 11 years of output; supply limits are expected to cost more than 6,000 aircraft through 2030 [M/SE, 2026] — AVIA; [Forecast International](https://flightplan.forecastinternational.com/2026/11/10/airbus-and-boeing-report-october-2026-commercial-aircraft-orders-and-deliveries/); [Oliver Wyman](https://www.oliverwyman.com/our-expertise/insights/2026/feb/global-fleet-and-mro-market-forecast-2026-2036.html)
- Gas turbine orders were about 110 GW at end-2025 against 60-70 GW of manufacturing capacity [SE, 2026] — ENER; [Wood Mackenzie](https://www.woodmac.com/press-releases/gas-turbine-prices-soar-195-as-market-faces-supply-demand-crisis)
- About half of the 12 GW of US data-center capacity planned for 2026 was projected to slip, with transformers, switchgear and batteries the constrained items [SE, 2026] — ENER; [Tom's Hardware via Yahoo](https://finance.yahoo.com/sectors/technology/articles/half-planned-us-data-center-150928890.html)
- Wood Mackenzie put the US power-transformer supply deficit at about 30% in 2025 and a later figure at 7% for 2026, with GSU gaps possibly under 10% by 2030 [SE] — ENER; [POWER Magazine](https://powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/); [VKTR](https://www.vktr.com/ai-technology/ais-data-center-boom-is-deepening-a-transformer-shortage/)
- PAC-3 MSE output is about 550 a year against a 3,203 request; the munitions portfolio plan falls 46% after FY2027 [SE, 2026] — DEFN; [CNAS](https://www.cnas.org/publications/reports/munitions-procurement-and-the-fiscal-year-2027-defense-budget)
- Aerospace castings and forgings take 6 to 18+ months per cycle and rebuilding lost engineering talent may take 5-10 years [SE, 2024] — AVIA and ROBO; [BCG](https://www.bcg.com/publications/2024/fixing-aerospaces-supply-chain-for-casting-and-forging)
- Constant-elasticity arithmetic: a 3x price cut gives 2.1x volume at an elasticity of -0.7 and 3x at -1.0; revenue grows only when elasticity exceeds 1 [D in HIST, section 4, built on its elasticity sources] — HIST; [IATA / InterVISTAS](https://www.iata.org/en/iata-repository/publications/economic-reports/estimating-air-travel-demand-elasticities---by-intervistas/)
- Across US industries, each point of productivity growth brought about 0.75 points more real output (Nordhaus) [SE] — HIST; [Wikipedia, Baumol effect](https://en.wikipedia.org/wiki/Baumol_effect)
- Margins after a cost collapse: China's four largest module makers lost about US$1.54B in H1 2025, while a sole-source certified parts maker (TransDigm) held an EBITDA margin near 54% [M/SE, 2025] — SKEP; [PV Tech](https://www.pv-tech.org/chinas-top-four-solar-manufacturers-suffer-1-54-billion-losses-h1-2025/); [Motley Fool](https://www.fool.com/data-news/2025/08/06/transdigm-tdg-q3-margin-hits-54)

### Inferences
Summary table (all figures [D]; inputs and formulas in sections 2-4; P10/P90 from the Monte Carlo run):

| ID | Candidate | Market today ($B/yr) | Existing shortage ($B/yr) and base close year | Price change by 2032, production only / total | Entrant lead-time change (plausible) | Expanded market multiple (low / base / high) | Entrant 2032 revenue $M (P10 / base / P90) | Capital ($M) | Revenue per $ | Model T score /14 | Type |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | Fast long-lead metal parts | 35 | 8.75 (2033) | -16% / -17% | -75% | 0.82x / 1.10x / 1.43x | 171 / 298 / 548 | 765 | 0.39 | 7 | Shortage play |
| C2 | Data-center / large-load power blocks | 20 | 6 (2030) | -24% / -24% | -73% | 0.77x / 1.13x / 1.87x | 178 / 263 / 522 | 603 | 0.44 | 8 | Shortage play |
| C3 | Scarce HV grid components | 10 | 2 (2030) | -11% / -11% | -65% | 0.82x / 1.10x / 1.43x | 2.3 / 9.4 / 19 | 327 | 0.03 | 5 | Shortage play (closing) |
| C4 | China-free drone/robot components | 1.5 | 0.45 (2030) | -29% / -29% | -84% | 0.93x / 2.55x / 15.28x | 43 / 51 / 153 | 157 | 0.32 | 11 | Protected-market play |
| C5 | Rocket motors, energetics, cheap interceptors | 4 | 4 (2031) | -16% / -16% | -36% | 1.27x / 2.38x / 6.30x | 66 / 92 / 221 | 312 | 0.29 | 9 | Shortage play inside a protected market |
| C6 | Satellite buses and space components | 12 | 0.6 (2029) | -13% / -13% | -50% | 0.88x / 1.17x / 1.94x | 54 / 82 / 181 | 335 | 0.25 | 8 | Protected-market play (government anchor) |
| C7 | Delivery-drone airframes | 0.06 | 0.1 (2029) | -18% / -18% | n/a | 1.40x / 8.21x / 55.34x | 0.4 / 0.5 / 2.0 | 101 | 0.01 | 8 | Neither yet (captive, regulation-gated) |
| C8 | Productized home solar + battery | 13 | none measured | -1% / -26% | no change | 0.75x / 1.15x / 2.42x | 41 / 64 / 126 | 407 | 0.16 | 9 | Neither by production (process play on elastic demand) |
| C9 | Factory-built housing (ADU, HUD infill, pods) | 18 | none measured | -8% / -22% | -9% | 0.73x / 0.99x / 2.17x | 21 / 33 / 67 | 150 | 0.22 | 3 | Neither (land, zoning, finance) |
| C10 | Automated cell-therapy manufacturing | 1.6 | 0.48 (2031) | -6% / -6% | -10% | 1.00x / 2.38x / 11.77x | 1.6 / 6.6 / 13 | 516 | 0.01 | 8 | Shortage play (capacity rationing) |
| C11 | Cash-pay scan / diagnostic clinics | 0.3 | 0.1 (2029) | -1% / -21% | n/a | 0.98x / 3.31x / 22.13x | 14 / 18 / 51 | 148 | 0.12 | 10 | Neither by production (new cash-pay service) |
| C12 | Affordable vehicles + MOSAIC aircraft | 45 | 0.4 (2029) | -4% / -20% | n/a | 0.54x / 0.91x / 1.18x | 10.0 / 38 / 84 | 1,554 | 0.02 | 2 | Neither (protected-market dependent) |
| C13 | Short-lead kitchens/cabinets, installed products | 25 | none measured | -8% / -22% | -50% | 0.77x / 0.96x / 1.35x | 39 / 68 / 138 | 158 | 0.43 | 5 | Neither (channel and lead-time play) |
| C14 | Humanoid robots and robotaxi vehicles | 2.1 | 0.4 (2031) | -30% / -30% | n/a | 1.05x / 2.47x / 21.73x | 0.6 / 0.6 / 2.4 | 1,504 | 0.00 | 10 | Model T on paper; capability-gated |
| C15 | Commercial airliners and jet engines (ref) | 120 | 95 (2033) | -6% / -6% | n/a | 1.34x / 1.71x / 1.98x | 0.0 / 0.0 / 0.0 | 20,000 | 0.00 | 6 | Shortage, closed to entrants |
| C16 | Commercial and naval ships (ref) | 48.4 | 14 (2035) | -4% / -4% | -20% | 1.05x / 1.28x / 1.72x | 24 / 92 / 187 | 1,674 | 0.05 | 3 | Protected-market play with shortage |
| C17 | Gas turbines and microreactors (ref) | 50 | 20 (2033) | -14% / -14% | -71% | 0.89x / 1.27x / 1.66x | 6.5 / 9.8 / 18 | 535 | 0.02 | 6 | Shortage play (upstream-gated) |
| C18 | Low-cost cruise missiles, attritable drones (ref) | 5 | 2 (2031) | -15% / -15% | -76% | 1.08x / 1.98x / 8.12x | 120 / 152 / 390 | 682 | 0.22 | 9 | Closest true Model T case, inside a protected monopsony |
| C19 | Medical devices for emerging markets (ref) | 5 | none measured | -1% / -30% | n/a | 0.43x / 1.00x / 6.10x | 0.6 / 1.4 / 5.5 | 33 | 0.04 | 6 | Neither (delivery-gated) |

- Key question 1, largest near-certain demand and window. Ranked by existing shortage at today's prices: airliners about $95B a year (to about 2033), gas turbines about $20B (about 2033), naval ships about $14B (about 2035), metal parts about $8.8B (about 2033), data-center power blocks about $6B (about 2030), rocket motors and interceptors about $4B (about 2031), HV grid components about $2B (about 2030). The first three need 4-8+ years and $0.5-20B before first revenue, so their shortage is real but not obtainable by a 2027 entrant. For the obtainable ones, the entrant's volume year falls after most of the shortage dollars have gone: 13% of 2027-2032 shortage dollars remain at or after the volume year for C1, 0% for C2, C3 and C5 (section 3, shortage-window table). Speed to first shipment decides whether this demand is reachable at all.
- Key question 2, true price-elastic latent demand. Nine candidates have a base elasticity of 1 or more (C4, C5, C6, C7, C8, C10, C11, C14, C18). At the plausible 2032 price change their unit volumes rise 1.06-1.71x, and the elastic gain in dollars is under $0.5B a year for every one of them. The 2.5x to 20x+ outcomes in the high cases come from new uses that do not exist at scale today (C4, C7, C10, C11, C14, C18), not from sliding down today's demand curve. Ten candidates (C1, C2, C3, C9, C12, C13, C15, C16, C17, C19) see served-market revenue fall when price falls, because elasticity is below 1.
- Key question 3, where the saving flows. Production abundance can touch 50-75% of delivered price in C1-C5, C10, C14, C15 and C17, 26-40% in C6, C7, C9, C13, C16 and C18, and 3-20% in C8, C11, C12 and C19. Where it can touch the price, the saving goes to the entrant only while a shortage or a legal wall lasts, then to buyers; where it cannot, the money sits with installers, channels, licence holders, lenders and land (section 6).
- Key question 4, risk-adjusted 2032 revenue per dollar of capital. Base case: C2 0.44, C13 0.43, C1 0.39, C4 0.32, C5 0.29, C6 0.25, C18 0.22, C9 0.22, C8 0.16, C11 0.12; all others 0.05 or less. C13 and C9 rank high only because little capital is at stake and their market-size inputs are my own estimates; in absolute revenue they are small ($68M and $33M).

### Gaps
- No first-round file gives a sourced cost stack for C1, C4, C5, C6, C7, C11, C13, C15 or C18, or a sourced market total for C1, C3, C4, C7, C11, C13 or C19. Those rows rest on [A] inputs with wide ranges and should be read as order-of-magnitude.
- The model gives revenue, not profit. It cannot say which candidate earns the best margin; section 6 gives the qualitative evidence.

## 2. Data table: market today, price, lead time, cost stack, touchable share, and the 2032 price and lead-time change from production abundance alone

### Takeaway
Production abundance alone lowers delivered price by 1-30% by 2032 in the plausible case and 1-45% in the aggressive case; nowhere does it approach 3x. The largest plausible cuts are in new, small, frozen-design goods (humanoids and robotaxis -30%, China-free components -29%) and where a scarcity margin can be competed away (data-center power blocks -24%). Entrant lead times fall much more than prices: 65-85% in C1-C4, C17 and C18, where most of today's lead time is queue.

### Cited Findings
Per-candidate inputs (market, price, lead time, cost-stack evidence). Years are in brackets.
- **C1 metal parts.** Howmet revenue US$8.25B and net income US$1.51B [M, 2025] — fetched: [Wikipedia, Howmet Aerospace](https://en.wikipedia.org/wiki/Howmet_Aerospace). Howmet says it has over 50% of the global gas-turbine airfoil market [SE, snippet] — AVIA; [Bloomberg via Tiger](https://www.itiger.com/news/2650735186). US metalcasting is a $52B industry across all end markets [SE, undated] — ROBO; [American Foundry Society](https://www.afsinc.org/industry-statistics). Xometry 9-month 2026 revenue $686.9M and Protolabs Q3 2026 revenue $154.3M with 44.5% gross margin; Xometry marketplace gross margin 36.0% [M, 2026] — ROBO; [Xometry](https://finviz.com/news/414090/xometry-reports-record-third-quarter-2026-results); [Protolabs](https://finviz.com/news/411151/protolabs-reports-financial-results-for-the-third-quarter-of-2026). Lead times 6 to 18+ months, one alloy 70-80 weeks; suppliers prefer margin to new capacity [SE, 2024] — AVIA; [BCG](https://www.bcg.com/publications/2024/fixing-aerospaces-supply-chain-for-casting-and-forging). Parts and materials are about 60% of engine overhaul direct cost [SE] — AVIA; [Airways](https://airwaysmag.com/new-post/airline-engine-bills-rise-groundings-ease). No sourced cost split exists for castings or machined parts (ROBO gap).
- **C2 data-center power blocks.** US data-center electrical equipment about $20B now, forecast about $65B by 2030; equipment lead times 18-36 months [SE, 2026] — ENER; [E&E News](https://www.eenews.net/articles/data-centers-to-triple-us-power-equipment-market-to-65b/). MV switchgear 52-80 weeks (2026 project data) — ENER; [Foley](https://www.foley.com/insights/publications/2026/09/the-grids-bottleneck-isnt-just-money-its-materials/). Standard substation units deliverable in 12-14 months when the spec is standard; MV switchgear prices +50%; brokers add 12-15% [SE] — ENER; [POWER Magazine](https://powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/). Transformer cost model: materials about 40% of cost, labor about 25%, capex about 25% [SE, analyst model] — ENER; [Thunder Said Energy](https://thundersaidenergy.com/downloads/transformers-companies-and-costs/). Margins about 20% of unit cost, up about 4-5x since 2020 [SE, 2024] — ENER; [Wood Mackenzie](https://www.woodmac.com/news/opinion/4-years-into-a-difficult-transformers-market-in-the-us-is-there-a-potential-end-in-sight/). Electrical gear is under 10% of data-center cost [SE] — ENER; [Tom's Hardware via Yahoo](https://finance.yahoo.com/sectors/technology/articles/half-planned-us-data-center-150928890.html).
- **C3 HV grid components.** GE Vernova is buying Trench Group for $9B with about $5B of backlog and framework agreements; no revenue disclosed [M, 2026] — ENER and fetched; [Utility Dive](https://www.utilitydive.com/news/ge-vernova-in-9b-deal-to-buy-high-voltage-manufacturer-as-gas-turbine-orde/873223/). EIA line-transformer investment $7.5B and distribution-substation equipment $6.1B [M, 2023]; transmission investment $39.9B [SE, 2025 projection] — ENER; [Foley](https://www.foley.com/insights/publications/2026/09/the-grids-bottleneck-isnt-just-money-its-materials/). Power transformers 128 weeks, GSUs 144 weeks [SE, Q2 2025]; prices since 2019: power transformers +77%, breakers +47% since 2021 — ENER; [POWER Magazine](https://powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/). HV breakers about 125 weeks [SE, snippet, H2 2025] — ENER; [Environment+Energy Leader](https://environmentenergyleader.com/stories/grid-equipment-bottleneck-isnt-just-a-data-center-problem,134481). No verified market total for transformers or breakers (ENER gap).
- **C4 China-free components.** Gauntlet I placed 22,320 one-way drone orders at $5,000; by 25 Aug 2026 about 60% had arrived; Neros builds about 1,200 a week; Phase 3 is $450M for about 60,000 drones [M/SE, 2026] — DEFN; [DroneXL](https://dronexl.co/2026/09/30/neros-gauntlet-ii-100-million-order-800-bonus-drones/). Target price $2,000 over the program's life [SE] — DEFN; [Breaking Defense](https://breakingdefense.com/2026/03/drone-dominance-pentagon-to-order-30000-one-way-drones-in-next-few-days/). Actuators are 40-60% of a humanoid bill of materials; non-China BOM about $131k [SE] — ROBO; [Humanoid.guide](https://humanoid.guide/the-humanoid-robot-supply-chain/). Unitree humanoid ASP about $24-25k at about 63% gross margin [M, 9M 2025] — ROBO; [KrASIA](https://kr-asia.com/what-is-the-secret-behind-unitrees-high-gross-margins). Ukraine signed about $8B of drone contracts in H1 2026 [SE] — DEFN; [Euromaidan Press](https://euromaidanpress.com/2026/10/11/ukraine-ordered-54-more-fpv-attack-drones-this-year-than-in-all-of-2025-and-deliveries-jumped-almost-fourfold/). No source gives the component share of a drone's price.
- **C5 rocket motors, energetics, interceptors.** Munitions procurement $24.4B in FY2026 and about $70.5B requested for FY2027 [M/SE] — DEFN; [Breaking Defense](https://breakingdefense.com/2026/04/the-pentagon-wants-a-188-percent-bump-for-missile-procurement-can-industry-deliver/). PAC-3 MSE about $4.3M per round [D in DEFN from CRS] — DEFN; [CRS R49023](https://www.everycrsreport.com/reports/R49023.html). Request-to-first-delivery 36-64 months, 72.5% of it award-to-delivery [SE] — DEFN; [CNAS](https://www.cnas.org/publications/reports/munitions-procurement-and-the-fiscal-year-2027-defense-budget). Army bought 13,000 Merops interceptors at about $15,000; Perennial ceiling $500M over three years [SE, 2026] — DEFN; [DefenseScoop](https://defensescoop.com/2026/05/19/pentagon-awards-500-million-contract-to-perennial-autonomy-for-counter-drone-systems/). NATO allies committed over $40B to counter-drone capability over five years [SE, 2026] — DEFN; [Startup Fortune](https://startupfortune.com/european-drone-startups-are-raising-billions-while-the-old-defense-giants-scramble-to-keep-up/). No source gives the motor share of missile cost.
- **C6 satellite buses.** Satellite manufacturing revenue $20.4B [M, 2025] — AVIA; [SIA](https://sia.org/affordability-productivity-drive-historic-satellite-industry-growth-satellite-industry-association-releases-29th-annual-state-of-the-satellite-industry-report/). Commercial demand outside Starlink about $8B with limited near-term growth; Apex Aries $3.5-5.7M, bus in as little as six months (claim); Apex 2025 revenue $60M [SE] — AVIA; [Contrary Research](https://research.contrary.com/company/apex). 4,544 spacecraft deployed in 2025, 85% carried by SpaceX [M] — AVIA; [BryceTech via Via Satellite](https://www.satellitetoday.com/launch/2026/04/10/brycetech-report-shows-spacex-accounted-for-50-of-launches-in-2025). SDA tracking satellites about $42-61M each [D in AVIA] — AVIA; [NewSpace Economy](https://newspaceeconomy.ca/2026/04/13/the-satellite-manufacturing-market-after-starlink-how-mass-production-changed-the-economics-of-building-spacecraft/).
- **C7 delivery drones.** Walmart passed 1 million US drone deliveries on 29 May 2026 from 66 stores, 40% in one quarter [M] — AVIA; [DroneXL](https://dronexl.co/2026/05/31/walmart-1m-drone-deliveries-40/). Walmart and Zipline agreed to add 300 sites [SE, Nov 2026] — AVIA; [Supermarket News](https://www.supermarketnews.com/grocery-technology/walmart-zipline-reach-agreement-to-add-300-drone-delivery-sites). Part 108 final rule was still at OIRA in mid-November 2026 [M] — AVIA; [UAV Coach](https://uavcoach.com/part-108-stuck/). No unit cost for a delivery drone was found (AVIA gap); the $40k used here is [A].
- **C8 home solar plus battery.** US residential price $2.53/W vs Australia $0.82/W (IEA 2023); EnergySage 2025 US $2.77/W = $0.94 hardware + $1.83 soft; marketing 20-29% of price; US wholesale panels $0.12-0.18/W; Australia order within a week and one-day install; penetration 33% of Australian homes vs 7% of US homes [SE] — CONS; [Boston University](https://www.bu.edu/eci/files/2025/07/Intnatl-Cost-Comparisons-final.pdf). US total solar installed 43,200 MWdc [M, 2025, SEIA table] — fetched: [Wikipedia, Solar power in the United States](https://en.wikipedia.org/wiki/Solar_power_in_the_United_States). Base Power raised two $1B rounds [SE] — ENER; [Energy-Storage.news](https://www.energy-storage.news/base-power-raises-another-us1-billion-in-series-d-financing-for-us-residential-bess/). Annual US residential installs were not retrievable; the 4.5-5 GWdc used is unverified recollection.
- **C9 factory-built housing.** 102,737 HUD-code shipments in 2025; Q1 2026 down 9.0% [M] — HOUS; [MHI](https://www.manufacturedhousing.org/wp-content/uploads/2026/05/MHI-Economic-Report-March-2026.pdf). Average new manufactured home price $131,500 [M, Oct 2025] — HOUS; [FRED SPTNSAUS](https://fred.stlouisfed.org/series/SPTNSAUS). California issued 30,231 ADU permits in 2024 [SE] — HOUS; [California Insider](https://californiainsider.com/california-news/business/real-estate/inside-the-backyard-housing-boom-in-california-5900675). California median ADU cost $150,000 [SE, 2021 survey] — HOUS; [Terner Center](https://ternercenter.berkeley.edu/blog/cci-adu-survey). Construction is 64.4% of a new home's price, lot 13.7%, profit 11.0% [SE, NAHB 2024] — HOUS; [NAHB](https://eyeonhousing.org/2025/01/cost-of-constructing-a-home-in-2024/). Direct labor is about half of construction cost; prefab savings historically 0-20% [SE] — HOUS; [Construction Physics](https://www.construction-physics.com/p/the-elusive-cost-savings-of-the-prefabricated). Cavco backlog $195M and average revenue per home $103,510 [M, FY2026] — HOUS; [Cavco 8-K](https://www.sec.gov/Archives/edgar/data/0000278166/000162828026037575/cvco-2026328xex991.htm).
- **C10 cell-therapy manufacturing.** CAR-T market about $5.21B [SE, 2025]; COGS estimates $35,000-$220,000 per batch; labor about 71% of batch cost; a facility model found full automation cut cost about 9% [SE] — MED; [IntuitionLabs](https://intuitionlabs.ai/articles/car-t-manufacturing-economics-cogs). List prices $462,000-$594,000; vein-to-vein 30.6-48.4 days commercial vs 9-15 days point-of-care; release tests 14-28 days vs hours [SE, 2025-26] — MED; [BioProcess Online](https://www.bioprocessonline.com/doc/closing-the-car-t-access-gap-with-hospital-based-manufacturing-0001).
- **C11 scan clinics.** Prenuvo about $100M revenue for 2024 at $2,499 a scan (company statement) — MED; [Radiology Business](https://radiologybusiness.com/topics/healthcare-management/healthcare-economics/whole-body-mri-startup-prenuvos-recent-milestone-would-mark-250m-revenue). Neko: over 100,000 scans, over 350,000 on the waitlist, 75% prepay the next scan [SE, 2026] — MED; [HIT Consultant](https://hitconsultant.net/2026/07/15/neko-health-raises-700-million-series-c/). Neko US price $499 [M] — MED; [eWeek](https://www.eweek.com/news/neko-health-us-body-scan/).
- **C12 affordable vehicles and MOSAIC aircraft.** Average US new-vehicle transaction price $51,109 [M, Oct 2026] — CONS; [Cox Automotive](https://www.coxautoinc.com/insights/oct-2026-atp-report/). US total vehicle sales averaged a 16.68M annual rate in 2025 [M, includes heavy trucks] — fetched: [FRED TOTALSA](https://fred.stlouisfed.org/data/TOTALSA.txt). Slate $24,950, about $1.5B raised, break-even about 80,000 a year (claim) — CONS; [The Next Web](https://thenextweb.com/news/slate-auto-ev-pickup-24950-preorders-bezos-production). Dealer gross per new vehicle $2,564 on $52,075 [M, 2025] — CONS; [Dealership Guy](https://news.dealershipguy.com/p/new-car-boom-used-car-squeeze-and-the-future-of-fixed-ops-2025-01-30). Honda N-One about $11,390 in Japan — CONS; [The Autopian](https://www.theautopian.com/president-trump-said-he-just-legalized-cheaper-smaller-cute-kei-cars-in-america/). GM Bolt relaunched under $30,000 — CONS; [Wikipedia, Chevrolet Bolt](https://en.wikipedia.org/wiki/Chevrolet_Bolt). 1,782 piston airplanes shipped worldwide [M, 2025] — AVIA; [GAMA](https://gama.aero/news-and-events/press-releases/gama-releases-2025-aircraft-shipment-and-billing-report/).
- **C13 kitchens and cabinets.** US kitchen and bath market about $228B [SE, 2026 forecast] — CONS; [NKBA](https://nkba.org/research/2026-kitchen-bath-industry-outlook/). Custom cabinets $25,000-$60,000+ per kitchen [low-grade cost guide] — CONS; [Angi](https://www.angi.com/articles/custom-cabinets-cost.htm). Installation about $6,400 [low-grade] — CONS; [HomeAdvisor](https://www.homeadvisor.com/cost/cabinets-and-countertops/install-cabinets/). Lead times 6-8 weeks semi-custom and 8-16 weeks custom; each channel layer adds 15-30% (claim by an interested seller) — CONS; [Quik Cabinets](https://quikcabinets.com/blogs/kitchen-remodeling-guides/kitchen-cabinet-costs-in-2026-complete-price-guide). No cabinet market size was sourced.
- **C14 humanoids and robotaxis.** Humanoid shipments forecast above 50,000 for 2026 [SE] — ROBO; [Counterpoint](https://counterpointresearch.com/en/insights/global-humanoid-robot-shipments-soar-nearly-300-percent-yoy-in-h1-2026). Unitree humanoid ASP RMB 167,600 (about $24-25k) [M, 9M 2025] — ROBO; [The Robot Report](https://www.therobotreport.com/unitree-ipo-shows-a-real-hardware-business-the-humanoid-case-is-still-early/). Waymo 3,871 robotaxis and about 500,000 paid rides a week [M, 2026] — ROBO; [Wikipedia, Waymo](https://en.wikipedia.org/wiki/Waymo). Pony.ai robotaxi cost below RMB 230,000 (about $33.7k) (company claim) — ROBO; [Caixin](https://www.caixinglobal.com/2026-05-04/chinese-robotaxi-firms-race-to-cut-costs-as-profitability-remains-out-of-reach-102440604.html).
- **C15 airliners (reference).** Annual new aircraft deliveries about US$120B [SE, snippet, 2026] — AVIA; [Avolon](https://avolon.aero/news/avolon-2026-outlook-up-next). Backlog 16,402; 1,145 deliveries Jan-Oct 2026 [M] — AVIA; [Forecast International](https://flightplan.forecastinternational.com/2026/11/10/airbus-and-boeing-report-october-2026-commercial-aircraft-orders-and-deliveries/). CSeries sold at $19.6M against $33.2M production cost (trade petition) — AVIA; [Wikipedia, Airbus A220](https://en.wikipedia.org/wiki/Airbus_A220).
- **C16 ships (reference).** FY2026 Navy shipbuilding request about $47.4B for 19 ships; shipyard labor about 40% of a military ship's cost [M/SE] — DEFN; [CRS RL32665](https://www.everycrsreport.com/reports/RL32665.html). Destroyers and submarines take 9-10 years to build vs 5-6 in the 2000s [SE, 2026] — DEFN; [CBO testimony](https://armedservices.house.gov/UploadedFiles/2026-04-22_Labs_Testimony.pdf). MR tanker over $220M in Philadelphia vs about $47M in Asia [SE, 2025] — DEFN; [WSJ via To Vima](https://www.tovima.com/wsj/south-korea-promises-it-will-rekindle-u-s-shipbuilding-thats-still-far-off/). Medium unmanned surface vessel about $40M per hull [SE] — DEFN; [Maritime Executive](https://maritime-executive.com/article/u-s-navy-takes-first-big-unmanned-step-buying-30-production-musv-hulls).
- **C17 gas turbines and microreactors (reference).** 846 turbines and 100.3 GW ordered worldwide in 2025; large units take more than five years, smaller 18-36 months [M/SE] — ENER; [EPRI author in Utility Dive](https://www.utilitydive.com/news/5-year-waits-and-rising-costs-how-demand-is-redefining-the-gas-turbine-mar/). Turbine price expected to reach $600/kW by end-2027, +195% vs 2019 [SE] — ENER; [Wood Mackenzie](https://www.woodmac.com/press-releases/gas-turbine-prices-soar-195-as-market-faces-supply-demand-crisis). Radiant's Army contract is up to $750M for 15 one-MW reactors [SE, 2026] — ENER; [EnergyTech](https://www.energytech.com/next-gen-nuclear/news/55401307/energy-in-a-box-nuclear-startup-radiant-secures-750m-contract-to-deploy-15-portable-microreactors-across-us-army-bases).
- **C18 low-cost cruise missiles and attritable drones (reference).** FAMM $0.35B for 1,000 units in the FY2027 request [M] — DEFN; [CRS R49023](https://www.everycrsreport.com/reports/R49023.html). Collaborative Combat Aircraft FY2027 procurement request $996.5M plus $150M advance procurement [SE] — DEFN; [Air & Space Forces Magazine](https://www.airandspaceforces.com/cca-builders-rev-production-await-2027-budget/). Air Force plans nearly 28,000 low-cost cruise missiles over five years [SE] — DEFN; [TWZ](https://www.twz.com/air/usaf-plans-to-buy-28000-low-cost-cruise-missiles-in-five-years-advance-with-new-deals). Army-led program aims for at least 10,000 within three years on firm-fixed-price contracts with minimum floors [SE] — DEFN; [DefenseScoop](https://defensescoop.com/2026/05/15/defense-department-low-cost-containerized-missile-contracts/).
- **C19 medical devices for emerging markets (reference).** Hearing aids cost about $150 to make (older CBC figure) against a prescription average above $2,600 per pair — MED; [CBC](https://amp.cbc.ca/lite/story/1.1367189); [Capitol Forum](https://thecapitolforum.com/four-years-after-otc-hearing-aid-rule-competition-in-hearing-aid-market-remains-limited/). Aurolab intraocular lens about US$2 vs $50-100+ imported [SE] — MED; [Community Eye Health Journal](https://cehjournal.org/?p=1715). United Imaging revenue about RMB 13.8B [SE, 2025] — MED; [PR Newswire Asia](https://en.prnasia.com/releases/global/united-imaging-healthcare-releases-2025-annual-report-and-q1-2026-results-delivering-strong-growth-with-accelerated-global-expansion-531290.shtml). No sector market total was sourced (MED gap).

Evidence behind the uniform cost-cut classes
- Learning rates cluster at 15-25% per doubling for small, modular, standardised factory goods (solar modules 20.2%, batteries about 19%, Model T 15%) and near zero for large, site-built, customised or regulated systems [SE] — HIST; [Our World in Data](https://ourworldindata.org/cheap-renewables-growth); [Construction Physics](https://www.construction-physics.com/p/where-are-my-damn-learning-curves)
- WWII: B-17 labor-hours fell about 7x while average aircraft cost fell 32%; Liberty ship build time fell from about 230 days to a median 39 days [SE] — HIST; [Construction Physics, airplanes](https://www.construction-physics.com/p/how-to-build-300000-airplanes-in); [Wikipedia, Liberty ship](https://en.wikipedia.org/wiki/Liberty_ship)
- Direct labor is about 10-12% of manufacturing cost for cars [SE] — HOUS; [Construction Physics](https://www.construction-physics.com/p/the-elusive-cost-savings-of-the-prefabricated)

### Inferences
Table 2a. Market, price and lead time today (hand-assembled from the findings above; label and year in brackets).

| ID | Product and unit | Served market today ($ a year) | Units today | Price today | Lead time today |
|---|---|---|---|---|---|
| C1 | Castings, forgings, turbine and engine parts, precision machined parts; counted in $ because part numbers vary too much for a unit | About $35B, range $20-52B [A, 2025-26]: long-lead aerospace, defense and energy metal parts outside China. Anchors: Howmet $8.25B [M, 2025] with over half of gas-turbine airfoils [SE]; US metalcasting $52B, all end markets [SE]; Xometry plus Protolabs about $1.5B [D, 2026] | n/a | No unit price; a CFM56-5B overhaul can exceed $10M, about 60% of it parts [SE] | 6 to 18+ months per cycle [SE, 2024]; model uses 12 |
| C2 | MV switchgear, pad-mount and medium power transformers, modular power skids; unit is MW of connected load | $20B [SE, 2026]; forecast $65B by 2030 | About 12,000 MW of US data-center capacity planned for 2026 [SE] | About $1.7M per MW [D: $20B / 12 GW, crude] | 18-36 months [SE, 2026]; standard units 12-14 months without the queue; model uses 24 |
| C3 | Bushings, HV breakers, instrument transformers, large power transformers and GSUs; counted in $ | About $10B US, range $6-15B [A]. Anchors: Trench priced at $9B with $5B backlog [M, 2026]; EIA substation equipment $6.1B and line transformers $7.5B [M, 2023] | n/a (plant benchmark: 57 large units a year per $150M plant [SE]) | Large units $2-7.5M each (unverified recollection in ENER); prices +77% since 2019 [SE] | 128 weeks power transformers, 144-160+ weeks GSUs, about 125 weeks HV breakers [SE, 2025-26]; model uses 30 months |
| C4 | Motors, actuators, magnets, batteries and electronics that pass US origin rules; unit is the component set for one small drone | About $1.5B, range $0.7-3B [A, 2026]. Build-up: US small-drone buys about $0.66B+ ($112M + $100M+ + $450M) × 60% component share = $0.4B; Western humanoid makers $0.2-0.4B; allied non-Chinese sourcing about $0.8B (10% of a 50% component share of Ukraine's about $16B a year) | About 80,000 drone-sets a year in the US [D/A] | About $3,000 per set [A: 60% of the $5,000 contract price] | About 5 months: 60% of Gauntlet I delivered five months after award [M] |
| C5 | Tactical solid rocket motors, energetics, low-cost interceptors and counter-drone effectors; counted in $ | About $4B, range $2.5-7B [A]. Build-up: 10% motor and energetics content [A] of $24.4B munitions [M, FY2026] = $2.4B; US counter-drone effectors about $0.4B [D]; allied effectors about $1.2B [A: 15% of NATO's $8B a year pledge] | PAC-3 MSE about 550 a year; 13,000 Merops bought [SE] | PAC-3 MSE about $4.3M [D]; Merops about $15,000 [SE] | 36-64 months request to first delivery [SE]; model uses 36 |
| C6 | Merchant satellite buses and components; unit is a satellite | $12B contestable, range $8-20.4B [D/A]: $8B non-Starlink commercial [SE, 2025] plus about $4B US defense proliferated [A]. Total manufacturing revenue $20.4B [M, 2025] | About 1,500 non-Starlink satellites a year [A] | Bus $3.5-5.7M; SDA tracking satellites $42-61M [SE/D] | Six months claimed for a small bus, 15 months GEO; model uses 12 |
| C7 | Delivery aircraft under 55 lb; unit is an aircraft | About $0.06B, range $0.02-0.15B [A]: about 1,500 aircraft × about $40k | About 1,500 a year [A] | About $40k [A, range $20-80k, unsourced] | Not lead-time constrained; gated by Part 108 |
| C8 | Installed rooftop solar plus battery, or battery as a service; unit is a home system | About $13B, range $9-17B [A/D]: 4.5-5 GWdc residential (unverified recollection, about 10% of the 43.2 GWdc US total [M, 2025]) × $2.77/W [SE] | About 550,000 systems a year [A] | $2.53-2.77/W, about $25-28k for 10 kW [SE]; Australia $0.82/W | About 3 months order to switch-on [A, unsourced]; Australia one week plus a one-day install [SE] |
| C9 | HUD-code homes, backyard units and pods; unit is a home | $18B, range $14-22B [D]: 102,737 × $131,500 = $13.5B [M, 2025] plus 30,231 × $150,000 = $4.5B [SE, 2024] | 132,968 a year | $131,500 average manufactured home; about $87 vs $166 per sq ft site-built [SE] | Factory backlog 5-6 weeks [D in HOUS]; backyard unit about 8 months on site (anecdote); model uses 8 |
| C10 | Manufacturing capacity for autologous cell therapy doses; unit is a dose | $1.6B of manufacturing spend, range $1.0-2.3B [D]: $5.21B product market [SE, 2025] / about $500k list = about 10,400 doses × about $150k COGS | About 10,400 doses a year [D] | List $462-594k; COGS $35-220k; model uses $150k [A] | 30.6-48.4 days vein-to-vein [SE]; model uses 40 days |
| C11 | Cash-pay preventive scans in owned clinics; unit is a scan | About $0.3B, range $0.15-0.6B [A]: Prenuvo about $100M [SE, 2024] plus Neko and unsourced others | About 150,000 scans a year [A] | $2,499 (Prenuvo MRI) vs $499 (Neko) [M] | Waitlist over 350,000 (Neko) [SE] |
| C12 | Sub-$25k car or truck, microcar, MOSAIC light aircraft; unit is a vehicle | Contestable low-price segment about $45B, range $25-80B [A: about 10% of units at about $27k]. Whole US market about $852B [D: 16.68M × $51,109] | About 1.6M in the segment [A]; 1,782 piston aircraft worldwide [M, 2025] | $51,109 average [M]; Slate $24,950; new Cessna 172 about $420-520k [SE] | Not lead-time constrained |
| C13 | Made-to-order cabinets, kitchens and fitted products, delivered and installed; counted in $ | About $25B, range $15-40B [A]: about 10% of the $228B kitchen and bath market [SE, 2026]; the share is my assumption | n/a | $25,000-60,000 per custom kitchen plus about $6,400 install [low-grade SE] | 8-16 weeks custom [SE]; model uses 12 weeks |
| C14 | Humanoid robots and purpose-built robotaxis; unit is a robot or vehicle | About $2.1B, range $1.2-3.5B [D/A]: about 55,000 humanoids × about $25k plus about 4,000 robotaxi vehicles × $34-120k | About 60,000 a year | Humanoid about $24k (Unitree) to $55-131k Western BOM; robotaxi $34k (China) to $100-150k (Waymo estimate) [SE] | Not lead-time constrained; capability- and rule-gated |
| C15 | Airliners and engines (reference); unit is an aircraft | About $120B [SE, 2026] | About 1,450 a year | About $80M average [D in AVIA] | About 11 years of backlog [M] |
| C16 | Naval and Jones Act ships (reference); unit is a ship | $48.4B [D]: $47.4B Navy request [M, FY2026] plus about $1B Jones Act [A: 5 ships × $220M] | 19 naval plus about 5 commercial | Destroyer $3.28B; unmanned vessel about $40M; tanker $220M US vs $47M Asia [SE] | 9-10 years naval [SE]; model uses 108 months |
| C17 | Gas turbines and microreactors (reference); unit is a turbine | About $50B of orders, range $35-60B [D]: 100.3 GW [M, 2025] × about $500/kW [A, on the way to $600/kW by end-2027] | 846 turbines [M, 2025] | About $500-600/kW equipment; first microreactors about $50,000/kW [D in ENER] | 5-7 years heavy-duty; model uses 66 months |
| C18 | Low-cost cruise missiles, one-way drones, attritable aircraft (reference); unit is a munition | About $5B, range $3-8B [A]: US about $2B (FAMM $0.35B, drones about $0.66B, CCA about $1.0B) plus accessible Europe about $3B. Ukraine's about $16B a year is noted, not counted | About 81,000 in the US [D/A] vs over 4M drones in Ukraine [SE, 2025] | FAMM about $350k; one-way drone $5,000; Tomahawk about $5.3M [D in DEFN] | Months; model uses 5 |
| C19 | Hearing aids, lenses, prostheses and low-cost imaging for low- and middle-income markets (reference); counted in $ | About $5B, range $2-10B [A]; no sector total in the notes | n/a | Lens about $2 vs $50-100; hearing aid about $150 to make vs about $2,400 retail per aid [SE] | Not lead-time constrained |

Uniform method for the price change (applied to every row)
- Split delivered price into materials floor M, conversion C (labor, energy, capital, factory overhead along the chain) and non-production N (certification, channel, installation, land, brand, normal and scarcity margin). R is the part of N that is scarcity rent. M + C + N = 100%.
- Conversion-cost cut by 2032 depends only on product class (low / base / high), from the learning-rate and WWII evidence above [A on the exact values]: A_new (small, shippable, frozen design, thousands to millions of units, little cumulative volume: about three doublings at 20%) 30% / 50% / 65%; A_mat (same architecture but mature, under one doubling left, gain mainly from automating the remaining 10-12% labor) 10% / 20% / 35%; B (platform or mass-customised factory goods, some per-customer engineering or frozen qualified process) 15% / 30% / 45%; C (large, complex, customised or batch-of-one, certification-bound) 0% / 10% / 25%.
- Plausible production-only price change = C × base cut + R × e_pl, where e is the share of the scarcity rent that added capacity erodes by 2032 (candidate-specific, from the incumbent-capacity evidence in section 4). Aggressive = C × high cut + R × e_ag + 10% × M (the last term allows for labor removed upstream inside "materials").
- A separate column shows a non-production lever (design-for-cost, channel removal, process) where the business itself rests on one. It is not production abundance and is kept apart: C8 -25% plausible ([D] from Tesla's stated path: ($0.57 + $0.67) of about $4.80/W, CONS; [Latitude Media](https://www.latitudemedia.com/news/can-the-us-bring-solar-installation-to-below-2-per-watt/)) and -60% aggressive (toward Australia's $0.82 vs $2.53); C9 -15% / -25% (chassis removal $5-10k and direct sale; HOUS judges 20-35% total realistic for the best wedges); C11 -20% / -40% [A, no source]; C12 -17% / -55% ([D]: Slate $24,950 vs Bolt under $30,000; kei-class $11,390 vs $24,950); C13 -15% / -30% (one or two channel layers); C19 -30% / -60% [A].

Table 2b. Cost stack, touchable share and derived price change (script output; arithmetic shown in the cells).

| ID | Candidate | Materials M | Conversion C | Non-production N (of which scarcity rent R) | Touchable share C+R | Class | Conversion cut by 2032 (low/base/high) | Rent erosion e (pl/ag) | Production-only price change: plausible = C×a_base + R×e_pl | aggressive = C×a_high + R×e_ag + 0.10×M | Non-production lever (pl/ag) | Total price change (pl/ag) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | Fast long-lead metal parts | 30% | 45% | 25% (10%) | 55% | B | 15%/30%/45% | 30%/60% | 0.45×0.30 + 0.10×0.30 = **-16.5%** | 0.45×0.45 + 0.10×0.60 + 0.10×0.30 = **-29.2%** | none | -17% / -29% |
| C2 | Data-center / large-load power blocks | 32% | 43% | 25% (15%) | 58% | B | 15%/30%/45% | 75%/100% | 0.43×0.30 + 0.15×0.75 = **-24.1%** | 0.43×0.45 + 0.15×1.00 + 0.10×0.32 = **-37.6%** | none | -24% / -38% |
| C3 | Scarce HV grid components | 40% | 35% | 25% (15%) | 50% | C | 0%/10%/25% | 50%/90% | 0.35×0.10 + 0.15×0.50 = **-11.0%** | 0.35×0.25 + 0.15×0.90 + 0.10×0.40 = **-26.2%** | none | -11% / -26% |
| C4 | China-free drone/robot components | 35% | 40% | 25% (15%) | 55% | A_new | 30%/50%/65% | 60%/100% | 0.40×0.50 + 0.15×0.60 = **-29.0%** | 0.40×0.65 + 0.15×1.00 + 0.10×0.35 = **-44.5%** | none | -29% / -45% |
| C5 | Rocket motors, energetics, cheap interceptors | 25% | 45% | 30% (5%) | 50% | B | 15%/30%/45% | 50%/100% | 0.45×0.30 + 0.05×0.50 = **-16.0%** | 0.45×0.45 + 0.05×1.00 + 0.10×0.25 = **-27.8%** | none | -16% / -28% |
| C6 | Satellite buses and space components | 40% | 35% | 25% (5%) | 40% | B | 15%/30%/45% | 50%/100% | 0.35×0.30 + 0.05×0.50 = **-13.0%** | 0.35×0.45 + 0.05×1.00 + 0.10×0.40 = **-24.8%** | none | -13% / -25% |
| C7 | Delivery-drone airframes | 45% | 35% | 20% (0%) | 35% | A_new | 30%/50%/65% | n/a | 0.35×0.50 = **-17.5%** | 0.35×0.65 + 0.10×0.45 = **-27.2%** | none | -18% / -27% |
| C8 | Productized home solar + battery | 17% | 5% | 78% (0%) | 5% | A_mat | 10%/20%/35% | n/a | 0.05×0.20 = **-1.0%** | 0.05×0.35 + 0.10×0.17 = **-3.5%** | -25%/-60% | -26% / -61% |
| C9 | Factory-built housing (ADU, HUD infill, pods) | 27% | 26% | 47% (0%) | 26% | B | 15%/30%/45% | n/a | 0.26×0.30 = **-7.8%** | 0.26×0.45 + 0.10×0.27 = **-14.4%** | -15%/-25% | -22% / -36% |
| C10 | Automated cell-therapy manufacturing | 25% | 60% | 15% (0%) | 60% | C | 0%/10%/25% | n/a | 0.60×0.10 = **-6.0%** | 0.60×0.25 + 0.10×0.25 = **-17.5%** | none | -6% / -18% |
| C11 | Cash-pay scan / diagnostic clinics | 4% | 4% | 92% (0%) | 4% | B | 15%/30%/45% | n/a | 0.04×0.30 = **-1.2%** | 0.04×0.45 + 0.10×0.04 = **-2.2%** | -20%/-40% | -21% / -41% |
| C12 | Affordable vehicles + MOSAIC aircraft | 60% | 20% | 20% (0%) | 20% | A_mat | 10%/20%/35% | n/a | 0.20×0.20 = **-4.0%** | 0.20×0.35 + 0.10×0.60 = **-13.0%** | -17%/-55% | -20% / -61% |
| C13 | Short-lead kitchens/cabinets, installed products | 26% | 26% | 48% (0%) | 26% | B | 15%/30%/45% | n/a | 0.26×0.30 = **-7.8%** | 0.26×0.45 + 0.10×0.26 = **-14.3%** | -15%/-30% | -22% / -40% |
| C14 | Humanoid robots and robotaxi vehicles | 20% | 60% | 20% (0%) | 60% | A_new | 30%/50%/65% | n/a | 0.60×0.50 = **-30.0%** | 0.60×0.65 + 0.10×0.20 = **-41.0%** | none | -30% / -41% |
| C15 | Commercial airliners and jet engines (ref) | 10% | 50% | 40% (5%) | 55% | C | 0%/10%/25% | 20%/50% | 0.50×0.10 + 0.05×0.20 = **-6.0%** | 0.50×0.25 + 0.05×0.50 + 0.10×0.10 = **-16.0%** | none | -6% / -16% |
| C16 | Commercial and naval ships (ref) | 45% | 40% | 15% (0%) | 40% | C | 0%/10%/25% | n/a | 0.40×0.10 = **-4.0%** | 0.40×0.25 + 0.10×0.45 = **-14.5%** | none | -4% / -15% |
| C17 | Gas turbines and microreactors (ref) | 15% | 35% | 50% (40%) | 75% | C | 0%/10%/25% | 25%/60% | 0.35×0.10 + 0.40×0.25 = **-13.5%** | 0.35×0.25 + 0.40×0.60 + 0.10×0.15 = **-34.2%** | none | -14% / -34% |
| C18 | Low-cost cruise missiles, attritable drones (ref) | 45% | 30% | 25% (0%) | 30% | A_new | 30%/50%/65% | n/a | 0.30×0.50 = **-15.0%** | 0.30×0.65 + 0.10×0.45 = **-24.0%** | none | -15% / -24% |
| C19 | Medical devices for emerging markets (ref) | 3% | 3% | 94% (0%) | 3% | A_mat | 10%/20%/35% | n/a | 0.03×0.20 = **-0.6%** | 0.03×0.35 + 0.10×0.03 = **-1.3%** | -30%/-60% | -30% / -61% |

Class assignments: A_new for C4, C7, C14, C18; A_mat for C8 (modules already at $0.133/W, HIST), C12 and C19 (a $2 lens); B for C1, C2, C5, C6, C9, C11, C13; C for C3, C10 (one independent model finds 9% from full automation), C15, C16, C17.

Uniform method for lead time: today's lead time = queue + physical build + per-order regulatory time. An entrant with open capacity has no queue. Build time is cut by class (plausible / aggressive): A_new 60% / 80%, A_mat 30% / 50%, B 50% / 70%, C 20% / 40% [A, bounded by the WWII 80% cut for one frozen design]. Per-order regulatory time is not touched.

Table 2c. Lead-time change for an entrant's customers by 2032 (script output). Splits of today's lead time into queue, build and regulatory parts are [A] built on the cited lead times.

| ID | Lead time today (months) | of which queue / build / per-order regulatory | Build-time cut (plausible/aggressive) | 2032 entrant lead time: plausible | aggressive | Change (pl / ag) |
|---|---|---|---|---|---|---|
| C1 | 12 | 6 / 6 / 0 | 50% / 70% | 6×0.5 + 0 = **3.0** | 6×0.3 + 0 = **1.8** | -75% / -85% |
| C2 | 24 | 11 / 13 / 0 | 50% / 70% | 13×0.5 + 0 = **6.5** | 13×0.3 + 0 = **3.9** | -73% / -84% |
| C3 | 30 | 17 / 13 / 0 | 20% / 40% | 13×0.8 + 0 = **10.4** | 13×0.6 + 0 = **7.8** | -65% / -74% |
| C4 | 5 | 3 / 2 / 0 | 60% / 80% | 2×0.4 + 0 = **0.8** | 2×0.2 + 0 = **0.4** | -84% / -92% |
| C5 | 36 | 0 / 26 / 10 | 50% / 70% | 26×0.5 + 10 = **23.0** | 26×0.3 + 10 = **17.8** | -36% / -51% |
| C6 | 12 | 0 / 12 / 0 | 50% / 70% | 12×0.5 + 0 = **6.0** | 12×0.3 + 0 = **3.6** | -50% / -70% |
| C7 | n/a | n/a | n/a | n/a | n/a | not lead-time constrained (see note) |
| C8 | 3 | 0 / 0.03 / 3 | 30% / 50% | 0.03×0.7 + 3 = **3.0** | 0.03×0.5 + 3 = **3.0** | no change / no change |
| C9 | 8 | 0 / 1.5 / 6.5 | 50% / 70% | 1.5×0.5 + 6.5 = **7.2** | 1.5×0.3 + 6.5 = **7.0** | -9% / -13% |
| C10 | 1.3 | 0 / 0.65 / 0.65 | 20% / 40% | 0.65×0.8 + 0.65 = **1.2** | 0.65×0.6 + 0.65 = **1.0** | -10% / -20% |
| C11 | n/a | n/a | n/a | n/a | n/a | not lead-time constrained (see note) |
| C12 | n/a | n/a | n/a | n/a | n/a | not lead-time constrained (see note) |
| C13 | 2.8 | 0 / 2.8 / 0 | 50% / 70% | 2.8×0.5 + 0 = **1.4** | 2.8×0.3 + 0 = **0.8** | -50% / -70% |
| C14 | n/a | n/a | n/a | n/a | n/a | not lead-time constrained (see note) |
| C15 | n/a | n/a | n/a | n/a | n/a | not lead-time constrained (see note) |
| C16 | 108 | 0 / 108 / 0 | 20% / 40% | 108×0.8 + 0 = **86.4** | 108×0.6 + 0 = **64.8** | -20% / -40% |
| C17 | 66 | 42 / 24 / 0 | 20% / 40% | 24×0.8 + 0 = **19.2** | 24×0.6 + 0 = **14.4** | -71% / -78% |
| C18 | 5 | 2 / 3 / 0 | 60% / 80% | 3×0.4 + 0 = **1.2** | 3×0.2 + 0 = **0.6** | -76% / -88% |
| C19 | n/a | n/a | n/a | n/a | n/a | not lead-time constrained (see note) |

Rows without a lead-time line (C7, C11, C12, C14, C15, C19) are not lead-time constrained for a buyer today, or (C15) the queue cannot be bypassed by an entrant. For C8, C9 and C10 the per-order regulatory part (permits and interconnection, site work and inspection, release testing) dominates, so faster production changes little.

- Cross-check against the sector notes: ENER's own judgment for electrical gear was "about 2x on price and 5-10x on delivery time" as a ceiling; this model's aggressive case for C2 is -38% on price and -84% on lead time. HOUS judged 20-35% lower delivered cost realistic for the best housing wedges; this model's total for C9 is -22% plausible and -36% aggressive, of which production alone is -8% and -14%.

### Gaps
- Cost stacks marked [A] (C1, C4, C5, C6, C7, C11, C13, C15, C18, and the M/N split for C16) have no source in the nine files. A bill-of-materials teardown or a 10-K cost-of-sales split for one incumbent per row would replace them.
- US residential solar installs, cabinet market size, the motor share of missile cost, the component share of drone cost and a delivery-drone unit cost were not found; each is flagged [A] in table 2a.
- The conversion-cut values by class are my calibration to the learning-rate evidence, not a published estimate. HIST and SKEP both note that no disclosed operating data yet supports 3x or greater cost gains from AI-run factories.


## 3. Demand response: existing shortage, elastic expansion and new uses, kept apart

### Takeaway
Three different things are often added together as "latent demand". Kept apart, the picture is: (i) shortage that exists at today's prices is large only where the buyer is waiting in a queue (airliners, turbines, ships, metal parts, data-center power, munitions); (ii) elastic expansion at lower prices is small under measured or conservative elasticities, between -$4.8B and +$0.4B a year per candidate at the plausible price; (iii) the multiples above 2x all come from new uses that are speculative today. In ten candidates served-market revenue shrinks as price falls.

### Cited Findings
Elasticity and mechanism evidence
- Air travel fare elasticity: route level -1.4, national -0.8, pan-national -0.6; gasoline -0.2 short run and -0.7 long run [SE] — HIST; [IATA / InterVISTAS](https://www.iata.org/en/iata-repository/publications/economic-reports/estimating-air-travel-demand-elasticities---by-intervistas/)
- Steel -0.2 to -0.3; pleasure air travel -1.5; cinema -0.87 [SE, textbook compilations] — HIST; [Wikipedia, Price elasticity of demand](https://en.wikipedia.org/wiki/Price_elasticity_of_demand)
- US new-vehicle demand: long-run market elasticity -0.34; household average -0.5, lowest-income group -0.84 [SE] — CONS; [RFF, Leard](https://www.rff.org/publications/working-papers/estimating-consumer-substitution-between-new-and-used-passenger-vehicles/); [RFF, Leard & Wu](https://www.rff.org/documents/4120/WP_23-33.pdf)
- Housing demand is "income and price inelastic" (below 1; no number retrieved) [SE] — HOUS and HIST; [NBER w22816](https://www.nber.org/papers/w22816)
- New manufactured homes cost about 48% less per sq ft than site-built yet hold 9-10% of new housing, down from 17-24% in the 1990s [M/SE] — SKEP; [NAHB Eye on Housing](https://eyeonhousing.org/2025/04/manufactured-homes-an-alternative-means-of-housing-supply/)
- Rooftop solar in Australia: installed price fell from about A$2.4/W (2013) to about A$0.90/W and quarterly installs roughly tripled [SE] — CONS; [Boston University](https://www.bu.edu/eci/files/2025/07/Intnatl-Cost-Comparisons-final.pdf)
- Lab-grown diamonds: wholesale down 96% since 2018; average stone grew 87% while average engagement-ring spend fell from about $6,000 (2021) to about $5,200 (2024) [SE] — CONS; [JCK](https://www.jckonline.com/editorial-article/lab-grown-wholesale-freefall/); [Stacker/BriteCo](https://stacker.com/stories/shopping/lab-grown-diamonds-now-cost-73-less-natural-diamonds-what-means-buyers-2026)
- OTC hearing aids: price fell from about $4,744 a pair to a few hundred dollars, yet 5.7% of people with hearing difficulty adopted OTC devices vs 33.5% with traditional devices [SE, 2025] — MED; [Capitol Forum](https://thecapitolforum.com/four-years-after-otc-hearing-aid-rule-competition-in-hearing-aid-market-remains-limited/); [Thieme, MarkeTrak 2025](https://www.thieme-connect.com/products/ejournals/html/10.1055/s-0045-1812040)
- Launch: Falcon is only about 3-4x cheaper than Saturn V or Atlas V and external launch demand did not grow 10x; Starlink's own demand did [SE/inference] — HIST; [Our World in Data](https://ourworldindata.org/grapher/cost-space-launches-low-earth-orbit)
- Cheap munitions: Tomahawk buys were 20-55 a year; the low-cost tier plans roughly 7,000-9,000 missiles a year at $350-450k [SE/D] — DEFN; [TWZ](https://www.twz.com/air/usaf-plans-to-buy-28000-low-cost-cruise-missiles-in-five-years-advance-with-new-deals); [CRS R49023](https://www.everycrsreport.com/reports/R49023.html)
- Ukraine's drone demand is funding-limited, not appetite-limited: capacity above 5 million a year while output was about 2 million for lack of money [SE] — DEFN; [United24](https://united24media.com/war-in-ukraine/ukraine-targets-annual-production-of-20-million-drones-under-new-eu-partnership-20805)
- Humanoids: Unitree units went from about 5 (2023) to about 5,200-5,500 (2025) as ASP fell from about $85k to about $24k, with 73.6% of revenue from research and education [M] — ROBO; [The Robot Report](https://www.therobotreport.com/unitree-ipo-shows-a-real-hardware-business-the-humanoid-case-is-still-early/)
- Electrical gear is under 10% of data-center cost but gates the project, so buyers are schedule-sensitive [SE/inference] — ENER; [Tom's Hardware via Yahoo](https://finance.yahoo.com/sectors/technology/articles/half-planned-us-data-center-150928890.html)

Shortage evidence (category i)
- Engines: single-aisle deliveries about 2,000 in 2024 against a need of about 3,700 a year in 2030-2040 [SE] — AVIA; [IATA/Emerton](https://www.iata.org/en/pressroom/2026-releases/06-24-urgent-action-needed-to-ease-engine-mro-bottlenecks/). An estimated 3,500+ engines stalled awaiting castings and forgings [SE, secondary] — ROBO; [fastener trade press](https://fastenershows.com/news/17000-aircraft-on-backlog-aviations-supply-chain-crisis/145609/). Airlines paid at least $11B in avoidable cost in 2025 [SE] — AVIA; [IATA](https://www.iata.org/en/pressroom/2026-releases/06-24-iata-outlines-four-priorities-to-strengthen-aviation-supply-chain)
- Munitions: THAAD production capped at 96 a year against an 857 order; rebuilding stocks takes at least three years [SE] — DEFN; [CNAS](https://www.cnas.org/publications/reports/munitions-procurement-and-the-fiscal-year-2027-defense-budget)
- Navy: attack submarines delivered at 1.1 a year against purchases of 2.0; 2026-2030 shortfall about 20 ships [SE] — DEFN; [CBO testimony](https://armedservices.house.gov/UploadedFiles/2026-04-22_Labs_Testimony.pdf)
- Cell therapy: about 2 in 10 eligible US patients receive CAR-T; 60% of wait-listed myeloma patients got a manufacturing slot [SE] — MED; [BioProcess Online](https://www.bioprocessonline.com/doc/closing-the-car-t-access-gap-with-hospital-based-manufacturing-0001)
- Housing: published national shortage estimates cluster at 3.7-4.9M homes [SE] — HOUS; [Boston Fed, Patel](https://www.bostonfed.org/-/media/Documents/events/2026/econ-conference/measuringhousingunderproductionwhyestimatesdivergeandwhatanationalnumbercansayelenapatel111326.pdf). Factory backlogs are short: Champion $316M at March 2026 [M] — HOUS; [Champion 8-K](https://www.sec.gov/Archives/edgar/data/0000090896/000119312526237809/sky-ex99_1.htm)
- Robotaxis: Waymo paid rides rose from 50,000 to 500,000 a week while the fleet stayed near 3,000 [M] — ROBO; [TechCrunch](https://techcrunch.com/2026/03/27/waymo-skyrocketing-ridership-in-one-chart/)
- Vehicles: Slate took 160,000-180,000 reservations at a $50 refundable deposit [SE] — CONS; [The Drive](https://www.thedrive.com/news/180000-people-reserved-slates-electric-truck-before-they-knew-it-would-cost-24950). Cybertruck converted under 5% of about 1 million $100 reservations [SE] — SKEP; [Carscoops](https://www.carscoops.com/2025/04/cybertrucks-1-million-reservations-translate-to-46k-sales-musk-rants-about-legions-of-robots/)

New-use evidence (category iii)
- FY2027 request for the Defense Autonomous Warfare Group: $53.6B mandatory plus $1.0B discretionary; the House drafted the $350B reconciliation request at $60B [M/SE] — DEFN; [CRS R49023](https://www.everycrsreport.com/reports/R49023.html); [CNAS](https://www.cnas.org/publications/reports/munitions-procurement-and-the-fiscal-year-2027-defense-budget)
- Golden Dome total program cost estimated about $185B; Apex estimates the satellite platform layer could exceed $30B [SE, interested party] — AVIA; [Contrary Research](https://research.contrary.com/company/apex)
- Omdia forecasts 2.6 million humanoids a year by 2035; UBTech's own executive puts current productivity at 30-50% of a human [SE] — ROBO; [VnExpress](https://e.vnexpress.net/news/tech/tech-news/humanoid-robots-only-half-as-efficient-as-humans-says-third-largest-global-maker-ubtech-5009929.html)
- The 2026 ROAD to Housing Act allows chassis-less manufactured homes; states must align by July 2027 [SE] — HOUS; [HousingWire](https://www.housingwire.com/articles/new-policy-impact-may-ignite-a-manufactured-housing-blue-sky-era/)
- Army Janus program allocates up to $2.2B through FY2031 for microreactors [SE] — ENER; [EnergyTech](https://www.energytech.com/next-gen-nuclear/news/55401307/energy-in-a-box-nuclear-startup-radiant-secures-750m-contract-to-deploy-15-portable-microreactors-across-us-army-bases)
- WHO: closing the global vision gap is estimated to cost $25B; hearing-aid production meets under 10% of need [SE] — MED; [WHO, vision](https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment); [WHO, assistive technology](https://www.who.int/news-room/fact-sheets/detail/assistive-technology)
- MOSAIC lets a four-seat airplane be sold on a statement of compliance; US shipments were 17,811 in 1978 vs 1,782 piston airplanes worldwide in 2025 [M] — AVIA; [FAA](https://www.faa.gov/aircraft/MOSAIC); [GAMA](https://gama.aero/news-and-events/press-releases/gama-releases-2025-aircraft-shipment-and-billing-report/)

### Inferences
Table 3a. Mechanism chosen per candidate and the basis for each input (all elasticity values are market-level, not firm-level; [A] where no measurement exists).

| ID | Primary mechanism | Elasticity low / base / high and basis | (i) Shortage at today's prices: derivation | (iii) New uses: derivation |
|---|---|---|---|---|
| C1 | Backlog release and schedule value | 0.1 / 0.3 / 0.5: derived demand, like steel at -0.2 to -0.3 | 25% of market (10-40%) [A]: turbine orders exceed capacity by 57-83%; engine need 3,700 vs 2,000 a year = $8.75B | $1B (0-4), p 0.3 [A]: hardware never launched because of tooling cost; no data |
| C2 | Schedule value and backlog release | 0.1 / 0.3 / 0.5: gear is under 10% of project cost [A on value] | 6 GW a year delayed × $1.67M/MW = $10B, 60% attributed to electrical gear [A] = $6B (3-10) | $3B (0-10), p 0.5 [A]: behind-the-meter industrial loads, charging hubs |
| C3 | Backlog release | 0.1 / 0.2 / 0.4: regulated utility buyers [A] | 20% of market (7-30%), between the 30% (2025) and 7% (2026) deficit figures = $2B | $0.5B (0-2), p 0.3 [A] |
| C4 | Protected-market substitution; budget-fixed buyers | 0.7 / 1.0 / 1.5: units = budget / price [A] | Measured: 8,880 late drones × $5,000 × 60% = $27M. Scaled to 30% of market [A] = $0.45B | $5B (1-20), p 0.4: autonomous-warfare request $54.6B (mostly unappropriated); humanoid forecasts; barred Chinese drone models |
| C5 | Backlog release; budget-fixed buyers | 0.8 / 1.2 / 1.8: budget-fixed is about 1; cheap-tier arc is about 2 | Orders about 2x output across motors [A] = $4B; low case $1.6B if reconciliation fails | $4B (1-12), p 0.5: NATO $40B over five years; Golden Dome |
| C6 | Protected-market substitution; government anchor | 0.5 / 1.0 / 1.5: launch precedent shows weak external response | 5% of market [A] = $0.6B; no measured shortage | $3B (0.5-8), p 0.5: Golden Dome platform layer over about ten years |
| C7 | Penetration gap, rule-gated | 0.5 / 1.0 / 1.5 [A] | 570 announced sites × about 10 aircraft × $40k over two years [A] = $0.1B a year | $0.7B (0.15-3), p 0.5: 20,000 aircraft a year × $35k (AVIA: "tens of thousands") |
| C8 | Elastic expansion, but through installed price | 0.7 / 1.1 / 1.5: Australia arc ln(3)/ln(2.4/0.9) = 1.12 [D] | None: demand is bought with marketing at 20-29% of price | $3B (0.5-10), p 0.5: battery as a service |
| C9 | None strong; legal unlock in niches | 0.3 / 0.5 / 0.8: inelastic [A on value] | None for factory product: 5-6 week backlogs, shipments falling | $6B (0-20), p 0.3: regaining the 1990s share would add about 100-150k homes × $130k = $13-20B [D] |
| C10 | Capacity rationing | 0.5 / 1.0 / 1.5 [A] | 30% of market (10-67%) = $0.48B; the 67% is 40/60 from the myeloma waitlist | $5B (0.5-16), p 0.35: autoimmune indications, about 3x today's spend [A] |
| C11 | Elastic cash-pay demand created by a new price point | 0.8 / 1.2 / 1.8: cross-product arc ln(4.5)/ln(5) = 0.9 [D]; leisure analogue 1.5 | 350,000 waitlist × $499 × 30% conversion [A] = $52M one-off; $0.1B a year | $1.5B (0.3-6), p 0.4: an annual scan habit [A] |
| C12 | Elastic, but below 1; legal lane for microcars and light aircraft | 0.34 / 0.5 / 0.84: measured | 170,000 reservations × 10% [A] × $27k = $0.46B one-off; $0.4B | $2B (0.3-8), p 0.3: light aircraft 10,000-30,000 a year at about $100k (AVIA estimate) plus microcars |
| C13 | Channel removal and lead time | 0.5 / 0.8 / 1.2 [A]; cinema -0.87 as a discretionary analogue | None: real project volume is soft | $1B (0-5), p 0.3 [A] |
| C14 | Penetration gap, capability-gated | 1.0 / 1.5 / 2.5 [A] | Waymo needs 6,000-8,000 vehicles vs 3,871 = about 3,000 × $120k = $0.4B | $8B (1-40), p 0.3: 80,000-100,000 robotaxis; humanoid forecasts |
| C15 | Backlog release | 0.2 / 0.4 / 0.6: aircraft is a minority of seat cost | About 1,200 aircraft a year × $80M = $95B (AVIA estimate) | none |
| C16 | Protected-market substitution; backlog | 0.3 / 0.5 / 0.8 [A] | About 30% of Navy shipbuilding undelivered [A] = $14B | $3B (0.5-15), p 0.4: unmanned fleet, port-fee plan |
| C17 | Backlog release | 0.2 / 0.4 / 0.7 [A, energy-like] | 35-45 GW × $500/kW = $20B | $2B (0.3-10), p 0.3: microreactors |
| C18 | Elastic new mass market, budget-capped | 1.0 / 1.5 / 2.0: arc ln(200)/ln(13.25) = 2.05 [D] | Contract floors: about $1.3B a year (10,000 / 3 × $400k) plus part of $3B [A] = $2B | $8B (1-30), p 0.35: autonomous-warfare request; NATO |
| C19 | Penetration gap, delivery-gated | 0.1 / 0.4 / 1.0: hearing-aid arc ln(1.17)/ln(10) = 0.07 [D]; Aurolab is the counter-case | None in paying terms | $5B (0.5-25), p 0.2: WHO gap figures |

Formulas: unit multiple = (1 - price cut)^(-elasticity); revenue multiple of the served market = (1 - price cut)^(1 - elasticity). "Production only" uses the plausible production-only price change from table 2b; "total" adds the non-production lever.

Table 3b. Elastic response (script output).

| ID | Mechanism inputs: elasticity (low/base/high) | Unit multiple at plausible price, production only | Unit multiple, plausible total | Unit multiple, aggressive total | Revenue multiple of today's served market (prod-only pl / total pl / total ag, base elasticity) | (ii) Elastic change in $B/yr: min / base / max over the grid |
|---|---|---|---|---|---|---|
| C1 | 0.1 / 0.3 / 0.5 | 1.06x | 1.06x | 1.11x | 0.88 / 0.88 / 0.78 | -9.37 / -4.15 / -3.02 |
| C2 | 0.1 / 0.3 / 0.5 | 1.09x | 1.09x | 1.15x | 0.82 / 0.82 / 0.72 | -6.91 / -3.52 / -2.58 |
| C3 | 0.1 / 0.2 / 0.4 | 1.02x | 1.02x | 1.06x | 0.91 / 0.91 / 0.78 | -2.40 / -0.89 / -0.68 |
| C4 | 0.7 / 1 / 1.5 | 1.41x | 1.41x | 1.80x | 1.00 / 1.00 / 1.00 | -0.24 / +0.00 / +0.51 |
| C5 | 0.8 / 1.2 / 1.8 | 1.23x | 1.23x | 1.48x | 1.04 / 1.04 / 1.07 | -0.25 / +0.14 / +1.19 |
| C6 | 0.5 / 1 / 1.5 | 1.15x | 1.15x | 1.33x | 1.00 / 1.00 / 1.00 | -1.59 / +0.00 / +1.83 |
| C7 | 0.5 / 1 / 1.5 | 1.21x | 1.21x | 1.37x | 1.00 / 1.00 / 1.00 | -0.01 / +0.00 / +0.01 |
| C8 | 0.7 / 1.1 / 1.5 | 1.01x | 1.39x | 2.85x | 1.00 / 1.03 / 1.10 | -3.23 / +0.39 / +7.92 |
| C9 | 0.3 / 0.5 / 0.8 | 1.04x | 1.13x | 1.25x | 0.96 / 0.89 / 0.80 | -4.80 / -2.07 / -0.86 |
| C10 | 0.5 / 1 / 1.5 | 1.06x | 1.06x | 1.21x | 1.00 / 1.00 / 1.00 | -0.15 / +0.00 / +0.16 |
| C11 | 0.8 / 1.2 / 1.8 | 1.01x | 1.33x | 1.90x | 1.00 / 1.05 / 1.11 | -0.03 / +0.01 / +0.16 |
| C12 | 0.34 / 0.5 / 0.84 | 1.02x | 1.12x | 1.60x | 0.98 / 0.89 / 0.63 | -20.77 / -4.83 / -1.61 |
| C13 | 0.5 / 0.8 / 1.2 | 1.07x | 1.22x | 1.51x | 0.98 / 0.95 / 0.90 | -5.64 / -1.19 / +2.69 |
| C14 | 1 / 1.5 / 2.5 | 1.71x | 1.71x | 2.21x | 1.20 / 1.20 / 1.30 | +0.00 / +0.41 / +2.53 |
| C15 | 0.2 / 0.4 / 0.6 | 1.03x | 1.03x | 1.07x | 0.96 / 0.96 / 0.90 | -15.62 / -4.37 / -2.93 |
| C16 | 0.3 / 0.5 / 0.8 | 1.02x | 1.02x | 1.08x | 0.98 / 0.98 / 0.92 | -5.03 / -0.98 / -0.39 |
| C17 | 0.2 / 0.4 / 0.7 | 1.06x | 1.06x | 1.18x | 0.92 / 0.92 / 0.78 | -14.25 / -4.17 / -2.13 |
| C18 | 1 / 1.5 / 2 | 1.28x | 1.28x | 1.51x | 1.08 / 1.08 / 1.15 | +0.00 / +0.42 / +1.58 |
| C19 | 0.1 / 0.4 / 1 | 1.00x | 1.16x | 1.45x | 1.00 / 0.80 / 0.57 | -2.83 / -0.98 / +0.00 |

Table 3c. Expanded market by component (script output). Low = today's market + the worst elastic outcome on the grid + low shortage, no new uses. Base = today's market + base elastic + base shortage (priced at the 2032 price) + probability-weighted new uses. High = today's market + best elastic outcome + high shortage + high new uses in full. Trend growth is excluded here and enters in section 4.

| ID | Served market today S0 ($B/yr; low/base/high) | (i) Backlog or shortage at today's prices ($B/yr; low/base/high) | Shortage closes (low/base/high) | (ii) Elastic change at plausible total price, base elasticity ($B/yr) | (iii) New uses by 2032 ($B/yr; low/base/high) and probability | Expanded market, no trend growth ($B/yr): low / base / high | Multiple of today (low / base / high) | Unit multiple, base | Units today → expanded units, base |
|---|---|---|---|---|---|---|---|---|---|
| C1 | 20 / 35 / 52 | 3.5 / 8.75 / 14 | 2030 / 2033 / 2036 | -4.15 | 0 / 1 / 4; p=0.3 | 28.6 / 38.5 / 50.0 | 0.82x / 1.10x / 1.43x | 1.32x | n/a ($ only) |
| C2 | 17 / 20 / 23 | 3 / 6 / 10 | 2028 / 2030 / 2032 | -3.52 | 0 / 3 / 10; p=0.5 | 15.4 / 22.5 / 37.4 | 0.77x / 1.13x / 1.87x | 1.49x | 12,000 → 17,824 MW of load/yr |
| C3 | 6 / 10 / 15 | 0.7 / 2 / 3 | 2028 / 2030 / 2033 | -0.89 | 0 / 0.5 / 2; p=0.3 | 8.2 / 11.0 / 14.3 | 0.82x / 1.10x / 1.43x | 1.24x | n/a ($ only) |
| C4 | 0.7 / 1.5 / 3 | 0.2 / 0.45 / 0.9 | 2028 / 2030 / 2032 | +0.00 | 1 / 5 / 20; p=0.4 | 1.4 / 3.8 / 22.9 | 0.93x / 2.55x / 15.28x | 3.59x | 80,000 → 286,911 drone-sets/yr |
| C5 | 2.5 / 4 / 7 | 1.6 / 4 / 8 | 2029 / 2031 / 2034 | +0.14 | 1 / 4 / 12; p=0.5 | 5.1 / 9.5 / 25.2 | 1.27x / 2.38x / 6.30x | 2.83x | n/a ($ only) |
| C6 | 8 / 12 / 20.4 | 0.2 / 0.6 / 1.5 | 2028 / 2029 / 2031 | +0.00 | 0.5 / 3 / 8; p=0.5 | 10.6 / 14.0 / 23.3 | 0.88x / 1.17x / 1.94x | 1.34x | 1,500 → 2,015 satellites/yr |
| C7 | 0.02 / 0.06 / 0.15 | 0.04 / 0.1 / 0.25 | 2028 / 2029 / 2030 | +0.00 | 0.15 / 0.7 / 3; p=0.5 | 0.1 / 0.5 / 3.3 | 1.40x / 8.21x / 55.34x | 9.95x | 1,500 → 14,924 aircraft/yr |
| C8 | 9 / 13 / 17 | 0 / 0 / 0.5 | no measured shortage | +0.39 | 0.5 / 3 / 10; p=0.5 | 9.8 / 14.9 / 31.4 | 0.75x / 1.15x / 2.42x | 1.54x | 550,000 → 848,597 systems/yr |
| C9 | 14 / 18 / 22 | 0 / 0 / 2 | no measured shortage | -2.07 | 0 / 6 / 20; p=0.3 | 13.2 / 17.7 / 39.1 | 0.73x / 0.99x / 2.17x | 1.26x | 133,000 → 167,208 homes/yr |
| C10 | 1 / 1.6 / 2.3 | 0.16 / 0.48 / 1.07 | 2029 / 2031 / 2034 | +0.00 | 0.5 / 5 / 16; p=0.35 | 1.6 / 3.8 / 18.8 | 1.00x / 2.38x / 11.77x | 2.53x | 10,400 → 26,285 doses/yr |
| C11 | 0.15 / 0.3 / 0.6 | 0.03 / 0.1 / 0.18 | 2028 / 2029 / 2030 | +0.01 | 0.3 / 1.5 / 6; p=0.4 | 0.3 / 1.0 / 6.6 | 0.98x / 3.31x / 22.13x | 4.19x | 150,000 → 628,473 scans/yr |
| C12 | 25 / 45 / 80 | 0.2 / 0.4 / 1.5 | 2028 / 2029 / 2030 | -4.83 | 0.3 / 2 / 8; p=0.3 | 24.4 / 41.1 / 52.9 | 0.54x / 0.91x / 1.18x | 1.15x | 1,600,000 → 1,833,439 vehicles/yr |
| C13 | 15 / 25 / 40 | 0 / 0 / 1 | no measured shortage | -1.19 | 0 / 1 / 5; p=0.3 | 19.4 / 24.1 / 33.7 | 0.77x / 0.96x / 1.35x | 1.23x | n/a ($ only) |
| C14 | 1.2 / 2.1 / 3.5 | 0.15 / 0.4 / 1 | 2029 / 2031 / 2033 | +0.41 | 1 / 8 / 40; p=0.3 | 2.2 / 5.2 / 45.6 | 1.05x / 2.47x / 21.73x | 3.53x | 60,000 → 211,836 robots+vehicles/yr |
| C15 | 110 / 120 / 130 | 60 / 95 / 120 | 2031 / 2033 / 2035 | -4.37 | 0 / 0 / 0; p=0 | 160.8 / 204.9 / 237.1 | 1.34x / 1.71x / 1.98x | 1.82x | 1,450 → 2,634 aircraft/yr |
| C16 | 40 / 48.4 / 60 | 8 / 14 / 20 | 2031 / 2035 / 2040 | -0.98 | 0.5 / 3 / 15; p=0.4 | 51.1 / 62.1 / 83.0 | 1.05x / 1.28x / 1.72x | 1.34x | 24 → 32 ships/yr (US) |
| C17 | 35 / 50 / 60 | 10 / 20 / 25 | 2030 / 2033 / 2035 | -4.17 | 0.3 / 2 / 10; p=0.3 | 44.4 / 63.7 / 82.9 | 0.89x / 1.27x / 1.66x | 1.47x | 846 → 1,247 turbines/yr |
| C18 | 3 / 5 / 8 | 0.5 / 2 / 4 | 2029 / 2031 / 2033 | +0.42 | 1 / 8 / 30; p=0.35 | 5.4 / 9.9 / 40.6 | 1.08x / 1.98x / 8.12x | 2.33x | 81,000 → 189,126 munitions/yr (US) |
| C19 | 2 / 5 / 10 | 0 / 0 / 0.5 | no measured shortage | -0.98 | 0.5 / 5 / 25; p=0.2 | 2.2 / 5.0 / 30.5 | 0.43x / 1.00x / 6.10x | 1.44x | n/a ($ only) |

Table 3d. The shortage window against the entrant's timeline (script output; V and the multipliers are from section 4).

| ID | Shortage at today's prices, base ($B/yr) | Base close year | Sum of shortage 2027-2032 ($B) | Entrant volume year V | Share of 2027-32 shortage dollars falling in or after V | Ramp-weighted share the entrant can address | Risk-adjusted entrant revenue from the shortage pool, 2027-32 sum ($M) |
|---|---|---|---|---|---|---|---|
| C15 | 95 | 2033 | 277.4 | 2039 | 0% | 0% | 0.0 |
| C17 | 20 | 2033 | 56.4 | 2033.5 | 0% | 0% | 3.9 |
| C16 | 14 | 2035 | 50.3 | 2031.5 | 9% | 2% | 29 |
| C1 | 8.75 | 2033 | 24.3 | 2030.5 | 13% | 4% | 67 |
| C2 | 6 | 2030 | 8.4 | 2029.5 | 0% | 0% | 1.6 |
| C5 | 4 | 2031 | 7.6 | 2030.5 | 0% | 1% | 6.9 |
| C3 | 2 | 2030 | 2.9 | 2032 | 0% | 0% | 0.0 |
| C18 | 2 | 2031 | 3.8 | 2029.5 | 9% | 3% | 7.0 |
| C6 | 0.6 | 2029 | 0.6 | 2030.5 | 0% | 0% | 0.0 |
| C10 | 0.48 | 2031 | 0.9 | 2032 | 0% | 0% | 0.1 |
| C4 | 0.45 | 2030 | 0.6 | 2029 | 15% | 3% | 0.6 |
| C12 | 0.4 | 2029 | 0.4 | 2031.5 | 0% | 0% | 0.0 |
| C14 | 0.4 | 2031 | 0.7 | 2033 | 0% | 0% | 0.0 |
| C7 | 0.1 | 2029 | 0.1 | 2031 | 0% | 0% | 0.0 |
| C11 | 0.1 | 2029 | 0.1 | 2029 | 0% | 1% | 0.0 |

- Where revenue shrinks when price falls (base elasticity below 1, plausible total price change): C12 -$4.8B a year, C15 -$4.4B, C17 -$4.2B, C1 -$4.2B, C2 -$3.5B, C9 -$2.1B, C13 -$1.2B, C16 -$1.0B, C19 -$1.0B, C3 -$0.9B. This is the lab-grown-diamond pattern: units rise, dollars fall. In C1, C2, C3, C15 and C17 the entrant should therefore sell speed at today's price, not a discount.
- Largest near-certain demand open to a new entrant: C1, then C2, then C5. C1's window is the longest (base 2033) because the casting and forging base rebuilds slowly and the airliner imbalance runs to 2031-2034. C2's is the shortest (base 2030) because about $2B of incumbent plants open in 2027-2028.
- True elastic latent demand is clearest in C18 (measured arc near 2 in planned buys), C8 (measured arc near 1.1, but the price lever is installation and selling, not the factory) and C11 (waitlist at a 5x lower price point). Even there the conservative model gives 1.3-1.4x units, not 10x.
- C7 and C14 show the largest multiples (8x and 2.5x base; 55x and 22x high) from tiny bases, almost entirely from category (iii). They are bets on rules and capability, not on price.

### Gaps
- No file gives a measured elasticity for metal parts, grid equipment, satellites, delivery drones, cell therapy, kitchens, ships or turbines; those values are [A] and set conservatively by analogy.
- The shortage percentages for C1, C4, C5, C6, C10 and C16 are my scaling of partial measurements to the whole candidate market.
- New-use pools and their probabilities are judgment. They are shown unweighted in the high case and probability-weighted in the base case so the reader can substitute their own.

## 4. Actor-response simulation, 2027-2032, and risk-adjusted entrant revenue

### Takeaway
Stepping a 2027-funded entrant through to 2032, the base-case risk-adjusted revenue is highest for metal parts (about $300M), data-center power blocks (about $260M), low-cost munitions (about $150M), rocket motors and interceptors (about $90M) and satellite buses (about $80M). Per dollar of capital, data-center power blocks, metal parts, China-free components and rocket motors lead at 0.29-0.44. Vehicles, humanoids and robotaxis, airliners, ships, turbines and cell therapy return 0.05 or less by 2032 because first volume arrives after 2031 or the entry ticket is $0.5B or more.

### Cited Findings
One line per factor: (a) market structure and incumbent response m_a (1.0 = fragmented, open buyers; above 1 where buyers sponsor second sources; below 1 where incumbents or captive supply block entry), (b) probability π that legal protection from Chinese supply persists to 2032 and share r of revenue that survives if it lapses, (c) years to first revenue d1 and extra years to volume d2, (d) buyer adoption lag d3, (e) complements m_e, (f) probability p_f that the shortage or budget surge ends before the factory ships. Values are [A] set from the cited evidence.
- **C1.** (a) 1.2: OEMs are advised to co-invest and pay rush premiums, and incumbents prefer margin to capacity, but Hadrian raised $1.37B and OEMs are integrating upstream — AVIA/ROBO; [BCG](https://www.bcg.com/publications/2024/fixing-aerospaces-supply-chain-for-casting-and-forging); [The Next Web](https://thenextweb.com/news/hadrian-1-37bn-series-d-7-87bn-defence-factories). (b) π 0.95, r 0.7: defense and aerospace buyers cannot import. (c) d1 2.0, d2 1.0: AVIA judges first revenue in 2-3 years and aviation-grade qualification 3-5+ years, so volume comes first from defense, space and land turbines. (d) 0.5: supplier contracts run 5-7 years (BCG). (e) 0.75: new vacuum furnaces have 2-year lead times and talent takes 5-10 years to rebuild — AVIA; [Bloomberg via Tiger](https://www.itiger.com/news/2650735186). (f) 0.25: munitions plan drops 46% after FY2027 and turbine orders were expected to peak in 2026 — DEFN; [CNAS](https://www.cnas.org/publications/reports/munitions-procurement-and-the-fiscal-year-2027-defense-budget). Capital: Machina reached a first factory on about $174M — ROBO; [Robotics & Automation News](https://roboticsandautomationnews.com/2026/02/08/machina-labs-raises-124-million-to-scale-manufacturing-infrastructure/98760/).
- **C2.** (a) 1.0: nearly $2B of incumbent capacity since 2023 but incumbents choose "value over volume"; data-center buyers need no utility vendor list — ENER; [POWER Magazine](https://powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/). Shortage close 2030: deficits forecast to narrow to single digits by 2030 — ENER; [Electrical Contractor](https://www.ecmag.com/magazine/articles/article-detail/investment-by-grid-equipment-makers-could-ease-shortage). (b) π 0.6, r 0.6: imports supply about 80% of power transformers and Chinese units rose from under 1,500 (2022) to over 8,000 (2025); the tariff regime was rewritten within a year — ENER; [tED Magazine](https://tedmag.com/trump-administration-increases-tariffs-on-certain-transformers/). (c) d1 1.5, d2 0.5: ENER estimates shipping on $50-150M within 18-24 months using bought-in components. (d) 0.5: Crusoe cancelled a $1.25B order months before delivery — ENER; [TechCrunch](https://techcrunch.com/2026/09/25/crusoe-abandons-1.25b-plan-to-use-boom-turbines-at-ai-data-centers/). (e) 0.8: one North American source of grain-oriented electrical steel — ENER; [Wood Mackenzie](https://www.woodmac.com/news/opinion/4-years-into-a-difficult-transformers-market-in-the-us-is-there-a-potential-end-in-sight/). (f) 0.4 and trend 7% / 15.3% / 25%: the base path takes the $20B to $65B forecast and cuts the increase by 40%, the haircut Grid Strategies applies to data-center load forecasts ($20B + 0.6 × $45B = $47B by 2030, held flat to 2032) — ENER; [Grid Strategies](https://gridstrategiesllc.com/?p=1799).
- **C3.** (a) 0.7: GE Vernova is buying the bushing maker and Hitachi invests only against secured backlog — ENER; [pv magazine](https://www.pv-magazine.com/2026/02/27/global-energy-transition-hits-a-hardware-bottleneck/). (b) π 0.6, r 0.5: same import and tariff facts as C2. (c) d1 2.5, d2 1.5: new plants take 2-3 years and tooling 2-4 years — ENER; [Thunder Said Energy](https://thundersaidenergy.com/downloads/transformers-companies-and-costs/); utility vendor-list time (1-3 years) is unsourced in ENER. (d) 1.0: 40-year asset lives and qualification rules (ENER). (e) 0.75. (f) 0.5: volume in 2032 arrives after the forecast narrowing. Capital: $150-457M plant benchmarks — ENER; [Foley](https://www.foley.com/insights/publications/2026/09/the-grids-bottleneck-isnt-just-money-its-materials/).
- **C4.** (a) 1.2: more than 20 drone makers are customers and 40% of Gauntlet I was late on compliant parts, but integrated makers build in-house (DEFN, ROBO). (b) π 0.75, r 0.2: Chinese rare-earth material is barred from the defense magnet chain from 1 Jan 2027 — DEFN; [AP via AJC](https://www.ajc.com/news/2026/08/us-faces-new-pressure-to-build-weapons-without-chinas-rare-earth-magnets/); the FCC listing of foreign drones is under litigation — SKEP; [DroneLife](https://dronelife.com/2025/12/22/fcc-adds-foreign-made-drones-and-components-to-covered-list-citing-national-security-risks/); the China cost gap is 3-6x (ROBO). (c) d1 1.0, d2 0.5 and (d) 0.5: DEFN ranks this the lowest-capital, fastest wedge; no certification gate. (e) 0.65: China makes over 90% of rare-earth magnets and has put US magnet firms on its export-control list — ROBO; [S&P Global](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2026/6/china-tightens-rare-earth-export-curbs-on-10-us-companies-103014947). (f) 0.35: most of the drone surge sits in an unpassed reconciliation bill (CNAS).
- **C5.** (a) 2.5: the buyer funds second sources (Northrop received over $3B as second source for PAC-3 and THAAD motors) and splits awards — DEFN; [Breaking Defense](https://breakingdefense.com/2026/08/northrop-gets-3b-framework-deal-to-increase-motor-production-for-pac-3-thaad/); second-source qualification is prioritised in the FY2026 NDAA — DEFN; [War on the Rocks](https://warontherocks.com/2025/12/an-industry-guide-to-the-fy2026-ndaa/). (b) π 0.98. (c) d1 1.5, d2 1.5: DEFN reads one to three years to a first motor contract; qualification is the stated top risk — DEFN; [Sacra, Castelion](https://sacra.com/c/castelion/). (d) 0.5 and (e) 0.7: on-time defense appropriations happened twice since 2008 (CNAS). (f) 0.4: plan falls 46% after FY2027 (CNAS). Capital: X-Bow's roughly $70M funds tooling for 500 motors a year — DEFN; [ASDNews](https://asdnews.com/news/defense/2026/10/07/xbow-awarded-nearly-70m-develop-advanced-booster-future-navy-missiles).
- **C6.** (a) 0.8: crowded (Apex, K2, York, Rocket Lab) and primes bought bus makers. (b) π 0.95. (c) d1 2.0, d2 1.0: Apex went from seed (Oct 2022) to $60M revenue in 2025. (d) 0.5: Apex was not among the Golden Dome prototype awardees. (e) 0.75: SpaceX carries 85% of satellites and is a competitor. (f) 0.3. All — AVIA; [Contrary Research](https://research.contrary.com/company/apex).
- **C7.** (a) 0.3: Zipline and Wing build their own aircraft, so merchant supply is small (AVIA). (b) π 0.7, r 0.3: FCC listing under litigation (SKEP, DroneLife link above). (c) d1 1.5, d2 1.5: Part 108 effective 2027 at the earliest; permits cap fleets at 100 active aircraft — AVIA; [DLA Piper](https://www.dlapiper.com/en/insights/publications/2025/08/faa-proposes-comprehensive-bvlos-uas-regulatory-framework). (d) 1.0. (e) 0.6. (f) 0.2.
- **C8.** (a) 0.8: well-funded rivals (Base Power, Tesla). (b) direct 0.9: the entrant buys hardware; exposure is to tariff and foreign-entity rules on cells, not to Chinese competition — SKEP; [Rhodium Group](https://rhg.com/wp-content/uploads/2026/05/Worlds-Apart-Contrasting-US-China-Approaches-to-Scaling-Clean-Technology-Manufacturing-1.pdf). (c) d1 1.0, d2 1.0 and (e) 0.6: Tesla's backup switch is approved by only 40% of utilities; permitting and interconnection are local — CONS; [Latitude Media](https://www.latitudemedia.com/news/can-the-us-bring-solar-installation-to-below-2-per-watt/). (d) 1.0: acquisition cost of roughly $5,000-7,300 a home (CONS). (f) 0.3: US clean-manufacturing support reversed within three years (Rhodium). Capital intensity 3.0: Base Power needed two $1B rounds for a small fleet (ENER).
- **C9.** (a) 0.5: Clayton's lenders make 56% of chattel loans; incumbents earn 22-26% gross margin with spare capacity — HOUS; [CFPB](https://files.consumerfinance.gov/f/documents/cfpb_manufactured-housing-finance-new-insights-hmda_report_2021-05.pdf). (b) direct 1.0: bulky and local. (c) d1 1.5, d2 1.0: HUD standards and state action by July 2027 make 2027-2028 the earliest window (HOUS). (d) 1.0 and (e) 0.5: chattel loans at 8.6% vs 4.1% and 50% denial; zoning stays local (CFPB). (f) 0.3: plants need about 70-80% utilisation in a cyclical market — SKEP; [OneBuild](https://onebuild.substack.com/p/the-prefab-and-modular-graveyard).
- **C10.** (a) 1.0: sponsors pay to reserve capacity (BMS up to $380M) but Cellares leads and sponsors' own plants reach 99% success. (b) direct 0.95. (c) d1 3.0, d2 1.5: Cellares was founded in 2019, made first GMP doses in 2026 and targets commercial scale in 2027; the process is locked into each product's approval. (d) 0.5. (e) 0.7: treatment centres and release testing. (f) 0.25. Capital: Cellares raised $612M before commercial revenue. All — MED; [PharmTech](https://www.pharmtech.com/view/cellares-secures-257m-to-scale-global-cell-therapy-manufacturing); [IntuitionLabs](https://intuitionlabs.ai/articles/car-t-manufacturing-economics-cogs).
- **C11.** (a) 1.0. (b) direct 1.0. (c) d1 1.0, d2 0.5: device clearance averages about 128 days — MED; [Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/07/fda-releases-draft-commitments-letter-for-medical-devices-review). (d) 0.5: 75% of Neko members prepay. (e) 0.7: clinical-value scepticism and clinic capital. (f) 0.3 [A]: discretionary cash-pay spend. Capital: Prenuvo raised $120M; Neko over $1B — MED; [HIT Consultant](https://hitconsultant.net/2026/07/15/neko-health-raises-700-million-series-c/).
- **C12.** (a) 0.5: dealer front-end margin about 5% and RV-maker gross 12.6% show a thin profit pool; GM answered with a sub-$30,000 Bolt (CONS). (b) π 0.7, r 0.2: the connected-vehicle rule bars Chinese-linked vehicles from model year 2027 — SKEP; [BIS](https://www.bis.gov/connected-vehicles); BYD sells a car at $7,800-10,300 at home (CONS). (c) d1 3.0, d2 0.5: Slate raised about $1.5B before its first delivery; Xiaomi took three years. (d) 1.0: small refundable deposits convert at under 5%. (e) 0.7. (f) 0.3: EV spending fell 43% in a quarter when the credit expired (Rhodium). Capital $1.5B — CONS; [The Next Web](https://thenextweb.com/news/slate-auto-ev-pickup-24950-preorders-bezos-production).
- **C13.** (a) 0.8: fragmented market, but the made-to-order furniture cohort ended in distress sales — CONS; [Business of Home](https://businessofhome.com/articles/interior-define-bankruptcy-questions-answered). (b) direct 0.9. (c) d1 1.0, d2 0.25: no certification gate. (d) 2.5: a consumer brand builds slowly (Warby Parker reached $872M after about 15 years, CONS). (e) 0.6: remodeling is constrained by trades labor — CONS; [Harvard JCHS](https://www.jchs.harvard.edu/improving-americas-housing-2025). (f) 0.3: kitchen and bath real volume is soft (NKBA).
- **C14.** (a) 0.3: $11.8B across 26 humanoid firms; Waymo has raised over $27B; Unitree's build cost is near $9k — ROBO; [Robotics 24/7](https://www.robotics247.com/article/humanoid-orders-vs-actual-deployments-how-much-commercial-progress-is-really-happening). (b) π 0.65, r 0.2: FCC barred new foreign robots in July 2026 and China threatened countermeasures — ROBO; [The Next Web](https://thenextweb.com/news/china-retaliation-us-fcc-robot-import-ban-rare-earths). (c) d1 2.5, d2 2.0: no published safety standard for balancing robots until late 2026-2027 — ROBO; [i-SCOOP](https://www.i-scoop.eu/iso-25785-1-explained-and-what-it-means-for-humanoid-robot-safety/); robotaxi exemptions are capped at 2,500 vehicles a year — ROBO; [Federal Register](https://public-inspection.federalregister.gov/2026-15485.pdf). (d) 1.5: buyers expect 99.99% reliability — SKEP; [IEEE Spectrum](https://spectrum.ieee.org/humanoid-robot-scaling). (e) 0.4. (f) 0.4.
- **C15.** (a) 0.2 and (c) d1 8: a new airliner takes 8-15 years and $7-25B; the duopoly used a 292% duty against the CSeries — AVIA; [Wikipedia, Airbus A220](https://en.wikipedia.org/wiki/Airbus_A220). No revenue by 2032.
- **C16.** (a) 0.8: the Navy outsources modules to more than 20 companies and split 30 unmanned hulls three ways. (b) π 0.9: statute bars foreign build. (c) d1 2.5, d2 1.5: Saronic's Series A was Oct 2023 and its large Navy award Dec 2025; new yards face a steep learning curve. (e) 0.5: workforce and sole-source suppliers. (f) 0.35: frigate and cutter cancellations. Capital: Saronic's Port Alpha is $3B. All — DEFN; [CBO testimony](https://armedservices.house.gov/UploadedFiles/2026-04-22_Labs_Testimony.pdf); [Sacra, Saronic](https://sacra.com/c/saronic/).
- **C17.** (a) 0.6: three OEMs capping expansion. (c) d1 4, d2 1.5: Boom raised $300M and has not delivered; ENER puts turbine hot-section supply and microreactors at $500M+ and 4+ years. (e) 0.5: single-crystal blades from a handful of suppliers. (f) 0.4: orders expected to peak in 2026. All — ENER; [POWER Magazine](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/); [Wood Mackenzie](https://www.woodmac.com/press-releases/gas-turbine-prices-soar-195-as-market-faces-supply-demand-crisis).
- **C18.** (a) 1.5: fly-offs place orders within days and awards are split three or four ways, but each program has four or more funded vendors. (c) d1 1.0, d2 1.0. (e) 0.65: compliant components were the Gauntlet I bottleneck. (f) 0.4. Capital: Neros $250M Series C. All — DEFN; [DroneXL](https://dronexl.co/2026/09/30/neros-gauntlet-ii-100-million-order-800-bonus-drones/); [DefenseScoop](https://defensescoop.com/2026/05/15/defense-department-low-cost-containerized-missile-contracts/).
- **C19.** (a) 0.4: Indian non-profits already sell at cost and the Big Five own the channels. (b) π 0, r 0.4: no protection; United Imaging's overseas revenue grew 42%. (c) d1 1.5, d2 1.0; (d) 2.0: Hyperfine sells 40-50 units a year five years after clearance. (e) 0.4: fitting, clinicians, ability to pay. All — MED; [Capitol Forum](https://thecapitolforum.com/four-years-after-otc-hearing-aid-rule-competition-in-hearing-aid-market-remains-limited/); [MD+DI](https://www.mddionline.com/business/hyperfine-hits-cash-flow-milestone-as-q3-revenue-finally-outpaces-cash-burn).

Evidence for the uniform share and ramp assumptions
- Shares actually reached by entrants: York $386M of a $20.4B satellite manufacturing market (about 1.9%) and Apex $60M (about 0.3%) in year three [D] — AVIA; [Contrary Research](https://research.contrary.com/company/apex). Slate's full plan of 150,000 a year would be about 0.9% of 16.68M US vehicles [D] — CONS and FRED. Neros took 5,200 of the 22,320 Gauntlet I orders (23%) [D] — DEFN; [DroneXL](https://dronexl.co/2026/09/30/neros-gauntlet-ii-100-million-order-800-bonus-drones/)
- Ramp: nearly every WWII aircraft type needed over a year to go from unit 5 to unit 500 [SE] — HIST; [Construction Physics](https://www.construction-physics.com/p/how-to-build-300000-airplanes-in). Saronic went from $12.5M (2024) to about $200M (2025) on one contract [SE] — DEFN; [Sacra](https://sacra.com/c/saronic/)
- Capital per dollar of revenue: Anduril about $5 raised per $1 of 2025 revenue [D in SKEP] — SKEP; [TechCrunch](https://techcrunch.com/2026/05/13/anduril-raises-5b-doubles-valuation-to-61b/). A $150M plant builds 57 large transformers a year [SE] — ENER; [Foley](https://www.foley.com/insights/publications/2026/09/the-grids-bottleneck-isnt-just-money-its-materials/)

### Inferences
Formulas (applied identically to every candidate; t runs 2027 to 2032; capital is committed at the start of 2027)
- Price path: p_t = 1 - ΔP × (t - 2026) / 6, with ΔP the plausible total price change from table 2b.
- Served market: S_t = S0 × (1 + g)^(t - 2026); at 2032 prices it is S_t × p_t^(1 - elasticity).
- Shortage: U_t = U0 × max(0, (Y_close - t) / (Y_close - 2026)) × p_t. The shortage shrinks in a straight line to zero at the close year. This is factor (a), incumbent capacity.
- New uses: N_t = N × probability × (t - 2026) / 6.
- Cycle (f): the shortage and the growth above today's market are multiplied by (1 - p_f).
- Entrant ceiling_t = m_a × m_b × m_e × [ s_U × U_t × (1 - p_f) + s_S × ( S0 × p_t^(1 - ε) + (S_t - S0) × p_t^(1 - ε) × (1 - p_f) + N_t ) ], with m_b = π + (1 - π) × r.
- Uniform shares [A]: s_U = 5% / 10% / 20% of the shortage pool and s_S = 1% / 2% / 5% of the served market (low / base / high), set from the York, Apex, Slate and Neros shares above.
- Timing (c, d): first revenue F = 2027 + d1; volume year V = 2027 + d1 + d2 + d3. Revenue_t = ceiling_t × ramp(t - V), where ramp = 10%, 25%, 50%, 75%, 90%, 100% at 0, 1, 2, 3, 4, 5 years after V (linear in between) and 3% between F and V (development contracts and pilots).
- Capital: K = K1 + κ × planned 2032 revenue, where planned revenue is the same formula without the m_b, m_e and p_f haircuts (the plant is sized to the plan, not to the expected value). κ = 0.75 to 1.0 for assembly or contract-built goods, 1.5 for process plants and clinics, 3.0 for owned fleets and shipyards [A, from the benchmarks above].
- Low and high: low uses the low value of every market input and share, one year more delay, m_a, m_e and π × 0.75, and p_f × 1.5. High uses the high values, half a year less delay, m_a × 1.25, m_e and π moved halfway to 1, and p_f × 0.5. These are all-at-once bounds, so they are very wide. The Monte Carlo columns draw each input from a triangular distribution over the same ranges and report the 10th, 50th and 90th percentiles.

Table 4a. Actor-response parameters (script inputs; justifications above).

| ID | Trend growth g/yr (low/base/high) | (a) Structure and incumbent response m_a | (b) P(protection persists) π; surviving share r; m_b = π+(1-π)r | (c) Years to first revenue d1; extra to volume d2 | (d) Adoption lag d3 (years) | Volume year V = 2027+d1+d2+d3 | (e) Complements m_e | (f) Cyclical risk p_f | Entry capital K1 ($M); κ |
|---|---|---|---|---|---|---|---|---|---|
| C1 | 3% / 6.0% / 9% | 1.2 | 0.95; 0.7; 0.98 | 2; 1 | 0.5 | 2030.5 | 0.75 | 0.25 | 100; 1.5 |
| C2 | 7% / 15.3% / 25% | 1 | 0.6; 0.6; 0.84 | 1.5; 0.5 | 0.5 | 2029.5 | 0.8 | 0.4 | 100; 1 |
| C3 | 3% / 6.0% / 9% | 0.7 | 0.6; 0.5; 0.80 | 2.5; 1.5 | 1 | 2032 | 0.75 | 0.5 | 300; 1.5 |
| C4 | 10% / 20.0% / 35% | 1.2 | 0.75; 0.2; 0.80 | 1; 0.5 | 0.5 | 2029 | 0.65 | 0.35 | 40; 1 |
| C5 | 0% / 5.0% / 10% | 2.5 | 0.98; 0.9; 1.00 | 1.5; 1.5 | 0.5 | 2030.5 | 0.7 | 0.4 | 100; 1.5 |
| C6 | 3% / 8.0% / 15% | 0.8 | 0.95; 0.8; 0.99 | 2; 1 | 0.5 | 2030.5 | 0.75 | 0.3 | 150; 1.5 |
| C7 | 20% / 40.0% / 70% | 0.3 | 0.7; 0.3; 0.79 | 1.5; 1.5 | 1 | 2031 | 0.6 | 0.2 | 100; 1 |
| C8 | -5% / 0.0% / 5% | 0.8 | direct m_b = 0.9 | 1; 1 | 1 | 2030 | 0.6 | 0.3 | 50; 3 |
| C9 | -3% / 0.0% / 3% | 0.5 | direct m_b = 1 | 1.5; 1 | 1 | 2030.5 | 0.5 | 0.3 | 50; 1.5 |
| C10 | 8% / 15.0% / 20% | 1 | direct m_b = 0.95 | 3; 1.5 | 0.5 | 2032 | 0.7 | 0.25 | 500; 1.5 |
| C11 | 15% / 30.0% / 50% | 1 | direct m_b = 1 | 1; 0.5 | 0.5 | 2029 | 0.7 | 0.3 | 100; 1.5 |
| C12 | -2% / 0.0% / 2% | 0.5 | 0.7; 0.2; 0.76 | 3; 0.5 | 1 | 2031.5 | 0.7 | 0.3 | 1,500; 0.75 |
| C13 | -2% / 1.0% / 3% | 0.8 | direct m_b = 0.9 | 1; 0.25 | 2.5 | 2030.75 | 0.6 | 0.3 | 30; 1 |
| C14 | 10% / 30.0% / 60% | 0.3 | 0.65; 0.2; 0.72 | 2.5; 2 | 1.5 | 2033 | 0.4 | 0.4 | 1,500; 1.5 |
| C15 | 3% / 4.0% / 5% | 0.2 | direct m_b = 0.95 | 8; 2 | 2 | 2039 | 0.4 | 0.3 | 20,000; 1.5 |
| C16 | 0% / 3.0% / 8% | 0.8 | 0.9; 0.5; 0.95 | 2.5; 1.5 | 0.5 | 2031.5 | 0.5 | 0.35 | 1,000; 3 |
| C17 | -5% / 2.0% / 5% | 0.6 | direct m_b = 0.95 | 4; 1.5 | 1 | 2033.5 | 0.5 | 0.4 | 500; 1.5 |
| C18 | 5% / 15.0% / 30% | 1.5 | 0.98; 0.9; 1.00 | 1; 1 | 0.5 | 2029.5 | 0.65 | 0.4 | 250; 1.5 |
| C19 | 2% / 5.0% / 8% | 0.4 | 0; 0.4; 0.40 | 1.5; 1 | 2 | 2031.5 | 0.4 | 0.15 | 20; 1.5 |

Table 4b. Year-by-year base case (script output).

| ID | Served market 2032 at 2032 prices ($B) | Shortage left 2032 ($B) | Weighted new uses 2032 ($B) | Ramp in 2032 | Risk-adjusted entrant revenue $M: 2027 | 2028 | 2029 | 2030 | 2031 | 2032 | Sum 2027-32 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| C1 | 43.8 | 1.04 | 0.30 | 0.38 | 0.0 | 0.0 | 29 | 27 | 149 | 298 | 503 |
| C2 | 38.7 | 0.00 | 1.50 | 0.62 | 0.0 | 0.0 | 12 | 63 | 146 | 263 | 484 |
| C3 | 12.9 | 0.00 | 0.15 | 0.10 | 0.0 | 0.0 | 0.0 | 2.7 | 2.8 | 9.4 | 15 |
| C4 | 4.5 | 0.00 | 2.00 | 0.75 | 0.0 | 1.2 | 4.4 | 12 | 29 | 51 | 97 |
| C5 | 5.6 | 0.00 | 2.00 | 0.38 | 0.0 | 0.0 | 10 | 8.5 | 40 | 92 | 150 |
| C6 | 19.0 | 0.00 | 1.50 | 0.38 | 0.0 | 0.0 | 5.3 | 5.7 | 36 | 82 | 129 |
| C7 | 0.5 | 0.00 | 0.35 | 0.25 | 0.0 | 0.0 | 0.0 | 0.0 | 0.2 | 0.5 | 0.7 |
| C8 | 13.4 | 0.00 | 1.50 | 0.50 | 0.0 | 3.5 | 3.6 | 12 | 31 | 64 | 115 |
| C9 | 15.9 | 0.00 | 1.80 | 0.38 | 0.0 | 0.0 | 2.7 | 2.7 | 16 | 33 | 54 |
| C10 | 3.7 | 0.00 | 1.75 | 0.10 | 0.0 | 0.0 | 0.0 | 1.6 | 1.7 | 6.6 | 9.9 |
| C11 | 1.5 | 0.00 | 0.60 | 0.75 | 0.0 | 0.3 | 1.2 | 3.9 | 9.8 | 18 | 34 |
| C12 | 40.2 | 0.00 | 0.60 | 0.17 | 0.0 | 0.0 | 0.0 | 6.7 | 6.6 | 38 | 51 |
| C13 | 25.3 | 0.00 | 0.30 | 0.31 | 0.0 | 6.5 | 6.5 | 6.5 | 30 | 68 | 117 |
| C14 | 12.1 | 0.00 | 2.40 | 0.03 | 0.0 | 0.0 | 0.0 | 0.4 | 0.4 | 0.6 | 1.3 |
| C15 | 146.3 | 12.76 | 0.00 | 0.00 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| C16 | 56.6 | 4.48 | 1.20 | 0.17 | 0.0 | 0.0 | 0.0 | 18 | 17 | 92 | 126 |
| C17 | 51.6 | 2.47 | 0.60 | 0.03 | 0.0 | 0.0 | 0.0 | 0.0 | 11 | 9.8 | 21 |
| C18 | 12.5 | 0.00 | 2.80 | 0.62 | 0.0 | 6.1 | 6.1 | 36 | 80 | 152 | 280 |
| C19 | 5.4 | 0.00 | 1.00 | 0.17 | 0.0 | 0.0 | 0.2 | 0.2 | 0.2 | 1.4 | 2.1 |

Table 4c. Risk-adjusted 2032 revenue and capital, ranked by base revenue per dollar of capital (script output).

| Rank by revenue per $ | ID | Candidate | Risk-adjusted 2032 revenue $M: all-low / base / all-high | Monte Carlo P10 / P50 / P90 ($M) | Planned 2032 revenue before probability haircuts ($M) | Capital to get there K = K1 + κ×plan ($M) | Base risk-adjusted revenue per $ of capital | P50 revenue per $ of capital |
|---|---|---|---|---|---|---|---|---|
| 1 | C2 | Data-center / large-load power blocks | 21 / **263** / 2,722 | 178 / 309 / 522 | 503 | 603 | **0.44** | 0.51 |
| 2 | C13 | Short-lead kitchens/cabinets, installed products | 2.9 / **68** / 838 | 39 / 75 / 138 | 128 | 158 | **0.43** | 0.48 |
| 3 | C1 | Fast long-lead metal parts | 15 / **298** / 3,036 | 171 / 313 / 548 | 444 | 765 | **0.39** | 0.41 |
| 4 | C4 | China-free drone/robot components | 1.8 / **51** / 1,213 | 43 / 82 / 153 | 117 | 157 | **0.32** | 0.52 |
| 5 | C5 | Rocket motors, energetics, cheap interceptors | 4.9 / **92** / 1,618 | 66 / 122 / 221 | 142 | 312 | **0.29** | 0.39 |
| 6 | C6 | Satellite buses and space components | 4.7 / **82** / 1,094 | 54 / 100 / 181 | 123 | 335 | **0.25** | 0.30 |
| 7 | C18 | Low-cost cruise missiles, attritable drones (ref) | 7.5 / **152** / 2,914 | 120 / 220 / 390 | 288 | 682 | **0.22** | 0.32 |
| 8 | C9 | Factory-built housing (ADU, HUD infill, pods) | 1.8 / **33** / 356 | 21 / 38 / 67 | 67 | 150 | **0.22** | 0.25 |
| 9 | C8 | Productized home solar + battery | 2.9 / **64** / 723 | 41 / 73 / 126 | 119 | 407 | **0.16** | 0.18 |
| 10 | C11 | Cash-pay scan / diagnostic clinics | 0.5 / **18** / 417 | 14 / 27 / 51 | 32 | 148 | **0.12** | 0.19 |
| 11 | C16 | Commercial and naval ships (ref) | 2.2 / **92** / 1,193 | 24 / 104 / 187 | 225 | 1,674 | **0.05** | 0.06 |
| 12 | C19 | Medical devices for emerging markets (ref) | 0.0 / **1.4** / 63 | 0.6 / 2.6 / 5.5 | 8.9 | 33 | **0.04** | 0.08 |
| 13 | C3 | Scarce HV grid components | 0.4 / **9.4** / 138 | 2.3 / 4.7 / 19 | 18 | 327 | **0.03** | 0.01 |
| 14 | C12 | Affordable vehicles + MOSAIC aircraft | 0.7 / **38** / 513 | 10.0 / 42 / 84 | 71 | 1,554 | **0.02** | 0.03 |
| 15 | C17 | Gas turbines and microreactors (ref) | 0.8 / **9.8** / 82 | 6.5 / 11 / 18 | 23 | 535 | **0.02** | 0.02 |
| 16 | C10 | Automated cell-therapy manufacturing | 0.1 / **6.6** / 118 | 1.6 / 3.4 / 13 | 11 | 516 | **0.01** | 0.01 |
| 17 | C7 | Delivery-drone airframes | 0.0 / **0.5** / 26 | 0.4 / 1.0 / 2.0 | 1.2 | 101 | **0.01** | 0.01 |
| 18 | C14 | Humanoid robots and robotaxi vehicles | 0.0 / **0.6** / 32 | 0.6 / 1.2 / 2.4 | 2.6 | 1,504 | **0.00** | 0.00 |
| 19 | C15 | Commercial airliners and jet engines (ref) | 0.0 / **0.0** / 0.0 | 0.0 / 0.0 / 0.0 | 0.0 | 20,000 | **0.00** | 0.00 |

- Reading the result. Worked example, C2: served market 2032 = $20B × 1.153^6 × 0.759^0.7 = $38.7B; cycle-adjusted pool = $20B × 0.824 + $27B × 0.824 × 0.6 + $1.5B = $31.4B; × 2% share × 1.0 × 0.84 × 0.8 = $422M ceiling; × ramp 0.625 (volume from mid-2029) = $263M. Planned revenue without the haircuts is $503M, so capital = $100M + 1.0 × $503M = $603M and the ratio is 0.44.
- The shortage adds little to 2032 revenue in any row, because straight-line closure and the ramp leave a small overlap (table 3d). An entrant that reaches volume a year earlier does much better: C2 rises from $263M to $347M in 2032 and from $484M to $806M cumulative; C1 from $298M to $496M and from $503M to $1,003M (script scenario runs).
- The Monte Carlo median sits above the deterministic base in most rows because the input ranges are skewed upward (the high values for shares, new-use pools and market size lie further from the base than the low values). Read the base as a cautious central case and P10-P90 as the plausible band.
- These are revenues for an average new entrant, not for the category leader. Real leaders have done better (Saronic about $200M in its second revenue year; Anduril $2.2B) and most entrants have done worse (Boxabl $2.6M in nine months). The uniform 2% share is the single largest driver and is the same for every row, so it does not change the ranking.
- The ratio does not include firm-level survival odds. SKEP's base rates say businesses needing $1B+ before proof (C12, C14, C15, C16) have mostly failed, and that under-$50M successes used existing contract manufacturing. Applying those odds would widen the gap between the top six and the rest.

### Gaps
- The share, ramp and capital-intensity assumptions are uniform by design and rest on a handful of named cases with survivorship bias (SKEP makes the same caveat about its tiers).
- The model has no explicit price response by incumbents beyond erosion of scarcity rent; where incumbents hold 65-95% gross margins (MED: hearing aids, aligners, GLP-1s) they can cut price further than the model allows. None of the 19 rows is in that group except C19.
- Straight-line closure of each shortage is a simplification. Wood Mackenzie's own view is that most transformer types stay in marginal shortage in 2030 (ENER), which the base case for C2 and C3 does not credit.


## 5. Model T test: which candidates match the conditions for a 10x+ expansion

### Takeaway
No candidate passes all seven conditions. The closest true Model T case is low-cost munitions and attritable drones (C18), where a roughly 13x price cut has already produced a roughly 200x increase in planned annual buys, and its component layer (C4) scores highest overall. Humanoids and robotaxis (C14) pass on paper but fail on capability and complements. Home solar (C8) and cash-pay scans (C11) have real elastic consumer demand, but the price lever is process or product redesign, not the factory. C1, C2, C3, C5, C10, C15 and C17 are shortage plays; C4, C5, C6, C16 and C18 are protected-market plays; C9, C12, C13 and C19 are neither.

### Cited Findings
- The seven conditions come from the historical screen: market-level elasticity above 1 (ideally above 1.5), penetration under about 20% of need, price well above the materials floor with conversion the largest share, production rather than site, land, permit or installation as the binding constraint, complements available or bundled, demand not positional, and a 15-25% learning rate, which appears only in small, modular, frozen-design factory goods [inference in HIST from its cited cases] — HIST sections 4 and 6; [NBER WP 31454](https://www.nber.org/papers/w31454); [Construction Physics](https://www.construction-physics.com/p/where-are-my-damn-learning-curves)
- Model T itself: real price down about 75% from 1909 to 1921 while Ford output rose about 91x; the decisive step was a roughly 6x cut against the average 1908 car, aimed at buyers who owned no car; the same car priced 20-130% higher abroad produced no mass market [SE/D] — HIST; [NBER WP 31454](https://www.nber.org/papers/w31454)
- Positional penalty: Tata Nano peaked at 74,527 units against a 250,000 plan [M] — HIST and SKEP; [Wikipedia, Tata Nano](https://en.wikipedia.org/wiki/Tata_Nano)
- Complements set the pace: air conditioning took 45 years to go from 10% to 80% of US homes; radio and color TV took 10-15 [M] — HIST; [Our World in Data](https://ourworldindata.org/grapher/technology-adoption-by-households-in-the-united-states)
- Vehicle stock is about 800 per 1,000 people in the US [SE, 2024] — CONS; [Wikipedia, motor vehicles per capita](https://en.wikipedia.org/wiki/List_of_countries_and_territories_by_motor_vehicles_per_capita)
- China-versus-West humanoid bill-of-materials gap is roughly 3-6x; Unitree earns about 60% gross margin [SE/D] — ROBO; [KrASIA](https://kr-asia.com/what-is-the-secret-behind-unitrees-high-gross-margins)

### Inferences
Scoring rules (0 = fail, 1 = partial, 2 = pass). Conditions 1, 3, 5 and 7 are computed from model inputs: (1) base elasticity 1.5 or more = 2, 1.0 or more = 1; (3) materials share 20% or less = 2, 40% or less = 1; (5) complements multiplier 0.8 or more = 2, 0.6 or more = 1; (7) class A_new = 2, B or A_mat = 1, C = 0. Conditions 2, 4 and 6 are my judgment from the notes: (2) served share of need under 20% = 2, 20-50% = 1; (4) production is the gate = 2, mixed = 1, regulation, land, installation or capability = 0; (6) utilitarian or business demand = 2, some status or stigma = 1, clearly positional = 0.

| ID | Candidate | 1 Elasticity >1 | 2 Low penetration vs need | 3 Price far above materials floor | 4 Production is the binding constraint | 5 Complements available | 6 Demand not positional | 7 Learning 15-25% (modular, frozen design) | Score /14 |
|---|---|---|---|---|---|---|---|---|---|
| C4 | China-free drone/robot components | 1 | 2 | 1 | 2 | 1 | 2 | 2 | **11** |
| C11 | Cash-pay scan / diagnostic clinics | 1 | 2 | 2 | 1 | 1 | 2 | 1 | **10** |
| C14 | Humanoid robots and robotaxi vehicles | 2 | 2 | 2 | 0 | 0 | 2 | 2 | **10** |
| C5 | Rocket motors, energetics, cheap interceptors | 1 | 1 | 1 | 2 | 1 | 2 | 1 | **9** |
| C8 | Productized home solar + battery | 1 | 2 | 2 | 0 | 1 | 2 | 1 | **9** |
| C18 | Low-cost cruise missiles, attritable drones (ref) | 2 | 1 | 0 | 1 | 1 | 2 | 2 | **9** |
| C2 | Data-center / large-load power blocks | 0 | 0 | 1 | 2 | 2 | 2 | 1 | **8** |
| C6 | Satellite buses and space components | 1 | 1 | 1 | 1 | 1 | 2 | 1 | **8** |
| C7 | Delivery-drone airframes | 1 | 2 | 0 | 0 | 1 | 2 | 2 | **8** |
| C10 | Automated cell-therapy manufacturing | 1 | 1 | 1 | 2 | 1 | 2 | 0 | **8** |
| C1 | Fast long-lead metal parts | 0 | 0 | 1 | 2 | 1 | 2 | 1 | **7** |
| C15 | Commercial airliners and jet engines (ref) | 0 | 1 | 2 | 1 | 0 | 2 | 0 | **6** |
| C17 | Gas turbines and microreactors (ref) | 0 | 0 | 2 | 2 | 0 | 2 | 0 | **6** |
| C19 | Medical devices for emerging markets (ref) | 0 | 2 | 2 | 0 | 0 | 1 | 1 | **6** |
| C3 | Scarce HV grid components | 0 | 0 | 1 | 1 | 1 | 2 | 0 | **5** |
| C13 | Short-lead kitchens/cabinets, installed products | 0 | 0 | 1 | 1 | 1 | 1 | 1 | **5** |
| C9 | Factory-built housing (ADU, HUD infill, pods) | 0 | 0 | 1 | 0 | 0 | 1 | 1 | **3** |
| C16 | Commercial and naval ships (ref) | 0 | 0 | 0 | 1 | 0 | 2 | 0 | **3** |
| C12 | Affordable vehicles + MOSAIC aircraft | 0 | 0 | 0 | 0 | 1 | 0 | 1 | **2** |

Judgment scores and their basis
- Condition 2 (penetration). Scored 2: C4 (compliant supply is a small fraction of a market over 90% Chinese-sourced), C7 (a few million deliveries a year against billions of trips), C8 (7% of homes), C11 and C14 (near zero), C19 (under 10% of hearing need met). Scored 1: C5 and C18 (output is a fraction of orders or of what a peer combatant uses), C6, C10 (about 20% of eligible patients), C15. Scored 0: C1, C2, C3, C9, C12, C13, C16, C17 (the need is mostly served; the gap is a queue or a quality step).
- Condition 4 (binding constraint). Production: C1, C2, C4, C5, C10, C17. Mixed: C3 (utility qualification), C6 (funding and launch), C11, C13, C15, C16, C18 (appropriations and qualification). Not production: C7 (Part 108), C8 (installation and selling), C9 (land, zoning, finance), C12 (trade and safety rules), C14 (capability), C19 (fitting and distribution).
- Condition 6 (positional). C12 scores 0 (the Nano and two-door evidence), C9, C13 and C19 score 1 (manufactured-home and hearing-aid stigma; kitchens are partly taste goods where buyers may trade up as with diamonds).

Classification
- True Model T pattern (a new mass market at a much lower price): C18. Caveat: one budget-capped buyer class, and planned quantities depend on appropriations. C4 is the same curve one tier down and has the highest score (11) because production is the gate and the buyer base is 20+ firms; its price umbrella is the legal exclusion of Chinese parts.
- Model T conditions met on paper, not yet in practice: C14 (score 10; fails on capability and complements, and a Chinese producer already holds the cost position), C7 (score 8; unit demand could rise 10x from a tiny base once Part 108 is in force, but operators build their own aircraft).
- Elastic consumer demand where the lever is not production: C8 (score 9) and C11 (score 10). They resemble the Model T's "new product for a new buyer" step, delivered through process (C8) and a redefined product (C11). A founder would be building an installer or a clinic chain.
- Shortage plays (sell speed into a backlog): C1, C2, C5 (inside a protected market), C10 (slots ration access), C3 (window closing before a new plant qualifies), and the reference rows C15 and C17 (shortage real, not reachable by 2032).
- Protected-market plays (sell compliance and origin): C4, C5, C6, C16, C18. C12 is not viable without protection but is not protected enough to earn a margin from it.
- Neither: C9 (inelastic, positional, land- and finance-bound), C12 (elasticity 0.34-0.84, saturated), C13 (channel and lead-time arbitrage in a flat market), C19 (products already at the materials floor; delivery is the gate).

### Gaps
- Conditions 2, 4 and 6 are scored by judgment; a different reader could move individual scores by one point. The classification is robust to that for C9, C12, C16 (bottom) and C4, C18 (top), less so for the middle group scoring 8.
- The test says nothing about who captures the profit; HIST keeps that as a separate screen and section 6 addresses it.

## 6. Where the cost saving from abundant production flows

### Takeaway
In the model the entrant keeps the saving only while one of two things holds: a shortage (the scarcity margin, 5-40% of price in C1-C6 and C17) or a legal wall against Chinese supply. When those end, the measured pattern is that buyers or channel owners take it. In C8, C9, C11, C12, C13 and C19 production can touch 3-26% of delivered price, so most of any saving is decided by installers, lenders, land, dealers and clinics.

### Cited Findings
- Commodity producers after a cost collapse: Jinko module gross margin -2.01% and LONGi module business -3.53% in H1 2025 [M] — SKEP; [pv magazine](https://www.pv-magazine.com/2025/09/05/chinese-pv-industry-brief-top-4-module-manufacturers-post-heavy-losses-in-h1/)
- Contract assembly: Hon Hai net margin about 2.3% in 2025 [D in SKEP] — SKEP; [Wikipedia, Foxconn](https://en.wikipedia.org/wiki/Foxconn)
- Scale leaders with a technical lead keep margin: CATL and Unitree about 17% net in 2025 [D in SKEP] — SKEP; [Wikipedia, CATL](https://en.wikipedia.org/wiki/CATL)
- Certified sole-source parts: TransDigm EBITDA margin near 54% [SE] — SKEP; [Motley Fool](https://www.fool.com/data-news/2025/08/06/transdigm-tdg-q3-margin-hits-54). Howmet net margin 18% [D: $1.51B / $8.25B, 2025] — fetched: [Wikipedia, Howmet Aerospace](https://en.wikipedia.org/wiki/Howmet_Aerospace)
- Incumbents in shortage hold price: Siemens Energy prioritises "value over volume"; GE Vernova's 2026 turbine order pricing is on track for +50% year on year [SE] — ENER; [POWER Magazine](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/); [Utility Dive](https://www.utilitydive.com/news/ge-vernova-in-9b-deal-to-buy-high-voltage-manufacturer-as-gas-turbine-orde/873223/)
- Channel keeps the margin: jewelers' markup over lab-grown wholesale stayed above 80% while wholesale fell 26% in 2025 [SE] — CONS; [JCK](https://www.jckonline.com/editorial-article/lab-grown-wholesale-freefall/)
- Installer profit is 17-18% of price in both the US and Australia; the US difference is selling, permitting and labor [SE] — CONS; [Boston University](https://www.bu.edu/eci/files/2025/07/Intnatl-Cost-Comparisons-final.pdf)
- Housing: Cavco's financial-services gross margin was 69.4% in its fourth quarter against 22.1% for factory-built housing [M/SE, FY2026] — HOUS; [Cavco 8-K](https://www.sec.gov/Archives/edgar/data/0000278166/000162828026037575/cvco-2026328xex991.htm); [Nasdaq](https://www.nasdaq.com/articles/cavco-industries-q4-earnings-call-highlights)
- Vehicles: about 87% of BYD's estimated $4,700 cost edge is supplier integration and overhead, not labor or subsidy [D in SKEP, secondary source] — SKEP; [The Star](https://www.thestar.com.my/business/business-news/2026/06/09/the-real-story-behind-chinas-manufacturing-might)
- Defense buyer practice: low-cost missile contracts are firm-fixed-price with minimum quantity floors, and awards are deliberately split [SE] — DEFN; [DefenseScoop](https://defensescoop.com/2026/05/15/defense-department-low-cost-containerized-missile-contracts/)
- Cell therapy: list prices are $462,000-$594,000 against COGS estimates of $35,000-$220,000; Spain's hospital-made product is reimbursed at about $101,000 [SE] — MED; [BioProcess Online](https://www.bioprocessonline.com/doc/closing-the-car-t-access-gap-with-hospital-based-manufacturing-0001)
- Hearing aids: all five large makers own US retail clinic networks and four run hearing benefit managers [SE] — MED; [Capitol Forum](https://thecapitolforum.com/four-years-after-otc-hearing-aid-rule-competition-in-hearing-aid-market-remains-limited/)

### Inferences
Table 6. Who receives the saving (my reading of the evidence; "touchable" is C + R from table 2b).

| ID | Touchable share of price | While the shortage or legal wall lasts | Afterwards | Evidence used |
|---|---|---|---|---|
| C1 | 55% | Entrant and incumbents (scarcity margin, rush premiums) | Engine and defense primes through 5-7 year contracts; certificate holders keep above-normal margin | Howmet 18% net, TransDigm 54% EBITDA; suppliers choose margin over capacity |
| C2 | 58% | Entrant (15 points of scarcity margin; buyers pay for schedule) | Hyperscale buyers, once roughly $2B of incumbent capacity lands | Margins up 4-5x since 2020; deficits forecast to narrow by 2030 |
| C3 | 50% | Incumbents with utility vendor-list positions | Utilities and ratepayers | GE Vernova paying $9B for a component maker |
| C4 | 55% | Entrant, sized by the legal wall (3-6x China gap) | Drone and robot makers and their government buyer; commodity pricing | $5,000 to $2,000 target price; integrated makers build in-house |
| C5 | 50% | Shared: buyer funds capacity, vendors get volume | Government buyer (fixed price, split awards) | Northrop second-source deal; 46% planned budget drop |
| C6 | 40% | Government buyer and the vertically integrated leader | Same | Starlink builds at under $1M a unit in-house; merchant buses $3.5-5.7M |
| C7 | 35% | Integrated operators and retailers | Same | Operators build their own aircraft |
| C8 | 5% | Hardware savings already passed to buyers in open markets; US price is held up by selling, permitting, tariffs | Homeowner if installers compete; otherwise installer and financier | Panels 5-7% of price; marketing 20-29% |
| C9 | 26% | Land owners, lenders and local market price | Same; incumbents' captive finance | 47% of price is outside the factory; chattel rates 8.6% vs 4.1% |
| C10 | 60% | Licence holders (list price is not cost-based); entrant earns capacity fees | Payers, if hospital or low-cost products spread | $101k Spain vs about $500k list |
| C11 | 4% | Clinic operator that owns the customer | Customers, as clinic chains compete | $499 vs $2,499 price points |
| C12 | 20% | Buyers; the tariff wall sets the ceiling | Buyers | Dealer front-end 4.9%; RV-maker gross 12.6% |
| C13 | 26% | Entrant only if it owns the channel; otherwise dealers and installers | Customers | Channel layers of 15-30% each (seller claim) |
| C14 | 60% | Cost leaders with integrated components; compute and model owners | Buyers | Unitree 60% gross margin; one chip vendor holds 80%+ of humanoid compute |
| C15 | 55% | Engine makers and the duopoly | Same | Overhaul spend +68% on 10% more flying |
| C16 | 40% | Navy and yard labor | Same | Wage contracts +40-45% over five years |
| C17 | 75% | Turbine makers and blade suppliers (40 points of scarcity margin) | Power buyers after about 2033 | Prices +195% since 2019; service margins five points higher |
| C18 | 30% | Government buyer | Government buyer | Fixed-price floors; four or more vendors per program |
| C19 | 3% | Clinic channel and benefit managers | Same | Manufacturing is about 6% of hearing-aid retail price |

- General rule from the cases: the producer keeps the saving when it is alone on the cost curve (Ford for about 15 years), holds a certificate or sole-source position, or also owns the demand. With China already on the cost curve in most categories (SKEP), a Western entrant's margin is the shortage premium or the legal wall, and both have an end date in the model (shortage close years 2029-2035; protection probability 0.6-0.98 where protection exists).
- Speed is paid for more reliably than cost. In C1, C2, C3 and C17 the plausible entrant lead-time cut is 65-75% while the production price cut is 11-24%, and elasticity is below 1, so a discount shrinks the market while a faster slot does not.

### Gaps
- No file gives a measured pass-through rate (what share of a cost cut reached buyers) for any candidate. The table is qualitative.
- Gross margins for Hadrian, Machina, Divergent, Cellares, Neko, Base Power and every drone and missile entrant are undisclosed, so the entrant's own share of the saving cannot be checked against results.

## 7. Sensitivity: which assumptions move the result

### Takeaway
For every candidate the uniform entrant-share assumption moves the result most (half or 2.5 times the base). After that, time to volume is the largest driver for C1, C5, C8, C9, C12 and C16; trend growth for C2 and C18; today's market size for C6 and C13; and the new-use pool for C4 and C11. Reaching volume one year earlier adds about two-thirds to C1's 2032 revenue and about a third to C2's, and roughly doubles C1's cumulative 2027-32 revenue. If legal protection lapses, C4 falls about 75% and C12 about 74%.

### Cited Findings
- Policy half-life: US clean-manufacturing support lasted about three years (2022-2025) [SE] — SKEP; [Rhodium Group](https://rhg.com/wp-content/uploads/2026/05/Worlds-Apart-Contrasting-US-China-Approaches-to-Scaling-Clean-Technology-Manufacturing-1.pdf)
- Utility data-center load forecasts may be overstated by about 40% [SE] — ENER; [Canary Media](https://www.canarymedia.com/articles/data-centers/data-center-power-forecasts-climb-to-unreachable-heights)
- Factory timing has slipped before: a $469M shell-body plant built on an unproven process had produced nothing two years on [SE] — DEFN; [Breaking Defense](https://breakingdefense.com/2026/07/army-well-short-of-155mm-ammo-production-goal-texas-facility-in-the-spotlight/)
- The munitions plan itself falls from $49.5B (FY2027) to an average $26.7B (FY2028-31) [SE] — DEFN; [CNAS](https://www.cnas.org/publications/reports/munitions-procurement-and-the-fiscal-year-2027-defense-budget)

### Inferences
Table 7a. One-at-a-time sensitivity of base 2032 risk-adjusted revenue (script output). Each cell shows the result if that assumption alone takes its low value and its high value (ranges as defined in section 4). The uniform share assumption is excluded from the ranking because it scales every row the same way: with shares at 5% and 1% every result halves; at 20% and 5% it rises about 2.5 times.

| ID | Base 2032 revenue ($M) | Assumption 1: result if low / if high ($M) | Assumption 2: result if low / if high ($M) | Assumption 3: result if low / if high ($M) |
|---|---|---|---|---|
| C1 | 298 | time to volume (delay): 139 / 397 | market size today (S0): 182 / 428 | (a) structure / incumbent response: 223 / 372 |
| C2 | 263 | trend growth (g): 193 / 385 | time to volume (delay): 158 / 316 | (a) structure / incumbent response: 197 / 329 |
| C18 | 152 | trend growth (g): 113 / 251 | new-use pool (N): 122 / 246 | market size today (S0): 105 / 223 |
| C16 | 92 | time to volume (delay): 16 / 131 | (e) complements: 69 / 138 | (a) structure / incumbent response: 69 / 115 |
| C5 | 92 | time to volume (delay): 43 / 122 | market size today (S0): 67 / 141 | new-use pool (N): 72 / 144 |
| C6 | 82 | market size today (S0): 57 / 135 | time to volume (delay): 38 / 109 | trend growth (g): 67 / 109 |
| C13 | 68 | market size today (S0): 41 / 108 | time to volume (delay): 30 / 95 | (e) complements: 51 / 90 |
| C8 | 64 | time to volume (delay): 32 / 80 | (e) complements: 48 / 86 | market size today (S0): 47 / 82 |
| C4 | 51 | new-use pool (N): 36 / 107 | market size today (S0): 34 / 83 | trend growth (g): 40 / 79 |
| C12 | 38 | time to volume (delay): 6.5 / 54 | market size today (S0): 21 / 67 | (a) structure / incumbent response: 28 / 47 |
| C9 | 33 | time to volume (delay): 16 / 44 | (e) complements: 25 / 50 | (a) structure / incumbent response: 25 / 42 |
| C11 | 18 | new-use pool (N): 13 / 37 | trend growth (g): 13 / 34 | market size today (S0): 12 / 31 |
| C17 | 9.8 | (e) complements: 7.4 / 15 | (a) structure / incumbent response: 7.4 / 12 | market size today (S0): 7.3 / 11 |
| C3 | 9.4 | time to volume (delay): 2.8 / 16 | market size today (S0): 5.7 / 14 | (a) structure / incumbent response: 7.0 / 12 |
| C10 | 6.6 | time to volume (delay): 2.0 / 11 | new-use pool (N): 4.5 / 12 | market size today (S0): 5.0 / 8.4 |
| C19 | 1.4 | market size today (S0): 0.7 / 2.5 | time to volume (delay): 0.2 / 2.0 | (e) complements: 1.0 / 2.4 |
| C14 | 0.6 | trend growth (g): 0.3 / 1.5 | new-use pool (N): 0.4 / 1.1 | (e) complements: 0.4 / 1.0 |
| C7 | 0.5 | new-use pool (N): 0.3 / 1.3 | trend growth (g): 0.4 / 1.1 | market size today (S0): 0.3 / 0.9 |
| C15 | 0.0 | market size today (S0): 0.0 / 0.0 | trend growth (g): 0.0 / 0.0 | shortage size (U): 0.0 / 0.0 |

Scenario runs on the top candidates (script output; 2032 revenue, base in brackets)
- Volume one year earlier: C2 $347M (base $263M), cumulative 2027-32 $806M (base $484M); C1 $496M ($298M), cumulative $1,003M ($503M); C5 $153M ($92M). Half a year earlier: C18 $182M ($152M); C4 $56M ($51M). C3 with volume 1.5 years earlier: $35M ($9M).
- Volume one year later (the low case in table 7a): C1 $139M, C2 $158M, C5 $43M, C6 $38M, C12 $6.5M.
- Legal protection lapses (m_b set to the surviving share r): C4 $13M ($51M); C12 $10M ($38M); C2 $188M ($263M); C3 $6M ($9M).
- The shortage and growth cycle ends for certain (p_f = 1): C2 $151M ($263M); C1 $207M ($298M); C18 $100M ($152M); C5 $80M ($92M); C6 $60M ($82M); C4 $33M ($51M).

What the result is if each top assumption is wrong
- C1 metal parts. (1) Time to volume: if qualification adds a year, $139M; this is the main risk because aviation-grade approval is 3-5+ years. (2) Market size: my $35B is an estimate; at $20B the result is $182M. (3) Structure: if OEMs integrate upstream and funded rivals take the second-source slots, $223M.
- C2 data-center power blocks. (1) Trend growth: if the market grows 7% a year instead of 15%, $193M; if the forecast is met in full, $385M. (2) Time to volume: a one-year slip gives $158M. (3) Structure: $197M if incumbents fill the standard-spec end. The cycle-ends case is $151M and the protection-lapse case $188M, so C2 keeps more than half its base revenue under each single adverse case.
- C18 low-cost munitions. (1) Trend growth 5% instead of 15%: $113M. (2) New-use pool at its low value: $122M. (3) Market size $3B instead of $5B: $105M.
- C5 rocket motors and interceptors. (1) A one-year slip in qualification: $43M. (2) Market size $2.5B: $67M. (3) New-use pool low: $72M. C5 depends on the structure multiplier of 2.5; at 1.0 (no second-source preference) the base would be $37M [D: $92M / 2.5].
- C6 satellite buses. (1) Contestable market $8B instead of $12B: $57M. (2) One-year slip: $38M. (3) Growth 3%: $67M.
- C4 China-free components. (1) New-use pool low ($1B): $36M; high ($20B): $107M. (2) Market size $0.7B: $34M. (3) Growth 10%: $40M. Protection lapse is the tail risk: $13M.
- C13 kitchens. (1) Market size $15B: $41M. (2) Adoption a year slower: $30M. (3) Complements (installers) low: $51M.
- C8 home solar. (1) One-year slip: $32M. (2) Complements low: $48M. (3) Market size $9B: $47M.

### Gaps
- Sensitivities are one-at-a-time; correlated shocks (an AI capital-spending pause would hit C2 growth, C2 cycle and C1 turbine demand together) are not modelled beyond the all-low bound.
- The low and high ranges for multipliers are mechanical (×0.75, halfway to 1), not sourced per candidate.

## 8. Consistency checks on the first-round notes

### Takeaway
I found no conflict large enough to change a ranking. The conflicts that matter for the model are in scope definitions (munitions budget, satellite market, transformer deficit, turbine price basis) and in dated versus current figures (FDA timelines, transformer lead times). Where files disagreed I used the measured, most recent and narrowest-scope figure and carried the spread into the low and high ranges.

### Cited Findings
Conflicts and what was used (file tags in brackets)
- Airliner backlog: 16,402 at end-October 2026 (Forecast International), about 17,000 at the start of 2026 (Oliver Wyman), over 18,000 in June 2026 (IATA) [all AVIA]. Used 16,402, the OEM count. Fleet age 15.2 years (IATA) vs about 13 (Oliver Wyman) differ by fleet definition; not used.
- Transformer deficit: about 30% for power transformers in 2025 vs 7% for 2026, same forecaster, flagged as not comparable [ENER]. Used 20% base with a 7-30% range.
- Transformer lead time: 128 weeks (Q2 2025 survey), up to four or five years (PwC, Sightline), and 12-14 months for standard units from a broker [ENER]. Used 30 months as today's figure and 13 months as the physical build time.
- Gas turbine orders: 100.3 GW in 2025 (EPRI author) vs 110 GW at end-2025 (Wood Mackenzie) [ENER]. Used 100.3 GW for the market and 110 vs 60-70 GW for the shortage. Turbine price: $600/kW equipment vs "$2,000 to $3,000/kW" in another source that ENER reads as all-in plant cost. Used the equipment basis.
- Boom and Crusoe: ENER reports the cancellation as fact (TechCrunch, 25 Sep 2026); AVIA calls it aggregator-reported and unverified. The same deal is valued at about $1,026/kW in ENER and about $43M per unit in AVIA (both follow from $1.25B for 29 units of 42 MW). Used ENER.
- Interconnection queue: "about 8,200 projects and 1,312 GW" [HIST] is generation only; "about 2,061 GW active" [ENER] adds 749 GW of storage. Same LBNL data. Not a model input.
- FY2027 munitions: $70.5B, $95.0B, $49.5B and $47.0B appear for different scopes [DEFN flags this]. Used the $24.4B FY2026 figure on the Breaking Defense definition as today's market and the CNAS plan for cycle risk. PAC-3 quantity is 3,203 in one source and 2,936 in another; used 3,203 against output and 2,936 only inside DEFN's unit-cost division.
- Collaborative Combat Aircraft: $2.58B in the CRS category table vs $996.5M plus $150M advance procurement [both DEFN]. Used about $1.0B in the C18 market build-up.
- US ship cost premium: four to five times (2025 press quotes), "roughly a quarter" of the cost abroad (CRS-cited), about 2x (academic) [DEFN]; SKEP says 2-4x. Quoted only as context.
- US commercial ships in 2022: "5 on order" [SKEP] vs "5 built" [DEFN], from the same author. Not used.
- Satellite market: $20.4B manufacturing revenue (SIA), $50-60B including China, Russia and captive production, and about $8B commercial outside Starlink (Contrary) [all AVIA]. Used $12B contestable ($8B plus my $4B defense estimate) with $20.4B as the high value.
- Hadrian: "about $500M raised by its July 2025 Series C" [SKEP] vs "$260M Series C" [ROBO, AVIA] are cumulative vs round. "Four sites" [SKEP, AVIA] vs three named locations [ROBO]. Not a model input.
- Anduril Arsenal-1: roughly $900M [SKEP] vs about $1B [DEFN]. Not used.
- Boxabl: listing dated 20 July [SKEP] vs 17 July 2026 [HOUS]; backlog 679 units and $45.0M [SKEP] vs third-quarter orders 209 units and $16.6M [HOUS] are different measures. Used only the nine-month revenue of $2.6M, on which both agree.
- Manufactured-home share: "9-10% of new housing" and 9% of single-family starts in 2024 [SKEP] vs 9.9% of single-family starts plus shipments and 7.0% of all starts plus shipments in 2025 [HOUS]. Used 9-10% in the new-use arithmetic.
- Construction share of a new home's price: "about 60%" [HIST] vs 64.4% [HOUS, NAHB 2024]. Used 64.4%.
- Direct labor share for cars: 10-12% of manufacturing cost [HOUS] vs "10-20%" and "10-25%", both flagged unverified [HIST, SKEP]. Used 10-12%.
- Slate capital: $1.4B [SKEP] vs about $1.5B [CONS]. Used $1.5B, the later figure.
- Unitree: list price about $16,000 for the G1 [SKEP, ROBO] vs average selling price about $24-25k [ROBO]; 2025 humanoid units 4,200 (one tracker) vs about 5,200-5,500 (prospectus coverage) [ROBO]. Used the average selling price. Global 2025 humanoid shipments are 13,318, 16,000 or about 20,000 depending on the tracker [ROBO]; used the 2026 forecast range of 50,000-60,000.
- Residential solar price: $2.53/W (IEA 2023), $2.77/W (EnergySage 2025), $4.20/W (LBNL, includes dealer and financing fees), "about $3/W" (Latitude) [all CONS]; penetration 7% vs "1 in 10". Used $2.77/W for market value and both splits for the cost stack.
- Module price: $0.133/W global in 2024 [HIST] vs US wholesale $0.12-0.18/W and an IEA 2023 US figure of $0.38/W [CONS]. Used only to state that panels are 5-7% of installed price.
- Lab-grown diamonds: down 74% from 2020 to early 2025 [HIST] vs wholesale down 96% since 2018 [CONS]. Different base years and price levels; used the CONS series.
- FDA device clearance: 31 months and $31M for a 510(k) from a 2010 industry survey, and a 112-day goal for FY2025 [HIST]; MED could not confirm the 2010 figures and gives 128 days under the draft 2028-2032 commitments, falling to 112 by FY2032. Used 128 days for C11.
- Joby certification: "stage 5 of 5" in August 2026 [HIST] vs "fourth of five stages" in November 2026 [AVIA]. Not a model input; unresolved.
- Launch cost per kg: Falcon 9 $2,600 and Falcon Heavy $1,500 [HIST] vs $2,700 and $1,400 [AVIA]; historical benchmark $65,400 (Shuttle) or $18,500. Not a model input.
- Timing differences that are not conflicts: Vertiv 2026 sales guidance $13.25-13.75B [ROBO, at Q4 2025] vs up to $14.85B [ENER, at Q3 2026]; Waymo fleet 3,067 (Dec 2025) vs 3,871 (June 2026) [ROBO]; heat pumps "about 4 million in 2024, unverified" [ENER] vs 3.64M in 2025, down 11.6% [HOUS], which implies about 4.1M in 2024.

### Inferences
- Rule applied: prefer [M] over [SE], the more recent over the older, the narrower scope over the broader, and the figure with a named primary source over a search-summary figure. Where two defensible figures remained, they became the low and high values.
- The three inputs most exposed to these conflicts are the C3 shortage (7% or 30%), the C6 market ($8B or $20.4B) and the C5 market (which scope of the munitions budget). All three are among the top sensitivity drivers for those rows, which is why their ranges are wide.
- Several first-round figures rest on search summaries where the page was not opened (marked "snippet" in the files). Those used here as inputs are: Howmet's airfoil share, HV breaker lead time, the 3,500 stalled engines, the Avolon $120B delivery value, and import shares of transformers. None is the sole basis for a base value.

### Gaps
- I did not re-verify any first-round figure against its original page except the three fetches listed in the reader notes.
- Figures that the first-round files themselves mark as unverified recollection (large transformer unit prices, MRI list price, global hearing-aid units, the Section 301 tariff level on Chinese EVs) are used only as context and are labelled where they appear.
