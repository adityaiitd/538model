# Time-to-power: stranded energized sites (5-100 MW) for AI compute — broker/aggregator viability (as of Nov 23, 2026)

Reading notes for the report writer:
- All figures are from web research on Nov 23, 2026. Items marked **[unverified]** come from a single secondary source, a search snippet, or a vendor page and were not checked against a primary filing.
- The amcompute.com lease tracker is compiled by a vendor with a commercial interest in miner financing; it is internally inconsistent in places (says 16 signed leases, table shows 15). Use it as a pointer to SEC filings, not as a primary source.
- $/kW-month figures derived from $/MW-year are my arithmetic (divide by 12,000).

## 1. Scale of the bottleneck in 2026 (queues, vacancy, rule changes)

### Takeaway
The scarcity is real and measurable: primary-market vacancy is 1.4%, >80% of capacity under construction is pre-leased, and ERCOT alone tracks 410-474 GW of large-load requests. But the 2025-2026 rule changes (ERCOT Batch Zero, SB6, PJM IRAS, FERC show-cause orders, SPP HILL) are all aimed at loads of 50-75 MW and up, and most queue volume is unstudied or speculative — so "the queue" overstates firm demand and says little about sub-50 MW sites.

### Cited Findings
**Vacancy and pre-leasing**
- Primary-market vacancy fell to a record 1.4% in H1 2026 (1.6% a year earlier); Northern Virginia about 0.2% (0.24%), with all 2026 deliveries committed; Chicago 2.2% — [CBRE H1 2026](https://www.cbre.com/insights/books/north-america-data-center-trends-h1-2026)
- More than 80% of capacity under construction is pre-leased (74.3% a year earlier); under 1,500 MW remains available, roughly six months of demand at current pace — [CBRE press release](https://www.cbre.com/press-releases/north-american-data-center-demand-continues-to-outpace-supply-despite-record-construction); [Data Center Frontier](https://www.datacenterfrontier.com/site-selection/news/55401462/cbre-record-data-center-construction-fails-to-ease-capacity-crunch)
- Tenants now commit 18 months to three years ahead of need ("we've gone from a just-in-time industry to having to pre-commit two years in advance" — Jennie Karnes, CBRE) — [Bisnow](https://www.bisnow.com/news/national/top-talent/powerbrokers20how20data20center20leasing20became20a20more20complicated20calculation0a-125519)

**Hyperscaler statements and capex**
- Combined 2026 capex plans of Microsoft, Alphabet, Amazon and Meta were pegged at about $725B after Q1 2026 earnings (Microsoft $190B calendar 2026; Meta $125-145B; Amazon $200B) — [Yahoo Finance](https://finance.yahoo.com/markets/article/magnificent-7-earnings-rush-reveals-ai-spending-surge-with-hyperscaler-capex-set-to-reach-725-billion-in-2026-224901707.html); [Tom's Hardware](https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion)
- Microsoft expects to stay capacity-constrained through at least 2026; Nadella and Jassy described Q4 2025 capacity additions in gigawatts of power rather than servers — [S&P Global](https://www.spglobal.com/energy/en/technology-ai-research-insights/blogs/hyperscaler-earnings-quarterly-what-price-inference)
- Core Scientific CEO (May 2026): behind-the-meter generation at hyperscaler sites has gone from "very low double digit" share to more than 50% of site power; medium-voltage switchgear lead time about 100 weeks, gensets about 14 months — [The Energy Mag](https://www.theenergymag.com/news/2026-05-29/core-scientific-ai-construction-cost)

**ERCOT and SB6**
- ERCOT tracked about 410 GW of large loads seeking interconnection, ~87% data centers (spring 2026) **[figure relayed via search summary of ERCOT materials]** — [ERCOT Large Load Update, Apr 2026](https://www.ercot.com/files/docs/2026/04/01/ERCOT_LargeLoad_Update_April2026_B-C_-Hearing.pdf)
- Large-load applications of 445.8 GW through 2033, of which 321 GW had no studies submitted — [ERCOT Monthly, June 2026](https://www.ercot.com/files/docs/2026/07/10/ERCOT-Monthly-June-2026-FINAL.pdf)
- Texas ordered an audit of about 474 GW of proposed large-load connections — [CryptoSlate, Nov 1 2026](https://cryptoslate.com/ai-wants-bitcoin-miners-power-but-the-contracts-reveal-who-really-gets-paid/); [Utility Dive](https://utilitydive.com/news/ercot-texas-puc-data-center-audit/828472)
- ERCOT received 225 new large-load requests in 2025 against a process built for 40-50 projects — [abc13 / Texas Tribune](https://abc13.com/story/data-centers-seek-tap-texas-energy-regulators-are-close-approving-new-vetting-requests/19322360/)
- "Batch Zero" approved by PUCT June 18, 2026; study deadline July 10, classification notices Aug 7; Batch 1 applications open summer 2027 — [Lloyd Gosselink](https://www.lglawfirm.com/ercot-develops-new-batch-study-process-for-large-load-interconnections/)
- About 205 GW was eligible for Batch Zero — [ERCOT Senate testimony, July 29 2026](https://www.ercot.com/files/docs/2026/07/29/ERCOT-Senate-July-29-Panel-1-Assessing-The-Grid.pdf). Enverus reports 204 projects / 66.4 GW conditionally classified as base load and 158 projects / 125.4 GW as studied load — [Enverus](https://www.enverus.com/newsroom/established-operators-lead-ercot-large-load-queue/); its own pre-deadline estimate was only 55 projects / 21.7 GW — [Enverus](https://www.enverus.com/newsroom/ercot-large-load-batch-zero-readiness/) (conflict not reconciled)
- SB6 draft rule (16 TAC §25.194, published Mar 12 2026): applies to new interconnections of 75 MW or more; study fee $100,000 for 75-250 MW and $300,000 above 250 MW; site control required; PUCT approval required for net-metering between new ≥75 MW loads and existing stand-alone generators; utilities must be able to curtail new transmission-voltage large loads — [Greenberg Traurig](https://www.gtlaw.com/ar/insights/2026/3/texas-senate-bill-6-update-what-data-centers-large-load-customers-should-know-about-proposed-interconnection-standards); [Foley](https://www.foley.com/insights/publications/2026/03/public-utility-commission-of-texas-issues-proposed-rules-for-large-load-interconn/); [Bracewell](https://www.bracewell.com/resources/texas-senate-bill-6-ushers-in-major-overhaul-of-large-load-interconnection-and-grid-access-rules/)

**PJM**
- PJM forecast about 32 GW of peak growth 2024-2030, ~30 GW from data centers; prospective large-load additions up to 70 GW by 2038 — [Data Center Frontier](https://www.datacenterfrontier.com/energy/article/55397507/pjms-new-data-center-power-equation)
- The 2027/28 capacity auction cleared 6.6 GW below the reliability target at the price cap; PJM filed a Reliability Backstop Procurement on July 31, 2026 for a 6,831.3 MW shortfall from the 2028/29 auction — [Utility Dive](https://www.utilitydive.com/news/pjm-backstop-capacity-auction-ferc-data-centers/826792/); [POWER](https://powermag.com/pjm-widens-response-to-data-center-load-as-capacity-shortfalls-deepen)
- Interim Resource Adequacy Service (renamed "connect and manage"): from June 1, 2027, new large loads that do not bring capacity can connect but are exposed to curtailment — [Data Center Knowledge](https://www.datacenterknowledge.com/energy-power-supply/pjm-says-ai-data-centers-must-bring-capacity-to-earn-firm-service)
- CBRE's read: PJM reform offers "no near-term relief" — [CBRE](https://www.cbre.com/insights/reports/pjm-large-load-reform-heats-up-with-dueling-announcements-no-near-term-relief)

**FERC**
- DOE issued its ANOPR on Oct 23, 2025 (docket RM26-4). FERC did not issue a final rule; on June 18, 2026 it issued six show-cause orders (one per RTO/ISO) covering large loads above 50 MW, requiring tariff revisions or a defence, plus generation-adequacy reports in 30 days. The orders make no final findings — [Willkie](https://www.willkie.com/publications/2026/06/ferc-directs-grid-operators-to-reform-procedures-for-large-loads-connecting-to-the-bulk-transmission); [Orrick](https://www.orrick.com/en/Insights/2026/07/FERC-Show-Cause-Orders-Signal-Broad-Reform-to-Large-Load-Interconnection-Policies); [FERC](https://ferc.gov/news-events/news/ferc-launches-aggressive-targeted-action-speed-large-load-integration-across)
- PJM's response deadline was moved from Aug 17 to Nov 16, 2026, answers due Dec 16, 2026 — [FERC order in EL26-67](https://www.pjm.com/-/media/DotCom/documents/ferc/orders/2026/20260921-el26-67-001.pdf)

**SPP / MISO**
- FERC accepted SPP's High Impact Large Load (HILL) process on Jan 14, 2026: 90-day expedited review for loads paired with generation. HILL threshold is ≥10 MW at ≤69 kV, or any load above 69 kV — [Troutman](https://www.troutmanenergyreport.com/2026/01/ferc-accepts-spps-large-load-interconnection-process/); [Perkins Coie](https://perkinscoie.com/insights/update/new-southwest-power-pool-rule-could-supercharge-industrial-and-data-center)
- MISO's expedited generator track (ERAS) grants agreements within 90 days; a separate large-load track for ≥250 MW loads with contracted generation was pending at FERC — [Utility Dive](https://www.utilitydive.com/news/ferc-miso-spp-fast-track-generator-eras/810343/); [Modo Energy](https://modoenergy.com/research/miso-lars-fast-track-co-located-data-centers)

**Flexible interconnection (Duke)**
- Duke "Rethinking Load Growth" (Feb 2025): 76 GW of new load could be integrated at 0.25% average annual curtailment (85 hours/yr), 98 GW at 0.5% (177 hours), 126 GW at 1% (366 hours), across 22 balancing authorities covering 95% of US load — [Duke Nicholas Institute](https://nicholasinstitute.duke.edu/publications/rethinking-load-growth); [Utility Dive](https://www.utilitydive.com/news/us-grid-headroom-flexible-load-data-center-ai-ev-duke-report/739767/)
- A Sept 2026 Duke deck extends the range to 76-215 GW (215 GW at 5% flexibility) — [Indiana IURC tech conference deck](https://secure.in.gov/iurc/files/Indiana%20Tech%20Conference_Profeta%20Load%20Flex%20ALIGN%20Sept%203%202026.pdf)
- Critique: the study is a planning tool, not an interconnection tool; system-wide headroom does not equal locational relief — [Medium, B. Handshy](https://medium.com/@brianwhandshy/dukes-rethinking-load-growth-study-is-being-misused-in-the-interconnection-debate-b7d3d981e8ca)

**Forecast scepticism**
- Grid Strategies (Feb 2026): aggregated utility forecasts imply ~90 GW of data center load vs ~65 GW benchmark scheduled by 2029 and ~60 GW implied by chip shipments; utility forecasts may overstate by ~25 GW by 2030 — [NASEO presentation, J. Wilson](https://energyoutlook2026.naseo.org/data/energymeetings/presentations/John%20Wilson.pdf)
- Dallas Fed (Mar 2026), via LBNL review: data centers raised wholesale energy prices 2-6% nationally 2021-2025, over 10% in northern Virginia, minimal in ERCOT — [LBNL Large Load Literature Review, Aug 2026](https://eta-publications.lbl.gov/sites/default/files/2026-07/lbnl_lllreview_august_update_final.pdf)

### Inferences
- Sub-75 MW sites in Texas fall under the SB6 threshold, and sub-50 MW loads fall outside the FERC show-cause scope. That is a regulatory advantage for small sites (less process) but also means no fast-track was built for them.
- 321 of 446 GW in ERCOT having no studies is direct evidence that most queue volume is option-hunting, not firm demand.

### Gaps
- No ISO-by-ISO published "wait time in years" for large loads was found; the commonly quoted 3-7 years could not be sourced. CAISO large-load data not found.
- No national GW total of utility large-load queues found for 2026.
- Whether FERC issued a NOPR after June 2026, and whether PJM filed on Nov 16, is unconfirmed.
- Final (adopted) SB6 rule text and fees not confirmed; figures above are from the March 2026 draft.

## 2. Price of power access (powered land, lease rates, conversion cost)

### Takeaway
Rents on miner-conversion leases cluster at $1.4-2.4M per MW-year ($120-200/kW-month), with a clear credit spread: investment-grade tenants pay less, unrated neoclouds pay more. Converting to AI-grade costs $8-15M per MW (Core Scientific now says $11.5-12M), so the energized interconnect is worth a small fraction of the delivered asset. No clean US $/MW price for energized small sites is published.

### Cited Findings
**Lease rates**
- Median across 21 disclosed miner/host AI leases: $1.86M per MW-year (~$155/kW-month). Investment-grade tenants: median $1.68M. Unrated tenants with pending credit support: $2.37-2.43M — [AM Compute tracker](https://www.amcompute.com/bitcoin-miners-ai) **[vendor-compiled]**
- Core Scientific/CoreWeave: base licence fee $100/kW/month, escalating 3.5% a year, 12-year term, tenant pays utilities; credits of up to $1.5M per MW for landlord equipment can halve rent until recovered (~30 months) — [CryptoSlate, Nov 1 2026](https://cryptoslate.com/ai-wants-bitcoin-miners-power-but-the-contracts-reveal-who-really-gets-paid/)
- Retail-style colocation (250-500 kW): record average asking rate $196.25/kW/month at H2 2025, up 6.6% y/y — [CBRE H2 2025](https://www.cbre.com/insights/books/north-america-data-center-trends-h2-2025)
- H1 2026: pricing for 10 MW+ deployments up 9.7% (another CBRE passage says 6.7%; not reconciled); 3-10 MW up 8.3%; Silicon Valley asking $200-275/kW/month — [CBRE H1 2026](https://www.cbre.com/insights/books/north-america-data-center-trends-h1-2026)

**Powered land**
- US data center land purchases about $6B in H1 2026, up 79% y/y (Avison Young) — [Data Center Knowledge](https://datacenterknowledge.com/data-center-construction/ai-data-center-land-buying-hits-6b-as-power-premiums-rise)
- Altus (80 US transactions): land near substations prices at ~2x baseline, on high-voltage lines ~2.4x; median ~$28,000/acre where committed load is limited vs $100,000-460,000/acre in growing markets with power — [Altus Group](https://www.altusgroup.com/insights/powered-land-how-utility-commitment-prices-data-center-sites/)
- Enverus: modeled value can rise more than 20-fold from raw screened land to energized capacity; only 4 of 28 reviewed deals disclosed capacity with price — [Enverus](https://www.enverus.com/newsroom/eirs-model-shows-powered-land-can-rise-more-than-20-fold-in-value-as-data-center-sites-reach-energization/)
- Land with an executed electric service agreement trades at many times land with only a queue position — [Kidder Mathews](https://kidder.com/trend-articles/when-power-becomes-the-property-the-real-estate-behind-the-ai-data-center-boom/)
- Europe only: grid-powered land €0.8-1.4M per MW; unrisked €0.2-0.7M per MW — [Linklaters](https://www.linklaters.com/insights/thought-leadership/powered-land/powered-land-power-policy-delivery-and-value)
- Aligned's ~$40B buyout implied ~$8M per MW vs ~$3M per MW for listed miners (VanEck's Sigel; late 2025) — [The Block](https://www.theblock.co/amp/post/374754/blackrock-nvidias-40-billion-data-center-deal-values-power-sites-160-above-public-bitcoin-miners)

**Build / conversion cost**
- Mining infrastructure costs ~$0.7-1.0M per MW; AI-grade capacity ~$8-15M per MW (CoinShares) — [Coincub, Aug 2026](https://coincub.com/mining/bitcoin-miners-ai/); [CryptoSlate](https://cryptoslate.com/ai-wants-bitcoin-miners-power-but-the-contracts-reveal-who-really-gets-paid/)
- Core Scientific CEO: ~$8M per MW a few years ago, now $11.5-12M; labor up ~20% y/y, electricians ~30%; hyperscale deals settle at ~12-14% development yield, 10% unlevered yield on cost at the upper end in some cases — [The Energy Mag](https://www.theenergymag.com/news/2026-05-29/core-scientific-ai-construction-cost)
- JLL: global average shell-and-core ~$11.3M per MW in 2026 (from $10.7M in 2025); tenant AI fit-out can add up to $25M per MW — [JLL 2026 Outlook](https://www.jll.com/en-us/insights/market-outlook/data-center-outlook.html)

### Inferences
- At $1.86M per MW-year rent and $11.5-12M per MW capex, gross yield on cost is ~15-16%; at Core Scientific's $1.2M base it is ~10%. The landlord, not the broker, needs the capital, and returns depend on tenant credit.
- The 40-70 cent/kW-month credit spread between IG and unrated tenants is the market's price for the main risk in small-site deals: small sites mostly attract unrated tenants.

### Gaps
- No US $/MW transaction price for energized sub-100 MW sites. A "~$27M per MW for stabilized Northern Virginia AI facilities (CoinShares)" figure appeared in a search snippet but could not be traced to a source.
- No published powered-shell $/kW-month rate for 2026. JLL H1 2026 report not located.

## 3. Bitcoin-miner conversions; is there demand for 5-50 MW sites?

### Takeaway
The conversion wave is large but almost entirely 150-500 MW campuses with investment-grade or backstopped tenants. Only a handful of sub-100 MW deals exist, all with unrated tenants, and only one has disclosed pricing. Demand for 20-90 MW metro inference sites is rising by practitioner testimony, but evidence for 5-20 MW rural stranded sites is thin and mostly vendor claims.

### Cited Findings
**Large deals (vendor tracker; verify against filings)**
- 23 priced leases, 2024-2026, e.g. TeraWulf/Anthropic 401 MW, $19B, 20 yr (Jul 2026); Hut 8 Beacon Point 352 MW x2, $9.8B each, 15 yr; Riot Rockdale 191 MW, $9.1B, 20 yr (Aug 2026); Cipher/AWS 216 MW, $5.5B, 15 yr; Hut 8 River Bend 245 MW, $7B, 15 yr, Fluidstack with Google backstop; Core Scientific/CoreWeave 390 MW, $6.7B, 12 yr; Galaxy Helios/CoreWeave 526 MW, 15 yr — [AM Compute tracker](https://www.amcompute.com/bitcoin-miners-ai)
- TeraWulf/Anthropic 401 MW and ~$19B, and Hut 8's Google-guaranteed River Bend lease, corroborated — [Coincub](https://coincub.com/mining/bitcoin-miners-ai/)
- Miners have announced >$100B of AI deals, but only ~550 MW was billing out of >4 GW contracted (Nov 2026) — [CryptoSlate](https://cryptoslate.com/ai-wants-bitcoin-miners-power-but-the-contracts-reveal-who-really-gets-paid/)
- Core Scientific Q2 2026: $136.7M colocation revenue of $164.2M total; 437 MW billing by mid-July; H1 capex $954.2M; $3.3B secured notes at 7.75% (May 2026); late-delivery credits $20,000-30,000 per day; uncapped completion guarantee on financed projects — [CryptoSlate](https://cryptoslate.com/ai-wants-bitcoin-miners-power-but-the-contracts-reveal-who-really-gets-paid/)
- Hut 8 Beacon Point: $4.25B senior secured notes rated Baa2, non-recourse — [Coincub](https://coincub.com/mining/bitcoin-miners-ai/)

**Sub-100 MW deals**
- WhiteFiber NC-1: 40 MW, Nscale, $865M, 10 yr, $2.16M per MW-year, no credit backstop (Dec 2025). Hyperscale Data: 28 MW with an unnamed California neocloud, no pricing. Digi Power X: 55 MW pipeline with Cerebras, no pricing — [AM Compute tracker](https://www.amcompute.com/bitcoin-miners-ai)
- Riot signed a 25 MW lease with AMD at a Texas mine conversion **[headline only]** — [DCD](https://datacenterdynamics.com/en/news/riot-to-convert-cryptomine-site-in-texas-to-hpc-signs-25mw-lease-with-amd/)
- Core Scientific is building a 70 MW data center for CoreWeave in Muskogee, next to a 600 MW Google site — [The Energy Mag](https://www.theenergymag.com/news/2026-05-29/core-scientific-ai-construction-cost)
- Keel (ex-Bitfarms): 18 MW Washington site engineered for 190 kW/rack is under 1% of its 2.2 GW pipeline; Bitdeer dismantled a 2018 mine in Wenatchee for a 13 MW AI facility due late 2026-early 2027 — [Coincub](https://coincub.com/mining/bitcoin-miners-ai/)
- Soluna paid $16.5M for remaining equity in 25 MW Dorothy 1A; conversion of the ~100 MW campus expected to take about two years, marketing to AI tenants by end-2026, energization end-2027; no tenant or capex disclosed — [The Energy Mag](https://theenergymag.com/news/2026-04-17/soluna-bitcoin-ai-dorothy)

**Small and private miners**
- Of 51 tracked miners/hosts, 15 have signed leases; 27 have no AI tenant (14 "announced, no tenant", 6 "exploring", 7 mining only). Lancium is the only private company with a signed lease — [AM Compute tracker](https://www.amcompute.com/bitcoin-miners-ai)
- Mid-sized operators running tens of MW are "too large to treat mining as a side business, but too small to finance a serious AI conversion on institutional terms" (opinion, CEO of mining pool EMCD) — [HackerNoon, May 2026](https://hackernoon.com/the-great-pivot-in-mining-inside-the-miner-to-gpu-migration)
- Listed miners' weighted cash cost ~$75,500 per BTC in Q2 2026 vs a quarter-end price of ~$58,400 (CoinShares); 15-20% of the global fleet runs at a loss; hashprice ~$28-30/PH/day — [Digital Today](https://www.digitaltoday.co.kr/en/view/103917/bitcoin-miners-exit-mining-as-funds-flow-into-ai-and-hpc); [HackerNoon](https://hackernoon.com/the-great-pivot-in-mining-inside-the-miner-to-gpu-migration)
- Keel shut its last mining sites June 29, 2026 — [Cryptopolitan](https://www.cryptopolitan.com/bitcoin-miners-shut-off-hashing-for-ai-cash/)
- The number of North American mining sites that clear the AI bar without a legacy power contract is "small, and shrinking" — [Coincub](https://coincub.com/mining/bitcoin-miners-ai/)

**Demand for small sites**
- "We've definitely seen the spike in 20 MW to 90 MW" (J. Rudin, Mintz); Legacy Investing focusing on 20-90 MW; Harrison Street says 30-50 MW can be delivered near population centres on grid power in reasonable time; utilities welcome 50-80 MW asks; infill sites (former manufacturing, steel, refining) with existing connections come online quickly — [Bisnow, May 17 2026](https://www.bisnow.com/news/national/data-center-development/whale-hunting-bragawatts-era-data-center-development-ending-134612)
- Equinix: inference was 60% of new bookings in the prior quarter — [Bisnow](https://www.bisnow.com/news/national/data-center-development/whale-hunting-bragawatts-era-data-center-development-ending-134612)
- "There's going to be this last-mile piece, which is going to be 20-to-50-megawatt inference design locations" — [Bisnow](https://www.bisnow.com/national/news/data-center/last-mile-data-centers-ai-adoption-is-pushing-data-centers-to-the-edge-129605)
- Hitachi Energy's taxonomy: regional inference hubs 20-100 MW; edge nodes under 10 MW — [Hitachi Energy](https://www.hitachienergy.com/news-and-events/blogs/2026/06/ai-data-centers-2030-2035-the-power-shift)
- Moonshot Energy / QumulusAI / IXP.us: 2 MW pods, first at Wichita State by July 2026, 25 sites planned, 125 identified; no customers or prices named — [Data Center Knowledge, Jan 2026](https://www.datacenterknowledge.com/modular-data-centers/firms-launch-ai-pods-for-smaller-us-cities-inference-needs)
- Stranded-power sites typically offer 15 kW-10 MW (Dell); substations average ~5 MW nominally available, max 20 MW (IEEE Spectrum) — [Dell](https://www.dell.com/en-us/blog/powering-ai-modular-data-centers-can-unlock-stranded-power/); [IEEE Spectrum](https://spectrum.ieee.org/amp/distributed-inference-data-centers-2676675952)

### Inferences
- The stated small-site demand is for metro-adjacent infill (latency, network density). Most stranded miner sites are rural and chosen for cheap interruptible power, which is the opposite profile.
- Listed miners with GW pipelines treat sub-25 MW sites as rounding errors. That leaves an orphan class, but also suggests the big players judged them not worth the effort.

### Gaps
- No data on what happened to small private miners' sites (sales, $/MW, closures); no transaction comps found.
- No evidence of named tenants signing multiple 5-20 MW rural sites as a programme. Could not verify neocloud site-size preferences (ABI data paywalled).

## 4. Who already does this — is it crowded?

### Takeaway
Yes at both ends: well-funded powered-land developers work at GW scale, and a second wave of venture-backed "find idle grid capacity" software and flexibility firms raised large rounds in 2026. Site-screening software is commoditised. The specific niche of brokering sub-50 MW stranded sites has no visible scaled incumbent — but also no visible proof that it is a business.

### Cited Findings
- Cloverleaf Infrastructure: launched with $300M (Sandbrook, NGP); has sold >7 GW of powered land incl. Wisconsin sites for Oracle/OpenAI; pipeline >10 GW; Nvidia took a minority stake Aug 21, 2026 — [Baxtel](https://baxtel.com/news/nvidia-backs-data-center-powered-land-company-cloverleaf); [DCD](https://www.datacenterdynamics.com/en/news/cloverleaf-infrastructure-secures-300m-for-clean-energy-data-center-campuses/); [HPCwire](https://www.hpcwire.com/aiwire/2026/08/21/cloverleaf-partners-with-nvidia-to-accelerate-data-center-infrastructure-development/)
- Tract: bought 343 acres in Morris, IL for ~$51.5M; energization targeted June 2028, 1 GW ramp by 2032 — [Bisnow](https://www.bisnow.com/news/chicago/data-center-capital-markets/data-center-infrastructure-developer-takes-343-acre-chicago-area-swing-132919)
- GridCARE: $64M Series A (May 2026, Sutter Hill), $77.5M total; uses AI to find underused grid capacity — [SiliconANGLE](https://siliconangle.com/2026/05/15/gridcare-raises-64m-speed-ai-data-center-projects/); [Bloomberg](https://www.bloomberg.com/news/articles/2026-05-14/early-nvidia-investor-backs-startup-to-tap-idle-grid-power)
- Emerald AI: $150M Series A at $1.05B valuation, >$220M total; cut AI workload power 25% for three hours in a Phoenix test — [DCVC](https://www.dcvc.com/news-insights/dcvc-co-leads-emerald-ais-150-million-series-a-round-to-transform-data-centers-into-intelligent-grid-responsive-assets); [Fortune](https://fortune.com/2026/03/31/emerald-ai-nvidia-fast-pass-data-center-grid-connects/)
- Marketplaces and screening tools already exist: Baxtel lists powered land, shells and turnkey sites with power, substation, zoning and fiber data — [Baxtel](https://baxtel.com/services/site-selection); Acres — [Acres](https://www.acres.com/data-center); LandGate — [LandGate](https://www.landgate.com/energy-markets/data-centers); Enverus — [Enverus](https://www.enverus.com/solutions/site-and-screen/); PVcase — [PVcase](https://get.pvcase.com/pvcase-standard-for-data-center-feasibility)
- Lancium: 1.2 GW across sites; Soluna: pipeline >4.3 GW — [AM Compute tracker](https://www.amcompute.com/bitcoin-miners-ai); [The Energy Mag](https://theenergymag.com/news/2026-04-17/soluna-bitcoin-ai-dorothy)
- Modular: Crusoe's 3.5 MW Spark unit — [Data Center Knowledge](https://www.datacenterknowledge.com/modular-data-centers/modular-ai-data-centers-gain-ground-as-crusoe-debuts-unit); ECL 35 MW Santa Clara phased from 2.5 MW with behind-the-meter power blocks — [Converge Digest](https://convergedigest.com/ecl-unveils-35mw-flexgrid-data-center-in-santa-clara-to-tackle-ai-power-constraints/?amp=1); typical prefab modules 2-5 MW — [AM Compute](https://www.amcompute.com/blog/modular-data-center-opportunity)
- Lease monetisation already offered: PeerSense advertises buying contracted hyperscale lease cash flows at up to 89% of contracted value — [PeerSense](https://peersense.com/contracted-revenue-sale) **[vendor claim]**
- Brokers: Big Tech "tend to have their own brokers and make their own land and lease deals"; Jim Kerrigan (NADC) describes hyperscalers "digging up farmers' phone numbers" to avoid brokers; JLL's Cvengros reports "pressure to lower commission rates" — [Bisnow](https://www.bisnow.com/news/national/top-talent/powerbrokers20how20data20center20leasing20became20a20more20complicated20calculation0a-125519)

### Inferences
- Data monetisation (c) looks weakest: five-plus funded tools already sell site/power screening data, and GridCARE has utility relationships a broker would lack.
- Module standardisation (b) competes with Crusoe, ECL, Moonshot, Eaton/Siemens and OEMs (Dell, Schneider), all with balance sheets.

### Gaps
- Could not find 2026 information on Paces, Halcyon, Verrus, PowerHouse, Prime, Giga Energy, Sangha, Digital Shovel or Armada in this session. From background knowledge only **[unverified, not sourced]**: Paces and Halcyon sell siting/energy-data software; Verrus (Alphabet/SIP spin-out) builds flexible data centers; Giga and Digital Shovel make mining containers/power gear; Sangha runs behind-the-meter mining at renewables; Armada sells modular edge data centers.
- No published data-center broker commission schedule (% of lease value) found. JLL/CBRE/Cushman do not disclose.

## 5. The catch: why small stranded sites stay stranded

### Takeaway
The energized interconnect transfers; almost nothing else does. Mining sites lack density, redundancy, cooling and firm (non-interruptible) power terms, and conversion needs $8-15M per MW that lenders fund only against a creditworthy lease. A broker without capital or tenant credit to offer controls neither the scarce input nor the financing.

### Cited Findings
- What carries over: interconnection agreement, substation, transmission spur, water rights, fiber, permits, land. What is scrapped: ASICs, racks, cooling, power distribution, often the building — [Coincub](https://coincub.com/mining/bitcoin-miners-ai/)
- Mining halls run a few kW per rack; AI needs 142 kW (GB300 NVL72) to 190 kW per rack with liquid cooling; mining curtails for revenue, AI leases carry service credits and concurrent-maintainability requirements — [Coincub](https://coincub.com/mining/bitcoin-miners-ai/); [CryptoSlate](https://cryptoslate.com/ai-wants-bitcoin-miners-power-but-the-contracts-reveal-who-really-gets-paid/)
- GPU clusters need low-latency, high-bandwidth fabrics and cloud-grade operations that mining sites and staff lack — [HackerNoon](https://hackernoon.com/the-great-pivot-in-mining-inside-the-miner-to-gpu-migration)
- Landlord carries the risk: Core Scientific borrows, builds, pays $20-30k/day late penalties and gives uncapped completion guarantees; one ground lease is contingent on the underlying power agreement staying in force — [CryptoSlate](https://cryptoslate.com/ai-wants-bitcoin-miners-power-but-the-contracts-reveal-who-really-gets-paid/)
- Large-load tariffs reach small sites: AEP Ohio's data center tariff applies at 25 MW and above — minimum bill 85% of contracted capacity, up to 12 years incl. 4-year ramp, exit fee of three years' minimum charges, collateral for weaker credits — [AEP Ohio](https://www.aepohio.com/company/about/rates/data-center-tariff); [Utility Dive](https://www.utilitydive.com/news/Ohio-regulators-approve-aep-data-center-interconnection-rules/752690/)
- No exclusivity norm: providers negotiate for months without granting exclusivity; commercial proposals expire in 30 days — [Bisnow](https://www.bisnow.com/news/national/top-talent/powerbrokers20how20data20center20leasing20became20a20more20complicated20calculation0a-125519)
- Tenant credit: "neoclouds are WeWork 2.0" (Haynes Boone chair, July 2026) — [Haynes Boone / Bisnow](https://www.haynesboone.com/news/articles/moerdler-in-bisnow-booming-ai-startups-concern-some-data-center-executives.pdf); Gartner projects ~80% of neoclouds lose independence by 2030 — [CRN Asia](https://www.crnasia.com/news/2026/cloud/gartner-80-of-neoclouds-to-lose-independence-by-2030-as-ai)
- Counterpoint: smaller projects draw a much larger pool of lenders and equity; smaller urban-edge sites seen as lower risk because they can be repurposed — [Bisnow](https://www.bisnow.com/news/national/data-center-development/whale-hunting-bragawatts-era-data-center-development-ending-134612)

### Inferences
- Disintermediation risk is structural: both sides are few, sophisticated and already in-market; hyperscalers bypass brokers by policy; and with no exclusivity norm, an introduction is hard to protect without a signed fee-tail agreement before disclosure.
- Change-of-use risk is real but unquantified: a miner's interruptible or legacy rate does not automatically become firm AI-grade service, and a 25 MW threshold tariff like AEP's can attach take-or-pay obligations on conversion.

### Gaps
- No source quantified how many small sites fail on fiber, zoning or utility change-of-use rules. No data on broker fee tails or disintermediation disputes in data center deals.

## 6. Licensing and regulatory status

### Takeaway
Earning a commission on a lease or site sale generally requires a state real-estate broker licence, with narrow and state-specific "finder" exceptions that vanish once the intermediary negotiates. Forming an entity takes days; lawfully collecting success fees across many states does not, unless the firm partners with licensed brokers or is paid as a consultant on non-contingent terms. Reselling electricity is a separate, state-by-state utility question.

### Cited Findings
- Paying a finder's or referral fee to an unlicensed person is prohibited fee-splitting in Idaho — [Idaho Real Estate Commission Guideline 10](https://dopl.idaho.gov/wp-content/uploads/2023/11/REC-Guideline-10-rev-03.19.pdf); Arizona guidance is similar — [ADRE](https://azre.gov/node/561)
- California recognises a finder's exception limited to introductions — [California AG Opinion 94-909](https://www.oag.ca.gov/system/files/opinions/pdfs/94-909.pdf)
- New Hampshire court denied a commission to an unlicensed individual — [NAR case summary](https://www.nar.realtor/legal-case-summaries/no-commission-for-unlicensed-individual); D.C. refused to enforce finders' agreements (1995) — [Arnold & Porter](https://www.arnoldporter.com/en/perspectives/publications/1995/06/dc-refuses-to-enforce-finders-agreements)
- Maine (2006 review): anyone, licensed or not, could engage in commercial leasing brokerage **[old; may have changed]** — [Maine Legislature](https://lldc.mainelegislature.org/Open/Rpts/hd278_m34_2006.pdf)
- Colorado lets a licensed broker pay a referral fee to an out-of-state licensed broker — [Colorado DRE](https://dre.colorado.gov/sites/dre/files/documents/Commission%20Position%2002%20-%20Broker%20Commissions.pdf)
- Electricity: if the data center consumes and does not resell, it is a state-jurisdictional retail sale; resale or surplus to the grid can trigger FERC sale-for-resale jurisdiction — [Mondaq](https://www.mondaq.com/unitedstates/utilities/1786360/structuring-behind-the-meter-generation-to-manage-ferc-jurisdiction)
- Many vertically integrated states bar third-party retail service via exclusive franchise territories; FERC declined to interpret Maryland's master-meter law in a co-location dispute — [Nelson Mullins](https://www.nelsonmullins.com/insights/alerts/megawatt-minute/all/bring-buy-or-build-state-utility-laws-may-complicate-data-center-power-procurement-strategies); [Steptoe](https://www.steptoe.com/en/news-publications/purpa-and-distributed-energy-resources-blog/retail-sales-to-behind-the-qf-meter-load-and-the-co-located-load-debate.html)
- States are legislating behind-the-meter rules for data centers into 2027 sessions — [MultiState](https://multistate.us/insider/2026/10/13/state-lawmakers-look-to-behind-the-meter-policies-for-data-centers)

### Inferences
- A pure arranger that never takes title to power avoids FERC/retail-provider issues. The "spread" model (lease the site, sublease to the tenant with power pass-through) moves the firm toward landlord and possibly reseller status, with state-specific exposure.

### Gaps
- No 50-state survey located; no authority specific to data-center leases or to "powered land" where the value is an interconnection agreement rather than real property. Whether placement of financing triggers securities broker-dealer registration was not researched. Needs counsel.

## 7. Unit economics examples

### Takeaway
A single 20-50 MW lease has a contract value in the hundreds of millions, so even a fraction-of-a-percent fee is meaningful per deal — but no public source confirms what brokers actually earn, deal counts in this size band are single digits, and timelines from engagement to rent are 1-2+ years.

### Cited Findings
- Only priced sub-100 MW comp: WhiteFiber/Nscale 40 MW, $865M, 10 years ($2.16M per MW-year) — [AM Compute tracker](https://www.amcompute.com/bitcoin-miners-ai)
- Benchmark rents $1.2M (Core Scientific base) to $1.86M (median) to $2.4M (unrated) per MW-year — [CryptoSlate](https://cryptoslate.com/ai-wants-bitcoin-miners-power-but-the-contracts-reveal-who-really-gets-paid/); [AM Compute tracker](https://www.amcompute.com/bitcoin-miners-ai)
- More than a quarter of Core Scientific's colocation revenue is passed-through power ($35.1M of $136.7M) — [CryptoSlate](https://cryptoslate.com/ai-wants-bitcoin-miners-power-but-the-contracts-reveal-who-really-gets-paid/)
- Timeline markers: Soluna expects ~2 years from decision to energized conversion; Bitdeer's 13 MW rebuild targets late 2026-early 2027 — [The Energy Mag](https://theenergymag.com/news/2026-04-17/soluna-bitcoin-ai-dorothy); [Coincub](https://coincub.com/mining/bitcoin-miners-ai/)
- HIVE: a $350M AI agreement needed an estimated $185M hardware build — [CryptoSlate](https://cryptoslate.com/ai-wants-bitcoin-miners-power-but-the-contracts-reveal-who-really-gets-paid/)

### Inferences
- Illustrative TCV (my arithmetic from the cited rents, 10-year term): 20 MW = $240M at $1.2M, $372M at $1.86M, $480M at $2.4M. 50 MW = $600M, $930M, $1.2B. At 15 years the median case is $558M (20 MW) and $1.4B (50 MW).
- Illustrative fee (assumed rates, not sourced): 0.25% of median 10-year TCV is ~$0.9M on 20 MW (~$46k/MW) and ~$2.3M on 50 MW; 1% is ~$3.7M and ~$9.3M (~$186k/MW).
- Conversion capex at $11.5-12M per MW: ~$230-240M for 20 MW, ~$575-600M for 50 MW. The fee is under 2% of the capital someone else must raise.
- Fees are back-ended: with only ~550 MW billing of >4 GW contracted, a fee tied to rent commencement could lag signing by 12-30 months.

### Gaps
- No sourced fee-per-MW for any closed data-center brokerage deal; no sourced LOI-to-close duration; no count of 5-50 MW AI leases signed in the US in 2026.

## 8. Signs of reversal

### Takeaway
As of November 2026 there is no confirmed demand collapse — capex guidance is at records and vacancy at lows — but financing stress around neoclouds, local opposition and take-or-pay tariffs are all intensifying, and each hits small sites with unrated tenants first.

### Cited Findings
- Bloomberg (Apr 2026): nearly half of data center projects planned for 2026 expected to be delayed or cancelled — [Semafor](https://www.semafor.com/article/04/02/2026/us-data-center-buildout-slows-on-supply-hurdles); SemiAnalysis disputes the framing, attributing delays to equipment supply rather than demand — [SemiAnalysis](https://newsletter.semianalysis.com/p/stop-saying-half-of-2026-us-datacenter)
- 61 major AI data center projects cancelled or put on hold over 15 months (Blackridge Research) — [inkl](https://www.inkl.com/news/ai-data-center-boom-falters-as-60-projects-are-scrapped-or-stalled)
- Microsoft walked away from ~2 GW of pending US/Europe leases (TD Cowen, 2025 — dated); Meta and Google reportedly backfilled — [Bisnow](https://bisnow.com/national/news/data-center/microsoft-is-stepping-away-from-more-than-2gw-of-data-center-capacity-128681)
- Microsoft reportedly exited a UK project with Nscale on Oct 19, 2026 **[unverified, single Chinese-language source]** — [Huxiu](https://www.huxiu.com/article/4900743.html?f=rss)
- Oct 2026: short sellers held ~$6B unrealised gains across five AI infrastructure names; CoreWeave fell 4.5% premarket Oct 26 after Musk warned lenders were reluctant to fund AI clouds (Reuters via) — [CryptoSlate](https://cryptoslate.com/ai-wants-bitcoin-miners-power-but-the-contracts-reveal-who-really-gets-paid/)
- Gartner: AI data center owners need ~$8.5T cumulative revenue through 2030 to earn 12% on announced capex; $3.5T of spending at risk — [Network World](https://www.networkworld.com/article/4242389/gartner-warns-3-5t-in-ai-infrastructure-spending-could-be-at-risk-by-2030.html)
- McKinsey: a small fall in GPU rental prices or utilisation below 80% flatlines neocloud returns — [McKinsey](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-evolution-of-neoclouds-and-their-next-moves)
- Local opposition: at least 75 projects worth $130B blocked or delayed in Q1 2026, ~$68B more in Q2 (Data Center Watch) — [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/more-than-75-data-center-build-outs-worth-usd130-billion-have-been-successfully-blocked-in-the-first-four-months-of-2026-bipartisan-opposition-mounts-nationwide-over-fears-of-soaring-power-and-water-costs); [Bloomberg Government](https://news.bgov.com/daily-tax-report/new-data-centers-worth-68-billion-disrupted-in-us-data-show)
- 54 local moratoriums and at least 15 states considering statewide ones (Bipartisan Policy Center); Maine's statewide moratorium vetoed; Prince George's County adopted a two-year moratorium — [E&E News](https://www.eenews.net/articles/coming-to-a-county-near-you-a-data-center-moratorium/); [Governing](https://www.governing.com/infrastructure/data-centers-are-spreading-so-are-moratoriums)
- Take-or-pay tariffs: see AEP Ohio (85% minimum, 12 years, 25 MW threshold) — [POWER](https://www.powermag.com/regulator-approves-aep-ohios-landmark-data-center-tariff/)
- Against reversal: record-low vacancy and rising rents in every size band in H1 2026 — [CBRE H1 2026](https://www.cbre.com/insights/books/north-america-data-center-trends-h1-2026)

### Inferences
- Existing brownfield sites with standing permits may be advantaged by moratoria on new builds — a point in the thesis's favour, though change-of-use approvals are untested.
- A broker's fee income is the most cyclical position in the chain: no asset, no contracted revenue, paid only on closings.

### Gaps
- No Q3 2026 hyperscaler earnings confirmed from primary sources (one outlet says Alphabet held 2026 capex at $195-205B; unverified). No Oct-Nov 2026 GPU rental price index or TD Cowen leasing data found.
