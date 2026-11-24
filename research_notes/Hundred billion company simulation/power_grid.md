# Electricity supply and electrical equipment bottlenecks (as of 24 November 2026)

Research notes. Method limits the reader must know:

- The shared web-search budget ran out after about 40 searches. Later work used direct page fetches of URLs already found. Topics hit by this are flagged in each Gaps section (nuclear, Base Power, MISO, Energy Transfer, Atlas, named Google demand-response contracts, Lazard LCOE+).
- Items marked † come from a search-result summary; the page itself was not opened. Treat these as leads to verify, not settled facts.
- Items marked "derived" are my arithmetic on sourced numbers.
- Several pages (SemiAnalysis, Bloomberg, Cleanview) were paywalled past the opening section.

## 1. Load growth forecasts, PJM capacity auctions, large-load interconnection requests

### Takeaway
Official forecasts are large but heavily discounted by the forecasters themselves: PJM cut utility data-center submissions for 2030 by 43%, and ERCOT says its 474 GW large-load queue is not committed demand. The hard evidence of scarcity is PJM's capacity market, which has cleared at its price cap three auctions running and is now 6.8 GW short of its reliability requirement.

### Cited Findings

PJM capacity market
- 2028/2029 Base Residual Auction (results 14 July 2026) cleared at the cap of $325/MW-day across the whole footprint, procuring 138,318 MW UCAP, 6,831 MW short of the reliability requirement — [PJM release](https://www.pjm.com/-/media/DotCom/about-pjm/newsroom/2026-releases/20260714-pjm-capacity-auction-procures-138318-mw-of-generation-resources.pdf); [PJM BRA report](https://www.pjm.com/-/media/DotCom/markets-ops/rpm/rpm-auction-info/2028-2029/2028-2029-bra-results-report.pdf)
- Third straight auction at the cap. Prior caps: $333.44/MW-day (2027/28) and about $329/MW-day (2026/27; sources differ between $329.17 and $329.43) — [OPIS](https://www.opis.com/resources/energy-market-news-from-opis/pjms-2028-2029-capacity-auction-clears-at-price-cap-for-third-time/)
- Without the price collar PJM's simulation gives about $555/MW-day RTO-wide and $777/MW-day in ComEd. Cost to load is $16.4B at the cap versus about $29.7B uncapped — [Utility Dive, 15 Jul 2026](https://www.utilitydive.com/news/pjm-capacity-auction-price-cap-reserve-shortfall-grows/825282/); [Modo Energy](https://modoenergy.com/research/English/pjm-capacity-auction-2028-2029-reliability-price-cap-elcc)
- Only about 525 MW of new generation cleared (208 MW of it uprates), down from 774 MW in the prior auction. Demand response cleared 7,365 MW. Shortfall grew from 6.5 GW to 6.8 GW against a 20% installed reserve margin target — [Utility Dive](https://www.utilitydive.com/news/pjm-capacity-auction-price-cap-reserve-shortfall-grows/825282/)
- PJM's board was preparing FERC filings for a one-off backstop capacity auction and a "connect and manage" framework for data centers — [Utility Dive](https://www.utilitydive.com/news/pjm-capacity-auction-price-cap-reserve-shortfall-grows/825282/)

PJM load forecast (January 2026)
- Summer peak forecast reaches 222,106 MW in 2036, a 10-year increase of 65,733 MW, 3.6%/yr average. The 2021 forecast assumed 0.3%/yr † — [PJM 2026 Load Report](https://www.pjm.com/-/media/DotCom/library/reports-notices/load-forecast/2026-load-report.pdf); [Utility Dive](https://www.utilitydive.com/news/pjm-interconnection-load-forecast-data-centers/809717/)
- PJM lowered the near-term outlook versus its 2025 forecast: summer peak down 2,564 MW for 2026 (−1.6%) and 4,414 MW for 2028 † — [POWER](https://www.powermag.com/pjm-dials-back-near-term-load-outlook-but-maintains-steep-long-term-growth-trajectory/)
- Utilities submitted about 60 GW of large-load additions for 2030; PJM accepted 34 GW, a 43% haircut. Large loads are 78% of forecast growth to 2046 † — [Modo Energy](https://modoenergy.com/research/English/pjm-load-forecast-data-centers-2046)

ERCOT
- ERCOT is tracking about 474 GW of large loads seeking interconnection as of June 2026, about 90% data centers — [ERCOT Senate briefing, 29 Jul 2026](https://www.ercot.com/files/docs/2026/07/29/ERCOT-Senate-July-29-Panel-1-Assessing-The-Grid.pdf)
- Progression in 2026: about 410 GW (April board update, after 198 new requests in Q1), about 438 GW (June), 474 GW (July briefing) † — [ERCOT April update](https://www.ercot.com/files/docs/2026/04/13/9-Interconnection-and-Grid-Analysis-Update.pdf)
- Of 445.8 GW of applications in the April monthly report, 321 GW had no studies submitted and only 5.9 GW of large load was observed energized † — [ERCOT Monthly, April 2026](https://www.ercot.com/files/docs/2026/05/13/ERCOT-Monthly-April-2026-FINAL.pdf)
- ERCOT moved to a batch study ("Batch Zero"): loads needed a qualifying study by 10 July 2026, must post financial security of $50,000/MW, and get year-by-year MW allocations for 2028–2032. ERCOT audits eligibility by asking for purchase orders for long-lead equipment, land agreements and end-user agreements — [ERCOT Senate briefing](https://www.ercot.com/files/docs/2026/07/29/ERCOT-Senate-July-29-Panel-1-Assessing-The-Grid.pdf)
- About 205 GW of large load was eligible for the first batch † — [ERCOT Senate briefing](https://www.ercot.com/files/docs/2026/07/29/ERCOT-Senate-July-29-Panel-1-Assessing-The-Grid.pdf)
- ERCOT generation queue at 30 June 2026: 462,785 MW across 1,949 requests: solar 161,554 MW, storage 170,945 MW (about 410 GWh), gas 77,607 MW, wind 47,991 MW — [ERCOT Senate briefing](https://www.ercot.com/files/docs/2026/07/29/ERCOT-Senate-July-29-Panel-1-Assessing-The-Grid.pdf)

National and global
- EIA STEO released 10 Nov 2026: US power-sector generation projected at a record of almost 4,390 BkWh in 2026 (+2.7%), then +1.2% in 2027. The page's data table shows different totals (4,539 and 4,595 BkWh), so the level should be checked; the growth rates are the text figures. Residential retail price 18.2 c/kWh in 2026 and 18.7 c in 2027, up from 17.2 c in 2025 — [EIA STEO](https://www.eia.gov/outlooks/steo/report/elec_coal_renew.php)
- EIA expects commercial electricity use to pass residential for the first time in 2027, and names ERCOT and PJM as the fastest-growing regions for data-center demand † — [EIA Today in Energy](https://www.eia.gov/todayinenergy/detail.php?id=67344)
- IEA Electricity 2026 (Feb 2026): global demand grows 3.6%/yr over 2026–2030, from 28,200 TWh (2025) to 33,600 TWh (2030), about 1,100 TWh added per year versus about 700 TWh/yr in 2015–2025. Data centres are about half of US demand growth to 2030 † — [IEA](https://www.iea.org/reports/electricity-2026/executive-summary)
- Grid Strategies (2025 report): 166 GW of forecast US peak growth through 2030, about 90 GW tied to data centers; the firm estimates utility forecasts overstate data-center growth by about 25 GW by 2030 † — [Grid Strategies](https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf)
- NERC's 2025 Long-Term Reliability Assessment forecast 224 GW of summer peak growth, more than 69% above its prior forecast — [POWER](https://www.powermag.com/the-new-large-load-compact/)
- Goldman Sachs: US data-center demand 66 GW in 2027, up from 31 GW in 2025. EPRI: data centers 9–17% of US electricity by 2030 versus 4–5% today — [Utility Dive, 26 Jun 2026](https://www.utilitydive.com/news/data-centers-flexibility-utilities-speed-to-power/822588/); [Power Engineering](https://www.power-eng.com/gas/data-center-power-crunch-lifts-engines-aeroderivatives-into-larger-role/)
- SemiAnalysis (25 Jun 2026): US data-center build of +21 GW in 2026 rising to +84 GW/yr by 2030; net new grid firm capacity only about 15 GW/yr rising to 20+ GW/yr; gas nameplate additions under 10 GW/yr in 2026 and 2027 — [SemiAnalysis](https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw)
- LBNL (July 2026): more than 700 new gas plants totaling 260 GW are in queues, up 270% since 2022; build-out cost could exceed $400B — [LBNL](https://eta-publications.lbl.gov/sites/default/files/2026-07/integrading_ai_data_centers_with_the_power_grid.pdf)
- FERC in June 2026 directed the six jurisdictional grid operators to justify or reform rules for large loads, with speed to power as the stated goal — [POWER](https://www.powermag.com/the-new-large-load-compact/)
- As of 31 Mar 2026 there were 77 approved or proposed large-load tariffs covering 60 utilities in 36 states; 29 were approved in 2025 versus 14 in 2018–2024. Pennsylvania's model tariff: 5-year minimum term, 80% minimum billing demand, security for network upgrades — [NC Clean Energy Technology Center, 20 Apr 2026](https://nccleantech.ncsu.edu/?p=13984)

### Inferences
- Queue numbers (474 GW in ERCOT, 300 GW "planned" nationally) are options, not orders. The forecasters' own haircuts are 40–70%. The supply-side numbers are firmer: about 15 GW/yr of new firm grid capacity against 21–84 GW/yr of intended data-center build.
- Regulators are raising the cost of holding a queue place ($50,000/MW security, 5-year minimum terms, 80% take-or-pay). That favors well-capitalized buyers and makes "proof of long-lead equipment purchase orders" a gating asset in its own right.
- PJM capacity at $325/MW-day is about $119/kW-yr (derived), still below the cost of new gas entry, which is why almost no new generation cleared.

### Gaps
- MISO load forecast and auction results: not researched (search budget).
- EIA consumption figures for 2026–2027 conflict across STEO editions (4,269 vs 4,211 BkWh in different reports); not resolved.
- No ERCOT large-load figure after September 2026 was found.

## 2. Gas turbines, reciprocating engines, aeroderivatives, fuel cells and new entrants

### Takeaway
The three large-frame makers hold about 260 GW of orders and reservations (GE Vernova 122 GW, Siemens Energy 104 GW, Mitsubishi 35 GW large-frame) against about 60–70 GW/yr of global capacity, and are selling 2030–2032 delivery slots. Order growth slowed sharply in Q3 2026, the first sign the scarcity may be peaking. Anything deliverable in 2027–2028 (engines, refurbished aeroderivatives, fuel cells) is selling at $1.0–2.5M/MW.

### Cited Findings

GE Vernova (Q3 2026, reported 28 Oct 2026)
- Gas equipment backlog plus slot reservations 122 GW (64 GW backlog, 58 GW slots), up from 116 GW in Q2 and 83 GW at the start of 2026. Target at least 130 GW by year-end. In Q3 it signed 11 GW and shipped 5 GW — [GE Vernova 8-K](https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000162/gevpressrelease3q26.htm); [Utility Dive](https://www.utilitydive.com/news/ge-vernova-in-9b-deal-to-buy-high-voltage-manufacturer-as-gas-turbine-orde/873223/)
- Reservations are open for 2032 delivery. Customer mix about 80% traditional (utilities and IPPs), 20% data centers. Management reported no slot exits — [Utility Dive](https://www.utilitydive.com/news/ge-vernova-in-9b-deal-to-buy-high-voltage-manufacturer-as-gas-turbine-orde/873223/)
- Pricing: Q3 order pricing more than 20% above Q4 2025; full-year 2026 order pricing on track to be up 50% year over year; per-kW pricing likely to dip next quarter on mix — [Utility Dive](https://www.utilitydive.com/news/ge-vernova-in-9b-deal-to-buy-high-voltage-manufacturer-as-gas-turbine-orde/873223/)
- Power segment: orders $21.8B (+178% organic), revenue $6.1B (+25%), segment EBITDA margin 21.4% (+800 bps). Company backlog $197B — [GE Vernova 8-K](https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000162/gevpressrelease3q26.htm)
- Slowdown: the +6 GW quarterly increase compares with double-digit GW increases earlier in 2026. CEO says 2027 quarters will look like Q3–Q4 2026, not H1 2026. Jefferies called the 2027 turbine guidance "soft" — [Utility Dive](https://www.utilitydive.com/news/ge-vernova-in-9b-deal-to-buy-high-voltage-manufacturer-as-gas-turbine-orde/873223/)
- GE Vernova makes about 50 large-frame turbines a year, rising to 70–80 by late 2026 — [Wood Mackenzie, 1 Apr 2026](https://www.woodmac.com/press-releases/gas-turbine-prices-soar-195-as-market-faces-supply-demand-crisis)

Siemens Energy (FY2026, reported 11 Nov 2026)
- Record 42 GW of gas turbine orders in FY2026. Year-end commitments 104 GW: 65 GW firm, 39 GW slot reservations expected to convert in FY2027 at better margins. Gas Services backlog €74B (+35%), segment margin 16.4% (13% prior year). Q4 orders only about 2 GW, attributed to timing — [Turbomachinery, 13 Nov 2026](https://www.turbomachinerymag.com/view/siemens-energy-fy2026-record-backlog-164-billion-gas-services-orders)
- Data centers are about €15B of backlog, under 10% of the total. Management expects turbine orders at roughly the current pace through 2030 and possibly 2035. About €4B of new capacity planned through 2030. Twenty-year service contracts signed this year carry margins 5 points higher than before — [Utility Dive, 17 Nov 2026](https://www.utilitydive.com/news/elevated-demand-for-gas-turbines-could-persist-through-2035-siemens-energy/874839/)
- Medium gas turbine capacity rising from about 50 to about 80 units a year; group backlog €164B; FY2027 Gas Services margin guided to 18–20% — [Turbomachinery](https://www.turbomachinerymag.com/view/siemens-energy-fy2026-record-backlog-164-billion-gas-services-orders)

Mitsubishi Heavy Industries
- Large-frame backlog 35 GW, up from 23 GW a year earlier. Orders booked in the latest quarter deliver 2028–2030. Plans to double capacity versus 2024 but will not take twice the orders; says it is being selective — [Utility Dive, 13 Aug 2026](https://www.utilitydive.com/news/mitsubishi-gas-turbine-backlog-earnings/827761/)
- Lead times have gone from two years to five or more; MHI is signing for 2031–2034 delivery † — [S&P Global, Jul 2026](https://www.spglobal.com/energy/en/news-research/latest-news/energy-transition/070326-interview-mitsubishi-power-gas-turbine-orders-stretch-to-2030-amid-ai-security-demand)
- MHI expects global orders to decline slightly in 2026 from 2025 and hold near 70 GW/yr through 2030 † — [Bloomberg, 12 May 2026](https://www.bloomberg.com/news/articles/2026-05-12/mitsubishi-heavy-sees-global-gas-turbine-demand-staying-strong)

Prices and lead times
- Wood Mackenzie (1 Apr 2026): turbine equipment price heading to $600/kW by end-2027, up 195% from 2019. Global orders 110 GW at end-2025 against 60–70 GW of manufacturing capacity. Lead times six years. Turbines are 20–30% of combined-cycle project cost. Wood Mackenzie expected orders to peak in 2026 — [Wood Mackenzie](https://www.woodmac.com/press-releases/gas-turbine-prices-soar-195-as-market-faces-supply-demand-crisis)
- Reuters (9 Nov 2026): new gas turbines $2.0–2.5M per MW; well-maintained used units $1.5–1.7M per MW; refurbished units about $1.3M per MW. New US turbine deliveries average six years — [Oil & Gas 360 / Reuters](https://www.oilandgas360.com/used-jet-engines-find-new-market-as-ai-developers-race-to-secure-electricity/)
- All-in combined-cycle cost: BNEF average $2,157/kW in 2025, up from under $1,500 in 2023 † — [Bloomberg, 23 Apr 2026](https://www.bloomberg.com/news/articles/2026-04-23/cost-to-build-natural-gas-fired-power-plant-surges-66-bnef-says). IEEFA: newest proposals at least $2,500/kW † — [IEEFA](https://ieefa.org/resources/misguided-stampede-build-gas-power-plants). E3 (Jan 2026): about $2,500/kW CCGT and about $1,700/kW frame CT for 2030 COD — [E3 RECOST](https://www.ethree.com/recost-q1-2026-update/)
- Older comparison (Sept 2025): projects for 2026–2027 completion reported $1,116–1,427/kW; projects for 2030–2031 report $2,000/kW or more. Two Kentucky utilities paid GE Vernova a $25M reservation fee for one turbine for 2030 — [Latitude Media](https://www.latitudemedia.com/news/gas-turbine-prices-are-up-and-arent-going-down-anytime-soon/); [APPA](https://www.publicpower.org/periodical/article/new-report-finds-rising-cost-new-gas-plants-outpacing-planning-assumptions)
- Gas turbine and generator step-up transformer lead times are 3–4 years versus a norm of about 18 months; gas plant development has gone from about 24 months to at least 4 years — [SemiAnalysis, 25 Jun 2026](https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw)

Reciprocating engines
- Caterpillar Q3 2026: backlog a record $78B, up about 96% year over year. Power generation sales up 30%. Power & Energy segment profit about $2.1B on $8.8B sales (about 24%, derived). Management says bringing capacity online is the top pacing factor — [Utility Dive, 3 Nov 2026](https://www.utilitydive.com/news/caterpillar-posts-highest-sales-quarter-ever-data-centers-q3-2026/873586/)
- Named Caterpillar deals: Nscale Monarch campus (West Virginia), 2 GW of G3500 engines; Joule Capital, 4 GW campus in Utah — [Power Engineering, 16 Apr 2026](https://www.power-eng.com/gas/data-center-power-crunch-lifts-engines-aeroderivatives-into-larger-role/); [POWER](https://www.powermag.com/engine-power-plants-surge-as-data-centers-drive-unprecedented-demand/) †
- Wärtsilä: more than 3 GW sold for US data centers across seven orders. The latest, 282 MW (15 × 50SG) booked Q3 2026, delivers in 2028 and reaches full operation in 2029. So engine orders placed today deliver about two years out — [Wärtsilä, 5 Oct 2026](https://www.wartsila.com/usa/media/news/05-10-2026-wartsila-to-supply-282-mw-onsite-power-solution-for-a-u-s-data-center-as-ai-growth-intensifies-demand-for-reliable-power-3797450)
- Wärtsilä is investing €190M to raise capacity 35% by early 2028. Sweet spot is 50–400 MW off-grid plants. Pipeline up about 50% in six months (Feb 2026) — [Wärtsilä](https://www.wartsila.com/investors/blog/post/highlights-from-the-data-centre-theme-call)
- INNIO and Rehlko signed a framework for 1.25 GW of Jenbacher engines over three years, expanding a 700 MW reservation — [Power Engineering](https://www.power-eng.com/gas/data-center-power-crunch-lifts-engines-aeroderivatives-into-larger-role/)

Fuel cells (Bloom Energy)
- Q3 2026 revenue $1,235.8M (+138%); product revenue $1,073.6M (+179%); non-GAAP gross margin 34.5%; non-GAAP operating income $285.7M. FY2026 guidance raised to $4.4–4.6B revenue (from $3.1–3.3B at the start of the year) — [Bloom Q3 release](https://finviz.com/news/406808/bloom-energy-reports-record-third-quarter-2026-financial-results-and-raises-full-year-2026-guidance); [Bloom Q4 2025 supplemental](https://www.sec.gov/Archives/edgar/data/1664703/000162828026005798/q4-2025xsupplementalxdec.htm)
- Backlog at end-2025: product about $6.0B (2.5× 2024), service about $14.0B. 2025 revenue $2.02B — [Bloom Q4 2025 supplemental](https://www.sec.gov/Archives/edgar/data/1664703/000162828026005798/q4-2025xsupplementalxdec.htm)
- Oracle agreed (14 Apr 2026) to buy up to 2.8 GW; 1.2 GW is contracted for use in 2026–2027 — [Bloomberg Law](https://news.bloomberglaw.com/esg/oracle-agrees-to-buy-power-from-bloom-for-ai-data-centers)
- Brookfield partnership reported as expanded from $5B to up to $25B in July 2026 † (secondary aggregator; verify) — [Enki AI](https://enkiai.com/why-bloom-energy-is-crushing-the-hydrogen-market/)

Aeroderivatives, refurbishers and new entrants
- ProEnergy converts used aircraft-engine cores into the 48–50 MW PE6000. Crusoe contracted 13 units (650 MW) in April 2026 for delivery by summer 2027 — [Power Engineering](https://www.power-eng.com/gas/data-center-power-crunch-lifts-engines-aeroderivatives-into-larger-role/)
- ProEnergy says it sold 21 units to two data-center projects totaling over 1 GW, for bridging power of five to seven years; a new GE Vernova LM6000 can mean a three-to-five-year wait † — [EEPower](https://eepower.com/news/can-repurposed-jet-engines-solve-ai-data-center-power-problems/)
- Boom Supersonic "Superpower": 42 MW turbine derived from its Symphony engine. Crusoe ordered 29 units (1.21 GW); Boom claims over $1.25B backlog; target over 4 GW/yr by 2030; $300M round led by Darsana (Dec 2025). The release reports no Superpower prototype run; Symphony core testing was slated for 2026 — [Boom press release](https://boomsupersonic.com/press-release/boom-supersonic-to-power-ai-data-centers)
- Crusoe also holds 29 GE Vernova aeroderivative units (nearly 1 GW) and filed for up to 933 MW of gas at its Goodnight campus, including 19 LM2500s — [Sacra](https://sacra.com/c/crusoe/); [SemiAnalysis](https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw)

### Inferences
- Boom's implied price is about $1.03M/MW (derived: $1.25B ÷ 1.21 GW), in line with refurbished units and half the $2.0–2.5M/MW quoted for new turbines. A buyer paid new-entrant risk for a 2027-ish slot at that price.
- The value of a delivery slot before 2029 is the scarce good. OEMs are monetizing it through reservation fees and 20-year service contracts, not just unit price.
- Demand is mostly not data centers: 80% of GE Vernova's and over 90% of Siemens Energy's book is traditional buyers. A data-center slowdown alone would not empty the order books, but the Q3 2026 deceleration at GE Vernova and Siemens' 2 GW Q4 are worth watching.
- Three OEMs are all adding capacity for 2027–2028 (GE to 70–80 units, MHI 2×, Siemens +€4B, Wärtsilä +35%, Caterpillar). A new hardware entrant shipping in 2029+ meets that added supply.

### Gaps
- No OEM discloses $/kW by slot year. The $600/kW (equipment) and $2.0–2.5M/MW (Reuters) figures are analyst and press numbers on different scopes.
- No 2026 delivery or test update for Boom Superpower was found.
- Rolls-Royce mtu and INNIO order totals and lead times: not found. Baker Hughes and Solar Turbines volumes: not researched.
- FTAI's jet-engine power turbine program (reported target of 100 units for 2027) surfaced only as a headline † — [Magica](https://magica.com/news/data-centers-retired-jet-engines-power-grid-delays)
- Bloom's current backlog and its price per kW: not disclosed in the Q3 release.

## 3. Behind-the-meter and onsite power for datacenters: deals, terms, financing, unit economics

### Takeaway
Onsite power has become a contracted infrastructure business with 10–15 year take-or-pay terms from investment-grade buyers, financed with high-yield notes, asset-backed loans, vendor finance and private-equity co-investment. Disclosed capital cost is about $1.4–1.5M/MW for engine fleets and targeted payback is four to six years. Announcements (90–177 GW) vastly exceed what is running (about 2 GW in mid-2026).

### Cited Findings

Market size and status
- Cleanview: 59 data centers plan about 90 GW of self-generation. About 2 GW is online across four projects as of mid-2026; about 1.2% of capacity is under construction, about 36% permitted, about 60% only announced † — [Cleanview](https://cleanview.co/reports/behind-the-meter-data-centers/full-report)
- Earthjustice/EIP/GEM (Oct 2026): 177 GW of planned gas "bring your own power" across 129 plants; nine projects are 4.5 GW or larger. Disclosed mix: 42% combined cycle, 27% reciprocating engines, 25% simple-cycle turbines, 6% fuel cells. Also 63 GW solar and 164 GWh of batteries proposed. Advocacy source — [Earthjustice](https://earthjustice.org/document/the-ai-gas-rush-risks-and-implications-of-bring-your-own-power-executive-summary)
- SemiAnalysis expects onsite power to serve well over half of new US data centers from 2028 and equipment demand above 50 GW/yr by 2029 — [SemiAnalysis](https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw)
- New Mexico blocked a gas pipeline meant to fuel a 2.45 GW onsite plant at an OpenAI/Oracle Stargate site † — [Cleanview](https://cleanview.co/content/power-strategies-report)

Solaris Energy Infrastructure (NYSE: SEI)
- Q3 2026: revenue $341.1M (+104%); adjusted EBITDA $136.1M (39.9% margin). Power Solutions revenue $284.2M, segment adjusted EBITDA $127.0M † — [Finviz](https://finviz.com/news/417401/solaris-doubles-the-eps-consensus-and-raises-guidance-again-but-a-services-heavy-mix-thins-margins-and-the-stock-has-gone-nowhere); [StockStory](https://stockstory.org/us/stocks/nyse/sei/news/earnings-call/sei-q3-2026-deep-dive-contract-wins-and-expansion-offset-by-margin-pressures)
- Contracted long-term capacity 3.2 GW (about 1.4 GW at end-2025). Backlog over $16B, average term about 11 years. Run-rate adjusted EBITDA potential about $1.6B. Average capacity earning revenue was 820 MW in Q3 — [Finviz](https://finviz.com/news/417401/solaris-doubles-the-eps-consensus-and-raises-guidance-again-but-a-services-heavy-mix-thins-margins-and-the-stock-has-gone-nowhere)
- New contract (29 Oct 2026): 900 MW for 15 years with a 15-year extension option, with an existing investment-grade industrial and technology customer; covers generation, balance of plant and O&M; deploys from H1 2027 through 2028. Also a 7-year O&M contract for about 400 MW owned by a customer — [Solaris 10-Q summary](https://last10k.com/sec-filings/sei/0001628280-26-071604.htm)
- Termination for convenience costs the customer 50% of undiscounted future revenue. No customer is expected to exceed about 35% of EBITDA — [Finviz](https://finviz.com/news/417401/solaris-doubles-the-eps-consensus-and-raises-guidance-again-but-a-services-heavy-mix-thins-margins-and-the-stock-has-gone-nowhere)
- Financing: Q3 capex $547M. Debt attributable to Solaris $2.4B (from $973M at year-end). $1.25B senior unsecured notes; $850M revolver undrawn; ratings BB- / Ba3 / BB. Part of the fleet sits in the Stateline Power JV — [Solaris 10-Q summary](https://last10k.com/sec-filings/sei/0001628280-26-071604.htm)
- Guidance: Q4 2026 adjusted EBITDA $165–185M; Q1 2027 $220–260M; 2027 more than double 2026. Margins fell as lower-margin services and equipment sales grew — [Finviz](https://finviz.com/news/417401/solaris-doubles-the-eps-consensus-and-raises-guidance-again-but-a-services-heavy-mix-thins-margins-and-the-stock-has-gone-nowhere)

Liberty Energy (Liberty Power Innovations)
- Q3 2026: signed a 1.2 GW integrated power agreement with a frontier AI lab and an infrastructure platform. 15-year terms. About $300M capacity-fee prepayment expected in Q4, not contingent on the energy service agreement. First ESA of about 500 MW targeted by December 2026. Energization phased Q4 2027 to Q1 2029. Non-recourse project financing planned for early 2027. About $450M of power equipment deposits in Q3 — [Finviz](https://finviz.com/news/407031/liberty-energy-misses-on-earnings-as-frac-margins-slip-but-a-12-gw-ai-power-deal-reshapes-the-story)
- Vantage Data Centers partnership (Jan 2026): up to 1 GW over five years, including a 400 MW reservation of 2027 power † — [Business Wire](https://www.businesswire.com/news/home/20260104200386/en/Vantage-Data-Centers-and-Liberty-Energy-Announce-Strategic-Partnership-to-Develop-and-Operate-One-Gigawatt-of-Power-Solutions-for-Next-Generation-Data-Centers)
- Liberty's company-wide trailing return on capital employed was 2% and it posted a GAAP net loss of $39.1M in Q3; power returns are not disclosed — [Finviz](https://finviz.com/news/407031/liberty-energy-misses-on-earnings-as-frac-margins-slip-but-a-12-gw-ai-power-deal-reshapes-the-story)

ProPetro (PROPWR)
- About 510 MW under contract, including about 230 MW for Targa (midstream). A hyperscaler project is live in the US Midwest. About 2.6 GW of generation capacity secured, over 1 GW of it Caterpillar 10 MW units. Target 250–275 MW deployed by end-2026 — [ProPetro 8-K](https://www.sec.gov/Archives/edgar/data/0001680247/000168024726000122/exhibit991-earningsrelea.htm)
- Capital cost $1.4–1.5M per MW including balance of plant. 2026 PROPWR capex $400–430M. Financed partly by Caterpillar Financial ($172M borrowed at 30 Sep 2026). Q3 segment revenue $22.3M, adjusted EBITDA $7.6M — [ProPetro 8-K](https://www.sec.gov/Archives/edgar/data/0001680247/000168024726000122/exhibit991-earningsrelea.htm)
- Management targets payback of four to six years (nearer four for oilfield and midstream). It stopped quoting its earlier $275,000–400,000 per MW annual cash profit figure † — [MarketBeat transcript summary](https://www.marketbeat.com/instant-alerts/transcript-propetro-q3-earnings-call-highlights-2026-10-29/)

VoltaGrid (private)
- Oracle deal (Oct 2025): 2,300 MW of modular gas power for Oracle AI data centers, gas supplied by Energy Transfer; terms undisclosed — [DCD](https://www.datacenterdynamics.com/en/news/voltagrid-to-supply-oracle-with-23gw-of-natural-gas-power-for-ai-data-centers/)
- Financing (Nov 2025): $5.0B package: $2.0B senior secured second-lien notes due 2030 plus a $3.0B asset-based revolver. Deployment plan of 4.3+ GW, fully contracted, through 2028 † — [Simpson Thacher](https://www.stblaw.com/about-us/news/view/2025/11/10/simpson-thacher-advises-on-$5-billion-debt-refinancing-by-voltagrid); [Energynews](https://energynews.pro/en/voltagrid-raises-5-0bn-to-deploy-4-3-gw-of-capacity-by-2028)
- Equity (May 2026): $1B from Blackstone Tactical Opportunities and Halliburton ($775M primary, $225M secondary), later closed at $1.575B total †. VoltaGrid also agreed to buy Propell, a key equipment supplier — [Kirkland & Ellis](https://kirkland.com/news/press-release/2026/05/kirkland-advises-voltagrid-on-investment-from-blackstone-and-halliburton-to-fund-pt); [Citybiz](https://www.citybiz.co/?p=913699)
- Bloomberg (24 Feb 2026): Oracle pays VoltaGrid more than $1B a year to serve one OpenAI site in Texas. Fitch expects EBITDA of $1.1B by 2028, more than five times 2024. A sale or IPO could value it above $10B. The company is about six years old — [Energy Connects / Bloomberg](https://www.energyconnects.com/news/gas-lng/2026/february/voltagrid-weighing-public-listing-or-sale-riding-the-ai-wave)

Williams (Power Innovation)
- Socrates (Meta, New Albany, Ohio): two 200 MW behind-the-meter gas plants, described as a 10-year agreement, nearing completion in mid-2026. Socrates South uses a mix of Solar Turbines units, Siemens SGT-400s and 15 Caterpillar G3520 engines, about 275–285 MW nameplate for 200 MW net. The source is an AI-maintained page citing Ohio Power Siting Board filings; verify — [Watkins research page](https://www.jaredwatkins.com/research/datacenters/behind-meter-power/williams-companies-btm/); [Williams Q1 recap](https://www.williams.com/2026/05/05/q1-earnings-recap-data-centers-accelerate-new-growth-paths-for-williams/)
- NEO, Williams' fifth Power Innovation project: 682 MW, in service H2 2028 — [Williams Q1 recap](https://www.williams.com/2026/05/05/q1-earnings-recap-data-centers-accelerate-new-growth-paths-for-williams/)
- Blackstone reportedly paid $5.34B for 49% of five Williams power projects (15 Jul 2026), with Williams able to buy it out in years 7–14. Williams has about $5.1B committed and cites a 6 GW backlog by the early 2030s. Low-confidence source; verify against Williams filings — [Watkins research page](https://www.jaredwatkins.com/research/datacenters/behind-meter-power/williams-companies-btm/); [Industrial Info](https://www.industrialinfo.com/news/article/williams-grows-legacy-pipeline-business-and-new-power-initiative--353304) †

Others
- Energy Vault (10 Aug 2026): 1.25 GW integrated off-grid power for a hyperscaler campus in Texas: grid-forming power conversion, batteries, control software and Caterpillar gensets via an EPC partner. Expected revenue $500–600M across H2 2026 and 2027. Deployment starts in 4–12 months — [Power Technology](https://www.power-technology.com/news/energy-vault-to-supply-power-platform/)
- Crusoe (founded 2018): Abilene campus heading to about 2.1 GW under a 15-year Oracle/OpenAI lease, with $9.6B of JPMorgan debt; 900 MW Microsoft campus; revenue $276M in 2024 (estimate), about $500M projected for 2025 and about $2B for 2026; valued at $30.9B in 2026 — [Sacra](https://sacra.com/c/crusoe/)
- ERCOT co-location: AWS at Comanche Peak, 1,200 MW under a 20-year PPA with Vistra, full capacity by 2032; CyrusOne/Constellation Freestone, 380 MW contracted; reported ERCOT co-location totals about 2,885 MW — [SemiAnalysis](https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw)
- A backup genset fleet costs about $1M/MW; some AI builds (Cipher, Fluidstack) are skipping gensets — [SemiAnalysis](https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw)

### Inferences
- Solaris implied economics (derived, rough): $16B backlog ÷ 11 years ÷ 3.2 GW is about $455,000 of revenue per MW-year, or about $38,000 per MW-month, or about $52/MWh at full output, excluding fuel. Power Solutions segment margin in Q3 was about 45% ($127.0M ÷ $284.2M). The $1.6B "run-rate EBITDA potential" exceeds backlog revenue per year on this arithmetic, so it must include uncontracted capacity, services or the logistics segment. Treat my per-MW figure as an order of magnitude.
- ProPetro's numbers close the loop: $1.4–1.5M/MW capex against a four-to-six-year payback implies roughly $250,000–375,000 of cash margin per MW-year, consistent with the range it used to quote.
- The business is a spread between equipment allocation plus cheap-enough capital on one side and a 10–15 year investment-grade contract on the other. Winners so far were oilfield-service firms that already had fleets, OEM relationships (Caterpillar, Jenbacher) and field crews. A $5–50M entrant cannot own the assets: $50M buys about 35 MW.
- Contract protections are strong (50% termination payment, $300M prepayment), which is why BB-rated notes and Blackstone equity are available. Customer concentration is the main risk: Solaris caps at 35% per customer; VoltaGrid's largest site alone is over $1B a year.
- Only about 2 GW is operating. Permitting (air permits, pipelines) is now a visible failure point, as in New Mexico.

### Gaps
- Energy Transfer, Atlas Energy Solutions and Caterpillar direct deals: not researched (search budget).
- No public $/MWh or $/MW-month price was found for any named contract. All per-MW figures above are derived or management targets.
- VoltaGrid revenue, EBITDA and note coupon: offering documents are private; only the Fitch projection was found.
- Solaris fleet by year, capex per MW and Stateline JV split are in the 10-Q but were behind a sign-in on the page fetched.
- Williams build multiples and capex per project: not found in the pages opened.

## 4. Transformers, switchgear, breakers, HV cable and electrical steel

### Takeaway
Large transformers take 2.5 to 4 years and cost about 80% more than in 2020; high-voltage breakers take about 125 weeks. Incumbents are earning record margins (Eaton Electrical Americas 29.8%, HD Hyundai Electric about 25%) and have committed roughly $2B to new North American plants that open in 2027–2028. Some suppliers argue the shortage is a procurement problem for standard units.

### Cited Findings

Lead times and prices
- Wood Mackenzie Q2 2025 survey: power transformers 128 weeks, generator step-up units 144 weeks, switchgear 44 weeks. Prices since 2019: power transformers +77%, GSUs +45%, some distribution classes up to +95%. Since 2021: circuit breakers +47%, medium-voltage switchgear +50% — [POWER, 2 Jan 2026](https://powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/)
- 2025 supply deficits: about 30% for power transformers and about 10% for distribution transformers. Demand since 2019: GSUs +274%, substation power transformers +116% — [POWER](https://powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/)
- May 2026: lead times up to four years for high-capacity units (PwC); prices up about 80% in five years — [pv magazine USA, 11 May 2026](https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/)
- GSU lead times passed 160 weeks by Q1 2026, from 143 weeks in 2024 † — [Cybernews / Reuters](https://cybernews.com/tech/data-center-power-utilities-grid-equipment/)
- Switchgear, June 2026 contractor data (Terrapin): 15 kV class 52–80 weeks; 38 kV class 78–104 weeks; about 24 weeks before the pandemic. High-voltage circuit breakers about 125 weeks. Data-center-spec medium-voltage gear approaching two to three years at the busiest makers † (trade-blog source) — [Industrial Sage](https://www.industrialsage.com/switchgear-lead-times-2026/)
- Dissent: a transformer broker (Bolt Electrical) says standard substation transformers can be delivered 12–14 months after drawing approval at a 12–15% markup on factory cost, and that the bottleneck is utility vendor qualification and specs. POWER notes this is hard to validate and does not apply to customized large units — [POWER](https://powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/)

Incumbent backlogs and margins
- GE Vernova Electrification: equipment backlog $42.2B (+60% year over year, including $5B from Prolec GE); Q3 2026 revenue $3.9B; segment EBITDA margin 19.1% (+400 bps). Buying Trench (bushings, instrument transformers) for $9B, closing late 2027, with about $5B of backlog and frameworks reaching into the next decade — [GE Vernova 8-K](https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000162/gevpressrelease3q26.htm); [Utility Dive](https://www.utilitydive.com/news/ge-vernova-in-9b-deal-to-buy-high-voltage-manufacturer-as-gas-turbine-orde/873223/)
- Eaton Q3 2026: Electrical Americas sales $4.2B (+22% organic), operating margin 29.8%, trailing-12-month orders +39%, backlog +33%. Electrical Global backlog +121%. Acquisitions: Boyd Thermal $9.55B, Fibrebond $1.43B, Resilient Power (solid-state transformers) $86M, pending COL Group €810M — [Eaton 8-K](https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000037/etn09302026exhibit99.htm)
- Eaton data-center revenue +65% and trailing-12-month data-center orders up more than 100% † — [TradingKey](https://www.tradingkey.com/news/transcripts/262269681-)
- Hitachi Energy: backlog $47.6B (later stated as over $50B) with about six years of visibility. Investing $6B+ over 2024–2027. Targets $30B revenue by 2030. Fiscal 2024 adjusted operating margin about 10.8% (derived) — [Toyo Keizai, 16 Mar 2026](https://toyokeizai.net/articles/-/937543)
- Siemens Energy: its North Carolina transformer and switchgear hub is sold out for its first two years of operation. Grid Technologies orders €24.0B in FY2026 (+14.5%) — [Utility Dive](https://www.utilitydive.com/news/elevated-demand-for-gas-turbines-could-persist-through-2035-siemens-energy/874839/); [Turbomachinery](https://www.turbomachinerymag.com/view/siemens-energy-fy2026-record-backlog-164-billion-gas-services-orders)
- Korea, Q3 2026: HD Hyundai Electric revenue ₩1.18T, operating profit ₩284.5B (about 24%); second Alabama plant raises extra-high-voltage transformer capacity about 50% (up to 765 kV). LS Electric revenue ₩1.88T (+54%), switchgear revenue +120%, North America about ₩500B in the quarter. Hyosung is spending $300M on its Memphis plant and formed a breaker JV with Quanta — [Korea Times, 28 Oct 2026](https://www.koreatimes.co.kr/business/tech-science/20261028/power-equipment-makers-race-to-expand-us-capacity-amid-ai-boom)
- Hyosung Heavy backlog about ₩11.9T at end-2025 (+34%); heavy-industry division margin 20.2% in Q4 2025 † — [FN News](https://en.fnnews.com/news/202603031605380931)

Capacity additions (North America)
- Nearly $2B committed since 2023: Hitachi Energy over $1B (South Boston, Virginia, $457M, largest US large-transformer plant by 2028); Siemens Energy Charlotte ($150M, production early 2027; another report says $421M); Eaton South Carolina $340M (2027); Prolec GE $300M+; Virginia Transformer $40M; ERMCO $70M+; Central Moloney $50M — [POWER](https://powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/); [pv magazine USA](https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/)

Grain-oriented electrical steel (GOES)
- Cleveland-Cliffs' Butler Works is the only US source. It is spending $200M to raise GOES output by up to 25% † — [GMK Center, 7 Oct 2026](https://gmk.center/en/news/cleveland-cliffs-is-investing-200-million-in-the-expansion-of-the-butler-works-plant-in-the-us/)
- The Defense Logistics Agency awarded Cliffs a sole-source contract worth up to $400M for up to 53,000 net tons (1 Jul 2026) † — [SMM](https://news.metal.com/newscontent/103999355-cleveland-cliffs-confirms-400-million-pentagon-contract-for-electrical-steel)
- Breakthrough Institute (advocacy) says Cliffs' GOES loses up to 39% more energy than Nippon or JFE grades in distribution cores † — [Breakthrough Institute](https://thebreakthrough.org/issues/energy/america-makes-the-wrong-steel-for-its-transformer-supply-chain)

New entrants
- FluxCo raised $26M (July 2026) for a software platform that sources transformers; it is not a manufacturer † — [Dealroom](https://app.dealroom.co/news/note/fluxco-raises-26m-for-ai-platform-to-source-electrical-transformers)
- Solid-state transformer startups are covered in section 6.

### Inferences
- Incumbent margins of 20–30% and six-year backlogs show pricing power, but the new plants land in 2027–2028, the same window a startup founded now would reach production.
- The broker's claim and the 44-week survey average against 2–3 years for data-center-spec gear suggest the acute shortage is in customized, high-voltage and data-center-spec equipment and in qualification, not in every transformer.
- The asset-light entrants (FluxCo, brokers at 12–15% markup) monetize qualification and sourcing friction with little capital.

### Gaps
- HV cable lead times and prices: not researched.
- Schneider Electric and ABB backlog figures: not retrieved.
- Current GOES price and import share: not found.
- No 2026 funding round for a new conventional large-transformer manufacturer was found.

## 5. Battery storage: costs, tariffs, FEOC, datacenter use, and whether flexibility speeds interconnection

### Takeaway
A US four-hour battery project costs about $309/kWh installed, and compliant US-made systems cost about $100/kWh more than Chinese supply. Tesla earns 33% gross margin on storage while Fluence earned 2.8% and lost money on delivery penalties. Batteries are now sold into data centers as part of off-grid power plants. Evidence that flexibility buys faster interconnection is real but small: pilots and MW-scale programs, no quantified GW-scale contract found.

### Cited Findings

Costs and policy
- Modo Energy (Nov 2026): median US four-hour project capex $309/kWh. Battery system $215/kWh US-made versus $115/kWh Chinese-supplied before tariffs. FEOC "material assistance" threshold for non-FEOC content: 55% for 2026 construction starts, 60% in 2027, rising to 75% by 2030. ITC worth 30% (up to 50% with adders) for projects starting construction through 2033 — [Modo Energy](https://modoenergy.com/research/feoc-rules-bess-tax-credit-non-feoc-battery-supply)
- Non-FEOC North American cell capacity announced: 100 GWh by end-2027 (up to 135 GWh), against 20 GWh at end-2025. Forecast new BESS in the seven US ISOs: 58 GWh in 2027 and 90 GWh in 2028 — [Modo Energy](https://modoenergy.com/research/feoc-rules-bess-tax-credit-non-feoc-battery-supply)
- US four-hour turnkey systems using 45X-credited batteries are still 31% dearer than systems with imported Chinese batteries (BNEF via ING) † — [ING](https://think.ing.com/articles/us-battery-storage-needs-innovation-for-long-term-growth/)
- Lazard's latest LCOE+ shows US utility-scale levelized storage cost rising, reversing earlier declines, after restrictions on Chinese cells † — [Energy-Storage.news](https://www.energy-storage.news/lazard-us-utility-scale-energy-storage-lcos-has-increased-since-restrictions-on-chinese-cells-came-into-force/)
- E3 levelized fixed cost for four-hour storage: $337/kW-yr without tax credits, $216/kW-yr with — [E3 RECOST, Jan 2026](https://www.ethree.com/recost-q1-2026-update/)

Tesla and Fluence
- Tesla Q3 2026: 13.7 GWh deployed (12.5 GWh a year earlier); 36 GWh in the first nine months. Energy revenue $2,881M, down 16%, partly from tariff-related customer refunds. Energy gross margin 33.1% † — [Energy-Storage.news](https://www.energy-storage.news/tesla-q3-2026-energy-storage-revenues-fall-despite-second-highest-quarterly-deployments/)
- Tesla reported its highest-ever storage order rate and backlog. Texas Megafactory (50 GWh planned) started production; Nevada LFP cells began shipping — [The EV Report](https://theevreport.com/tesla-q3-2026-results-energy-storage-semi)
- Tesla says 2027 Megapack capacity is nearly sold out amid data-center demand; combined nameplate about 110 GWh † — [Stocktwits](https://stocktwits.com/news-articles/markets/equity/tesla-ramping-megapack-production-as-much-as-possible-after-2027-capacity-nearly-sold-out-amid-data-center-demand/cZxUx9eRBDZ)
- Fluence FY2026 (to 30 Sep 2026): revenue $2.33B (flat); GAAP gross margin 2.8% (13.1% prior year); Q4 gross margin −5.0%; adjusted EBITDA −$202.8M. Cause: liquidated damages from project delays tied to a contract manufacturer's ramp, plus new-product cost overruns. Backlog $8.9B (from $5.3B); order intake over $6.2B, $3.5B of it in Q4 — [Fluence 8-K](https://www.sec.gov/Archives/edgar/data/0001868941/000186894126000056/flncq4andfullfy26earningsp.htm)
- Fluence had secured about $850M of data-center business through July 2026, including its first large behind-the-meter order and about $550M from a hyperscaler † — [Fluence Q3 FY26 8-K](https://www.sec.gov/Archives/edgar/data/0001868941/000186894126000028/flncq3fy26earningspressrel.htm)

Data-center use of batteries
- Energy Vault's 1.25 GW Texas hyperscaler project pairs batteries and grid-forming inverters with gensets to run off-grid and absorb AI load swings; $500–600M revenue — [Power Technology](https://www.power-technology.com/news/energy-vault-to-supply-power-platform/)
- CyrusOne and Eolian are building a 200 MW data center at an existing grid battery site in Fort Worth, with the battery supplying early phases † — [Energy-Storage.news](https://www.energy-storage.news/eolian-and-cyrusone-team-up-to-deploy-texas-data-centre-at-site-of-100mw-bess/)
- Google will buy all output from a 1.6 GW solar plus 1.9 GWh storage project in Arkansas, delivered through Entergy † — [Benchmark](https://source.benchmarkminerals.com/article/google-to-purchase-all-power-from-largest-under-construction-bess-project-in-us)
- In the 800 VDC roadmap, battery racks are about $200,000 per MW of content and replace power racks in the 2028–2029 phase — [SemiAnalysis, 26 May 2026](https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part)

Does flexibility speed interconnection?
- LBNL (July 2026): PG&E and Portland General Electric have programs that let customers connect before full upgrades are complete, using flexibility to bridge the gap; "these programs have started with MW-scale loads." Idaho Power requires some large customers to accept remote disconnection for up to 10 hours per event and 225 hours per year. Google has explored compute flexibility with utilities in Tennessee, Indiana, Michigan and Nebraska — [LBNL](https://eta-publications.lbl.gov/sites/default/files/2026-07/integrading_ai_data_centers_with_the_power_grid.pdf)
- Utility Dive (26 Jun 2026): PGE wants interconnection agreements that guarantee "visibility" and "dispatchability" in exchange for accelerated interconnection, and says bill credits are too small to move workloads. Silicon Valley Power calls 100% control of the load-side breaker "non-negotiable." The article reports no executed deal with quantified MW or time saved — [Utility Dive](https://www.utilitydive.com/news/data-centers-flexibility-utilities-speed-to-power/822588/)
- Demonstrations: Emerald AI cut an AI workload 25% for three hours at Salt River Project; EPRI demonstrations reached up to 40% flexibility; Boston University modeling gives 18–55% — [Utility Dive](https://www.utilitydive.com/news/data-centers-flexibility-utilities-speed-to-power/822588/)
- Duke (2026): a 1–2% cut in data-center peak demand could lower rates 0.5–2.8% — [Utility Dive](https://www.utilitydive.com/news/data-centers-flexibility-utilities-speed-to-power/822588/)
- Texas SB 6 requires large loads to share load-shed obligations; PJM is filing a "connect and manage" framework; Pennsylvania's model tariff gives lower charges for onsite generation or interruptible service — [NC Clean Energy Technology Center](https://nccleantech.ncsu.edu/?p=13984); [Utility Dive](https://www.utilitydive.com/news/pjm-capacity-auction-price-cap-reserve-shortfall-grows/825282/)

### Inferences
- The storage hardware business is brutal for anyone but the scale leader: same market, 33% margin at Tesla and about 3% at Fluence. Delivery penalties, not demand, sank Fluence's year.
- The $100/kWh domestic premium plus FEOC thresholds make compliant cell supply (about 100 GWh by end-2027 against 58–90 GWh/yr of demand) a temporary pinch that eases in 2028.
- Flexibility-for-speed is moving from idea to rule (SB 6, PJM connect-and-manage, PGE and PG&E programs), but utilities want hard control of the breaker, not software promises. Batteries or onsite generation that make curtailment invisible to the workload are what the data-center side will pay for.

### Gaps
- No BNEF 2026 turnkey $/kWh figure was retrieved directly.
- Current tariff rates on Chinese cells (Section 301, AD/CVD): not retrieved.
- The Indiana Michigan Power/Google special contract and other named Google demand-response terms: listed in a Brattle/ESIG deck but terms not retrieved — [ESIG deck](https://www.esig.energy/attachment/serve/lam_4i_june2026)
- No evidence found of a GW-scale load energized earlier because of a flexibility commitment, with dates.

## 6. Solid-state transformers and 800 V DC datacenter architecture

### Takeaway
800 VDC is real and dated: sidecar power racks ship in 2026–2027 and Kyber-class racks make 800 VDC mandatory in 2027–2028. Solid-state transformers are the last phase; no vendor had UL certification for a data-center unit as of May 2026 and scale adoption is not expected before 2029. Startups have raised over $320M but disclose megawatts of shipments, not gigawatts.

### Cited Findings

Nvidia roadmap (SemiAnalysis, 26 May 2026; free portion)
- Phase 1 (2026–2027): 800 VDC power-rack sidecars at row level, AC backbone kept. Phase 2 (2027–2028): Kyber-style racks take 800 VDC directly, no AC fallback. Phase 3 (late 2028–2029): centralized rectifiers, battery racks. Phase 4 (after 2029): solid-state transformers convert medium voltage straight to 800 VDC — [SemiAnalysis](https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part)
- Nvidia's 800 V reference design is rated 660 kW per rack. Vera Rubin NVL72 (late 2026–2027) tops out near 180–220 kW and can still run on AC — [SemiAnalysis](https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part)
- Nvidia's own wording is a transition "starting in 2027," with an MGX-compatible 800 VDC power rack in H2 2026 † — [Nvidia blog](https://blogs.nvidia.com/blog/800-vdc-power-architecture/)
- Content values: sidecar power rack $400–500k per unit (about $40k for a standard AC power rack), about $0.5M/MW; SST about $1.0–1.5M/MW, replacing about $0.75M/MW of low-voltage gear and rectifiers. Total electrical content stays within $3.6–4.8M/MW across architectures. Incremental 800 VDC capacity about 39 GW by 2030 — [SemiAnalysis](https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part)
- End-to-end efficiency: about 82.0% for the AC baseline versus 87.4% with SSTs; about 69 MW saved per GW of IT load — [SemiAnalysis](https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part)
- No major SST adoption expected before early 2029. As of May 2026 no vendor had UL certification for a data-center SST. More than $320M went into SST startups in the 12 months to March 2026 — [SemiAnalysis](https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part)
- Standards: Nvidia, Google and Microsoft published an OCP white paper in March 2026 and an LVDC solid-state transformer specification v0.3 in July 2026 † — [SemiAnalysis](https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part)

Startups
- Heron Power (founded 2025 by ex-Tesla executive Drew Baglino): $140M Series B (18 Feb 2026) led by a16z American Dynamism and Breakthrough Energy Ventures, after a $38M Series A. Plans a 40 GW/yr US factory, full-scale production in H2 2027, "hundreds of megawatts" produced by end-2027. Claims about 50 GW of demand from a dozen-plus prospective customers in technical collaboration (the company's release says "early interest" of over 40 GW). Named customers: Intersect Power and Crusoe. Claims price parity with current solutions — [Canary Media](https://www.canarymedia.com/articles/climatetech-finance/heron-power-raises-140m-electrical-transformers); [TechCrunch](https://techcrunch.com/2026/02/18/heron-power-raises-140m-to-ramp-production-of-grid-altering-tech/) †
- DG Matrix (Raleigh): $60M Series A (Feb 2026) led by Engine Ventures with ABB, Mitsubishi Heavy Industries and Chevron. Shipping pre-certification units; targeted UL certification by end of Q2 2026; the only SST in Nvidia's MGX reference architecture; data centers are about 90% of its pipeline. Says its system costs 60–70% of the equipment it replaces — [TechCrunch](https://techcrunch.com/2026/02/20/why-investors-are-going-gaga-over-solid-state-transformers/); [SemiAnalysis](https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part)
- Amperesand (Singapore/US, spun out of NTU in 2023): $80M Series A (21 Nov 2025) co-led by Walden Catalyst and Temasek. Plans 30 MW of commercial shipments in 2026; first deployment at the Port of Singapore; unnamed hyperscaler pilots — [Converge Digest](https://convergedigest.com/amperesand-raises-80m-to-accelerate-medium-voltage-solid-state-transformers/)
- Incumbents: Eaton bought Resilient Power for $86M at close (reported as up to $150M); ABB backs DG Matrix and sells a solid-state breaker; Delta ships 110 kW power shelves and 800 VDC busway; China XD Electric reportedly deployed 2.4 MW data-center SSTs — [Eaton 8-K](https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000037/etn09302026exhibit99.htm); [SemiAnalysis](https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part)
- Earlier grid power-electronics startups failed: Gridco closed and Varentec faded — [Canary Media](https://www.canarymedia.com/articles/climatetech-finance/heron-power-raises-140m-electrical-transformers)

### Inferences
- The near-term money (2026–2028) is in sidecar power racks, DC busway, DC protection and battery racks, where Delta, ABB, Eaton, Vertiv and Schneider are already qualified. SSTs are a 2029+ market that startups are funding now.
- SSTs avoid grain-oriented steel but depend on silicon carbide devices and on certification. The disclosed 2026 shipment plans (30 MW at Amperesand, "pre-certification units" at DG Matrix) are tiny next to the 39 GW forecast.
- Heron's "50 GW of orders" should be read as interest until binding contracts are disclosed.

### Gaps
- No binding order values, delivery confirmations or UL certification news after May 2026 were found for any SST startup.
- Vertiv, Schneider and Eaton 800 VDC product shipment dates: not retrieved.
- Novos Power and Hyperscale Power funding: not found.

## 7. Nuclear, geothermal and SMRs: what delivers before 2030

### Takeaway
Almost nothing new delivers before 2030. Fervo's Cape Station is the only next-generation plant now operating (about 100 MW phase, first block online September 2026). The two reactor restarts add about 1.6 GW if they happen; Palisades hit a fuel-loading setback in August 2026. SMR dates are 2028 at the earliest and mostly 2030 or later.

### Cited Findings
- Fervo Cape Station (Utah): first power and grid sync on 24 Sep 2026; commercial operation declared 30 Sep 2026, one day before its contractual date. Phase I is about 100 MW in three 33 MW blocks; the other two blocks are due by 1 Jan 2027 † — [Energy Global](https://www.energyglobal.com/other-renewables/05102026/fervo-energy-declares-commercial-operation-at-cape-station-ahead-of-schedule/); [Fortune](https://fortune.com/2026/09/24/fervo-next-gen-geothermal-power-grid-ai-boom/)
- Fervo and Google signed a 396 MW PPA expected online in 2028 † — [Barchart](https://www.barchart.com/story/news/4373083/fervo-energy-and-google-sign-396-mw-ppa)
- Palisades (805 MW, Holtec): NRC returned it to operational status on 27 Aug 2025. On 30 Aug 2026 a fuel assembly bent during loading and refueling was halted; the NRC approved a license amendment to remove it on 14 Oct 2026. No restart date is given. $1.5B DOE loan; Wolverine Power takes up to two-thirds of output (Wikipedia; verify) — [Wikipedia](https://en.wikipedia.org/wiki/Palisades_Nuclear_Generating_Station)
- Crane Clean Energy Center (819 MW, Constellation): restart targeted for 2027; 20-year Microsoft contract; $1B DOE loan (Nov 2025); $1.6B restart cost (Wikipedia; verify) — [Wikipedia](https://en.wikipedia.org/wiki/Crane_Clean_Energy_Center)
- Kairos Power: Hermes 2 (50 MWe) broke ground April 2026 and is due to supply TVA and Google in 2030; Google's 500 MW deal runs to 2035 (Wikipedia; verify) — [Wikipedia](https://en.wikipedia.org/wiki/Kairos_Power)
- X-energy: NRC issued the Long Mott (Dow, Texas) construction permit on 10 Nov 2026 after an 18-month review; IPO in April 2026 raised over $1B; Amazon/Energy Northwest project expected mid-2030s (Wikipedia; verify) — [Wikipedia](https://en.wikipedia.org/wiki/X-energy)
- Oklo: aims for commercial operation of Aurora-INL by 2028; no NRC construction or operating license issued; a separate isotope test reactor reached criticality on 5 Aug 2026; "around 15 GW order book" consists of agreements and letters of intent (Wikipedia; verify) — [Wikipedia](https://en.wikipedia.org/wiki/Oklo_Inc.)
- Earthjustice count of proposed data-center power: 4 GW of geothermal by 2033 and 22 GW of nuclear by 2040 — [Earthjustice](https://earthjustice.org/document/the-ai-gas-rush-risks-and-implications-of-bring-your-own-power-executive-summary)
- AWS's 1,200 MW at Vistra's Comanche Peak is existing nuclear output under a 20-year PPA, reaching full capacity by 2032 — [SemiAnalysis](https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw)

### Inferences
- Before 2030 the firm-power answer is gas, engines, fuel cells and batteries. Nuclear and geothermal matter to a founder as post-2030 competition for long contracts, not as a near-term entry point at $5–50M.

### Gaps
- Nuclear facts rest on Wikipedia because the search budget ran out; primary NRC, Holtec and Constellation sources were not checked. Status of Palisades after October 2026 is unknown.
- Duane Arnold restart, TerraPower and uprates at existing plants: not researched.

## 8. Skilled labor constraints

### Takeaway
Electrical labor is a binding constraint on both data centers and onsite power. Electrical work is 45–70% of data-center construction cost, data-center projects need several times the local electrician base, and pay premiums of 30–42% are reported. Hard national wage-inflation data specific to electricians and linemen was not found.

### Cited Findings
- More than 300,000 new electricians needed over the next decade; about 20,000 retire each year; nearly 30% of union electricians are aged 50–70. Electrical work is 45–70% of data-center construction cost (IBEW). A single data center can need up to 1,500 workers at peak — [Fortune, 2 Mar 2026](https://fortune.com/2026/03/02/ai-data-centers-electrician-shortage-gen-z-training-careers)
- IBEW Local 26 (northern Virginia): apprentices start near $26/hour; journeymen earn about $59.50/hour, over $120,000 a year, approaching $200,000 with overtime or as foremen — [Fortune](https://fortune.com/2026/03/02/ai-data-centers-electrician-shortage-gen-z-training-careers)
- Apprenticeship applications rose from about 70,000 to 120,000 between 2022 and 2024 (NECA); apprenticeships take four to five years. Google pledged $15M to the electrical workforce pipeline — [Fortune](https://fortune.com/2026/03/02/ai-data-centers-electrician-shortage-gen-z-training-careers)
- Construction industry short roughly 439,000 workers as of Nov 2025, mostly skilled trades; data-center construction jobs pay up to 30% more; contractors on data-center work carry backlogs near a year (WSJ via ITIF) — [ITIF, 12 Jan 2026](https://itif.org/publications/2026/01/12/construction-industry-facing-worker-shortage-driven-by-growth-of-data-centers/)
- ABC estimates the industry needs about 349,000 net new workers in 2026 — [Fortune](https://fortune.com/2026/03/02/ai-data-centers-electrician-shortage-gen-z-training-careers)
- BLS projects about 81,000 electrician openings a year through 2034. Indeed data: data-center installation jobs pay about 42% more than comparable roles; construction wages rose 3.4% versus 2.4% for all US pay † — [Quartz](https://qz.com/ai-data-center-boom-electricians-skilled-trades)
- IBEW locals report single data-center projects needing two to four times their membership † — [IBEW](https://ibew.org/the-data-center-surge-a-new-generation-of-ibew-jobs/)
- The traveling-electrician pool is depleted: a 5,000-member Detroit local has fewer than 100 on its out-of-work list; a town with about 100 electricians may need about 500 for one project (vendor blog, illustrative) — [RIVET, 14 Nov 2026](https://www.rivet.work/blog/where-have-all-the-traveling-electricians-gone)
- Large projects typically employ 1,500–3,000 at peak, up to 4,000; over 60% of data-center providers report difficulty hiring qualified candidates — [BRG](https://www.thinkbrg.com/thinkset/the-data-center-labor-shortage-a-hidden-bottleneck-for-ai-infrastructure/)
- Amperesand claims its solid-state system halves installation labor; ProEnergy test-fits turbine packages at the factory to cut site commissioning time — [Converge Digest](https://convergedigest.com/amperesand-raises-80m-to-accelerate-medium-voltage-solid-state-transformers/); [Power Engineering](https://www.power-eng.com/gas/data-center-power-crunch-lifts-engines-aeroderivatives-into-larger-role/)
- Eaton paid $1.43B for Fibrebond, a maker of prefabricated power enclosures — [Eaton 8-K](https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000037/etn09302026exhibit99.htm)

### Inferences
- With a four-to-five-year apprenticeship, labor supply cannot respond before 2030. Products that move electrical work from site to factory (prefabricated skids, e-houses, pre-tested packages) substitute for the scarce input, and Eaton's Fibrebond price shows what that is worth.
- Higher wages reshuffle a fixed pool; they do not add workers in the relevant window.

### Gaps
- Lineman and commissioning-engineer shortage counts and wage series: none found.
- No official NECA/IBEW wage-scale time series was retrieved, so wage inflation is evidenced by premiums, not a clean rate.

## 9. Startups founded 2019–2025 in power or electrical equipment that reached $100M+ revenue quickly

### Takeaway
The only clear cases found sold contracted onsite power as a service, not equipment: VoltaGrid (about 2020) and the oilfield-service pivots (Solaris, Liberty, ProPetro). No equipment startup founded since 2019 was found with $100M+ of reported revenue; the best-funded ones have backlogs and factories in progress.

### Cited Findings
- VoltaGrid (about six years old in Feb 2026): Oracle pays it more than $1B a year for one site; Fitch projects $1.1B EBITDA by 2028, more than five times 2024, which implies 2024 EBITDA of roughly $200M (derived); $5B debt package and $1.575B equity; possible valuation above $10B — [Energy Connects / Bloomberg](https://www.energyconnects.com/news/gas-lng/2026/february/voltagrid-weighing-public-listing-or-sale-riding-the-ai-wave); [Citybiz](https://www.citybiz.co/?p=913699) †
- Solaris Power Solutions (entered power in 2024): segment revenue $284.2M in Q3 2026 alone; 3.2 GW contracted; $16B backlog † — [Finviz](https://finviz.com/news/417401/solaris-doubles-the-eps-consensus-and-raises-guidance-again-but-a-services-heavy-mix-thins-margins-and-the-stock-has-gone-nowhere)
- ProPetro PROPWR (new division): $22.3M revenue in Q3 2026 with 510 MW contracted; not yet at $100M — [ProPetro 8-K](https://www.sec.gov/Archives/edgar/data/0001680247/000168024726000122/exhibit991-earningsrelea.htm)
- Crusoe (founded 2018, just outside the window): revenue $276M in 2024, about $500M projected for 2025 and about $2B for 2026; it sells compute and data-center capacity and builds its own power — [Sacra](https://sacra.com/c/crusoe/)
- Energy Vault (founded 2017, outside the window): one hyperscaler power contract worth $500–600M of revenue over about 18 months — [Power Technology](https://www.power-technology.com/news/energy-vault-to-supply-power-platform/)
- Boom Supersonic's Superpower line: over $1.25B of claimed backlog from one order, no reported deliveries — [Boom](https://boomsupersonic.com/press-release/boom-supersonic-to-power-ai-data-centers)
- Fermi America (founded January 2025): no revenue through 31 Dec 2025, net loss $486.4M since inception, IPO'd at about $16B market value in October 2025, and has since reset its project timeline † — [Fortune](https://fortune.com/2025/10/10/rick-perry-ai-power-startup-fermi-ipo-zero-revenue/); [Converge Digest](https://convergedigest.com/fermi-america-resets-timeline-for-project-matador/)
- Heron Power (2025), DG Matrix and Amperesand (2023): $178M, $60M and $80M+ raised respectively; shipments in 2026 measured in tens of MW; no revenue disclosed — [Canary Media](https://www.canarymedia.com/articles/climatetech-finance/heron-power-raises-140m-electrical-transformers); [Converge Digest](https://convergedigest.com/amperesand-raises-80m-to-accelerate-medium-voltage-solid-state-transformers/)
- Fervo (founded 2017): first 33 MW block online Sept 2026; revenue not found — [Energy Global](https://www.energyglobal.com/other-renewables/05102026/fervo-energy-declares-commercial-operation-at-cape-station-ahead-of-schedule/)

### Inferences
- Fast revenue came from owning scarce, deliverable megawatts and renting them under long contracts, funded mostly by debt. That model needs billions; it rewards incumbents with fleets and OEM allocation.
- Equipment startups have taken two to four years from founding to first units even with $100M+ raised. None has yet shown $100M revenue.
- The asset-light precedents are small so far (FluxCo's $26M raise; brokers at 12–15% markup; Emerald AI pilots).

### Gaps
- Base Power (home batteries, Texas): revenue, funding and deployments not retrieved (search budget; Wikipedia page not found).
- No systematic screen of private-company revenue was possible; other candidates (for example Redwood's energy storage arm, Mainspring, Peak Energy, ON.energy) were not checked.
- VoltaGrid's actual revenue is not public.
