# Stress test of three energy-hardware candidates: C2 fast power blocks, C3 scarce HV components, C8 productized home energy (as of 24 Nov 2026)

Reader notes
- This is the second pass. It checks the first-round notes (`energy_grid_hardware.md`, `consumer_goods.md`, `skeptic_red_team.md`, `historical_analogs_framework.md`, `robots_industrial_machinery.md`) against fresh sources and plays out actor responses. It does not assume the first-round ranking is right.
- Tags: **[measured]** = reported data or filings; **[claim]** = company or vendor statement; **[forecast]** = analyst projection; **[inference]** = my own reasoning or arithmetic; **[unverified recollection]** = from memory, not sourced this session, do not quote without checking.
- "Summary-level" means the figure came from a search-result summary and the page was not opened.
- Every figure carries its year. Web search worked this session; `www.nrel.gov` was not tried; a few pages returned 403 (noted under Gaps).
- Layout: four cross-cutting key questions first, then one section per candidate. Each candidate section holds the seven deliverables (thesis and assumptions, assumption check, actor simulation, market arithmetic, bear/base/bull, kill criteria and 90-day test, verdict) under Inferences, with the evidence under Cited Findings.

Headline result (inference): none of the three is a Model T case. C2 is a real but crowded speed niche where the automated factory is the wrong first asset. C3 has the best moat and the worst founder access. C8 is not a production problem at all, and its best-funded version is already owned by Base Power.

| | C2 fast power blocks | C3 HV components | C8 home energy |
|---|---|---|---|
| Demand certainty | 6 | 7 | 6 |
| Production is the true bottleneck | 4 | 5 | 2 |
| Regulatory / qualification drag (10 = little) | 7 | 2 | 4 |
| Defensibility after shortage ends | 3 | 7 | 3 |
| Capital to first revenue (10 = low) | 6 | 2 | 8 (installer) / 3 (battery service) |
| Founder buildability | 7 | 2 | 6 |
| Unweighted total (of 60) | 33 | 25 | 29 / 24 |

## 1. Is data-center load growth real enough to sustain equipment demand through 2030?

### Takeaway
Demand is solid through about 2028 because it is already under construction and pre-leased, and 2027 capex guidance points up. It is uncertain from 2029: utility forecasts are inflated by 30-50% wherever they have been tested, and equipment makers' new capacity lands in 2027-2028. A realistic 2030 US data-center electrical equipment market is roughly $25-40B, not Wood Mackenzie's $65B (my estimate).

### Cited Findings
Forecasts and their haircuts
- Utility forecasts sum to 166 GW of new US peak by 2030, about 90 GW from data centers; analysts see little more than 65 GW of data-center growth, so the utility figure is about 25 GW too high (Grid Strategies, report dated 2025). No 2026 edition was found — [Grid Strategies](https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf); [Canary Media](https://www.canarymedia.com/articles/data-centers/data-center-power-forecasts-climb-to-unreachable-heights)
- ERCOT: large loads with 2022-2024 in-service dates arrived about 220 days late on average and data centers reached only about 50% of requested load; ERCOT's adjusted 2030 forecast keeps 37% of requested load (ERCOT, April 2025) — [RMI, Jul 2026](https://rmi.org/resources/planners-have-tools-to-manage-large-load-forecast-uncertainty-are-they-working/)
- AEP Ohio: about 30 GW was requested before its data-center tariff; only 5.6 GW of new contracts were signed under it (plus 12.2 GW already contracted); its 2030 forecast fell by about one third. Indiana Michigan Power's 2030 forecast fell by about half (PJM materials, Sept 2025) — [RMI](https://rmi.org/resources/planners-have-tools-to-manage-large-load-forecast-uncertainty-are-they-working/)
- Georgia Power: potential 2032 large load above 68 GW, over 80% of it in early "technical review" with no binding commitment (PSC filing, May 2026) — [RMI](https://rmi.org/resources/planners-have-tools-to-manage-large-load-forecast-uncertainty-are-they-working/)
- JP Morgan (May 2026): more than 60% of data-center capacity planned for completion in 2027 was not yet under construction — [RMI](https://rmi.org/resources/planners-have-tools-to-manage-large-load-forecast-uncertainty-are-they-working/)
- Sightline Climate (2026): 30-50% of US projects planned for 2026 delayed or cancelled; mostly delays, nine cancellations tracked in February 2026 — [Axios, Feb 2026](https://axios.com/2026/02/24/ai-data-center-boom-projects-numbers); [Tom's Hardware via Yahoo, Apr 2026](https://finance.yahoo.com/sectors/technology/articles/half-planned-us-data-center-150928890.html)
- October 2026: at least 47 major projects delayed, withdrawn or blocked in the year (RegLayers); Bernstein judged about 35% of planned US projects viable; the FT reported Stargate schedule slips; Cipher agreed to absorb the first $359M of overruns on a Texas site; TeraWulf reworked leases (summary-level) — [SBS, Oct 2026](https://news.sbs.co.kr/english/endPagePrintPopup.do?news_id=N1008803646); [Dealroom](https://dealroom.co/news/163868-americas-10tn-ai-build-out-runs-into-towns-grids-and-lenders-at-least-47/)

Evidence that demand is real now
- JLL: record 25 GW of North American absorption in H1 2026; 66 GW under construction, 95% pre-committed; vacancy about 1% for a third year; 77% of capacity under development is in frontier markets (West Texas, Ohio, Louisiana, Carolinas) — [JLL, H1 2026](https://www.jll.com/en-us/newsroom/data-center-demand-exceeds-expectations-in-h1-2026)
- CBRE (eight primary markets only): 7,481 MW under construction in H1 2026, a record; more than 80% pre-leased; vacancy 1.4% — [CBRE](https://www.cbre.com/press-releases/north-american-data-center-demand-continues-to-outpace-supply-despite-record-construction-activity); [Data Center Frontier](https://www.datacenterfrontier.com/site-selection/news/55401462/cbre-record-data-center-construction-fails-to-ease-capacity-crunch)
- Hyperscaler 2026 capex guidance after Q3 2026 results: Alphabet $195-205B, Amazon about $220B, Meta $130-145B, Microsoft about $170-175B for calendar 2026 (lowered from about $190B, attributed to delays in third-party data-center capacity). Alphabet's CFO expects capex to rise "significantly" in 2027; Amazon expects "meaningfully more" (summary-level; sources conflict slightly on Microsoft) — [Yahoo Finance](https://finance.yahoo.com/markets/article/magnificent-7-earnings-rush-reveals-ai-spending-surge-with-hyperscaler-capex-set-to-reach-725-billion-in-2026-224901707.html); [Hargreaves Lansdown](https://www.hl.co.uk/news/ai-hyperscalers-are-expected-to-finish-the-year-spending-a-whopping-828-billion-on-capex)
- S&P Global estimates (not guidance) for 2027: Alphabet $357B, Amazon $319B, Meta $164B, Microsoft $189B (summary-level) — [Hargreaves Lansdown](https://www.hl.co.uk/news/ai-hyperscalers-are-expected-to-finish-the-year-spending-a-whopping-828-billion-on-capex)
- Eaton Q3 2026: electrical backlog $20.4B (+46% year on year); data-center revenue up about 65%; rolling-12-month data-center orders more than doubled; Electrical Americas segment margin 29.8%; it expects its end markets to grow about 11% in 2027 — [Eaton 8-K exhibit](https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000037/etn09302026exhibit99.htm); [MarketBeat call summary](https://www.marketbeat.com/instant-alerts/transcript-eaton-q3-earnings-call-highlights-2026-11-03/)
- Vertiv Q3 2026: sales $4.31B (+61%), organic orders up more than 100% (summary-level, first-round note) — [DCD](https://datacenterdynamics.com/en/news/vertiv-shares-jump-14-percent-as-data-center-earnings-beat-expectations)
- US data-center electrical equipment market: about $20B (2026) to $65B by 2030 (Wood Mackenzie forecast) — [E&E News](https://www.eenews.net/articles/data-centers-to-triple-us-power-equipment-market-to-65b/)

### Inferences
- Arithmetic on the hyperscaler numbers: 2026 midpoints sum to about $730B (200 + 220 + 172.5 + 137.5). S&P's 2027 estimates sum to about $1,029B, a 41% rise. Microsoft's cut is a supply-side signal (it could not get capacity built), which is the C2 thesis in miniature, not a demand signal.
- "40% overstated" needs care. 90 GW is 38% above 65 GW; equivalently 28% of the utility figure is excess. ERCOT's and AEP Ohio's tested realization rates (37-60%) say the haircut on requests is larger than the haircut on forecasts.
- Equipment demand follows megawatts under construction, not utility forecasts. Implied electrical gear per MW: $20B over roughly 10-12 GW a year is about $1.7-2.0M per MW (2026). Published under-construction figures range from about 26 GW (US, Q1 2026, unattributed) to 66 GW (JLL, North America, includes frontier campuses). At 12-18 GW a year through 2030 and $1.8-2.0M per MW, the 2030 market is $22-36B at 2026 prices. Wood Mackenzie's $65B needs about 30 GW a year or large price rises. I use $25-40B as the base range.
- The slowdown evidence so far is physical friction (power, permits, local opposition, gear, lender strain), not a demand retreat. That supports equipment orders through 2028. It also means electrical gear is one of several gates, so removing it does not release all the delayed capacity.
- The fragile layer is the neocloud and developer tier (Cipher, TeraWulf overruns). That tier is exactly who buys from new vendors (Section 3). A startup's customer base is the first to cancel in a pause.
- Timing judgement: high confidence in demand for 2027-2028, moderate for 2029, low for 2030-2032. Past analog: the dot-com turbine boom left excess capacity (first-round note).

### Gaps
- No measured figure for US data-center MW actually energized in 2025 or 2026.
- No Grid Strategies 2026 report found; JLL's 66 GW definition was not checked against the report itself.
- The AWS lease-pause report (Wells Fargo via Quartz) could not be dated; do not treat it as a 2026 signal.
- Wood Mackenzie's scope for the $20B/$65B figures (whether it includes UPS, gensets, busway) is unknown, so the share addressable by C2 is my estimate.

## 2. What do the new entrants show?

### Takeaway
Venture money went to solid-state transformers, which have reservations but no volume deliveries before 2028. The entrants with real revenue or firm orders in conventional gear are asset-light or bootstrapped: Ayr (over $500M order book on $25M raised, built in India) and Giga Energy (CEO claims over $150M revenue in 2025). No startup doing automated winding of conventional transformers was found. Customers are developers, IPPs, neoclouds and, at reservation level, hyperscaler-owned developers.

### Cited Findings
Solid-state transformers
- Heron Power: $140M Series B (Feb 2026); total raised reported as $178-183M. Factory One in Morgan Hill, California: 286,000 sq ft, over $100M, mass production from late 2027, design capacity up to 10,000 units of 5 MW a year. Intersect (owned by Alphabet) reserved 1.5 GW with deliveries from 2028 (announced 19 Nov 2026; deposit and binding status not disclosed). Deals with NiSource, Vantage and Microsoft announced (terms not retrieved). RWE pilot in Texas with a contingent 500 MW reservation (summary-level) — [PV Tech, Nov 2026](https://www.pv-tech.org/heron-power-1-5gw-power-electronics-deal-google-owned-intersect/); [DCD](https://www.datacenterdynamics.com/en/news/heron-power-raises-140m-in-series-b-funding-to-support-build-out-of-40gw-us-manufacturing-facility/); [Energy-Storage.news](https://www.energy-storage.news/heron-power-and-nisource-announce-us-data-centre-and-bess-focused-deals-with-vantage-microsoft/)
- Heron's CEO cites 50 GW of "orders" from more than a dozen prospective customers; TechCrunch says customers "expressed interest" in over 40 GW; data centers are about a third of its business (Feb 2026) — [Canary Media](https://www.canarymedia.com/articles/climatetech-finance/heron-power-raises-140m-electrical-transformers); [TechCrunch](https://techcrunch.com/2026/02/18/heron-power-raises-140m-to-ramp-production-of-grid-altering-tech/)
- Amperesand: $80M Series A (Walden Catalyst, Temasek); target of 30 MW of commercial shipments in 2026; first units to the Port of Singapore in early 2026. No delivery confirmation found — [mgrid, Jan 2026](https://mgrid.org/2026/01/22/amperesand-targets-30-megawatts-of-commercial-medium-voltage-solid-state-transformer-shipments-to-hyperscale-ai-data-centers-in-2026/)
- DG Matrix: $60M Series A (Feb 2026; Engine Ventures, ABB, Mitsubishi Heavy among investors); partnership with PowerSecure (Southern Co.) — [TechCrunch](https://techcrunch.com/2026/02/18/dg-matrix-raises-60m-to-make-data-center-power-smarter); [Canary Media](https://www.canarymedia.com/articles/climatetech-finance/heron-power-raises-140m-electrical-transformers)
- Incumbents are in the same race: Eaton has 10 solid-state transformer pilots, a 15 kV, 2 MW unit that passed UL testing, and expects several to ship in 2026 (Q3 2026 call) — [MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-eaton-q3-earnings-call-highlights-2026-11-03/). Vertiv's 5 MW medium-voltage unit was due in H2 2026 — [IEEE Spectrum](https://spectrum.ieee.org/data-center-dc-2676581047)
- Nvidia says 800 V DC data centers reach full-scale production with its Kyber racks in 2027 and that it is still weighing conventional versus solid-state transformer designs — [Nvidia](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)

Conventional gear
- Ayr Energy: iron-core transformers built to its designs by manufacturers in India; $25M raised over two rounds (Energy Impact Partners); order book "north of $500 million" (Apr 2026); customers are renewable developers, IPPs and data-center developers — [TechCrunch, Apr 2026](https://techcrunch.com/2026/04/15/this-energy-startups-bet-on-100-year-old-grid-tech-is-paying-off/)
- Giga Energy (Houston, founded 2019 by two students supplying bitcoin miners): revenue about $800K in 2021 and above $150M in 2025 (CEO statements, unaudited); pad-mounts up to 10 MVA, MV switchgear, UL 891 switchboards, a 3.6 MVA power skid, modular data centers; plants in Houston and Long Beach, supply chain in Mumbai, office in Shanghai; a 60,000 sq ft Houston MV transformer plant was announced Dec 2025 for Q1 2026 production (start not confirmed); customer logos include CoreWeave, Vultr, Fluidstack; claims a 7-week turnaround for one hyperscaler (unverified). No outside funding disclosed — [third-party profile](https://www.jaredwatkins.com/research/datacenters/power-infrastructure/giga-energy/); [PR Newswire](https://www.prnewswire.com/news-releases/giga-energy-announces-new-houston-manufacturing-facility-to-expand-us-transformer-production-to-power-ai-infrastructure-302643008.html)
- Crusoe makes its own switchgear through Crusoe Industries (from its June 2022 purchase of Easter-Owens): it says in-house MV switchgear cuts lead time 40%; SemiAnalysis says LV gear went from quotes of up to 100 weeks to about 22; Crusoe says it is one of three approved US makers of an ABB gas-insulated design (secondary source, summary-level) — [FourWeekMBA](https://fourweekmba.com/ai-openais-abilene-builder-crusoe-cuts-power-gear-wait-by-40/)
- Trench (incumbent, for comparison): Charlotte bushing plant cost over $60M and was operating just over 15 months after the investment decision (opened July 2026) — [POWER Magazine](https://www.powermag.com/can-u-s-high-voltage-grid-equipment-supply-keep-pace-with-765-kv-expansion-and-data-center-demand/)
- Cautionary case: Crusoe cancelled a $1.25B, 29-turbine order with Boom in Sept 2026, months before delivery — [TechCrunch](https://techcrunch.com/2026/09/25/crusoe-abandons-1.25b-plan-to-use-boom-turbines-at-ai-data-centers/)

### Inferences
- Capital efficiency ranking of what exists: Ayr (about $20 of orders per $1 raised, contract manufacturing) and Giga (bootstrapped to nine-figure revenue) beat every factory-first story. The evidence says the fast path is design, standardization and supply-chain control with rented production.
- Solid-state reservations are soft by the red-team standard: no deposits disclosed, deliveries start 2028. Heron's factory funded in early 2026 ships at volume in 2028, which is the same two-year lag a C2 factory would face.
- The natural C2 customers are integrating backward (Crusoe, reportedly Fluidstack). That shrinks the open market among neoclouds and shows the skill is assembly and licensing of incumbent designs, not novel production.
- A founder entering C2 in 2027 is not first. Giga, Ayr, Crusoe Industries, Korean makers with US plants and three funded solid-state firms are already selling "faster".

### Gaps
- No delivered-unit counts for Heron, Amperesand or DG Matrix.
- Giga's revenue and lead-time claims are unaudited; whether its Houston plant started on time is unknown.
- Ayr's delivered volume, margins and Indian partners are undisclosed; its exposure to the August 2026 executive order and to Section 232 is unknown.
- "Foundational Industries" ($25M seed, July 2026, "AI-native US factories") appeared in results but was not researched.

## 3. How long does a utility take to approve a new vendor versus a data-center developer buying behind-the-meter gear?

### Takeaway
I found no sourced duration for utility approval. The indirect evidence is consistent: utilities demand a US track record and type tests and avoid unfamiliar vendors, while data-center developers have bought from Chinese, Korean, Indian-built and start-up suppliers to cut lead time. The buyers who can produce revenue inside 18-24 months are neoclouds, behind-the-meter power developers, renewable and storage EPCs and smaller colocation developers. Hyperscalers buy through multi-year capacity agreements with bankable makers. Investor-owned utilities are a 2030s customer.

### Cited Findings
- A PacifiCorp substation specification asks a manufacturer seeking approval for a list of units supplied to the US market over the past ten years that were tested to IEEE and IEC standards — [Utah PSC docket](https://pscdocs.utah.gov/electric/20docs/2003505/A-7.04.2_EBU_PX-S02_Substation_Equipment%20Collector_Substation_Main_Power.pdf)
- A municipal utility specification (Burlington Electric) requires proof the design passed short-circuit criteria under IEEE C57.12.00 and C57.12.90 — [Burlington Electric](https://www.burlingtonelectric.com/wp-content/uploads/094-24-50-KVA-XFR-SUB-00130-1.pdf)
- A transformer broker says qualification rules, vendor lists and internal hierarchies, not supply, keep alternative suppliers out of utilities (single source, hard to verify) — [POWER Magazine, 2026](https://powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/)
- Wood Mackenzie: utilities have "largely avoided" Chinese suppliers since the first bulk-power ban, while data centers "have been using Chinese units to minimize lead times" (Aug 2026) — [Wood Mackenzie](https://www.woodmac.com/press-releases/us-executive-order-banning-chinese-bulk-power-equipment-set-to-worsen-critical-transformer-shortage/)
- Tech companies are showing willingness to accept standardized rather than bespoke equipment (Jan 2026, summary-level) — [Semafor](https://www.semafor.com/article/01/13/2026/electric-grid-transformer-delays-show-no-sign-of-easing)
- Utilities now buy years ahead: Roseville Electric moved from about one year to a three-year procurement horizon (Reuters, 2026, summary-level) — [Cybernews/Reuters](https://cybernews.com/tech/data-center-power-utilities-grid-equipment/)
- Trench's US plant ramps by voltage class: below 230 kV in 2026, up to 550 kV in 2027, first 765 kV bushings in early 2028; its CEO says demand is outpacing the industry's ability to qualify new capacity — [POWER Magazine](https://www.powermag.com/can-u-s-high-voltage-grid-equipment-supply-keep-pace-with-765-kv-expansion-and-data-center-demand/)
- Hyperscaler and developer buying pattern: Schneider and Digital Realty signed a $373M supply capacity agreement (Nov 2025) with dedicated lines; LS Electric signed a roughly $126.75M two-year (2027-2028) deal and a $133.41M 345 kV transformer order with unnamed US big-tech customers; Meta holds a strategic capacity agreement with Trench for bushings; Amazon signed a long-term generator agreement with Generac — [Schneider](https://www.se.com/us/en/about-us/newsroom/news/press-releases/schneider-electric-and-digital-realty-announce-373m-supply-capacity-agreement-to-meet-rising-data-center-demand-691d192005c0c16f5902ca3c); [Blackridge](https://www.blackridgeresearch.com/news-releases/ls-electric-secures-usd-126-75-million-power-equipment-supply-contract-for-us-ai-data-centers); [POWER Magazine](https://www.powermag.com/can-u-s-high-voltage-grid-equipment-supply-keep-pace-with-765-kv-expansion-and-data-center-demand/); [Data Center Frontier](https://www.datacenterfrontier.com/energy/article/55407678/amazon-generac-deal-puts-backup-power-in-the-ai-infrastructure-spotlight)
- FERC issued show-cause orders on 18 June 2026 to six grid operators (60 days to defend or revise tariffs), requiring them to accommodate co-location and behind-the-meter generation and to offer services for flexible large loads. It was not a final rule — [Renewable Energy World](https://www.renewableenergyworld.com/energy-business/policy-and-regulation/ferc-takes-historic-action-orders-us-grid-operators-to-defend-or-revise-large-load-interconnection-tariffs/)

### Inferences
- Ranked by speed to a first purchase order (my judgement):
  1. Neoclouds, crypto-to-AI converters, behind-the-meter gas and battery developers: one procurement cycle, roughly 3-9 months, on a factory test and a third-party listing. Evidence: Giga's customer list, Ayr's order book.
  2. Solar and storage EPCs and IPPs (collector-side pad-mounts and MV gear are developer-owned): similar speed, more price-sensitive.
  3. Colocation developers: 6-18 months; they follow their tenants' approved lists.
  4. Hyperscalers: 12-36 months, through capacity agreements; they have signed with Korean entrants and with Heron, so not closed, but they want balance sheet and volume.
  5. Co-ops and munis: mixed; small volumes, often via brokers and distributors.
  6. Investor-owned utilities: about 2-5 years from first contact to volume orders **[unverified recollection of typical practice: factory audit, design review, type and short-circuit tests, a few trial units, then field history]**.
- FERC's push toward co-location and behind-the-meter supply moves more substation and MV equipment purchases from utilities to developers. That enlarges the fast-buyer pool for C2 and, at the HV end, for C3.
- The ten-year US track-record clause is the cleanest statement of why C3 cannot start with utilities.

### Gaps
- No sourced duration for utility approved-vendor qualification, UL listing or IEEE design tests; no data on high-power test-lab queue times.
- No hyperscaler prepayment amounts to equipment makers were found. A reported "$285.3 billion" Hyosung contract figure in one Rystad summary is almost certainly a unit error and is not used.

## 4. C8 facts: Base Power, Sunrun, Tesla, net-metering changes, the end of 25D, and why Australia is cheaper

### Takeaway
After the 25D credit ended on 31 Dec 2025, US residential solar fell (Q2 2026 was the weakest quarter in five years; 2026 forecast down 15-23%) and the market moved to third-party ownership, which keeps the 48E credit through 2027. Base Power raised over $2.5B and installs about 100 batteries a day. Australia reached about 40% of homes with solar and added 600,000 subsidized home batteries in about 16 months. No US company has reproduced the Australian price; the cheapest large US state (Texas) is at $2.00/W.

### Cited Findings
Base Power
- Funding: $200M Series B (Apr 2025); $1B Series C (Oct 2025, $4B post-money); $1B Series D (3 Aug 2026, $13B post-money; Ribbit, Addition, Valor, JPMorganChase); over $2.5B in total — [Sacra](https://sacra.com/c/base-power/); [TechCrunch, Aug 2026](https://techcrunch.com/2026/08/03/base-power-raises-another-1b-to-save-the-grid-using-backyard-batteries/)
- Scale: over 100 MWh deployed by Oct 2025 and over 500 MWh by Aug 2026 (company); about 100 batteries a day and about 8 MWh a day, with a goal to double by end-2026 (WSJ via TechCrunch). Homes: about 1,500 (Jul 2025) to about 7,000 (Dec 2025), a third-party estimate. Operates in Texas and Illinois — [TechCrunch](https://techcrunch.com/2026/08/03/base-power-raises-another-1b-to-save-the-grid-using-backyard-batteries/); [Sacra](https://sacra.com/c/base-power/)
- Customer price (Houston, Aug 2026): $695 upfront, $19 a month, 13.1 cents/kWh. Sacra lists about $650 upfront, $19-29 a month and an 8.5 cent energy charge plus delivery on a 36-month contract — [TechCrunch](https://techcrunch.com/2026/08/03/base-power-raises-another-1b-to-save-the-grid-using-backyard-batteries/); [Sacra](https://sacra.com/c/base-power/)
- Unit economics (Sacra estimates, not company data): about $10,000 installed per battery, $3,000 federal credit, about 3.5-year payback driven by retail and wholesale margin; lease fees alone ($228-348 a year) would take 20+ years; 2025 annualized revenue about $12M, 2026 projection $70M; 10+ homes per electrician per day; permits next-day to 2-4 weeks — [Sacra](https://sacra.com/c/base-power/)
- Utility contracts: Austin Energy pays up to $4.08M a year for 40 MW (about $8.50/kW-month, derived by Sacra); a 50 MW deal with Guadalupe Valley Electric Cooperative; programs with El Paso Electric, Austin Energy and CoServ total over 200 MW (summary-level) — [Sacra](https://sacra.com/c/base-power/); [Utility Dive](https://www.utilitydive.com/news/base-power-partnership-to-mitigate-price-spikes-load-peaks-for-south-tx-co-op-ceo-says/818221/)

Sunrun, Tesla, Enphase (Q3 2026)
- Sunrun: 22,957 subscriber additions (-24% year on year); 24,096 customer additions (18,081 with storage); 1,057,695 subscribers; storage attachment 75%; 203.7 MW solar (-15%) and 374.4 MWh storage (-9%) installed; 5.0 GWh networked storage; Subscriber Value $55,342 at a 43.4% average tax-credit rate; Net Subscriber Value $9,462 (-28%); sales and marketing expense $240M; 2026 cash generation guided to about $200M, the bottom of the prior range; direct-business installs +9% — [Sunrun 8-K exhibit](https://www.sec.gov/Archives/edgar/data/0001469367/000162828026070143/exhibit991q326.htm)
- Tesla: 13.7 GWh of storage deployed in Q3 2026 (mostly utility-scale); energy revenue $2.88B (-16%); Powerwall volumes not broken out — [Energy-Storage.news](https://www.energy-storage.news/tesla-q3-2026-energy-storage-revenues-fall-despite-second-highest-quarterly-deployments/)
- Enphase: Q3 2026 revenue $293.3M (about -28.5% year on year); 129.9 MWh of batteries shipped; US sell-through down 35% year on year, attributed to rates and the 25D expiry; Q4 guide $225-255M (summary-level) — [PV Tech](https://www.pv-tech.org/enphase-reports-stable-revenue-q3-2026-identifies-storage-key-growth-driver/)

US market after 25D
- Residential solar installed 995 MWdc in Q2 2026, the lowest quarter in five years; Wood Mackenzie expects 2026 residential installs down 23%; BNEF expects 4.1 GW, down 15% — [Wood Mackenzie](https://www.woodmac.com/news/opinion/us-solars-foundation-holds-strong-even-as-the-ground-keeps-shifting/); [Mercom](https://mercomindia.com/us-solar-installations-jump-45-yoy-to-11-4-gw-in-q2-2026); [Bloomberg Law](https://news.bloomberglaw.com/states-of-play/us-residential-solar-industry-faces-slump-in-2026-bnef-says)
- EnergySage H1 2026: median quoted price $2.57/W ($2.62 solar-only); Texas $2.00/W, Illinois $3.07/W; battery quotes $1,130/kWh, rising partly on foreign-entity sourcing rules; installers quoting third-party ownership rose from about 14% to 41% between January and June 2026; 74% of contractors report higher labor rates — [EnergySage](https://www.energysage.com/news/home-energy-market-h1-2026-highlights/); [pv magazine](https://www.pv-magazine.com/2026/10/24/residential-solar-prices-rise-3-2-as-third-party-ownership-gains-ground/)
- 48E remains available to lease and PPA providers through 2027; banks active in the sector are reported "pens down" on 48E; Section 232 tariffs on polysilicon take effect 4 Dec 2026 — [Latitude Media](https://www.latitudemedia.com/news/post-obbb-where-does-rooftop-solar-go-from-here/); [EnergySage](https://www.energysage.com/news/home-energy-market-h1-2026-highlights/); [pv magazine](https://www.pv-magazine.com/2026/10/24/residential-solar-prices-rise-3-2-as-third-party-ownership-gains-ground/)
- US solar-plus-battery systems cost about $5.20/W versus $2.00/W in Australia; customer acquisition $1,000-3,000 per customer for small installers; cancellation rates around 30%; a third of US rooftop solar is sold by someone other than the installer; about 80% is financed (Aug 2025) — [Latitude Media](https://www.latitudemedia.com/news/post-obbb-where-does-rooftop-solar-go-from-here/)
- Residential storage counts conflict: Wood Mackenzie/ACP report a record 1.3 GWh in Q1 2026; SEIA/Benchmark report 515 MWh in Q1 and forecast 2,024 MWh for 2026 (-37%) (summary-level) — [Wood Mackenzie](https://www.woodmac.com/press-releases/u.s.-energy-storage-market-sets-q1-2026-records-across-sectors); [SEIA](https://seia.org/news/largest-quarter-on-record-for-energy-storage/)

California net billing ("NEM 3.0", April 2023)
- Export credit value cut about 75%; Wood Mackenzie forecast a 40% fall in California residential solar for 2024; storage attachment about 60% under net billing versus about 10% before (LBNL); the top five installers' share rose from 40% to 51% in the first year; Sunworks, Titan Solar and Lumio went bankrupt; installs have stayed flat since — [Utility Dive](https://www.utilitydive.com/news/residential-solar-storage-california-after-nem-30-lbnl/716589/); [pv magazine USA](https://pv-magazine-usa.com/2024/03/11/california-has-become-rooftop-solar-and-batteries-nem-esis); [PV Tech](https://www.pv-tech.org/lbnl-residential-solar-pv-installations-remain-flat-since-nem-3-0-in-california)
- A US appeals court upheld the net billing tariff in March 2026 — [pv magazine](https://www.pv-magazine.com/2026/03/11/u-s-court-upholds-current-net-billing-mechanism-dealing-blow-to-rooftop-solar-in-california/)

Australia
- Mid-2026: one in 2.5 homes has rooftop solar (Clean Energy Council); 4.5 million systems and 30.3 GW (Clean Energy Regulator, July 2026) — [Clean Energy Council](https://cleanenergycouncil.org.au/news-resources/record-home-battery-surge-charges-up-australia-s-biggest-power-station-on-aussie-rooftops); [Finder](https://www.finder.com.au/energy/is-solar-worth-it)
- Cheaper Home Batteries (about 30% off upfront, from July 2025): 400,000 installs and 11.2 GWh by May 2026 at about 2,000 a day; 500,000 in August; over 600,000 and 16.8 GWh by autumn 2026; budget raised from A$2.3B to A$7.2B (Dec 2025); 153 batteries per 100 solar installs in H1 2026; average size peaked at 35.3 kWh in April 2026 — [Energy-Storage.news](https://www.energy-storage.news/australias-cheaper-home-batteries-program-hits-16-8gwh-installed-capacity/); [Energy-Storage.news](https://www.energy-storage.news/australia-hits-400000-home-battery-installations-with-11-2gwh-capacity-in-under-a-year/); [Clean Energy Regulator](https://cer.gov.au/news-and-media/news/2025/december/changes-to-cheaper-home-batteries-program)
- Cost decomposition (IEA 2023 data): US $2.53/W = $1.28 hardware + $1.25 soft; Australia $0.82/W = $0.46 hardware + $0.36 soft. Australia buys tariff-free in bulk from China, has "minimal" customer acquisition cost because demand is high and steady, automatic interconnection under about 10 kW and one-day installs — [Boston University, Jul 2025](https://www.bu.edu/eci/files/2025/07/Intnatl-Cost-Comparisons-final.pdf)
- Tesla's path to cheaper US systems: $0.54/W from regulatory reform, $0.57/W from installer operations, $0.67/W from hardware; instant permitting alone saves about $0.04/W of labor; Tesla's backup switch is approved by only 40% of utilities (Oct 2025) — [Latitude Media](https://www.latitudemedia.com/news/can-the-us-bring-solar-installation-to-below-2-per-watt/)

Permitting reform
- SolarAPP+ is used by about 350 US cities (Aug 2025) — [Latitude Media](https://www.latitudemedia.com/news/post-obbb-where-does-rooftop-solar-go-from-here/)
- State laws: New Jersey (statewide automated platform), Maryland, California (Solar Access Act for larger cities and counties), Florida (permits within five days, July 2025), Minnesota funding; bills pending in New York and Massachusetts (summary-level) — [NCEL](https://ncel.net/articles/new-jersey-enacts-landmark-law-to-boost-rooftop-solar-access-affordability/); [pv magazine USA](https://pv-magazine-usa.com/2026/06/12/permitting-can-add-7000-to-rooftop-solar-costs-ny-lawmakers-want-to-automate-it/)
- A March 2026 scorecard gave California and Texas a B and New Jersey and Colorado a C; "best practices elude even the best states" — [pv magazine USA](https://pv-magazine-usa.com/2026/03/26/new-report-finds-adoption-of-solar-permitting-best-practices-eludes-even-the-best-states/)
- Permit Power (advocacy group): matching German and Australian permitting cost would add 18-20 million solar households and about 198 GW by 2040 — [pv magazine](https://www.pv-magazine.com/2025/10/31/cutting-solar-permit-delays-could-add-20-million-us-rooftop-systems/); [TaiyangNews](https://taiyangnews.info/markets/cutting-red-tape-could-add-198-gw-more-rooftop-solar-in-us-by-2040)

### Inferences
- Sunrun's real cost to create a customer (derived from the 8-K): $55,342 - $9,462 = $45,880 per subscriber. Average system is 8.45 kW (203.7 MW / 24,096) with 20.7 kWh on storage customers (374.4 MWh / 18,081). That is about $5.43/W all-in for solar with 75% storage attachment. Sales and marketing is about $10,450 per added subscriber ($240M / 22,957), or about $1.24/W. This one line item exceeds Australia's whole installed solar price.
- Base Power reconciliation: 100 batteries a day at 39.2 kWh is 3.9 MWh, not 8 MWh. The numbers match only if the count is homes with two units each (78.4 kWh). On that reading Base runs at about 2.9 GWh a year, roughly double Sunrun's storage rate (about 1.5 GWh a year) and above the SEIA/Benchmark forecast for the whole 2026 residential market. Either Base is now the largest US home-battery deployer or its figures are not in the trade counts. Homes served are probably 20,000-25,000 by late Nov 2026 (500 MWh at 35-50 kWh per home in August, plus about 100 a day since).
- Base's capital burn: 100 homes a day at $10,000-20,000 of installed hardware is $1-2M a day, or $0.4-0.7B a year. Two $1B rounds buy about two to three years of deployment. Revenue of $70M (2026 projection) against over $2.5B raised is the balance-sheet shape of a utility, not a manufacturer.
- Nobody in the US has replicated Australia. The closest are Texas's $2.00/W median and Base's sub-$700 upfront battery, and Base gets there by owning the asset and the retail contract, not by lowering installed cost.
- Australia's low acquisition cost is partly a result of high penetration (neighbours already have it), not only a cause. A US entrant cannot assume it on day one.

### Gaps
- Tesla Powerwall unit volumes and Tesla residential solar pricing: not found.
- Base Power's own unit economics, cell supplier, debt facilities and tax-credit use are undisclosed; Sacra's figures are third-party estimates.
- Australian installed battery price per kWh in 2026: not found. **[unverified recollection]** roughly A$500-900/kWh before rebate for large systems.
- The exact 48E and 25D statutory text was not opened. **[unverified recollection]**: leased residential solar keeps 48E if placed in service by end-2027 or if construction began by 4 July 2026; storage keeps 48E into the 2030s subject to foreign-entity sourcing tests.
- Plug-in ("balcony") solar law in US states was not sourced. **[unverified recollection]**: Utah passed an enabling law in 2025 and other states considered bills in 2026.

## 5. Candidate C2: fast-delivery standardized power blocks for data centers and large loads

### Takeaway
The demand and the buyer's willingness to pay for schedule are real through 2028, and behind-the-meter buyers will take a new vendor. But the thesis as written ("automated factory, 3 months instead of 1-3 years") fails on two points: the constraint is components and qualified designs rather than assembly, and the lead-time gap will be closer to 2-4x than 5-10x by the time a 2027-funded factory ships. The buildable version is an asset-light integrator, and that seat is already partly taken.

### Cited Findings
Lead times and prices
- Wood Mackenzie Q2 2025 survey: switchgear 44 weeks, power transformers 128 weeks; pad-mount lead times rising in that quarter — [POWER Magazine](https://powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/)
- Contractor data, 2026: MV switchgear 52-80 weeks, pad-mounts 40-65 weeks (Terrapin) — [Foley, Sep 2026](https://www.foley.com/insights/publications/2026/09/the-grids-bottleneck-isnt-just-money-its-materials/)
- Vendor and analyst claims, 2026: data-center-spec MV gear "two to three years" at the busiest makers; switchgear "spoken for through 2028 at some suppliers"; SemiAnalysis models switchgear and transformers at 12-18 months; distribution transformers average about 30 weeks, down from over 100 in 2023 (Wood Mackenzie as cited by a vendor) — [IPS](https://www.ips.co/news/the-hidden-risk-in-data-center-growth-power-equipment-lead-times); [Giga Energy profile](https://www.jaredwatkins.com/research/datacenters/power-infrastructure/giga-energy/); [FourWeekMBA](https://fourweekmba.com/ai-openais-abilene-builder-crusoe-cuts-power-gear-wait-by-40/)
- Wood Mackenzie expects the three-phase pad-mount deficit to widen from 2% (2026) to 7% (2030) — [VKTR, Nov 2026](https://www.vktr.com/ai-technology/ais-data-center-boom-is-deepening-a-transformer-shortage/)
- Wood Mackenzie, Aug 2026: 15% shortage in power transformers and 8% in substations — [Wood Mackenzie](https://www.woodmac.com/press-releases/us-executive-order-banning-chinese-bulk-power-equipment-set-to-worsen-critical-transformer-shortage/)
- Prices since 2019-2021: MV switchgear +50%, circuit breakers +47%, some distribution transformer classes +95% — [POWER Magazine](https://powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/)
- Electrical infrastructure is under 10% of data-center cost — [Tom's Hardware via Yahoo](https://finance.yahoo.com/sectors/technology/articles/half-planned-us-data-center-150928890.html)

Incumbent response
- Eaton: 18 of 25 expansion projects complete (Q3 2026); a larger three-phase transformer plant due H1 2027; a 350,000 sq ft Nebraska MV switchgear campus due 2027 within a $500M US programme; Electrical Americas margin 29.8%; bought Boyd Thermal and agreed to buy COL Group for about $921M — [MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-eaton-q3-earnings-call-highlights-2026-11-03/); [EnergyTech](https://energytech.com/infrastructure/news/55369856/eaton-expands-us-switchgear-manufacturing-to-support-data-center-growth)
- Schneider: $700M in US operations through 2027 (announced Mar 2025); Siemens: over $200M for plants in Georgia and Texas — [The Register](https://www.theregister.com/2025/03/26/schneider_electric_ai_investment/); [Renewable Energy World](https://www.renewableenergyworld.com/power-grid/manufacturers-expand-u-s-operations-to-meet-unrelenting-grid-demand/)
- Siemens Energy's North Carolina transformer and switchgear hub is sold out for its first two years (Nov 2026) — [Utility Dive](https://www.utilitydive.com/news/elevated-demand-for-gas-turbines-could-persist-through-2035-siemens-energy/874839/)
- Vertiv counts only firm purchase orders, with a 12-18 month horizon, and sells a prefabricated 10 MW block — [DCD](https://datacenterdynamics.com/en/news/vertiv-shares-jump-14-percent-as-data-center-earnings-beat-expectations); [Data Center Frontier](https://www.datacenterfrontier.com/machine-learning/article/55357689/vertivs-ai-infrastructure-surge-record-orders-liquid-cooling-expansion-and-grid-scale-power-reshape-data-center-growth)

Trade policy and inputs
- Section 232: from April 2026 duties apply to full customs value; "certain electrical grid equipment" pays a reduced 15% through 31 Dec 2027 (10% if made with US metal); default 25% for covered products from 8 June 2026 through 2027 — [White & Case](https://www.whitecase.com/insight-alert/united-states-modifies-steel-aluminum-and-copper-section-232-tariffs); [Taft](https://www.taftlaw.com/news-events/law-bulletins/trump-amends-tariffs-on-steel-aluminum-and-copper-imports/)
- Executive order of 26 Aug 2026 restricts Chinese-made bulk-power equipment (substation transformers, grid inverters, storage, HV breakers, turbines, and UPS for critical infrastructure); DOE rulemaking due 24 Dec 2026; how it applies to data-center loads is unclear. Sources number it 14420 or 14421 — [Wood Mackenzie](https://www.woodmac.com/press-releases/us-executive-order-banning-chinese-bulk-power-equipment-set-to-worsen-critical-transformer-shortage/); [Rystad](https://www.rystadenergy.com/news/us-executive-order-targets-chinese-grid-hardware-but-battery-storage-serving-ai-d)
- China's share of US imports by value, 12 months to June 2026: transformers 3%, HV breakers under 1%; Korea, Mexico and Canada supply 48% of transformer imports (Rystad). By units, Chinese high-power transformer imports rose from under 1,500 (2022) to over 8,000 (2025 through October) (Wood Mackenzie via Bloomberg). The two measures conflict — [Rystad](https://www.rystadenergy.com/news/us-executive-order-targets-chinese-grid-hardware-but-battery-storage-serving-ai-d); [Tom's Hardware via Yahoo](https://finance.yahoo.com/sectors/technology/articles/half-planned-us-data-center-150928890.html)
- Grain-oriented electrical steel: Cleveland-Cliffs' Butler Works is the only US source; a $200M expansion (with a $75M DOE grant) adds up to 25%; a five-year defense contract reserves up to 53,000 tons; critics say its steel is narrower (920 mm) and lossier than Japanese grades — [GMK Center, Oct 2026](https://gmk.center/en/news/cleveland-cliffs-is-investing-200-million-in-the-expansion-of-the-butler-works-plant-in-the-us/); [AIST](https://www.aist.org/the-defense-logistics-agency-makes-us$400-million-supply-agreement-with-cleveland-cliffs); [Breakthrough Institute](https://thebreakthrough.org/issues/energy/america-makes-the-wrong-steel-for-its-transformer-supply-chain)
- Transformer cost model: materials about 40%, labor about 25%, capital about 25% (analyst model) — [Thunder Said Energy](https://thundersaidenergy.com/downloads/transformers-companies-and-costs/)

### Inferences

**5.1 Thesis and assumptions**
Thesis: data-center and large-load builders lose months of revenue waiting for MV switchgear, pad-mount and medium power transformers and power skids, and because this gear is under 10% of project cost they will pay for speed and accept a new supplier. A start-up that standardizes the designs and builds them in an automated factory can deliver in about 3 months and take share while the incumbents ration.

Assumptions: (A1) data-center equipment demand keeps growing to 2030; (A2) lead times are still long when the start-up ships; (A3) assembly capacity is the constraint and a new factory relieves it; (A4) buyers accept a new vendor fast and pay for schedule; (A5) 3-month delivery is achievable on $50-150M inside 18-24 months; (A6) incumbents do not close the gap; (A7) the AC power-block architecture stays stable; (A8) trade policy does not undercut a US maker.

**5.2 Assumption check**

| # | Supporting | Contradicting | Mark |
|---|---|---|---|
| A1 demand | 66 GW under construction, 95% pre-committed (JLL H1 2026); Eaton and Vertiv orders doubling (Q3 2026); 2027 capex guided up | Tested realization of requests is 37-60% (ERCOT, AEP Ohio); 60% of 2027 capacity not started (JPM, May 2026); developer-tier financing strain | Holds to 2028, Shaky after |
| A2 lead times persist | MV gear 52-80 weeks (2026 contractor data); pad-mount deficit widening to 7% by 2030 (WoodMac); Siemens hub sold out two years | Switchgear averaged 44 weeks (Q2 2025); distribution transformers about 30 weeks; Crusoe in-house 22 weeks; Eaton, Schneider, Siemens capacity lands 2027 | Shaky |
| A3 assembly is the constraint | Labor is 25% of transformer cost; OEMs cite labor shortage | Switchgear is assembled from breakers, relays and bus made largely by the incumbents; Crusoe builds under ABB approval; Ayr and Giga grew without automated plants; steel has one US source | Fails as stated |
| A4 buyers accept new vendor | Data centers bought Chinese units for speed; Giga and Ayr order books; standardization accepted (Semafor) | Hyperscalers lock multi-year capacity deals with bankable makers; neoclouds integrating backward | Holds for developers, Shaky for hyperscalers |
| A5 3 months on $50-150M | Trench built a plant in 15 months for $60M; Giga claims 7 weeks | 3 months needs stock of long-lead breakers and cores, which is working capital and allocation, not robots | Shaky |
| A6 incumbents leave the gap | "Value over volume" statements (turbines); record margins | In LV/MV gear they are adding volume too: Eaton 25 projects, Schneider $700M, Siemens $200M+; they buy what they lack | Shaky |
| A7 architecture stable | Vertiv: AC and DC will coexist | Nvidia 800 V DC from 2027; Eaton, Vertiv and three start-ups shipping MV solid-state units 2026-2028 | Shaky |
| A8 trade policy | Aug 2026 order removes the Chinese fast option for data centers if DOE reads it broadly | Section 232 rate on grid gear was cut to 15% through 2027; Korean, Mexican and Canadian plants are the real rivals and are unaffected | Shaky |

**5.3 Actor simulation, 2027-2032**
- 2027. Hyperscaler capex up about 40% on S&P estimates. Gear stays tight. The DOE rule under the August 2026 order takes effect; developers who used Chinese units need alternatives, which helps any non-Chinese fast supplier for a year or two. Eaton's and Siemens's new lines start. FERC compliance filings bring co-location and behind-the-meter rules, so more developers buy their own substations. Nvidia's 800 V DC racks begin shipping. Start-up: an asset-light entrant can book first deliveries late in the year; a factory-first entrant is still pouring concrete. Price: a 10-20% speed premium is available. Volume: capped by component allocation.
- 2028. Capacity started in 2025-2026 commissions. Incumbent lines ramp; standard-gear lead times fall toward 30-40 weeks (inference). Hyperscalers extend capacity agreements (the Schneider-Digital Realty and LS Electric pattern) to anyone bankable. Incumbents launch or buy quick-ship modular lines; a start-up with $100M+ revenue becomes an acquisition target (Eaton, Vertiv, Schneider, Legrand and nVent have all bought into this space). The reduced Section 232 rate has expired at end-2027; direction unknown. Start-up: best revenue year for an asset-light entrant; first units off an own-factory line.
- 2029. The danger year. If AI capex plateaus, neocloud and developer orders are cancelled first (the Boom-Crusoe pattern), and incumbents with roughly 30% segment margins can cut price 10-20% and still earn. If the boom continues, 800 V DC and solid-state designs take a rising share of new AI halls and the 2026-era AC block needs redesign. Either way the start-up's price falls to parity or below, and an automated plant sized for the boom runs under 50% utilization.
- 2030-2032. Market settles at $25-40B (my range) or $65B (Wood Mackenzie). Winners own qualified designs, service and frame agreements. The start-up is absorbed (base) or gone (bear).
- Buyers by segment: hyperscalers pay for schedule but want frame agreements and financial strength; neoclouds buy fastest and cancel fastest; colocation follows tenants; utilities, co-ops and munis are not early customers; EPCs want price and delivery guarantees backed by damages.
- Regulators and gatekeepers: third-party listing and IEEE design tests are a months-long gate, not years **[unverified recollection]**; no utility vendor list applies behind the meter; large-load tariffs (AEP Ohio style) cut speculative projects, which removes the least reliable customers.
- Labor: site electricians are scarce (Vertiv names construction labor as a pacing item), which favours factory-built skids. **[unverified recollection]** Some union jurisdictions resist prefabricated electrical assemblies.
- Financiers: venture has funded solid-state (about $280-330M across three firms), not conventional gear; Ayr raised only $25M. Customer deposits are the natural funding; without them the business is a working-capital trap.
- Input suppliers: breakers and relays come from competitors; electrical steel from one US mill or tariffed imports; copper tariffs up to 50%. The start-up's delivery promise is only as good as its allocation letters.
- Net effect on the start-up: price premium 10-20% in 2027-2028, zero or negative from 2029; volume limited by components and cash before 2029 and by demand after; first revenue in 12-18 months if asset-light, 24-36 months with an own plant.

**5.4 Market arithmetic**
- Market today: about $20B of US data-center electrical equipment (2026, Wood Mackenzie). The C2 slice (MV switchgear, pad-mount and medium transformers, skids) is perhaps 30-40%, or $6-8B (my assumption; scope of the $20B is unknown).
- Supply gap: single-digit to mid-teens percent (8% substations, 15% power transformers, 2-7% three-phase pad-mounts, 2026). At 8% of $6-8B the truly unserved demand is about $0.5-0.6B a year. Everything else a start-up sells is share taken from makers earning about 30% margins.
- If lead time fell 5-10x: the mechanism is pull-forward, not new demand. Roughly 6 GW a year is delayed (Sightline). If 20-35% of that is gated only by this gear (my assumption; no source), 1.2-2.1 GW a year arrives 6-12 months sooner. At $1.8-2.0M per MW and a 30-40% slice, that is $0.65-1.7B of equipment shifted earlier. Steady-state market growth from speed alone: about 0-10%.
- If price fell 30-50%: gear is under 10% of project cost, so project cost falls 3-5% and volume barely moves (at a project-cost elasticity of -0.5, +1.5-2.5%). The dollar market shrinks by roughly the price cut. The surplus goes to hyperscalers.
- Material floor: materials are about 40% of transformer cost, so 30-40% below today's scarcity price is achievable and 10x is not (first-round finding, unchanged).
- Start-up share: 1% of a $10-16B 2030 slice is $100-160M, which is where Giga claims to be already; 5% is $0.5-0.8B.

**5.5 Bear / base / bull to 2032**

| Case | Probability (my judgement) | 2032 revenue | Capital consumed | Main reason |
|---|---|---|---|---|
| Bear | 40% | Under $50M or wound down | $80-150M | Factory funded 2027 ships 2028-2029 as incumbent capacity lands and deficits are single-digit; anchor customer cancels; plant has near-zero resale value |
| Base | 40% | $150-400M at 20-25% gross margin | $60-120M equity plus working-capital debt | Asset-light integrator serving developers, IPPs and behind-the-meter power; acquired at roughly 1-2x revenue |
| Bull | 20% | $1-2B | $300-500M | Build stays above 20 GW a year, Chinese gear is excluded, and the company wins a hyperscaler frame agreement and adapts to DC architectures |

Timing risk, directly: a factory funded in 2027 arrives as the queue premium fades. The plan must clear at normal margins against incumbents who can drop price. The asset-light route reaches revenue in 2027-2028, inside the high-confidence demand window, and leaves the factory decision until orders justify it.

**5.6 Kill criteria and 90-day test**
- Kill if: (1) fewer than three purchase orders with 20-30% non-refundable deposits within six months of a quotable design; (2) incumbent quotes for standard MV gear fall below about 30 weeks; (3) breaker, relay or core suppliers will not commit allocation, or quote over 26 weeks; (4) 2027 hyperscaler guidance turns flat or pre-commitment of capacity under construction drops below about 80%; (5) DC-architecture designs exceed about 30% of newly ordered AI capacity before the product is adapted.
- 90-day test (about $150-300K, no factory): write specifications and single-line diagrams for two or three standard blocks. Get firm prices and delivery dates from contract manufacturers and component vendors in the US, Korea, Mexico and India. Take the offer to 30 buyers (neoclouds, colocation developers, behind-the-meter power developers, EPCs) with a 12-16 week delivery guarantee backed by damages, and ask for a purchase order with a deposit. Mystery-shop Giga, Ayr and two incumbents for real quoted lead times on the same specification. Pass: at least $10M of deposit-backed orders at a price premium of 10% or more, plus written component allocation. This tests A2, A3 and A4 together.

**5.7 Verdict**
Scores: demand certainty 6; production as true bottleneck 4; regulatory and qualification drag 7; defensibility after the shortage 3; capital to first revenue 6; founder buildability 7.
Judgement: C2 is the most buildable of the three and the least defensible. The first-round note ranked it first on the strength of long lead times and a price-insensitive buyer, and both hold for now. What does not hold is the production thesis: the entrants with real orders rent production, the core components come from the incumbents, and those incumbents are adding capacity in exactly this category while earning record margins. Speed here is a 2027-2028 arbitrage that funds a company only if it converts early orders into something durable (qualified designs, a service base, a frame agreement, or a DC-architecture product). Build it as a design-and-supply-chain company with deposits, not as a factory, and expect an acquisition rather than a Ford-style outcome.

### Gaps
- No Wood Mackenzie lead-time survey later than Q2 2025 was found; 2026 figures are contractor, vendor or analyst-model numbers.
- No sourced cost breakdown for switchgear; no data on breaker or relay lead times to independent assemblers.
- How DOE will apply the August 2026 order to data-center equipment is undecided until its rule (due 24 Dec 2026).
- The share of delayed data-center capacity gated only by MV gear is my assumption.

## 6. Candidate C3: scarce high-voltage grid components

### Takeaway
The scarcity is the deepest of the three (bushings up to two years, HV breakers about 125 weeks, GSUs over 160 weeks) and a qualified position is durable. But the constraint is qualification and know-how at least as much as floor space, incumbents are spending billions and buying the component makers, and the main forecaster has the power-transformer deficit at about 5% by 2030, when a 2027 start would be seeking its first approvals. It is a strong business for an incumbent spin-out with a prepaying OEM or hyperscaler, and a poor one for a typical founder.

### Cited Findings
- Lead times: HV circuit breakers about 125 weeks in H2 2025 versus 77 weeks in 2023; GSUs above 160 weeks by Q1 2026 (Wood Mackenzie via Reuters, summary-level) — [AJOT/Reuters](https://www.ajot.com/news/us-power-companies-scramble-to-secure-equipment-as-surging-data-center-demand-strains-supplies)
- Bushings have the longest lead times, up to two years; the bottleneck is specialty components, particularly insulators (Trench CEO, 2026) — [POWER Magazine](https://www.powermag.com/can-u-s-high-voltage-grid-equipment-supply-keep-pace-with-765-kv-expansion-and-data-center-demand/)
- Trench: revenue over €1B a year after 30% growth in each of the past two years; backlog over €2.1B; about €400M of capacity spending through 2030; Charlotte plant (over $60M, opened July 2026) makes dry-type bushings from 25 to 765 kV, about 3,500 units a year expandable to 10,000; capacity agreements with transformer OEMs and with Meta; about half of new orders are for North America — [POWER Magazine](https://www.powermag.com/can-u-s-high-voltage-grid-equipment-supply-keep-pace-with-765-kv-expansion-and-data-center-demand/)
- GE Vernova agreed to buy Trench for $9B (close expected late 2027) and plans the first US factory for bushings up to 765 kV — [Utility Dive](https://www.utilitydive.com/news/ge-vernova-in-9b-deal-to-buy-high-voltage-manufacturer-as-gas-turbine-orde/873223/)
- Deficit forecasts (Wood Mackenzie, Aug 2025): power transformers 30% in 2025 falling to 5% by 2030; GSUs 47% falling to 14% (summary-level). A later reading: GSU demand 100% above supply in 2025, gap under 10% by 2030 — [pv magazine USA](https://pv-magazine-usa.com/2025/08/14/grid-transformers-face-significant-supply-deficits-says-wood-mackenzie/); [T&D World](https://tdworld.com/substations/news/55310262/report-warns-of-worsening-transformer-shortages-amid-rising-us-power-demand); [Electrical Contractor](https://www.ecmag.com/magazine/articles/article-detail/investment-by-grid-equipment-makers-could-ease-shortage)
- Aug 2026: 15% shortage in power transformers; the segment above 100 MVA is most acute; the market above 10 MVA has grown nearly 300% since 2020 — [Wood Mackenzie](https://www.woodmac.com/press-releases/us-executive-order-banning-chinese-bulk-power-equipment-set-to-worsen-critical-transformer-shortage/)
- Incumbent capacity: nearly $2B committed in North America since 2023: Hitachi Energy over $1B (South Boston, Virginia $457M, largest US large-transformer plant by 2028); Siemens Energy Charlotte $150M (production early 2027, 57 units a year); Eaton $340M; Prolec GE over $300M; Virginia Transformer +70%; HD Hyundai +30% — [POWER Magazine](https://powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/)
- Hitachi Energy's Mississippi plant is scheduled to produce from 2029 (summary-level) — [Cybernews/Reuters](https://cybernews.com/tech/data-center-power-utilities-grid-equipment/)
- Factory equipment for large transformer plants has 2-4 year lead times (Hitachi Energy executive) — [pv magazine, Feb 2026](https://www.pv-magazine.com/2026/02/27/global-energy-transition-hits-a-hardware-bottleneck/)
- Imports supply about 80% of US power transformers (summary-level) — [Electrical Contractor](https://www.ecmag.com/magazine/articles/article-detail/investment-by-grid-equipment-makers-could-ease-shortage)
- China supplies under 1% of US HV breaker imports and 3% of transformer imports by value; Korea, Mexico and Canada supply 74% of breakers (12 months to June 2026) — [Rystad](https://www.rystadenergy.com/news/us-executive-order-targets-chinese-grid-hardware-but-battery-storage-serving-ai-d)
- SF6-free breakers already sold by incumbents: Siemens Energy to 145 kV, Hitachi Energy to 420 kV, GE Vernova at 420 kV (summary-level) — [Datam Intelligence](https://www.datamintelligence.com/blogs/us-high-voltage-circuit-breaker-epa-sf6-regulations)
- Turbine deliveries that need GSUs peak later than orders: GE Vernova targets 24 GW a year in 2028 and 30 GW in 2030 and is mostly sold out through 2030 — [POWER Magazine, Sep 2026](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/)
- Utility qualification evidence: ten-year US supply list required by one utility specification — [Utah PSC docket](https://pscdocs.utah.gov/electric/20docs/2003505/A-7.04.2_EBU_PX-S02_Substation_Equipment%20Collector_Substation_Main_Power.pdf)

### Inferences

**6.1 Thesis and assumptions**
Thesis: bushings, HV breakers, tap changers and large or GSU transformers have the longest waits in the grid supply chain, the US imports most of them, and one bushing maker just sold for $9B. A new domestic producer could sell everything it makes at scarcity prices and end up holding a qualified, hard-to-copy position.

Assumptions: (B1) the shortage lasts past 2030; (B2) capacity, not qualification, is the constraint and automation relieves it; (B3) a start-up can master the technology; (B4) OEMs and utilities will qualify a new vendor within its runway; (B5) capital and time to revenue are financeable; (B6) incumbents will not close the gap; (B7) policy favours a domestic entrant; (B8) the component markets are large enough.

**6.2 Assumption check**

| # | Supporting | Contradicting | Mark |
|---|---|---|---|
| B1 shortage lasts | GSUs over 160 weeks (Q1 2026); breakers 125 weeks; 15% power-transformer shortage (2026); turbine deliveries peak 2028-2032 so GSU demand lags orders | WoodMac: power transformers to 5% and GSUs to 14% or less by 2030; higher-voltage deficits "improving substantially" | Holds to 2029 for GSUs, Shaky after |
| B2 capacity is the constraint | Real output shortfall; 80% import share | Trench: the limit is qualifying capacity and insulator supply; tooling takes 2-4 years; plant ramps by voltage class over two years | Fails as a pure production story |
| B3 start-up can master it | None found | No start-up found in HV bushings, breakers or tap changers; products fail violently; field history is the product | Fails without an incumbent team |
| B4 qualification within runway | OEMs and Meta sign capacity deals at component level; behind-the-meter gas plants need GSUs outside utility lists | Utility specs want ten years of US supply history | Fails for utilities, Shaky for OEMs and developers |
| B5 capital and time | Trench $60M and 15 months (with existing designs and staff) | Large-transformer plants $150-457M and 2+ years for incumbents; a start-up adds design, tests and qualification | Shaky |
| B6 incumbents leave gap | "Invest only against backlog" (Hitachi); pricing discipline | Nearly $2B of US transformer capacity; Trench €400M; GE Vernova buying Trench; frame agreements lock buyers in to 2030 | Fails |
| B7 policy helps | Buy America rules for federally funded work; Aug 2026 order | China is already under 3% of imports; rivals are allied-country plants; the Section 232 rate on grid gear was cut to 15% through 2027 | Shaky |
| B8 market size | Trench alone is over €1B revenue; one 57-unit transformer plant implies roughly $250-500M a year at $4-9M a unit (my estimate) | No verified US market size for bushings, breakers or tap changers | Holds |

**6.3 Actor simulation, 2027-2032**
- 2027. Utilities keep buying three to five years ahead from approved makers. Siemens Energy's Charlotte plant starts; Trench reaches 550 kV in Charlotte. GE Vernova closes Trench late in the year. That is the one opening: Siemens Energy, Hitachi, Hyundai, Hyosung and independent US transformer makers will then depend on a bushing supplier owned by a competitor, and will want a second source (inference). Start-up: design, team and test planning; no revenue.
- 2028. Hitachi's Virginia plant opens; first 765 kV bushings ship from Charlotte. Start-up: prototypes in type testing; a first paid qualification with a transformer OEM or a behind-the-meter power developer is the best case.
- 2029. GSU demand is at its strongest as 2026-2027 turbine orders deliver. Hitachi's Mississippi plant starts. Start-up: first qualified low-voltage-class products, small volumes.
- 2030-2032. Power-transformer deficit about 5%, GSUs 10-14% (forecast). Utilities trial new vendors with a handful of units. Incumbents defend with bundles, long service contracts and tied supply. Start-up: volume orders begin only now; the scarcity price has mostly gone, but a qualified second source keeps a position.
- Buyers: investor-owned utilities are last; co-ops and munis buy through brokers; hyperscalers have reached into HV (Meta-Trench, Korean transformer contracts) but place those orders with makers that have decades of history; transformer OEMs and repair shops are the realistic first customers for components.
- Incumbents: add capacity only against frame agreements, buy suppliers, keep price. This discipline is real in HV, unlike in LV/MV gear.
- China and trade: little effect either way; China is already excluded in practice. If tariffs fall, Korean and European imports get cheaper and the domestic premium narrows.
- Regulators and gatekeepers: IEEE type tests, high-power laboratory slots and utility lists are the binding gate. State SF6 phase-outs create product turnover, but incumbents already sell the replacements.
- Labor: large-transformer winding is skilled manual work (about 45 man-hours per MVA in the analyst model); OEMs cite labor as a barrier. Local politics are favourable (jobs, incentives).
- Financiers: venture has not funded conventional HV; DOE grant money has gone to incumbents (for example $75M to Cleveland-Cliffs). Customer prepayment is the only plausible early money.
- Input suppliers: a new transformer maker queues for the same bushings (two years), tap changers and single-source steel as everyone else. Making large transformers depends on first solving components.
- Net effect on the start-up: price is good if it ever ships (scarcity margin to 2029, normal after); volume is negligible before 2030; time to first revenue 3-5 years.

**6.4 Market arithmetic**
- Size anchors: Trench (bushings, instrument transformers, reactors) over €1B revenue and €2.1B backlog (2026); nearly $2B of North American transformer capacity investment since 2023; US utility capex about $208B (2025). No verified US dollar figure for bushings, breakers or tap changers.
- Supply gap: 15% for power transformers (2026), 47-100% for GSUs (2025), falling to 5% and 10-14% by 2030 (forecast).
- If lead time fell 5-10x and price 30-50%: demand is set by utility capital plans, regulator approvals, interconnection (median over three years to an agreement) and turbine slots (five to seven years), not by transformer price. A GSU is a low single-digit percentage of a gas plant's cost (my estimate), so price elasticity is near zero. Faster delivery would speed some replacement and substation work, but the parallel gates remain. Expansion: about 0-10% in units; the dollar market shrinks if prices fall. The value of entry is share at scarcity margin, then a qualified position.
- Exit arithmetic: $9B for Trench on revenue of about $1.1-1.2B is roughly 8x revenue. A qualified component maker at $100M of revenue could be worth $300-800M to an OEM at 3-8x. That is the whole bull case for a founder.

**6.5 Bear / base / bull to 2032**

| Case | Probability (my judgement) | 2032 revenue | Capital consumed | Main reason |
|---|---|---|---|---|
| Bear | 55% | Under $20M | $100-250M | Qualification outlasts cash; first approved units arrive in 2030-2031 as deficits reach about 5%; plant sold cheaply to an incumbent |
| Base | 30% | $50-150M | $100-200M | Narrow component (for example bushings up to 230 kV or instrument transformers) sold to independent transformer makers and behind-the-meter developers as a second source; acquired |
| Bull | 15% | $300-600M | $300-500M | Becomes the independent second source after GE Vernova absorbs Trench, with OEM or hyperscaler prepayment; acquired for $2-4B |

Timing risk, directly: fund in 2027, plant in 2028-2029, type tests and approvals in 2029-2030, volume in 2030-2031. That lands after the forecast trough in power-transformer deficits. GSUs and bushings are the better-timed sub-segments because turbine deliveries run to 2032.

**6.6 Kill criteria and 90-day test**
- Kill if: (1) no transformer OEM or hyperscaler will sign a paid qualification and offtake agreement before the plant decision; (2) the founding team cannot recruit at least five senior engineers from Trench, Hitachi Energy, Reinhausen, Siemens Energy or HSP; (3) high-power test-lab slots are more than 12 months out; (4) GE Vernova gives rival OEMs binding supply assurances at closing; (5) forecast HV deficits for 2029 fall below 5%.
- 90-day test (under $100K): interview procurement heads at 15-20 independent transformer makers and repair shops and three hyperscaler energy teams. Ask for a signed second-source qualification agreement with paid engineering ($250K-1M). In parallel, get written test-slot quotes. Pass: one paid agreement. Without it, do not raise.

**6.7 Verdict**
Scores: demand certainty 7; production as true bottleneck 5; regulatory and qualification drag 2; defensibility after the shortage 7; capital to first revenue 2; founder buildability 2.
Judgement: C3 is where scarcity is deepest and where a position, once earned, behaves like the certificate-holder businesses in the red-team note. That same qualification wall is why abundant production does not unlock it: Trench built a plant in 15 months and still needs until 2028 to ship its top voltage class. Incumbents are closing the gap with their own capital and are buying the scarce suppliers. The only founder-accessible wedge is a narrow second-source component with a transformer OEM or hyperscaler paying for qualification, staffed by people who have done it before. For anyone else this is a capital sink with a 2030s payoff.

### Gaps
- No verified market size for bushings, HV breakers or tap changers; no tap-changer lead-time data. **[unverified recollection]**: Maschinenfabrik Reinhausen holds a dominant share of tap changers.
- No sourced type-test durations or utility qualification timelines.
- Terms of GE Vernova's Trench deal regarding supply to rival OEMs are unknown.
- Large-transformer unit prices in 2026 not sourced. **[unverified recollection]**: DOE's 2012 report cited $2-7.5M a unit.

## 7. Candidate C8: productized home energy (Australian-cost solar plus battery, or battery storage as a service)

### Takeaway
Latent demand is real: Australia shows 40% solar penetration and 600,000 batteries in 16 months when the price is right. But the US price gap is tariffs, customer acquisition, local rules and financing, none of which a factory fixes and only about half of which a company can change. A realistic company-achievable price is about $1.50-1.80/W, not $1.00/W. The storage-as-a-service version works where a retailer can capture wholesale value (Texas) and is now a contest of balance sheets that Base Power leads with over $2.5B.

### Cited Findings
(Evidence is in Section 4. Additional items used below.)
- US solar penetration is about 7% of homes versus 33% in Australia (BU, 2025); "1 in 10 vs 1 in 3" (Latitude, Oct 2025) — [Boston University](https://www.bu.edu/eci/files/2025/07/Intnatl-Cost-Comparisons-final.pdf); [Latitude Media](https://www.latitudemedia.com/news/can-the-us-bring-solar-installation-to-below-2-per-watt/)
- Marketing is 20-29% of the US price; US and Australian installer profit percentages are about the same (17-18%) — [Boston University](https://www.bu.edu/eci/files/2025/07/Intnatl-Cost-Comparisons-final.pdf)
- Automating permitting could cut permitting soft cost from 54 to 6 cents/W and overhead from 74 to 37 cents/W (SolarAPP founder's estimate, 2025) — [Latitude Media](https://www.latitudemedia.com/news/post-obbb-where-does-rooftop-solar-go-from-here/)
- China supplies 50% of US lithium-ion battery imports by value (12 months to June 2026); the August 2026 order names battery storage and grid inverters; residential impact not addressed — [Rystad](https://www.rystadenergy.com/news/us-executive-order-targets-chinese-grid-hardware-but-battery-storage-serving-ai-d)
- US turnkey grid storage cost $219/kWh versus $73/kWh in China (2025, BNEF) — [Energy-Storage.news](https://www.energy-storage.news/battery-storage-system-prices-continue-to-fall-sharply-bnef-and-ember-reports-find/)
- Base's strongest economics exist only in deregulated retail markets; outside ERCOT it depends on utility capacity payments, "a thinner and less proven stack" (third-party analysis) — [Sacra](https://sacra.com/c/base-power/)
- Base's 7,000 homes at end-2025 were 0.09% of ERCOT's deregulated single-family market — [Sacra](https://sacra.com/c/base-power/)

### Inferences

**7.1 Thesis and assumptions**
Thesis: the same solar hardware costs about $2.6/W installed in the US and about $0.8-1.0/W in Australia, and US penetration is a fifth of Australia's, so a vertically integrated company that sells a standard system with remote quoting, instant permits and one-day installs could unlock 15-20 million households. Alternatively, put a large battery at a home for almost nothing upfront and earn the return from retail energy and grid services, as Base Power does.

Assumptions: (D1) US households would adopt at Australian rates at Australian prices; (D2) the price gap is mostly cost a company can remove; (D3) customer acquisition cost falls with a productized offer; (D4) permitting and interconnection reform spreads fast enough; (D5) the economics work without 25D and under net billing; (D6) asset finance is available; (D7) incumbents cannot or will not match; (D8) compliant hardware is available at a workable price.

**7.2 Assumption check**

| # | Supporting | Contradicting | Mark |
|---|---|---|---|
| D1 latent demand | Australia: 40% of homes (2026), 600,000 batteries in about 16 months; advocacy estimate of +18-20M US households by 2040 | US volume fell only 15-23% when the buyer's price rose about 43% (loss of the 30% credit), implying modest short-run elasticity; Australian retail power prices are higher | Holds in direction, Shaky in size |
| D2 gap is removable | $0.57/W from installer operations; overhead and cancellation savings | Hardware is $1.28/W in the US versus $0.46/W (tariffs); $0.54/W needs regulatory change; instant permits save only $0.04/W directly | Fails for $1.00/W, Shaky for $1.50-1.80/W |
| D3 acquisition cost falls | Small installers at $1,000-3,000 per customer; Base's battery offer sells on backup at under $700 | Sunrun spends about $10,450 per subscriber (derived, Q3 2026); Australia's low cost follows from high penetration; 30% cancellations | Shaky |
| D4 reform spreads | State laws in NJ, MD, CA, FL; about 350 cities on SolarAPP+ | Best states score a B; utilities gate equipment (40% approve Tesla's switch) | Shaky |
| D5 economics without credit | Rising retail rates; batteries capture self-consumption | California volumes fell about 40% and stayed flat after net billing; Enphase US sell-through -35% (Q3 2026) | Shaky |
| D6 finance available | Base raised $2B in ten months | Banks "pens down" on residential 48E; Sunrun's net value per subscriber -28% and cash guidance at the bottom of range | Shaky |
| D7 incumbents cannot match | Dealer-heavy incumbents carry high selling cost | Base at $695 plus $19 a month with $13B valuation; Sunrun at 75% storage attachment and 1.06M subscribers; Tesla | Fails |
| D8 hardware supply | Domestic pack assembly (Base's Austin plant) | Battery quotes at $1,130/kWh and rising on sourcing rules; half of battery imports from China; polysilicon tariffs from Dec 2026 | Shaky |

**7.3 Actor simulation, 2027-2032**
- 2027. Last year third-party-owned solar can claim 48E by placing in service. Sunrun, Tesla and other lessors with safe-harboured equipment sell leases carrying a 30-43% credit that a new cash-sale installer cannot match. Cash and loan sales stay depressed. Base passes roughly 50,000-80,000 homes if it holds 100-200 installs a day (inference). Start-up: can sell on price in Texas and Florida, but against subsidized leases.
- 2028-2029. Safe-harboured equipment runs down; the solar credit ends for new leases. Installer bankruptcies and consolidation continue (the California pattern, where the top five went from 40% to 51% in a year). Storage keeps its credit, so battery-first offers dominate. More states adopt net billing; more adopt instant permits. Base and Tesla compete as retailers in Texas; utilities elsewhere contract home-battery capacity at single-digit dollars per kW-month. Start-up: this is the better entry window for a low-cost installer, since incumbents lose their credit advantage, but demand is thinner.
- 2030-2032. If retail rates keep rising and hardware tariffs ease, US prices drift toward $1.50-2.00/W and volumes recover above 2025 levels. If tariffs and sourcing rules tighten, prices stay above $2.50/W and the market stays near 400,000-500,000 systems a year.
- Homeowners: respond to bill savings and outage fear more than to system price; they convert when the upfront cost is near zero. Roughly 80% finance.
- Homebuilders: will accept a battery or solar package that costs them nothing and does not slow closings; Base already has a builder partnership of 200+ homes. This is a near-zero acquisition-cost channel, and the incumbent is already in it.
- Incumbents: Sunrun shifts to storage and its direct channel; Tesla bundles Powerwall with retail power in Texas; Enphase shrinks and relaunches batteries; Texas retailers can copy Base by partnering with a battery maker. Expect price matching, not retreat.
- China and trade: Australia's price depends on tariff-free Chinese hardware. US policy is moving the other way (sourcing rules, polysilicon tariffs, the August 2026 order). If tariffs fall, every installer gets the same benefit, so it is not a moat. If they rise, firms with domestic cell contracts win.
- Regulators and gatekeepers: thousands of local permit offices and hundreds of utilities; state export-rate cuts continue; instant-permit laws spread slowly. Battery-only installs avoid most roof and export approvals, which is why Base gets permits in days to weeks.
- Labor: licensed electricians are the scarce input; 74% of contractors report higher labor rates (2026). Base claims 10+ homes per electrician per day, against 1-2 normally.
- Financiers: venture will fund one or two national champions at billion-dollar scale; tax equity and securitization are tight for residential. A new battery-service entrant needs asset finance from the first thousand homes.
- Net effect on the start-up: price is set by Base in Texas and by subsidized leases elsewhere until about 2029; volume is limited by capital and by which jurisdictions are workable; margins are installer margins (17-18% gross) unless it owns the assets.

**7.4 Market arithmetic**
- Market today: about 4.1 GW of residential solar in 2026 (BNEF) at $2.57/W is about $10.5B. Residential storage of roughly 2.0-4.0 GWh (sources conflict) at $1,130/kWh adds $2.3-4.5B. Total about $13-15B a year, on roughly 450,000-500,000 systems at 8-9 kW.
- What sets the US price, and what a company can change (per W, from the Tesla, BU and Sunrun figures):
  - Hardware and tariffs, about $0.5-0.8 of the gap: policy, not changeable.
  - Permitting, inspection, interconnection, about $0.5: mostly not changeable; a company can only choose jurisdictions.
  - Customer acquisition, $0.5-1.2: partly changeable through a simple offer, builder and utility channels and local density.
  - Install operations, overhead, cancellations, about $0.6: changeable.
  - Dealer and financing fees, 5-50% of price: changeable with own capital.
  - Result: a best-in-class operator in a fast-permit state can plausibly reach $1.50-1.80/W for solar. $1.00/W needs tariff-free hardware and national rule changes.
- Households at $1/W, three ways:
  - Elasticity. The 25D natural experiment: price up 43%, volume down 15-23%, so arc elasticity is -0.5 to -0.7; because half the market kept a credit through leasing, the true figure is probably nearer -1 to -1.5. A 2.6x price cut then gives 1.6x (at -0.5), 2.6x (at -1.0) or 4.2x (at -1.5) of today's roughly 475,000 systems: 0.75-2.0 million a year.
  - Australia's run-rate. About 3% of homes a year at peak **[unverified recollection of install counts; first-round note cites 90-110k a quarter]** applied to about 70 million US owner-occupied detached homes **[unverified recollection]** gives about 2 million a year.
  - Advocacy model. Permit Power: +18-20 million households by 2040.
  - My estimate: at a true $1/W, 1.0-1.5 million installs a year and 15-20 million added homes over 12-15 years, taking the US to about 25-30% of suitable homes. At the company-achievable $1.50-1.80/W, about 0.7-0.9 million a year.
  - Revenue check: 1.2 million systems at $8,000 is $9.6B a year, below today's $10.5B. Units triple; dollars do not grow. The gain goes to households.
- Payback sanity check (my arithmetic; assumes 8 kW, 1,400 kWh per kW-year, half self-consumed at 17 cents and half exported at 5 cents **[rates unverified]**): $1,230 a year. At $1/W payback is 6.5 years; at $2.57/W it is 16.7 years. That gap is the difference between a mass product and a niche one.
- Households at zero-upfront storage:
  - Australia added batteries to 5.3% of all homes in about 16 months (600,000 of about 11.25 million homes, derived from 4.5 million systems at one in 2.5 homes) with a 30% rebate and customers still paying thousands. Scaled by homes, that is 3.7 million of 70 million US detached owner-occupied homes; scaled by solar homes (13% of them), about 0.7-1.2 million.
  - The limit is the value stack, not willingness. ERCOT's competitive area is about 7.8 million single-family homes (7,000 / 0.09%). Elsewhere a utility must pay for capacity. At $8.50/kW-month and about 10 kW per home (my assumption) that is about $1,000 a year plus $230-350 of lease fees against about $7,000 of net cost: a simple payback over five years before overhead and cost of capital.
  - My estimate: 1-2.5 million US homes on battery-service contracts by 2032 across all providers, needing $10-25B of asset capital. One or two firms will hold most of it.

**7.5 Bear / base / bull to 2032 (a start-up founded in 2027)**

| Case | Probability (my judgement) | 2032 revenue | Capital consumed | Main reason |
|---|---|---|---|---|
| Bear | 50% | Under $50M | $40-80M | Acquisition cost does not fall without penetration; subsidized leases undercut until 2029; a state changes export rates; sold or closed |
| Base | 35% | $250-500M (15,000-25,000 installs a year at $16-20K with battery) | $150-300M equity plus $300M+ asset debt | Regional low-cost installer in three or four fast-permit, high-rate states; installer-level margins |
| Bull | 15% | $1.5-2B | $500M-1B+ | Tariffs ease, national permitting and interconnection reform, rates up 30%; builder and utility channels deliver 100,000 installs a year |

Timing note: C8 has the opposite timing problem from C2 and C3. Entering in 2027 means competing against the last subsidized lease cohort; the cleaner window opens in 2029-2030.

**7.6 Kill criteria and 90-day test**
- Kill if: (1) blended acquisition cost stays above about $3,000 a home (about $0.40/W) after 500 installs; (2) median sale-to-permission-to-operate exceeds 30 days; (3) cancellations exceed 15%; (4) asset finance is unavailable below about 10%; (5) Base or Tesla enters the launch market at a price below your cost; (6) the launch state cuts export or capacity compensation.
- 90-day test, installer version (about $300-600K, hardware cost recovered in the sale price): one Texas or Florida metro with fast permits and a co-operative or municipal utility. One fixed package (for example 6 kW plus one battery) at a posted all-in price near $1.60/W-equivalent, quoted remotely. Three channels in parallel: neighbourhood-dense marketing, one homebuilder, one utility partner. Subcontract 20-30 installs. Measure acquisition cost, close rate, days to operation, crew hours and cancellations. Take $1,000 deposits, because smaller deposits measure curiosity (red-team note).
- 90-day test, battery-service version (under $100K): obtain one signed term sheet from a co-op or muni for a ten-year capacity payment at $8/kW-month or better, and one from a warehouse lender. If neither signs, the model does not exist outside ERCOT.

**7.7 Verdict**
Scores: demand certainty 6; production as true bottleneck 2; regulatory and qualification drag 4; defensibility after the shortage 3; capital to first revenue 8 for the installer version and 3 for the battery-service version; founder buildability 6.
Judgement: C8 has the largest pool of households that would buy at a lower price, and it is the candidate where "abundant production" matters least. China already makes the hardware at Australian prices; US law and local process keep it out of reach. A founder can remove perhaps half the gap through process, which makes a decent regional installer with thin margins, not a Model T. The version with venture-scale economics is the battery as a financed grid asset, and there the scarce inputs are cheap capital, a retail licence and utility contracts. Base Power holds all three at a scale a 2027 entrant cannot match. If pursued, do it as a capital-light installer in fast-permit states timed for the 2029 credit cliff, or as a channel partner to utilities and builders, not as a hardware company.

### Gaps
- US counts of owner-occupied detached homes and average retail rates used above are from memory and need sourcing.
- Australian 2026 installed prices for solar and batteries were not retrieved; the $0.82/W figure is 2023 IEA data via Boston University.
- The 25D elasticity estimate is confounded by demand pulled into 2025 and by substitution into leases.
- No data on Base Power's acquisition cost, churn beyond August 2025, or performance in Illinois.
- Whether the August 2026 order and sourcing rules reach residential batteries and inverters is unknown.
- Tesla Energy's residential volumes and pricing were not found.
