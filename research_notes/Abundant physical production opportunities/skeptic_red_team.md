# Skeptic / Red-Team Notes: Why "radically cheaper or faster physical products" startups usually fail, who succeeded, and what is buildable in 2026-27

_Research date: 24 Nov 2026. Method note: the shared web-search budget ran out roughly halfway through, so later evidence comes from direct fetches of known pages (Wikipedia company pages, trade press, one Rhodium PDF). Wikipedia figures are secondary and should be re-checked against filings before publication. "(derived)" marks my own arithmetic on cited figures. Anything I could not source is listed under Gaps, not asserted._

## 1. Failure post-mortems: what killed the companies that promised cheaper/faster physical production

### Takeaway
Across roughly 35 cases the dominant cause of death is scaling fixed cost (factories, vertical integration, headcount) ahead of proven, paying demand and ahead of a working process. Chinese-scale commoditization and certification delay are the second and third killers. Soft "orders" and reservations almost never saved anyone.

### Cited Findings

**Construction / housing**
- Katerra raised over $2 billion (incl. $865M from SoftBank), peaked at 8,000+ employees in 9 countries, and was recapitalized in early 2021 at $400M, down 90% from $4B, before filing in June 2021 — [Construction Physics (Brian Potter, ex-Katerra)](https://www.construction-physics.com/p/another-day-in-katerradise)
- Potter's primary diagnosis: Katerra scaled before it had a product customers wanted (no product-market fit). Products sat in design 3+ years before a first prototype; prefab designs repeatedly came back from estimating priced above site-built; ~$100M went into a CLT plant whose output was routinely value-engineered out of projects — [Construction Physics](https://www.construction-physics.com/p/another-day-in-katerradise)
- Katerra made 20+ acquisitions that never integrated; by 2019 it had "failed to complete roughly a dozen projects and could only name one that was delivered on time" — [The Real Deal, 2021](https://therealdeal.com/la/2021/10/06/youve-built-it-now-will-they-come-inside-construction-techs-struggle/); [Architect Magazine](https://www.architectmagazine.com/technology/katerras-2-billion-legacy_o)
- Immediate trigger: the Greensill collapse left a disputed $440M debt that reportedly blocked Katerra's construction bonding — [Construction Physics](https://www.construction-physics.com/p/another-day-in-katerradise)
- Veev raised $600M at a >$1B valuation in 2022, announced shutdown in 2023 when a round fell through as rates rose; assets went to Lennar in 2024. Entekra (LP invested $45M) closed 2023; Blu Homes (>$100M) failed 2016 — [OneBuild, "The Prefab and Modular Graveyard"](https://onebuild.substack.com/p/the-prefab-and-modular-graveyard)
- Recurring modular causes per the same analysis: factories need ~70-80% utilization while housing demand is cyclical; a factory serves only a ~200-300 mile radius so expansion multiplies fixed cost; robotics added before designs were stable; trades, developers and lenders resisted process change — [OneBuild](https://onebuild.substack.com/p/the-prefab-and-modular-graveyard)
- Boxabl listed via SPAC on Nasdaq (BXBL) on 20 July 2026 at a reported $3.5B valuation — [The Real Deal, July 2026](https://therealdeal.com/national/2026/07/21/boxabl-ignites-spac-market-goes-public-at-3-5b-valuation/)
- Boxabl Q3 2026: revenue $578K (nine months: $2.6M); gross loss $3.9M in the quarter; 9 units delivered in Q3 and 36 in nine months; 54 produced in nine months; cash $14.0M (from $29.0M at end-2025); backlog 679 Casitas / $45.0M; "substantial doubt" going-concern language — [Panabee summary of the 10-Q](https://www.panabee.com/news/boxabl-earnings-q3-2026) (AI-generated summary of the filing; verify against the 10-Q)
- View (smart glass): ~$700M raised by 2017 plus $1.1B from SoftBank Vision Fund in 2018; warned of going-concern risk in 2022; Chapter 11 in 2024 with ~$350M debt, taken over by lenders — [Wikipedia: View, Inc.](https://en.wikipedia.org/wiki/View,_Inc.)

**EV and vehicle startups (SPAC cohort)**
- Nikola: valued ~$30B at peak per one account, ~$13B in Aug 2020 per another; 2022 revenue $50.8M against a $784M net loss; 209 Tre BEVs delivered by end-2023, all recalled; Chapter 11 on 19 Feb 2025; founder convicted of fraud (pardoned March 2025) — [Barchart](https://www.barchart.com/story/news/31083125/nikola-just-filed-for-bankruptcy-which-ev-stock-will-be-next); [Wikipedia: Nikola](https://en.wikipedia.org/wiki/Nikola_Corporation)
- Fisker: $2.9B SPAC (2020); asset-light contract manufacturing did not save it; 2023 net loss >$463M; Chapter 11 on 17 June 2024; remaining Oceans liquidated for $46.25M, about $14,000 each — [Wikipedia: Fisker Inc.](https://en.wikipedia.org/wiki/Fisker_Inc.)
- Lordstown: $1.6B SPAC equity value (Oct 2020); Hindenburg showed its "pre-orders" were non-binding, no-deposit expressions of interest; said in Aug 2022 it needed more capital just to build 500 trucks; Chapter 11 on 27 June 2023; assets sold for $10M — [Wikipedia: Lordstown Motors](https://en.wikipedia.org/wiki/Lordstown_Motors)
- Arrival ("microfactories"): worth $15B at peak, $250M by Jan 2023; held a UPS order for 10,000 vans (+10,000 option); UK arm in administration Feb 2024; assets bought by Canoo — [Wikipedia: Arrival](https://en.wikipedia.org/wiki/Arrival_(company))
- Canoo: $2.4B SPAC; announced orders from Walmart (4,500), Kingbee (9,300 "binding"), Zeeba (5,450); delivered 22 vehicles in 2023 on $886K revenue; Chapter 7 on 17 Jan 2025 with under $50K of assets — [Wikipedia: Canoo](https://en.wikipedia.org/wiki/Canoo)
- Proterra: delivered 199 transit buses in 2022; Chapter 11 on 7 Aug 2023; cited causes include each transit agency demanding heavy customization, supply-chain penalties and inflation eroding margins over 12-18 month delivery cycles; battery unit sold to Volvo for $210M — [Wikipedia: Proterra](https://en.wikipedia.org/wiki/Proterra_(bus_manufacturer))
- Local Motors (3D-printed cars, microfactories; founded 2007) closed 14 Jan 2022 — [Wikipedia: Local Motors](https://en.wikipedia.org/wiki/Local_Motors)

**Batteries, solar, energy hardware**
- Northvolt raised more than $14B (the commonly quoted ~$15B was not confirmed in my sources), held $55B of customer contracts, lost a €2B BMW order over quality in June 2024, and filed Chapter 11 in Nov 2024 with $5.8B debt and $30M cash (about one week of operations); Swedish bankruptcy 12 March 2025 — [TechCrunch](https://techcrunch.com/2025/03/12/battery-manufacturer-northvolt-nears-the-end-as-it-files-for-bankruptcy-in-sweden); [BNN Bloomberg](https://www.bnnbloomberg.ca/business/company-news/2024/11/29/how-europes-ev-battery-pioneer-northvolt-came-unstuck/); [Wikipedia: Northvolt](https://en.wikipedia.org/wiki/Northvolt)
- Northvolt causes: could not raise yield at Skellefteå; high faulty-cell rate; problems with imported Chinese machinery; expanded into Germany, Canada, Poland and new chemistries before fixing the core plant. Chinese LFP cells were priced near half the $95/kWh global average — [BNN Bloomberg](https://www.bnnbloomberg.ca/business/company-news/2024/11/29/how-europes-ev-battery-pioneer-northvolt-came-unstuck/); [Project Blue](https://projectblue.com/blue/news-analysis/1076/northvolt-bankruptcy-demonstrates-technical-and-geopolitical-challenges-of-core-battery-manufacturing--)
- Britishvolt: planned £2.6-3.8B gigafactory; "still years from generating revenue"; administration 17 Jan 2023 owing up to £160M; sold for £8.6M; the site later sold for £110M for a data-centre campus — [Wikipedia: Britishvolt](https://en.wikipedia.org/wiki/Britishvolt)
- Solyndra: $535M DOE guarantee; polysilicon prices fell ~89% between 2009 and mid-2011, making its CIGS design uncompetitive against Chinese crystalline silicon; Chapter 11 on 1 Sept 2011; loan programme booked a $528M loss — [Wikipedia: Solyndra](https://en.wikipedia.org/wiki/Solyndra)

**Aerospace / eVTOL / launch**
- Lilium: $2.4B SPAC valuation (2021); ~€1.359B accumulated losses by March 2024; never delivered a certified aircraft; self-administration Oct 2024 after a €50M state guarantee was refused, final insolvency Feb 2025 — [Wikipedia: Lilium](https://en.wikipedia.org/wiki/Lilium_GmbH); [AIN](https://ainonline.com/aviation-news/futureflight/2025-02-21/lilium-closes-evtol-business-new-investment-falls-through)
- Volocopter: filed for insolvency in late Dec 2024; missed its showcase at the 2024 Paris Olympics because engine certification was not obtained — [Wikipedia: Volocopter](https://en.wikipedia.org/wiki/Volocopter); [Fortune](https://fortune.com/europe/2024/12/31/german-flying-taxi-volocopter-insolvency/)
- Virgin Orbit: $3.7B SPAC valuation, but the SPAC raised only $228M of an expected $483M; six flights, four successes; Chapter 11 on 4 April 2023; assets fetched $36M — [Wikipedia: Virgin Orbit](https://en.wikipedia.org/wiki/Virgin_Orbit)
- Astra: $2.1B SPAC enterprise value (2021); taken private in 2024 at an $11.25M valuation — [Wikipedia: Astra](https://en.wikipedia.org/wiki/Astra_(American_spaceflight_company))
- Relativity Space: $1.335B raised, $4.2B valuation (2021); Terran 1 flew once and failed to reach orbit, then was retired; the company moved away from 3D printing for tanks and other major structures on Terran R; Eric Schmidt took control in March 2025 — [Wikipedia: Relativity Space](https://en.wikipedia.org/wiki/Relativity_Space)

**Digital / additive manufacturing**
- Desktop Metal: ~$437M of venture capital; $2.5B SPAC valuation (2020), peak near $6B; 2023 revenue $190M; acquired by Nano Dimension for $179.3M in April 2025, then filed Chapter 11 on 28 July 2025 — [Wikipedia: Desktop Metal](https://en.wikipedia.org/wiki/Desktop_Metal); [3DPrint.com](https://3dprint.com/319669/desktop-metal-bankruptcy-analysis-karma-police); [ElevenFlo](https://elevenflo.com/blog/desktop-metal-bankruptcy)
- Fast Radius went public by SPAC in 2022 and was insolvent, with its stock down over 95%, within the same year — [Wikipedia: Fast Radius](https://en.wikipedia.org/wiki/Fast_Radius)

**Consumer hardware and "cheap version" bets**
- Tata Nano: launched at ₹100,000 (~$2,000-2,500) with a 250,000/yr plan; sales peaked at 74,527 (FY2011-12), fell to 7,591 (FY2016-17); one unit built in June 2018. Cited causes: "poor man's car" stigma, fires, quality perception, plant relocation delay; loss-making throughout — [Wikipedia: Tata Nano](https://en.wikipedia.org/wiki/Tata_Nano)
- Segway sold only ~140,000 units over its lifetime at a ~$5,000 launch price; production ended 2020 — [Wikipedia: Segway](https://en.wikipedia.org/wiki/Segway)
- Juicero: ~$120M raised; $699 press cut to $399; shut Sept 2017; teardown blamed absent cost discipline — [Wikipedia: Juicero](https://en.wikipedia.org/wiki/Juicero)
- SmileDirectClub: $3.2B private valuation (2018), $750M revenue (2019); orthodontists filed complaints with 36 state dental boards; Chapter 11 in Sept 2023 and liquidation in Dec 2023 — [Wikipedia: SmileDirectClub](https://en.wikipedia.org/wiki/SmileDirectClub)
- Zume: $375M from SoftBank at a $2.25B valuation (2018); robot pizza abandoned, packaging pivot hit PFAS rules; closed June 2023 — [Wikipedia: Zume](https://en.wikipedia.org/wiki/Zume_Pizza)
- Peloton: ~$50B market cap in Jan 2021, ~$1.3B by June 2024; moved back to outsourced manufacturing in 2022; 2025 revenue $2.49B with a $119M net loss — [Wikipedia: Peloton](https://en.wikipedia.org/wiki/Peloton_Interactive)

**Indoor farming**
- AeroFarms (>$300M raised) filed June 2023; AppHarvest filed 24 July 2023 after building 165 acres of greenhouse in three years; Plenty filed after raising nearly $1B (last valued $1.9B); Bowery ceased operations Nov 2024 — [Ambrook Research](https://ambrook.com/research/supply-chain/vertical-farms-venture-capital-chapter-11); [Wikipedia: AppHarvest](https://en.wikipedia.org/wiki/AppHarvest)
- Bowery's total raised is reported as $472M by [Wikipedia](https://en.wikipedia.org/wiki/Bowery_Farming) and as more than $700M by [Ambrook](https://ambrook.com/research/supply-chain/vertical-farms-venture-capital-chapter-11); the sources conflict (the higher figure may include debt).

### Inferences
- Ranked recurring causes, by how often they appear above: (1) factory and headcount built before demand or process was proven (Katerra, Veev, Northvolt, Britishvolt, AppHarvest, Arrival, Peloton); (2) "orders" that were non-binding or undeliverable (Lordstown, Canoo, Arrival, Northvolt's $55B book, Relativity's $2.9B backlog); (3) Chinese scale collapsing the price umbrella mid-build (Solyndra, Northvolt, US solar and battery plants); (4) certification taking longer than the cash (Lilium, Volocopter); (5) customization eating the standardization thesis (Proterra, Katerra); (6) process novelty as the pitch rather than the product (Relativity's printing, Arrival's microfactories, Local Motors, Desktop Metal).
- Liquidation values are a useful prior: Lordstown $10M, Virgin Orbit $36M, Britishvolt £8.6M, Astra $11.25M, Fisker cars at ~$14K. Specialized factories and tooling have almost no resale value, so "the assets back the capital" is false. Britishvolt's land was worth 13x the company (derived: £110M vs £8.6M).
- Contract manufacturing is not a cure: Fisker (Magna) and Lordstown (Foxconn) failed with asset-light models because demand and quality, not factory ownership, were the binding problems.
- What would have to be true for a repeat attempt to work: a paying anchor customer before the first factory; one product, one plant, one geography until gross margin is positive; and a cost position that survives the Chinese price two years out, not today's.

### Gaps
- Bright Machines, Velo3D, Arcimoto, Olive, Eargo, IronOx, Enovix: no reliable data retrieved (search budget exhausted; Velo3D page returned 404). Do not cite figures for these from this note.
- Volocopter's reported sale to Wanfeng/Diamond and its price, and Lilium's "~$1.5B raised", were not confirmed. AIN says only "over US$1 billion".
- Fisker units produced/delivered and reservation counts not retrieved.
- Northvolt actual output: Wikipedia gives 79.8 MWh for the first three quarters of 2023 against a 16 GWh 2024 projection; the unit looks implausibly low and needs checking.
- Katerra revenue and total losses not found; one aggregator's "$3B loss" figure conflicts with the ~$2B consensus and was excluded.

## 2. Success patterns: what the winners had, and how much capital they consumed

### Takeaway
The winners almost all had a customer who paid before or during development (NASA, the Rwandan government, DoD, Amazon, deposit-paying consumers) and either a 10x capability or a protected market, rather than merely a lower price. Even so, the successful Western capital-intensive cases took roughly 10-17 years and from $1B to more than $25B to reach durable profitability. The capital-light exceptions used existing contract manufacturers and sold a differentiated product.

### Cited Findings
- SpaceX: Falcon 1 development cost about $90-100M; three failures (2006-2008) before orbit on flight 4 in Sept 2008 — [Wikipedia: Falcon 1](https://en.wikipedia.org/wiki/Falcon_1)
- SpaceX's first ten years used roughly $1B in total: about $100M from Musk, ~$200M private equity, ~$100M other investors, and about $400-500M of NASA progress payments on launch contracts (as of 2012) — [Wikipedia: History of SpaceX](https://en.wikipedia.org/wiki/History_of_SpaceX)
- Tesla: by Jan 2009 it had raised ~$187M and delivered 147 cars; survived on a $40M emergency round (Dec 2008), Daimler's $50M (2009), a $465M DOE loan (2009-10, repaid 2013) and a $226M IPO (2010); raised more than $4.5B after IPO by 2016; first run of four consecutive profitable quarters was July 2019-June 2020, about 17 years after founding — [Wikipedia: History of Tesla](https://en.wikipedia.org/wiki/History_of_Tesla,_Inc.)
- Tesla Model 3 demand was evidenced by 455,000 net reservations carrying $1,000 refundable deposits (2017) — [Wikipedia: Tesla Model 3](https://en.wikipedia.org/wiki/Tesla_Model_3)
- Rivian: ~$11B raised pre-IPO plus $13.5B IPO proceeds; net losses of $1.0B (2020), $4.7B (2021), $6.8B (2022), $5.4B (2023), $4.7B (2024), $3.6B (2025), about $26B cumulative (derived); 2025 deliveries 42,247; propped by an Amazon order for 100,000 vans (50,000+ in fleet by 2026), a VW JV of up to $5.8B and a $6B federal loan; R2 deliveries began June 2026 — [Wikipedia: Rivian](https://en.wikipedia.org/wiki/Rivian)
- Anduril: 2025 revenue $2.2B (doubled); May 2026 Series H of $5B at $61B; more than $11B raised in total; Arsenal-1 factory in Ohio budgeted at roughly $900M — [TechCrunch, May 2026](https://techcrunch.com/2026/05/13/anduril-raises-5b-doubles-valuation-to-61b/); [Barchart](https://www.barchart.com/story/news/2399792/anduril-s-61b-valuation-signals-a-defense-industrial-reset-that-will-reshape-the-primes)
- Hadrian (status 2026): ~$500M raised by its July 2025 Series C; valued $1.6B in Jan 2026, then raised $1.37B at $7.87B in Aug 2026, plus a $360M revolver; four sites totalling just under 3M sq ft; sells "factories as a service". No revenue, backlog, margin or productivity figures are disclosed in any source I found — [TechCrunch, July 2025](https://techcrunch.com/2025/07/17/hadrian-raises-260m-to-build-out-automated-factories-for-space-and-defense-parts); [The Robot Report, Aug 2026](https://www.therobotreport.com/hadrian-raises-1-37b-accelerate-u-s-manufacturing/); [Dealroom](https://dealroom.co/news/145088-hadrian-closes-360m-revolving-credit-facility-to-expand-us-manufacturing/)
- Rocket Lab: founded 2006, first orbit Jan 2018; $75M Series D (2017) and $150M Series E (2018); $777M from its 2021 SPAC; 2025 revenue $602M with a $198M net loss, still unprofitable 19 years in; large US government satellite contracts ($515M, $816M) — [Wikipedia: Rocket Lab](https://en.wikipedia.org/wiki/Rocket_Lab)
- Zipline: founded 2014; first customer was the Rwandan government (Oct 2016); FAA Part 135 in June 2022 and BVLOS without observers in Sept 2023; over 2 million deliveries by Jan 2026; US commercial service came about eight years after founding — [Wikipedia: Zipline](https://en.wikipedia.org/wiki/Zipline_(drone_delivery_company))
- Unitree: 2025 revenue RMB 1.7B and net income RMB 288M (~17% net margin, derived); G1 humanoid priced around $16,000; filed for a Shanghai STAR listing in March 2026 — [Wikipedia: Unitree](https://en.wikipedia.org/wiki/Unitree_Robotics)
- DJI: over 90% of the global consumer drone market (2024); ~CN¥80B (~$11.5B) revenue in 2025 — [Wikipedia: DJI](https://en.wikipedia.org/wiki/DJI)
- CATL: 2025 revenue RMB 423.7B, net income RMB 72.2B (~17% net margin, derived); ~37% global EV battery share — [Wikipedia: CATL](https://en.wikipedia.org/wiki/CATL)
- Xiaomi SU7: about three years from announcement (March 2021) to launch (March 2024) on a stated RMB 10B programme; 70,000 orders by April 2024; 139,487 delivered in 2024 and 242,291 in 2025 — [Wikipedia: Xiaomi SU7](https://en.wikipedia.org/wiki/Xiaomi_SU7)
- Bambu Lab: founded Aug 2020 by ex-DJI engineers; first printer shipped 21 months later via a ~US$7M Kickstarter — [Wikipedia: Bambu Lab](https://en.wikipedia.org/wiki/Bambu_Lab)
- Framework: founded Jan 2020; $9M seed; first laptops shipped July 2021 (18 months) using Compal as ODM; about $44M raised through Series A-1 — [Wikipedia: Framework Computer](https://en.wikipedia.org/wiki/Framework_Computer)
- Shein: revenue ~$38B (2024) on ~$1B operating income; tests ~100-unit batches across 3,000+ Guangzhou suppliers and can produce ~3 days after spotting a trend; valuation fell from $100B (2022) to $26.2B at its Aug 2026 Hong Kong listing after the US ended de minimis treatment in 2025 — [Wikipedia: Shein](https://en.wikipedia.org/wiki/Shein)
- Redwood Materials: $200M revenue in 2024; ~$6B valuation (Oct 2025); now pushing an energy-storage business built on used packs — [Wikipedia: Redwood Materials](https://en.wikipedia.org/wiki/Redwood_Materials)
- Slate Auto (live 2026 test of "cheap vehicle" demand): $1.4B raised before production; targets a $24,950 pickup; production targeted for end-2026 at up to 150,000/yr — [Wikipedia: Slate Auto](https://en.wikipedia.org/wiki/Slate_Auto)

### Inferences
- Customer money, not venture money, funded the hard part for the winners. NASA supplied roughly 40-50% of SpaceX's first $1B (derived). Zipline's first two years of flight were paid by a government. Rivian's survival rests on Amazon, VW and a federal loan. Anduril and Rocket Lab are revenue-backed by DoD.
- Speed of the capital-light route: Framework and Bambu reached shipping product in 18-21 months on under $10M of initial money, because they designed a better product and rented existing Asian manufacturing. Neither is a "cheaper production" company.
- Chinese winners (Unitree, DJI, CATL, Xiaomi) show hardware can earn ~17% net margins, but with scale, technical lead and a deep domestic supply base. That is evidence that the supply chain, not the factory, is the asset.
- Hadrian is the closest live example of the founder's thesis ("abundant production as a service") and remains unproven on the only numbers that matter. Its valuation rose about 5x in seven months (derived: $1.6B to $7.87B) with zero disclosed revenue or margin. Treat it as evidence that capital is available, not that the model works.
- Shein is the purest "fast, cheap, on-demand production" winner, and its operating margin is under 3% (derived) with value cut 74% from peak (derived) when one trade rule changed.

### Gaps
- Base Power, Crusoe, BYD, Formlabs, Sonos, Saronic: nothing retrieved before the search budget ran out.
- First positive gross-profit quarter for Rivian, Tesla accumulated deficit, and SpaceX first profitable year: not found in fetched sources.
- Anduril profitability and capital consumed before positive gross margin are undisclosed. Database totals for capital raised conflict ($6.3-6.8B pre-Series H in CB Insights/Sacra versus ">$11B" after it).
- Bambu Lab revenue (a reference title mentions ~CNY 1.5B) is unverified.

## 3. Who captures the value of a cost collapse?

### Takeaway
Measured margins say the commodity producer usually does not. Undifferentiated producers earn 0-3% or lose money once capacity floods in, while owners of a certificate, sole-source position or the customer relationship keep 17-54%. "Be the cheap producer" is only a good business when paired with scale leadership and technical lead (CATL) or a protected niche.

### Cited Findings
- Hon Hai/Foxconn 2025: revenue NT$8.1 trillion, net income NT$189.4B, a ~2.3% net margin (derived), with 826,608 employees — [Wikipedia: Foxconn](https://en.wikipedia.org/wiki/Foxconn)
- TransDigm (proprietary, mostly sole-source aerospace parts; most EBITDA from aftermarket): "EBITDA As Defined" margin of 53.9% in fiscal 2025, up from 52.6% in fiscal 2024 (non-GAAP) — [TransDigm investor release](https://transdigmgroupinc.gcs-web.com/node/22131/pdf) (figure as returned in search results; confirm the exact document); Q3 FY2025 margin of ~54% reported by [Motley Fool](https://www.fool.com/data-news/2025/08/06/transdigm-tdg-q3-margin-hits-54)
- Solar after the cost collapse: China's four largest module makers (LONGi, Jinko, Trina, JA) lost a combined ~RMB 11B (US$1.54B) in H1 2025 — [PV Tech](https://www.pv-tech.org/chinas-top-four-solar-manufacturers-suffer-1-54-billion-losses-h1-2025/)
- Module gross margins were negative in H1 2025: Jinko -2.01%, LONGi's module business -3.53% — [pv magazine](https://www.pv-magazine.com/2025/09/05/chinese-pv-industry-brief-top-4-module-manufacturers-post-heavy-losses-in-h1/)
- Full-year 2025 loss forecasts: LONGi RMB 6.0-6.5B, Tongwei RMB 9-10B, TCL Zhonghuan RMB 8.2-9.6B, JA Solar RMB 4.5-4.8B — [pv magazine, Jan 2026](https://www.pv-magazine.com/2026/01/23/chinese-pv-industry-brief-longi-tongwei-announce-sharp-losses-for-fiscal-2025/)
- Chinese module prices fell 60% between 2022 and 2024; China's solar manufacturing investment fell 80% from its 2023 peak to ~$16B in 2025, yet another 458 GW of cell capacity is under construction — [Rhodium Group, "Worlds Apart", May 2026](https://rhg.com/wp-content/uploads/2026/05/Worlds-Apart-Contrasting-US-China-Approaches-to-Scaling-Clean-Technology-Manufacturing-1.pdf)
- Batteries: pack prices hit $108/kWh (2025), stationary storage $70/kWh (down 45% in a year), with "continued cell manufacturing overcapacity" named as a driver — [BloombergNEF](https://about.bnef.com/insights/clean-transport/lithium-ion-battery-pack-prices-fall-to-108-per-kilowatt-hour-despite-rising-metal-prices-bloombergnef/)
- Counter-examples where the low-cost producer keeps margin: CATL ~17% net (2025) and Unitree ~17% net (2025), both derived from [Wikipedia: CATL](https://en.wikipedia.org/wiki/CATL) and [Wikipedia: Unitree](https://en.wikipedia.org/wiki/Unitree_Robotics)
- Shein, the fast on-demand producer-retailer, earned ~$1B operating income on ~$38B revenue in 2024 — [Wikipedia: Shein](https://en.wikipedia.org/wiki/Shein)
- Rhodium's forward view: if China's market consolidates, survivors such as BYD and CATL benefit from subsidy mechanisms that scale with revenue, further entrenching them — [Rhodium Group](https://rhg.com/wp-content/uploads/2026/05/Worlds-Apart-Contrasting-US-China-Approaches-to-Scaling-Clean-Technology-Manufacturing-1.pdf)

### Inferences
- In the limiting case the founder describes (production truly abundant), production itself is the commodity and its margin goes to zero or below, exactly as in modules. The scarce things then are demand ownership, certification, installed base, service network, sole-source position and regulatory permission. A ranked list of businesses should score each idea on which of those it owns, not on how much cheaper it produces.
- The honest version of the Model T analogy: Ford captured value because he was alone on the cost curve for about 15 years. Today China is already on that curve in most categories, so a Western entrant arrives as the high-cost follower unless law excludes the leader.
- What would have to be true for a "cheap producer" strategy: top-three global scale within the capital available, a process or chemistry lead of at least one generation, and a buyer base that cannot simply import.

### Gaps
- Margins for LEDs, TVs, DRAM, Apple, ASML and Intuitive were not retrieved; I can vouch only for the figures above.
- TransDigm's 53.9% came from a search-result summary of the company release; the exact filing should be linked before publication.

## 4. China check: abundant production already exists. What does that say about the Western bottleneck?

### Takeaway
Where it could be measured, China already delivers the "3x cheaper" outcome (storage systems ~3x cheaper than the US, ships 2-4x, humanoids at ~$16K), and its producers are losing money doing so. The Western constraint is therefore mostly legal and institutional access (tariffs, security bans, certification, installation, financing), not an absence of cheap production. The realistic opening for a domestic fast producer is where law excludes Chinese supply, with the warning that protection alone has produced the Jones Act outcome.

### Cited Findings
- Battery packs (2025): China $84/kWh; North America 44% higher and Europe 56% higher — [BloombergNEF](https://about.bnef.com/insights/clean-transport/lithium-ion-battery-pack-prices-fall-to-108-per-kilowatt-hour-despite-rising-metal-prices-bloombergnef/)
- Turnkey grid storage systems: US$73/kWh in China versus $177/kWh in Europe and $219/kWh in the US (BNEF survey), i.e. 3.0x for the US (derived) — [Energy-Storage.news](https://www.energy-storage.news/battery-storage-system-prices-continue-to-fall-sharply-bnef-and-ember-reports-find/)
- China's announced lithium-ion capacity exceeds expected 2025 global demand about threefold — [Fortune, Aug 2025](https://fortune.com/2025/08/29/trump-ev-tax-credit-cuts-battery-surplus-us-manufacturing/); global battery investment plans of $1.1 trillion for 2024-2030 stood against $242B of expected demand — [BNN Bloomberg](https://www.bnnbloomberg.ca/business/company-news/2024/11/29/how-europes-ev-battery-pioneer-northvolt-came-unstuck/)
- EVs: Rhodium estimates BYD's cost advantage over Tesla China at ~$4,700 per vehicle; subsidies explain only ~5% ($292 direct + $12 financing); avoided supplier markup from vertical integration ~$2,369 and lower R&D/admin overhead ~$1,719; BYD makes ~80% of tier-one components in-house — [China Daily/ANN op-ed via The Star, June 2026](https://www.thestar.com.my/business/business-news/2026/06/09/the-real-story-behind-chinas-manufacturing-might) (secondary and written by a Chinese academic; the underlying Rhodium study was not retrieved)
- Ships: in 2022 the US had 5 large oceangoing commercial ships on order versus 1,794 for China and 734 for South Korea; the US Navy estimates China's capacity at 232x America's; a US-built ship costs roughly 2-4x a foreign one — [Construction Physics](https://www.construction-physics.com/p/why-cant-the-us-build-ships)
- The Jones Act (US-built requirement for domestic trade) kept a small industry alive without making it competitive; when the construction subsidy ended around 1982, output went from ~20 commercial vessels a year to five in the next eight years — [Construction Physics](https://www.construction-physics.com/p/why-cant-the-us-build-ships)
- Drones: DJI held over 90% of the global consumer market (2024) and 77% of the US market (2020) — [Wikipedia: DJI](https://en.wikipedia.org/wiki/DJI)
- Humanoids and quadrupeds: Unitree sells its G1 humanoid at about $16,000 and is profitable — [Wikipedia: Unitree](https://en.wikipedia.org/wiki/Unitree_Robotics)
- Wages are not the main story: Chinese urban manufacturing wages rose from ~72,088 yuan (2018) to 107,987 yuan (~$15,895) in 2024 while export prices stayed flat or fell — [The Star/China Daily](https://www.thestar.com.my/business/business-news/2026/06/09/the-real-story-behind-chinas-manufacturing-might)

**Markets closed to Chinese supply by law (sourced)**
- Drones: on 22 Dec 2025 the FCC added foreign-made drones and critical components to its Covered List, blocking authorization of new models; previously approved models can still be sold. DJI sued in Feb 2026 and the case was unresolved in my sources — [DroneLife](https://dronelife.com/2025/12/22/fcc-adds-foreign-made-drones-and-components-to-covered-list-citing-national-security-risks/); [Wikipedia: DJI](https://en.wikipedia.org/wiki/DJI)
- Connected vehicles: Commerce/BIS rule issued 14 Jan 2025 bars sale of connected vehicles by PRC- or Russia-controlled manufacturers and covered software from model year 2027, and covered hardware from model year 2030, for vehicles under 10,001 lb — [BIS](https://www.bis.gov/connected-vehicles)
- Defense: the FY2024 NDAA bars defense funding for CATL products and DoD listed CATL as a "Chinese military company" in Jan 2025 — [Wikipedia: CATL](https://en.wikipedia.org/wiki/CATL)
- Batteries and solar via tax law: from 2026, Section 45X credits require a 60% non-"prohibited foreign entity" sourcing ratio for battery components, rising to 85% by 2030 — [Rhodium Group](https://rhg.com/wp-content/uploads/2026/05/Worlds-Apart-Contrasting-US-China-Approaches-to-Scaling-Clean-Technology-Manufacturing-1.pdf)
- Consumer imports: the US ended de minimis duty-free entry for China/Hong Kong parcels in 2025 — [Wikipedia: Shein](https://en.wikipedia.org/wiki/Shein)

### Inferences
- If cheap, fast production were sufficient to unlock latent demand, the unlock would already be visible wherever Chinese goods are admitted. Western shortfalls are therefore better explained by exclusion (tariffs and bans), by the non-factory share of delivered cost (installation, interconnection, permitting, dealer and service networks, financing), and by trust and certification.
- The BYD decomposition implies about 87% of its cost edge (derived: $2,369 + $1,719 of $4,700) is integration and overhead, not labor or subsidy. Robots that replace direct labor do not close that gap; a dense supplier base and lean overhead do.
- Protected markets are real but carry three discounts: (a) they are small relative to consumer markets; (b) protection is litigated and reversible (DJI suit pending; IRA demand supports reversed within three years); (c) protection without export discipline produces the Jones Act equilibrium of 2-4x cost and negligible volume.
- What would have to be true: the founder picks a category where Chinese supply is legally barred and the buyer has budget and urgency (defense, public-safety drones, grid and telecom security), and prices against the protected Western incumbent rather than against China.

### Gaps
- No sourced cost gaps obtained for appliances, machine tools, transformers, construction machinery, prefab, medical imaging or port cranes. ITIF, MERICS, CAAM and MIIT data were not retrieved.
- BIOSECURE Act status, port-crane tariffs, grid-equipment security rules and current Section 301/232 tariff rates on Chinese EVs were not verified.
- The CSIS shipbuilding report returned 403; ship figures rely on Construction Physics.

## 5. Actor-response evidence: how each class of actor actually behaves

### Takeaway
Revealed behavior is far more conservative than stated intent. Consumers under-buy stigmatized cheap versions and convert small deposits at low single-digit rates. Business "orders" evaporate. Unions and regulators can block or slow adoption by contract or rule. Policy and capital cycles reverse faster than a factory pays back.

### Cited Findings

**(a) Consumers: stated versus revealed**
- New manufactured homes cost $86.62/sq ft versus $165.94/sq ft for site-built excluding land (2023), about 48% less (derived), yet hold only ~9-10% of new housing, down from 17-24% in the 1990s — [NAHB Eye on Housing, April 2025](https://eyeonhousing.org/2025/04/manufactured-homes-an-alternative-means-of-housing-supply/); 9% of single-family starts in 2024 — [Manufactured Housing Institute fact sheet](https://www.manufacturedhousing.org/wp-content/uploads/2025/09/US-fact-Sheet.pdf)
- Why the cheap option under-sells: ~80% of new manufactured homes are titled as personal property (derived from 20% real-estate titling), which Fannie/Freddie do not buy as conventional mortgages; zoning bans and large-lot rules exclude them — [NAHB](https://eyeonhousing.org/2025/04/manufactured-homes-an-alternative-means-of-housing-supply/)
- Tata Nano peaked at ~30% of its 250,000/yr plan (derived: 74,527 units) and carried a "poor man's car" stigma — [Wikipedia: Tata Nano](https://en.wikipedia.org/wiki/Tata_Nano)
- Cybertruck: Musk claimed over 1 million reservations ($100 refundable deposit); 46,096 were delivered from Nov 2023 to Feb 2025, a conversion under 5% — [Carscoops](https://www.carscoops.com/2025/04/cybertrucks-1-million-reservations-translate-to-46k-sales-musk-rants-about-legions-of-robots/)
- Before launch, a Recurrent survey found ~75% of Cybertruck reservation holders said they intended to buy — [InsideEVs](https://insideevs.com/news/662718/tesla-cybertruck-orders-follow-through-survey/)
- Coverage quotes a Cox Automotive analyst saying the industry aims for reservation conversion of about 2-16% — [Torque News](https://www.torquenews.com/11826/end-only-25-cybertruck-reservation-holders-decided-buy-truck-tesla-officially-finishes) (secondary; the exact article carrying the quote was not verified)
- Counter-evidence that cheap, small vehicles sell when policy rewards them: kei cars reached a record 40% of Japanese new-car sales in 2013 and over a third in FY2016, supported by lower tax and insurance and exemption from parking-space certificates in rural areas — [Wikipedia: Kei car](https://en.wikipedia.org/wiki/Kei_car)
- Counter-evidence that deposits can be real: Tesla Model 3 held 455,000 net reservations at $1,000 each; Xiaomi's SU7 took 70,000 orders in its first month and delivered 139,487 in 2024 — [Wikipedia: Tesla Model 3](https://en.wikipedia.org/wiki/Tesla_Model_3); [Wikipedia: Xiaomi SU7](https://en.wikipedia.org/wiki/Xiaomi_SU7)

**(b) Business buyers**
- Announced fleet orders did not convert: Canoo (Walmart 4,500; Kingbee 9,300 "binding") delivered 22 vehicles in 2023; Arrival's 10,000-van UPS order preceded insolvency — [Wikipedia: Canoo](https://en.wikipedia.org/wiki/Canoo); [Wikipedia: Arrival](https://en.wikipedia.org/wiki/Arrival_(company))
- Qualified buyers cancel on quality: BMW pulled a €2B Northvolt order in June 2024, which triggered the failed equity round and the collapse of a $5B green loan — [BNN Bloomberg](https://www.bnnbloomberg.ca/business/company-news/2024/11/29/how-europes-ev-battery-pioneer-northvolt-came-unstuck/)
- Industrial buyers expect 99.99% reliability; at 99% a line loses ~5 hours a month and downtime can cost tens of thousands of dollars per minute — [IEEE Spectrum, Sept 2025](https://spectrum.ieee.org/humanoid-robot-scaling)
- Builders resist: mid-size homebuilders cannot absorb workflow disruption and large ones have little incentive to change — [OneBuild](https://onebuild.substack.com/p/the-prefab-and-modular-graveyard)
- DoD spreads awards rather than crowning one startup (the Air Force chose Shield AI software for Anduril's Fury airframe) — [TechCrunch](https://techcrunch.com/2026/05/13/anduril-raises-5b-doubles-valuation-to-61b/)

**(c) Incumbents**
- Incumbents use regulators and courts: orthodontists filed complaints against SmileDirectClub in 36 state dental boards; Align won $43.4M in arbitration against it — [Wikipedia: SmileDirectClub](https://en.wikipedia.org/wiki/SmileDirectClub)
- Domestic challengers lobby too: Skydio is cited in connection with lobbying for DJI restrictions — [Wikipedia: DJI](https://en.wikipedia.org/wiki/DJI)
- Analysts expected a venture-backed defense startup to be bought by a prime in 2026, and defense VC exits in 2025 were mostly acquisitions — [Defense News, Jan 2026](https://www.defensenews.com/industry/2026/01/20/defense-tech-startups-had-their-best-funding-year-ever-in-2025/)

**(d) Regulators: fast and slow**
- Fast when the state is the buyer and takes the risk: Operation Warp Speed went from launch (15 May 2020) to first EUA (11 Dec 2020) in about seven months on an ~$18B budget, pre-paying for manufacturing before approval (e.g. $1.95-2B to Pfizer for 100M doses, $1.6B to Novavax) — [Wikipedia: Operation Warp Speed](https://en.wikipedia.org/wiki/Operation_Warp_Speed)
- Fast when the aim is exclusion: FCC foreign-drone listing (Dec 2025) and the BIS connected-vehicle rule (Jan 2025) — [DroneLife](https://dronelife.com/2025/12/22/fcc-adds-foreign-made-drones-and-components-to-covered-list-citing-national-security-risks/); [BIS](https://www.bis.gov/connected-vehicles)
- Slow for new product categories: Zipline needed until 2022 (Part 135) and 2023 (BVLOS without observers), eight to nine years after founding; Lilium and Volocopter went insolvent after roughly a decade without type certification — [Wikipedia: Zipline](https://en.wikipedia.org/wiki/Zipline_(drone_delivery_company)); [Wikipedia: Lilium](https://en.wikipedia.org/wiki/Lilium_GmbH); [Wikipedia: Volocopter](https://en.wikipedia.org/wiki/Volocopter)
- Local rules bite: Zume's packaging could not legally hold food in San Francisco because of PFAS — [Wikipedia: Zume](https://en.wikipedia.org/wiki/Zume_Pizza)

**(e) Labor and local politics**
- The ILA demanded a total automation ban at 36 US ports, struck on 1 Oct 2024, and won a six-year master contract with a 62% wage increase and "full protections against automation" — [Wikipedia: International Longshoremen's Association](https://en.wikipedia.org/wiki/International_Longshoremen%27s_Association); [Wikipedia: 2024 port strike](https://en.wikipedia.org/wiki/2024_United_States_port_strike)
- Union resistance to technological change is cited as one cause of US shipbuilding's long-run uncompetitiveness — [Construction Physics](https://www.construction-physics.com/p/why-cant-the-us-build-ships)

**(f) Financiers**
- Defense-tech VC hit a record $49.1B in 2025 (PitchBook, includes dual-use) versus $27.2B in 2024; CB Insights' narrower count is $17.9B versus $7.3B; US deals rose 30% to 155 — [Defense News](https://www.defensenews.com/industry/2026/01/20/defense-tech-startups-had-their-best-funding-year-ever-in-2025/)
- Manufacturing-focused defense investment was only $4.7B across 39 deals in 2025 (from $2.6B across 24), i.e. under 10% of the PitchBook total (derived) — [Defense News](https://www.defensenews.com/industry/2026/01/20/defense-tech-startups-had-their-best-funding-year-ever-in-2025/)
- 2026: a record $19.8B in Q1; H1 total $35.4B across 415 deals, but deal count fell from 251 in Q1 to 164 in Q2 while average Q2 deal size rose to ~$91M — [PitchBook Q2 2026 Defense Tech VC First Look](https://pitchbook.com/news/reports/q2-2026-defense-tech-vc-first-look) (figures taken from the search-result summary; the page itself returned 403)
- Money is concentrating: the same trio (Anduril, Helsing, Saronic) led funding in both 2024 and 2025; investors warn that "execution, not invention, will determine returns" — [Defense News](https://www.defensenews.com/industry/2026/01/20/defense-tech-startups-had-their-best-funding-year-ever-in-2025/)
- Factory debt: the 2025 budget law (OBBBA) eliminated DOE's ATVM loan programme, "the primary financing mechanism for large clean manufacturing projects that were too capital-intensive for equity alone" — [Rhodium Group](https://rhg.com/wp-content/uploads/2026/05/Worlds-Apart-Contrasting-US-China-Approaches-to-Scaling-Clean-Technology-Manufacturing-1.pdf)
- KORE Power dropped its ~$1B Arizona cell plant, which depended on a federal loan for nearly 80% of cost — [Energy-Storage.news](https://www.energy-storage.news/us-battery-gigafactories-face-delays-and-cancellations-amid-market-uncertainty)
- Bank and strategic capital is appearing for defense manufacturing: Morgan Stanley arranged Hadrian's $360M revolver and JPMorgan's Security and Resiliency Initiative co-led its Series D — [Dealroom](https://dealroom.co/news/145088-hadrian-closes-360m-revolving-credit-facility-to-expand-us-manufacturing/); [The Robot Report](https://www.therobotreport.com/hadrian-raises-1-37b-accelerate-u-s-manufacturing/)
- Public markets misprice then abandon: Virgin Orbit's SPAC raised $228M of an expected $483M — [Wikipedia: Virgin Orbit](https://en.wikipedia.org/wiki/Virgin_Orbit)

**(g) Insurers, surety and liability**
- Surety bonding is a chokepoint in construction: a disputed $440M debt reportedly blocked Katerra's bonding and hence its ability to take work — [Construction Physics](https://www.construction-physics.com/p/another-day-in-katerradise)
- Early field failures are existential for a new brand: all 209 Nikola Tre BEVs were recalled; Nano fires fed a durable safety stigma — [Wikipedia: Nikola](https://en.wikipedia.org/wiki/Nikola_Corporation); [Wikipedia: Tata Nano](https://en.wikipedia.org/wiki/Tata_Nano)

**(h) Macro: boom-bust overcapacity**
- Global clean-tech manufacturing investment peaked at $265B in 2023 and fell 42% to $155B in 2025; China's fell nearly 70% from its 2023 peak — [Rhodium Group](https://rhg.com/wp-content/uploads/2026/05/Worlds-Apart-Contrasting-US-China-Approaches-to-Scaling-Clean-Technology-Manufacturing-1.pdf)
- US clean manufacturing investment rose from $9B (2021) to $50B (2024), then fell 17% in 2025. In 2025, 24 projects worth $22.5B were cancelled ($46B across 95 projects including earlier-stage ones); 97% of cancelled dollars were in the EV supply chain; battery cancellations ($11B) exceeded new battery announcements ($8B); about $98B of unbuilt projects remain exposed — [Rhodium Group](https://rhg.com/wp-content/uploads/2026/05/Worlds-Apart-Contrasting-US-China-Approaches-to-Scaling-Clean-Technology-Manufacturing-1.pdf)
- Demand moved with policy: after the $7,500 EV credit expired in Sept 2025, US EV consumer spending fell 43% quarter on quarter and EV inventory reached 168 days' supply by Jan 2026 — [Rhodium Group](https://rhg.com/wp-content/uploads/2026/05/Worlds-Apart-Contrasting-US-China-Approaches-to-Scaling-Clean-Technology-Manufacturing-1.pdf)
- Atlas Public Policy counted ~$20.8B of clean-energy manufacturing cancellations and ~27,300 anticipated jobs lost in 2025 — [Tech Brew](https://www.techbrew.com/stories/2025/11/25/ev-sector-woes-q4-2025) (different scope from Rhodium; do not add the two)

### Inferences
- A $100 deposit measures curiosity; a $1,000 deposit or a prepaid, penalty-bearing contract measures demand. Use the deposit size and cancellation terms, not the count, to discount any reservation figure. A working prior from the evidence: under 5% conversion for small refundable deposits on a delayed, repriced product; materially higher only when the product ships on time at the promised price.
- The cheap version loses when the cheapness is visible as a class marker (Nano, manufactured homes) or when financing, zoning and resale rules penalize it. The kei car case shows the reverse works when regulation actively rewards the cheap form. A founder should ask which regulation would make their cheap product the rational choice, and whether it exists.
- Policy half-life is shorter than factory payback: US clean manufacturing support lasted about three years (2022-2025). Any plan that needs a subsidy or tariff to hold for ten years should be discounted heavily.
- Capital is abundant for defense and "reindustrialization" narratives in 2026, but it is concentrating in fewer, larger rounds and little of it (under 10%) goes to manufacturing-focused companies. A seed-stage founder competes for attention with $1B+ rounds.

### Gaps
- OTC hearing-aid uptake since the 2022 FDA rule: search failed (budget). Not sourced here.
- Building-trades opposition to modular, NIMBY data, FAA MOSAIC, drone BVLOS Part 108 and the 2025 NRC orders: not retrieved.
- DOE LPO status in 2026 and Office of Strategic Capital loans: both pages returned 404; no data.
- Fund sizes for a16z American Dynamism, Founders Fund, 8VC and General Catalyst: not retrieved.
- Incumbent price-matching episodes (e.g. legacy launch providers, legacy automakers) were not sourced.
- Product-liability insurance costs for new hardware categories: no data found.

## 6. Limits of AI/robot abundance by 2030-2035

### Takeaway
The evidence supports "robots are real but not yet a cost revolution." Humanoid deployments are pilots, the best-known automation-first factories were walked back, and where cost gaps have been decomposed the driver is supply-chain integration and overhead rather than direct labor. Claims of 3-100x cost or speed gains from AI plus robotics are not yet backed by disclosed operating data from any company I could find.

### Cited Findings
- As of Sept 2025 the most successful humanoid firms had deployed "only a small handful of robots in carefully controlled pilot projects" — [IEEE Spectrum](https://spectrum.ieee.org/humanoid-robot-scaling)
- Capacity runs far ahead of demand: Agility's factory can build 10,000+ Digits a year but expected to ship "hundreds" in 2025; Tesla planned 5,000 Optimus in 2025 and 50,000 in 2026; Figure spoke of a path to 100,000 by 2029 — [IEEE Spectrum](https://spectrum.ieee.org/humanoid-robot-scaling)
- Melonee Wise (then Agility's chief product officer): "I don't think anyone has found an application for humanoids that would require several thousand robots per facility," and "Currently AI is not robust enough to meet the requirements of the market" — [IEEE Spectrum](https://spectrum.ieee.org/humanoid-robot-scaling)
- Duty cycle: Digit runs ~90 minutes per charge and in practice recharges after about 30 minutes of work; it lifts up to 16 kg — [IEEE Spectrum](https://spectrum.ieee.org/humanoid-robot-scaling)
- Safety standards for dynamically balancing legged robots are still being written (ISO work involving Boston Dynamics) — [IEEE Spectrum](https://spectrum.ieee.org/humanoid-robot-scaling)
- Tesla Optimus slipped repeatedly: "production-ready by 2023" was missed; a 2024 goal of 1,000+ units in Tesla plants in 2025 has no reported fulfilment; production start was most recently guided to about July-August 2026; demos in 2024 relied on teleoperation; the programme head left in June 2025 — [Wikipedia: Optimus](https://en.wikipedia.org/wiki/Optimus_(robot))
- Forecast spread shows how speculative the field is: Bank of America expected 18,000 humanoid shipments in 2025 while Morgan Stanley projects over 1 billion by 2050 — [IEEE Spectrum](https://spectrum.ieee.org/humanoid-robot-scaling)
- Tesla Model 3: built 260 cars in Q3 2017 against a 1,500 goal and 2,425 in Q4 against a 5,000/week target, which was finally hit on 1 July 2018 — [Wikipedia: Tesla Model 3](https://en.wikipedia.org/wiki/Tesla_Model_3)
- Musk, April 2018: "Yes, excessive automation at Tesla was a mistake. To be precise, my mistake. Humans are underrated" — [CNBC](https://www.cnbc.com/2018/04/13/elon-musk-admits-humans-are-sometimes-superior-to-robots.html)
- Adidas closed its robotic Speedfactories in Ansbach and Atlanta by April 2020 and moved the technology to Asian suppliers; the Ansbach plant used 160 people to make 1,500 pairs a day, against more than a million workers in Adidas's contract factories — [TechCrunch](https://techcrunch.com/2019/11/11/adidas-backpedals-on-robotic-factories/); [Bloomberg Opinion](https://www.bloomberg.com/opinion/articles/2019-11-13/adidas-stumbles-on-the-path-to-running-shoe-perfection)
- Foxconn reportedly replaced 60,000 workers with robots at one site (2016) yet still employed 826,608 people in 2025 — [Wikipedia: Foxconn](https://en.wikipedia.org/wiki/Foxconn)
- Novel process as product has reversed: Relativity dropped printing for Terran R's tanks; Zume abandoned robotic pizza; Katerra's and Veev's automation preceded stable designs — [Wikipedia: Relativity Space](https://en.wikipedia.org/wiki/Relativity_Space); [Wikipedia: Zume](https://en.wikipedia.org/wiki/Zume_Pizza); [OneBuild](https://onebuild.substack.com/p/the-prefab-and-modular-graveyard)
- Skilled commissioning and yield, not robot count, sank Northvolt: it could not diagnose early yield problems and struggled with imported Chinese equipment — [Project Blue](https://projectblue.com/blue/news-analysis/1076/northvolt-bankruptcy-demonstrates-technical-and-geopolitical-challenges-of-core-battery-manufacturing--); [BNN Bloomberg](https://www.bnnbloomberg.ca/business/company-news/2024/11/29/how-europes-ev-battery-pioneer-northvolt-came-unstuck/)
- Indoor farming shows energy as a hard floor: critics attribute failures chiefly to the cost of artificial light and capital intensity — [Fortune, Sept 2023](https://fortune.com/2023/09/18/indoor-farming-startups-bankruptcy-dumb-idea-expensive/)
- Hadrian, the flagship "AI-automated factory" company, publishes no quantitative productivity or efficiency figures — [The Robot Report](https://www.therobotreport.com/hadrian-raises-1-37b-accelerate-u-s-manufacturing/)

### Inferences
- Reliability arithmetic is the core obstacle: moving from 99% to 99.99% is a 100x reduction in failure rate (derived), and that is the gap between a demo and a production line.
- Automation tends to work after a product and process are stable and volumes are high (the Asian contract factories that inherited Speedfactory technology), and to fail when used to substitute for process maturity (Model 3 in 2017-18, Katerra, Veev). For a startup, automation is a year-five optimization, not a founding premise.
- Well-evidenced in my sources: Chinese integrated supply chains produce 15-67% lower costs today (EV ~15%, packs 31-36% below Western prices (derived from the 44-56% premiums), storage systems ~67% below US). Speculative: any claim that AI-driven factories deliver 3x or more on finished-product cost in the West by 2030. I found no disclosed data supporting it.
- What would have to be true: published unit economics from an AI-native factory showing sustained gross margin above incumbent job shops, plus humanoid or general-purpose robots at 99.9%+ uptime over multi-shift operation.

### Gaps
- Direct labor's share of manufacturing cost (commonly cited as ~10-25%) could not be sourced after the search budget ran out; treat that range as unverified.
- Terry Gou's 2011 "one million robots" target and the shortfall were not found in the fetched text.
- Evidence on AI gains in design cycle time, quoting, CAM programming, inspection and changeover: none retrieved. This is the most important missing piece for the optimistic case and should be covered by other researchers.
- Critical-minerals, energy and factory-permitting constraints: not researched. A Gartner January 2026 forecast (fewer than 20 companies scaling humanoids in supply chains by 2028) appeared only in a low-quality secondary source and is not relied on.

## 7. Buildability filter for a founder raising $5-50M in 2026-27

### Takeaway
On the evidence, a $5-50M company can reach revenue in 18-24 months only if it (i) sells a differentiated product built on existing contract manufacturing, or (ii) sells into a paying government or enterprise customer with progress payments, or (iii) sells a component or service into a protected market. Anything requiring its own gigafactory, vehicle plant, type certificate or new housing system has historically needed $500M to $25B before proof, with most attempts failing.

### Cited Findings

**Tier A: reached shipping product within ~2 years on under $50M**
- Framework: $9M seed, product shipping in 18 months via Compal; ~$44M raised through its 2024 Series A-1 — [Wikipedia: Framework Computer](https://en.wikipedia.org/wiki/Framework_Computer)
- Bambu Lab: first product 21 months after founding, launched with ~US$7M of Kickstarter pre-sales — [Wikipedia: Bambu Lab](https://en.wikipedia.org/wiki/Bambu_Lab)
- Zipline: founded 2014, paid government service operating by Oct 2016 — [Wikipedia: Zipline](https://en.wikipedia.org/wiki/Zipline_(drone_delivery_company))
- Unitree reached RMB 1.7B revenue and RMB 288M profit (2025) from a Chinese component base — [Wikipedia: Unitree](https://en.wikipedia.org/wiki/Unitree_Robotics)

**Tier B: $100M-$1B before proof**
- SpaceX reached orbit on ~$90-100M of development spend but needed ~$1B over ten years, about half of it from NASA — [Wikipedia: Falcon 1](https://en.wikipedia.org/wiki/Falcon_1); [Wikipedia: History of SpaceX](https://en.wikipedia.org/wiki/History_of_SpaceX)
- Tesla had consumed ~$187M to deliver 147 cars and then required a $465M government loan — [Wikipedia: History of Tesla](https://en.wikipedia.org/wiki/History_of_Tesla,_Inc.)
- Rocket Lab raised at least $225M in its 2017-18 rounds around first orbit, 12 years after founding — [Wikipedia: Rocket Lab](https://en.wikipedia.org/wiki/Rocket_Lab)
- Hadrian had raised nearly $500M by mid-2025 with revenue still undisclosed — [TechCrunch](https://techcrunch.com/2025/07/17/hadrian-raises-260m-to-build-out-automated-factories-for-space-and-defense-parts)
- Xiaomi, an incumbent with brand and cash, budgeted RMB 10B (~$1.4B) and three years for its first car — [Wikipedia: Xiaomi SU7](https://en.wikipedia.org/wiki/Xiaomi_SU7)
- Slate has raised $1.4B before building its first production truck — [Wikipedia: Slate Auto](https://en.wikipedia.org/wiki/Slate_Auto)

**Tier C: $1B+ and usually fatal**
- Rivian: ~$24.5B raised (pre-IPO plus IPO, derived) and ~$26B of cumulative net losses 2020-2025 (derived) for 42,247 deliveries in 2025 — [Wikipedia: Rivian](https://en.wikipedia.org/wiki/Rivian)
- Northvolt >$14B, Katerra >$2B, View ~$1.8B, Relativity $1.3B, Lilium >$1B: all failed or were rescued without reaching positive unit economics — sources in Section 1
- Anduril is the exception at >$11B raised for $2.2B of 2025 revenue, roughly $5 raised per $1 of annual revenue (derived) — [TechCrunch](https://techcrunch.com/2026/05/13/anduril-raises-5b-doubles-valuation-to-61b/)

**Capital-to-revenue sanity checks from failures**
- Canoo: $2.4B SPAC valuation, $886K revenue in 2023 — [Wikipedia: Canoo](https://en.wikipedia.org/wiki/Canoo)
- Boxabl: $3.5B SPAC valuation, $2.6M revenue in the first nine months of 2026 with negative gross margin — [The Real Deal](https://therealdeal.com/national/2026/07/21/boxabl-ignites-spac-market-goes-public-at-3-5b-valuation/); [Panabee](https://www.panabee.com/news/boxabl-earnings-q3-2026)
- Nikola: $50.8M revenue against a $784M loss in 2022 — [Wikipedia: Nikola](https://en.wikipedia.org/wiki/Nikola_Corporation)

**Demand de-risking mechanisms and their observed conversion**
- Small refundable consumer deposits: under 5% (Cybertruck, $100) — [Carscoops](https://www.carscoops.com/2025/04/cybertrucks-1-million-reservations-translate-to-46k-sales-musk-rants-about-legions-of-robots/)
- Larger deposits on a product delivered roughly as promised: Model 3's 455,000 at $1,000 sustained a multi-year ramp; Xiaomi's 70,000 first-month orders became 139,487 deliveries in year one — [Wikipedia: Tesla Model 3](https://en.wikipedia.org/wiki/Tesla_Model_3); [Wikipedia: Xiaomi SU7](https://en.wikipedia.org/wiki/Xiaomi_SU7)
- No-deposit LOIs: effectively zero (Lordstown) — [Wikipedia: Lordstown Motors](https://en.wikipedia.org/wiki/Lordstown_Motors)
- "Binding" B2B orders without prepayment: did not prevent failure (Canoo, Arrival, Northvolt's $55B book, Relativity's $2.9B backlog) — sources above
- Strategic customer who also invests and takes delivery: Amazon's 100,000-van order produced 50,000+ vans — [Wikipedia: Rivian](https://en.wikipedia.org/wiki/Rivian)
- Government progress payments and advance purchase: NASA covered ~40-50% of SpaceX's first decade; Operation Warp Speed pre-paid manufacturing before approval — [Wikipedia: History of SpaceX](https://en.wikipedia.org/wiki/History_of_SpaceX); [Wikipedia: Operation Warp Speed](https://en.wikipedia.org/wiki/Operation_Warp_Speed)
- Crowdfunded pre-sales as launch capital: Bambu Lab's ~US$7M — [Wikipedia: Bambu Lab](https://en.wikipedia.org/wiki/Bambu_Lab)

### Inferences
Proposed rubric (score each candidate business; examples are from the evidence above):
1. **Who pays before the factory exists?** Cash prepayment or progress payments (SpaceX/NASA, OWS, Amazon/Rivian) = pass. LOIs, reservations under ~$1,000, "binding" orders with no deposit = fail.
2. **Can the first product ship through existing contract manufacturing?** Yes (Framework, Bambu) = 18-24 months on <$50M. Needs own plant = add $100M-$1B and 3-5 years.
3. **Is there a certification gate longer than the runway?** Type certification, new building systems, medical device classes historically took 8-10+ years (Zipline, Lilium). Fail unless selling into an existing certified pathway or a government waiver.
4. **Is the Chinese equivalent legally excluded from this buyer?** Yes (defense, new foreign drones, connected vehicles from MY2027) = pricing umbrella exists. No = assume a 30-67% price disadvantage and negative-margin competitors.
5. **Is the product better, not just cheaper?** Winners sold capability (reusable launch, autonomous systems, repairable laptop, fast multicolor printer). "Same thing, cheaper" lost to stigma or to incumbents with distribution (Nano, manufactured homes).
6. **Is installation, service or financing the real cost?** If the factory share of delivered cost is small (housing, storage systems, home energy), a production breakthrough moves the end price little.
7. **Does the plan survive losing its subsidy or tariff within three years?** US clean-tech support reversed in three.

Applying the rubric adversarially to likely opportunity classes:
- **Factory-built housing / prefab:** strongest case against. Fifty years of cheaper product stuck at ~9-10% share; Katerra, Veev, Entekra, Blu, and Boxabl's 2026 numbers. Works only if the founder owns land, entitlement and financing (is a developer) and treats the factory as a cost centre, or sells components to existing builders.
- **Cheap EVs / vehicles:** Tier C capital, a decade of losses even for survivors, and China is ~15% cheaper before tariffs. Works only inside the legal wall (connected-vehicle rule), in a niche incumbents ignore, with $1B+ (Slate is the live test; watch its conversion from preorder to delivery in 2027).
- **Batteries, solar, commodity energy hardware:** value has already been competed away; top Chinese firms post negative gross margins. Works only as a PFE-compliant supplier with contracted offtake, or downstream (deployment, software, service) where margins sit.
- **Humanoid / general robots:** Chinese price point is already ~$16K with a profitable producer; Western demand per site is unproven. Works as a narrow application sold on uptime guarantees, or as a US-compliant supplier to defense and critical infrastructure.
- **eVTOL / new aircraft:** certification outlasts cash. Works only for defense or uncrewed cargo with a government customer.
- **Defense and security hardware (drones, munitions, components):** best fit to the rubric (protected market, paying customer, capital available), but crowded, increasingly dominated by $1B+ rounds, single-buyer risk, and DoD deliberately splits awards. Works for a focused component or subsystem supplier with production contracts, not for another prime.
- **AI-automated contract manufacturing:** capital is abundant but no operating proof is public; competing with a $7.9B-valued Hadrian on capex is not a seed-stage game. Works as software and process sold into existing shops, or a single narrow process with a named anchor customer.
- **Differentiated consumer and prosumer hardware via ODMs:** the only class with repeated sub-$50M successes in the evidence. Limited by tariffs and by Chinese fast followers; durable only with brand, community or software attached.
- **Indoor farming and other energy-bound production:** physics-bound; fails without near-free energy.

Bottom line for the writer: discount any "massive latent demand" figure by (a) the share of delivered cost that is not manufacturing, (b) the legal availability of Chinese supply, (c) the conversion rate appropriate to the type of demand evidence offered, and (d) the capital tier. The businesses that survive the filter look less like "the Ford of X" and more like "the supplier, certificate holder or demand owner in a protected or underserved niche, renting production wherever it is cheapest allowed."

### Gaps
- SBIR-to-production and OTA conversion rates (the defense "valley of death"): not retrieved; no number should be quoted from this note.
- Hyperscaler prepayment examples (e.g. for power or cooling hardware) and Base Power or Crusoe capital figures: not retrieved.
- Median time and capital to first revenue for hardware seed companies (PitchBook/Crunchbase cohort data): not retrieved; the tiers above are built from named cases, not a statistical sample, and suffer from survivorship and notoriety bias.
- Slate's reservation count and conversion are not yet known; this is the single most useful 2027 datapoint for the cheap-vehicle thesis.
