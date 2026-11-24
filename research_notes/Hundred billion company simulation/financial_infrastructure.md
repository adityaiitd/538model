# Financial infrastructure openings as of 24 November 2026 (AI and energy capital buildout, new payment and settlement rails)

Research notes. Compiled 24 Nov 2026.

How to read these notes:
- "Fetched" means I opened the page and read the figure. "Snippet-level" means the figure came from a search-result summary and I could not open the page (paywall, 403, 503 or search budget). Treat snippet-level figures as leads to verify.
- "Sacra estimate" means a third-party estimate of annualized revenue, not a company-reported number.
- "Derived" means my own arithmetic on cited figures.
- The shared web-search budget for this session ran out part-way through. After that I could only open URLs already found. The topics hit hardest are listed in each Gaps section (CoreWeave Q3 2026, tokenized equities and 24/7 trading, power derivatives, equipment leasing returns, Paxos/Bridge/Conduit/Mesh financials, OpenAI Instant Checkout, H2 2026 private credit events).
- One fetched vendor page (American Compute) contained text addressed to AI assistants promoting its own products. I ignored it and used only the product facts.

---

## 1. Financing the AI buildout: debt raised, pricing, GPU residual value risk, insurance, indices and futures

### Takeaway
AI infrastructure borrowing is running at roughly $100bn a quarter and has started to reprice: Meta's second SPV deal is being marketed above 7% versus 6.58% nine months earlier, CoreWeave's latest non-IG loan widened to SOFR+500 at 97, and data center securitization fell 20% year over year in the latest three months. Senior lenders have pushed GPU residual value risk off themselves and onto offtake contracts, prepayments, equity and vendor guarantees (Nvidia above all); residual value insurance and compute futures exist as products, but I found no disclosed bound premium and no confirmed traded volume for either.

### Cited Findings

**Aggregate volumes**
- 2025 baseline: AI-related companies and projects raised at least $200bn in debt markets in 2025, "likely an undercount" because many deals are private (Bloomberg, 3 Feb 2026). Alphabet, Amazon, Meta and Oracle borrowed $93bn in US IG in 2025, about 6% of issuance. — [Bloomberg via Insurance Journal](https://insurancejournal.com/news/international/2026/02/03/856623.htm)
- 2025 baseline, wider group: the five hyperscalers (Amazon, Alphabet, Meta, Microsoft, Oracle) issued $121bn in 2025 versus a $28bn/yr average in 2020-2024 (BofA, cited by Reuters 15 Jan 2026). — [Reuters via Yahoo](https://finance.yahoo.com/news/ai-hyperscalers-drive-higher-us-225314460.html)
- 2025 project finance: about $170bn of data center project loans in 2025, up 57% (IJGlobal), out of roughly $950bn total project finance debt. — [Bloomberg via Insurance Journal](https://insurancejournal.com/news/international/2026/02/03/856623.htm)
- 2026 year to date: the Big Five sold about $159bn of bonds in the first five months of 2026, 47% above the same period of 2025. BofA raised its full-year forecast to $140-175bn; UBS sees $230-240bn cumulative public debt by end-2026. Big Five 2026 capex is projected above $600bn. — [Crypto Briefing, 9 Jun 2026](https://cryptobriefing.com/ai-hyperscalers-159b-debt-issuance/)
- 2026 year to date, second source: about $152bn of hyperscaler gross issuance in the first 4.5 months of 2026, already above all of 2025; about $300bn expected for the year. AI-related debt is roughly 30% of net new USD IG supply and AI-tagged debt about 15% of the US IG market. At least $65bn sits in off-balance-sheet vehicles (BIS "shadow borrowing"). Hyperscaler 2026 capex expectations rose from $296bn (start of 2025) to over $690bn (mid-May 2026). — [IESE Insight, 30 Jun 2026](https://www.iese.edu/insight/articles/ai-credit-market-debt/)
- Conflicting snippet-level figures: one search summary gave hyperscaler issuance of $132bn through July 2026 versus $93bn in all of 2025 (likely the narrower four-issuer scope), and US IG issuance of $2.2tn through September 2026 (Morgan Stanley). A second gave $1.88tn US IG through 4 Nov 2026 (LSEG via Reuters). I could not open either page to reconcile them. — [Morgan Stanley (503 on fetch)](https://www.morganstanley.com/insights/articles/credit-markets-financing-ai-infrastructure); [tech-insider citing Reuters/LSEG (403 on fetch)](https://tech-insider.org/big-tech-us-corporate-bond-record-1-88-trillion-2026/)
- High yield, snippet-level: US high-yield absorbed $31.9bn of new AI-related bonds through 8 July 2026, nearly all for new data centers; headline says total AI-backed bond issuance topped $250bn. — [Morningstar (403 on fetch)](https://www.morningstar.com/bonds/bond-issuance-backing-ai-investment-tops-250b-testing-limits-voracious-investor-demand)
- Pace: UBS strategist Matthew Mish put AI-related debt accumulation at "roughly $100bn a quarter by some estimates" (July 2026). — [Capacity Global, 24 Jul 2026](https://capacityglobal.com/news/metas-12bn-el-paso-bond-exposes-ai-debt-repricing/)
- Private credit: more than $200bn of private credit loans outstanding to AI-related companies; BIS estimates $300-600bn by 2030 (as of Feb 2026). — [Bloomberg via Insurance Journal](https://insurancejournal.com/news/international/2026/02/03/856623.htm)
- Financing need (bank forecast, not a TAM report but still a forecast): Morgan Stanley estimates $2.9tn of global data center capex 2025-2028, of which $1.4tn from hyperscaler cash flow, $200bn corporate debt, $150bn ABS/CMBS, $800bn private credit (asset-based finance and JV debt), $350bn other. — [Structured Finance Association, 23 Jul 2026](https://structuredfinance.org/wp-content/uploads/2026/07/SFA-Research-Corner_How-Data-Center-ABS-and-CMBS-Fit-in-a-Broader-Financing-Ecosystem.pdf)

**Named deals and pricing**
- Meta/Blue Owl Hyperion ("Beignet", Oct 2025): about $30bn total; Morgan Stanley arranged over $27bn of debt with Pimco as anchor, about $2.5bn equity from Blue Owl; Blue Owl owns 80%, Meta 20%. Bonds traded as high as 110. — [Bloomberg via Insurance Journal](https://insurancejournal.com/news/international/2026/02/03/856623.htm)
- Beignet terms, snippet-level: $27.3bn of 6.581% senior secured bonds due May 2049, fully amortizing, priced about 225bp over Treasuries, rated A+ by S&P. — [Fortune, 31 Oct 2025](https://fortune.com/2025/10/31/metas-27-billion-bet-turns-ai-compute-into-wall-streets-hottest-new-investment/); [fourweekmba citing IFR](https://fourweekmba.com/ai-hyperions-27-3b-bond-pays-6-581-above-every-meta-note/)
- Meta's own corporate bond the same week (30 Oct 2025): $30bn, $125bn order book, 30-year at T+98bp, 40-year at T+110bp. — [IESE Insight](https://www.iese.edu/insight/articles/ai-credit-market-debt/)
- Pimco holds about $18bn of the $27bn Hyperion debt. — [Wing VC, Sep 2026](https://www.wing.vc/content/how-the-gpu-became-collateral)
- Meta El Paso ("Project Sopaipilla", July 2026): more than $12bn of bonds marketed by BlackRock for a ~1GW campus due 2028, same 80/20 JV mechanics as Hyperion. Investors were seeking yields "north of 7%". Moody's noted short lease terms and residual value guarantees may not appear as balance-sheet liabilities. — [Capacity Global, 24 Jul 2026](https://capacityglobal.com/news/metas-12bn-el-paso-bond-exposes-ai-debt-repricing/)
- Oracle/Vantage (Stargate, Texas and Wisconsin): $38bn of bank loans. — [Bloomberg via Insurance Journal](https://insurancejournal.com/news/international/2026/02/03/856623.htm). Snippet-level terms: two facilities ($23.25bn Texas, $14.75bn Wisconsin), five-year tenor, about 6.4%, almost 2 points over Oracle's comparable bond, 30+ lenders, 15-year Oracle lease. — [WSJ via iTiger](https://www.itiger.com/news/2582394141)
- Oracle raised about $43bn of debt in fiscal 2026 and was downgraded by S&P to BBB-. Oracle sold $30bn in Feb 2026. — [Capacity Global](https://capacityglobal.com/news/metas-12bn-el-paso-bond-exposes-ai-debt-repricing/); [IESE Insight](https://www.iese.edu/insight/articles/ai-credit-market-debt/)
- Apollo and Blackstone: $35bn chip-backed SPV facility for Anthropic's compute buildout. — [Capacity Global](https://capacityglobal.com/news/metas-12bn-el-paso-bond-exposes-ai-debt-repricing/)
- xAI/Valor Colossus 2: about $20bn SPV of equity and debt to buy Nvidia GPUs and lease them to xAI; Nvidia may invest up to $2bn. xAI's own $5bn bond/loan carried a 12.5% coupon on fixed portions. — [Bloomberg via Insurance Journal](https://insurancejournal.com/news/international/2026/02/03/856623.htm); [Wing VC](https://www.wing.vc/content/how-the-gpu-became-collateral)
- 2025 pricing reference points: IG five-year coupons about 4-4.5%; high-yield data center issuers 7-9%; CoreWeave $3.75bn HY at about 9%; CoreWeave $2.25bn convertible at 1.75% (Dec 2025). — [Bloomberg via Insurance Journal](https://insurancejournal.com/news/international/2026/02/03/856623.htm)

**GPU-backed loans (CoreWeave and peers)**
- CoreWeave DDTL 1.0 (Aug 2023): $2.3bn, reported 11-14% all-in (about SOFR+600-870), reported ~70 cent advance rate against $3bn+ of H100 servers; led by Magnetar and Blackstone. DDTL 2.0 (May 2024): $7.5bn. Unsecured notes (May 2025): $2.0bn at 9.25%. — [Wing VC, Sep 2026](https://www.wing.vc/content/how-the-gpu-became-collateral)
- CoreWeave DDTL 4.0 (Mar 2026): $8.5bn, SOFR+225 with a 5.9% fixed tranche, rated A3/A(low), non-recourse, secured by project assets and one investment-grade customer contract. After customer acceptance, sizing moves to a 1.2x coverage test, which CoreWeave says can support leverage above the equipment's original cost. — [Wing VC](https://www.wing.vc/content/how-the-gpu-became-collateral); [Dave Friedman, 10 Aug 2026](https://davefriedman.substack.com/p/the-market-is-pricing-payment-certainty)
- CoreWeave DDTL 5.0 (2026): $3.1bn, SOFR+450, Ba2/BB+, two non-investment-grade customers, 1.35x DSCR with liquidity reserves and equity cures. — [Dave Friedman](https://davefriedman.substack.com/p/the-market-is-pricing-payment-certainty)
- CoreWeave $2.6bn delayed-draw loan (mid-July 2026, customers include Anthropic, Jane Street, Hudson River Trading): launched at SOFR+425-450 at 99, widened to as much as SOFR+500 at 97; 1.35x DSCR, take-or-pay contracts. CoreWeave's DDTL 3.0 was amended to postpone DSCR testing and allow unlimited equity cures through 28 Oct 2026. — [Dave Friedman](https://davefriedman.substack.com/p/the-market-is-pricing-payment-certainty)
- Peers: Lambda $926m term loan B at SOFR+300, Baa2, fully amortizing to 2030 (Aug 2026); Nebius $775m at SOFR+250 against a Microsoft offtake (Jul 2026, MUFG-led ten-bank group); Fluidstack up to $10bn of Macquarie capacity; Crusoe about $425m via Upper90; IREN $3.65bn IG financing at a 6% blended cost for a Microsoft contract. — [Wing VC](https://www.wing.vc/content/how-the-gpu-became-collateral); [Dave Friedman](https://davefriedman.substack.com/p/the-market-is-pricing-payment-certainty)
- Announced GPU-backed facility capacity exceeds $20bn (CoreWeave $14.2bn, Fluidstack up to $10bn, Lambda $1.4bn, Nebius $775m, Crusoe $425m); this is capacity, not drawn balance. — [Wing VC](https://www.wing.vc/content/how-the-gpu-became-collateral)
- Lender sizing: lenders size neocloud debt at roughly 70-80% loan-to-value against backstopped revenue and test against a DSCR (vendor blog, promotional). — [Parametrix, 10 Aug 2026](https://www.parametrixinsurance.com/blog/who-backstops-the-backstop-the-operational-gap-in-neocloud-financing)

**Who bears residual value risk**
- Senior lenders moved the borrowing base from hardware value to contract cash flow and amortization. Offtakers prepay 15-25% of contract value at signing, acting as first loss. Vendors sell the tail: Nvidia's $6.3bn guarantee of CoreWeave's unsold capacity through 2032, an option to backstop up to $125bn of a $500bn financing platform, and a Residual Value Guaranty of up to $105bn on about 4.25GW of SB Energy data centers for OpenAI. Google backstops $1.8bn of Fluidstack lease obligations at TeraWulf and $1.4bn at Cipher in return for warrants/equity. — [Wing VC](https://www.wing.vc/content/how-the-gpu-became-collateral)
- Nvidia is backstopping a $35bn cloud deal between Lambda and Anthropic (Hut 8's 350MW Texas site), assuming the lease risk; it has offered to backstop financing intended to unlock $500bn from institutions including Goldman Sachs and Apollo. — [Bisnow relaying the FT, 30 Sep 2026](https://www.bisnow.com/news/national/data-center-capital-markets/nvidia-asks-insurers-to-shoulder-financing-risk-for-some-of-its-largest-customers)
- Depreciation and resale assumptions: CoreWeave depreciates over six years, Nebius over four. Estimates put going-concern value of 2-3-year-old hardware at 50-70% of new and orderly liquidation value at 30-50%. Publicly documented used-GPU transactions total only 3,009 listings, 10,911 units and $26.3m over three years (CCIR dataset). — [Wing VC](https://www.wing.vc/content/how-the-gpu-became-collateral)
- H100-class rental rates: about $8/hour (early 2024), $1.70 (Oct 2025), about $2.35 (Mar 2026). — [Wing VC](https://www.wing.vc/content/how-the-gpu-became-collateral)
- KBRA (via a low-reliability aggregator) lists residual value erosion as a top GPU-finance risk and says banks do not expect early-2026 advance rates to recur. — [AI CERTS](https://www.aicerts.ai/news/kbra-spotlight-on-gpu-finance-risks-amid-compute-backed-loan-boom/)

**Residual value insurance**
- Nvidia has been in early-stage talks with insurers, with broker Howden Re, about cover that pays lenders if a neocloud defaults and the chips sell for too little. No insurer named, no agreement, and deals may be too large for one insurer, so risk may be spread to hedge funds. — [Bisnow relaying the FT, 30 Sep 2026](https://www.bisnow.com/news/national/data-center-capital-markets/nvidia-asks-insurers-to-shoulder-financing-risk-for-some-of-its-largest-customers)
- American Compute: GPU residual value insurance for lenders and lessors, placed by Matcha Specialty through the Accelerant Risk Exchange on Incline carriers (A.M. Best A-). No floors, premium rates, capacity or bound deals disclosed. — [American Compute](https://www.amcompute.com/blog/gpu-residual-value-insurance-incline-accelerant)
- Arbol: parametric "GPU Residual Value Protection" launched 19 Nov 2026; pays cash at term end if a GPU rental index is below a client-chosen strike. Capacity backers, pricing and volume not disclosed. — [Artemis.bm, 19 Nov 2026](https://www.artemis.bm/news/arbol-launches-parametric-insurance-for-gpu-residual-value-risk/)
- USD.AI / Barker / Munich Re (4 Mar 2026): Barker's value warranty covers the gap between predicted and realised sale price on defaulted GPU loans in the USD.AI protocol, backed by Munich Re's aiSure via Great Lakes Insurance. Limits, loan volume and premium not disclosed. — [Reinsurance News, 4 Mar 2026](https://www.reinsurancene.ws/usd-ai-barker-launch-insured-gpu-loan-coverage-backed-by-munich-re/)
- Ryan Specialty's Tera Underwriters (6 Aug 2026): property programme for GPUs/ASICs with limits over $1bn per policy on a $625m lead binder. This is physical damage cover, not residual value. — [Reinsurance News, 6 Aug 2026](https://www.reinsurancene.ws/ryan-specialtys-tera-launches-insurance-programme-for-industrial-scale-computing-hardware/)
- Parametrix sells neocloud SLA/downtime insurance, arguing the Nvidia backstop covers price and demand but not uptime. — [Parametrix](https://www.parametrixinsurance.com/blog/who-backstops-the-backstop-the-operational-gap-in-neocloud-financing)

**GPU price indices, forwards and futures**
- CME and Silicon Data announced H100 and B200 Rental Index futures (codes GPU1, GPU2; 730 GPU-hours per contract; cash-settled) for a 5 Oct 2026 trade date "pending regulatory review". — [CME press release, 11 Aug 2026](https://www.cmegroup.com/media-room/press-releases/2026/8/11/cme_group_and_silicondatatolaunchcomputefuturesonoctober5tounloc.html); [CME notice SER-9785](https://www.cmegroup.com/content/dam/cmegroup/notices/ser/2026/08/ser-9785.pdf)
- CME had not named the regulator whose approval it awaited. DRW is CME's trading partner. — [Finance Magnates, 11 Aug 2026](https://www.financemagnates.com/institutional-forex/cme-group-says-it-will-launch-first-regulated-compute-futures-contracts/); [Benzinga via Yahoo, 1 Jun 2026](https://finance.yahoo.com/markets/commodities/articles/compute-oil-cme-intercontinental-launch-131607531.html)
- The CFTC issued a request for comment on compute derivatives in August 2026 (cash market, liquidity, oversight, manipulation). The FIA explainer says the first US exchange launch "is scheduled for November", which conflicts with CME's 5 October date. — [FIA MarketVoice, 23 Sep 2026](https://www.fia.org/marketvoice/articles/explainer-what-are-compute-futures-and-how-do-they-work)
- Other venues: ICE plans futures on Ornn's Compute Price Index (H100, H200, B200) and on NATIVX's energy-normalised COIL index; Nodal (which holds more than half of US electricity futures open interest) partnered with Compute Desk; Architect launched GPU and DRAM rental perpetuals on its Bermuda AX exchange in Jan 2026 with Ornn indices, acquired a CFTC-registered DCM (IMX Health) and plans "The AI Exchange"; BGC launched Compute Infrastructure Markets in June 2026; Kalshi published non-tradable forward curves for B200/H200/A100 in July 2026; Compute Exchange (DRW-backed, launched early 2025) opened a secondary marketplace for older Nvidia GPUs in July 2026. — [FIA MarketVoice](https://www.fia.org/marketvoice/articles/explainer-what-are-compute-futures-and-how-do-they-work); [GARP, 28 Aug 2026](https://www.garp.org/risk-intelligence/technology/cant-get-enough-compute-260828)
- Entrant funding: Silicon Data raised a $30.5m initial Series A close (Aug 2026, Valor Atreides AI Fund) after a $4.7m seed, and claims 500+ clients; it launched a GPU forward curve in April 2026. Ornn raised $33m in June 2026 (a16z lead) after a $5.7m seed in Oct 2025. — [GARP, 28 Aug 2026](https://www.garp.org/risk-intelligence/technology/cant-get-enough-compute-260828)
- Market structure critique: "no deep, transparent secondary market" for compute and no mandatory reporting of physical compute transactions. — [GARP](https://www.garp.org/risk-intelligence/technology/cant-get-enough-compute-260828)
- Silicon Data's residual value product is a DCF off its rental curve; it measures earning value, not recovery value. — [Wing VC](https://www.wing.vc/content/how-the-gpu-became-collateral)

**ABS and CMBS**
- US data center ABS and CMBS issuance was $21.9bn through October 2026, up 7% year over year, but the latest three months were down 20.2% on the same period of 2025 (CREFC, 9 Nov 2026). Outstanding (Barclays, 8 Oct 2026): secured project bonds about $116bn, ABS $44.2bn, CMBS $22.4bn. An SEC staff interpretation in July 2026 put certain data center ABS structures outside the 5% risk retention requirement. — [CREFC release via Webull, 9 Nov 2026](https://www.webull.com/news/15894422686658560)
- Snippet-level split from the same CREFC coverage (not in the fetched text): through 6 Nov 2026, $15.3bn ABS (70%) and $6.55bn SASB CMBS (30%), against $26.9bn for full-year 2025. — [CREFC release via Webull](https://www.webull.com/news/15894422686658560)
- 2025 data center securitization was about $27bn; JPMorgan projected $30-40bn a year for 2026 and 2027. — [Bloomberg via Insurance Journal](https://insurancejournal.com/news/international/2026/02/03/856623.htm)
- Barclays: outstanding data center securitizations grew from $4bn (2020) to $61bn (mid-2026); data center ABS is about 12% of esoteric ABS and data center CMBS about 6% of SASB. Average deal about $600m (ABS) and $1.2bn (CMBS). Select 2026 deals priced from roughly 100bp (AAA ABS) to about 400bp (BB- CMBS) over benchmarks. Equipment-backed (GPU) financings "may emerge as a complementary ABS sector". — [Structured Finance Association, 23 Jul 2026](https://structuredfinance.org/wp-content/uploads/2026/07/SFA-Research-Corner_How-Data-Center-ABS-and-CMBS-Fit-in-a-Broader-Financing-Ecosystem.pdf)
- Trepp: through July 2026, data centers were 9.8% of SASB issuance ($58.0bn) and 7.5% of all private-label CMBS ($76.2bn), from only five loans. — [Trepp via EACCNY](https://eaccny.com/news/trepp-office-deals-led-cmbs-growth-through-july-2026-data-centers-arrived/)

### Inferences
- The SPV premium over the tenant's own credit is large and widening. Beignet priced about 127bp wider than Meta's own 30-year bond the same week (T+225 vs T+98, derived), and the second Meta SPV is being asked for more than 7%. The spread is payment for structure, construction and residual risk that nobody can yet measure.
- Pricing in GPU-backed loans tracks the offtaker's rating (SOFR+225 for an IG customer, SOFR+450-550 for non-IG), not the hardware. That means hardware value is not doing any work in underwriting, and a credible recovery-value product would have to prove itself against almost no transaction history ($26.3m of documented used-GPU sales).
- The real residual value underwriter today is Nvidia's balance sheet. Nvidia seeking insurers suggests its own appetite has limits, and that is the most concrete demand signal for third-party risk transfer in this section.
- Five or more index providers and six or more venues are chasing a compute futures market with no confirmed volume. Index and venue supply exceeds hedging demand at this stage.
- A pure GPU ABS market has not formed. Securitization still finances stabilized, leased buildings.

### Gaps
- I could not confirm that CME's compute futures began trading on 5 Oct 2026 or find any volume or open interest for CME, ICE, Nodal or Architect. CME's product pages timed out or returned 503. No post-launch coverage surfaced before the search budget ran out.
- No premium rates, attachment points, bound limits or claims for any GPU residual value insurance product. No named reinsurer other than Munich Re (through Barker).
- CoreWeave Q3 2026 results (total debt, interest expense, backlog) were not retrieved; the investor site did not render and the search failed on budget.
- Exact advance rates for 2026 facilities are not disclosed in what I read; the 70-80% figure is from a vendor blog.
- I found no rated, term GPU-equipment ABS deal. I cannot say none exists.
- Full-year 2026 totals for hyperscaler and AI-related debt across all markets were not available from an openable primary source; the figures above conflict on scope.

---

## 2. Financing power and industrial equipment: behind-the-meter power, transformers, batteries, leasing

### Takeaway
Behind-the-meter generation is expected to power more than half of new US data centers from 2028, while turbine and step-up transformer lead times have stretched to three to four years and OEM slots are sold into the early 2030s. The financing evidence I found is about procurement and security posting (owners buying long-lead equipment before permits, performance letters of credit), not about a documented shortage of lenders; I found no data on equipment leasing returns or battery financing terms.

### Cited Findings
- SemiAnalysis (25 Jun 2026): BTM "will power well over half of new US datacenters in 2028+"; the BTM equipment market crosses 50GW/yr by 2029; US data center additions go from +21GW in 2026 to +84GW by 2030; US gas additions stay under 10GW/yr in 2026 and 2027. — [SemiAnalysis](https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw)
- Lead times: gas turbines and generator step-up transformers each three to four years versus a historical norm of about 18 months; gas plant development at least four years versus about 24 months. Backup gensets cost about $1m/MW. — [SemiAnalysis](https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw)
- OEM backlogs (1 Apr 2026): GE Vernova had 83GW of gas equipment under firm order or slot reservation entering 2026 (62GW a quarter earlier), targets 100GW by year-end, and prices slot reservations "another 10 to 20 points" above backlog. Siemens Energy has 80GW of gas commitments, 22GW tied to data centers. Delivery slots are filling into the early 2030s. — [POWER Magazine](https://www.powermag.com/full-throttle-five-trends-reshaping-the-gas-power-boom/)
- Named BTM contracts: Atlas Energy Solutions/Caterpillar $840m framework for about 1.4GW of BTM generation through 2029; Babcock & Wilcox/Applied Digital $2.4bn design-build for 1.2GW of gas boilers and steam turbines with an option for 1.2GW more; xAI permitted a 41-turbine plant in Mississippi; Crusoe's Goodnight campus has about 665MW from 19 GE Vernova LM2500s. — [POWER Magazine](https://www.powermag.com/full-throttle-five-trends-reshaping-the-gas-power-boom/); [SemiAnalysis](https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw)
- Procurement shift: owners are buying long-lead equipment directly, sometimes before permits; lump-sum turnkey is giving way to target-price contracts. Seven hyperscalers committed under the White House Ratepayer Protection Pledge to supply their own generation and pay full upgrade costs. — [POWER Magazine](https://www.powermag.com/full-throttle-five-trends-reshaping-the-gas-power-boom/)
- Security posting: Switch closed a multi-billion-dollar performance letter-of-credit facility in 2026; grid-connected developers may need to post letters of credit, deposits or take-or-pay commitments. — [SemiAnalysis](https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw)
- Grid queues: ERCOT has more than 230GW of load requests, 70% data-center driven. PJM's 2026/27 capacity auction cleared at the $329.17/MW-day cap. — [POWER Magazine](https://www.powermag.com/full-throttle-five-trends-reshaping-the-gas-power-boom/)
- Enverus (snippet-level): more than 25GW of new industrial demand served behind the meter by 2030, about 90% data centers; almost all of it from projects that secured turbine slots before waits exceeded five years. — [Enverus](https://www.enverus.com/?p=321637)
- Stranded-asset angle: dedicated substations and generation built for one campus could become underused; Academy Securities suggests stranded-cost securitization may finance recovery of utility investments. — [Structured Finance Association](https://structuredfinance.org/wp-content/uploads/2026/07/SFA-Research-Corner_How-Data-Center-ABS-and-CMBS-Fit-in-a-Broader-Financing-Ecosystem.pdf)
- Delays: an estimated 30-50% of large-scale data center capacity due in 2026 is likely to be delayed (Currence, snippet-level). — [Network World](https://www.networkworld.com/article/4201941/up-to-50-of-data-center-capacity-slated-for-2026-could-be-delayed.html)

### Inferences
- Implied contract prices span a wide range: about $600/kW for the Atlas/Caterpillar framework and about $2,000/kW for the B&W/Applied Digital design-build (derived; scopes differ, so these are not like-for-like).
- The binding constraint is equipment slots, not capital. A financing product only helps if it secures or transfers a slot (deposit finance, slot-reservation finance, lessor-owned fleets of mobile or aeroderivative units).
- Single-campus power assets carry the same tenant-renewal and obsolescence risk as the data center they serve, with less collateral mobility. That argues for mobile or redeployable generation as the leasable asset class.

### Gaps
- No sourced data on equipment leasing structures, lessor returns, lease rate factors or residual assumptions for turbines, engines, transformers or batteries. The search budget ran out before I could query this.
- No sourced data on battery storage project finance terms, tax equity pricing after 2025 legislation, or battery performance warranty insurance volumes.
- No transformer-specific financing data beyond lead times.
- I did not find a quantified "financing gap" for BTM power from a lender, rating agency or filing.
- Bloom Energy, VoltaGrid and Solaris contract and financing terms were not retrieved (S&P article returned 403).

---

## 3. Stablecoins and tokenized assets: volumes, GENIUS Act status, issuer and intermediary economics

### Takeaway
Stablecoin supply stalled in 2026 (USDT about $184bn all year, USDC about $74bn and flat year over year) while transfer volume and payment-network volume kept growing, and issuer income is falling with rates. The OCC's final GENIUS rule takes effect 18 January 2027 with the first deemed approvals for new applicants no earlier than 18 May 2027. The money so far is in reserve yield (kept by Tether, split between Circle and Coinbase) and in acquisition prices of 15-50x revenue for orchestration firms; per-transaction take rates on dollar corridors are 1-15bp.

### Cited Findings

**Supply and transfer volume**
- USDT supply stayed around $184bn through the first three quarters of 2026; Tether's liabilities were $183.5bn at 30 Sep 2026. — [Crypto Briefing, 30 Oct 2026](https://www.cryptobriefing.com/tether-q3-2026-profit-reserve-buffer/)
- USDC in circulation was about $74bn at end-Q3 2026, less than one percentage point above both Q3 2025 and Q2 2026; USDC's share of stablecoins was 27%, down two points year over year. — [FXC Intelligence](https://www.fxcintel.com/research/analysis/ct-circle-q3-2026-earnings)
- Total stablecoin market about $297.3bn with USDT around 60% (DefiLlama, late Oct 2026; snippet-level from Tether Q3 coverage, exact article not re-verified). — [Securities.io](https://www.securities.io/tethers-q3-attestation-shows-1-5b-profit-and-a-nearly-8b-buffer/)
- Visa/Allium adjusted stablecoin transaction volume hit a record $1.79tn in June 2026 (previous high $1.78tn in Feb 2026; May about $1.1tn); USDC about 67% and USDT about 32% of adjusted volume; Base led chains with $565bn (snippet-level). Two reports give H1 2026 adjusted volume of $8.82tn and trailing-12-month volume of about $10.2tn; these do not reconcile and I could not check the dashboard. — [Cointelegraph](https://cointelegraph.com/news/stablecoin-transaction-volume-hits-record-179t-in-june-visa)
- Circle reports USDC on-chain transaction volume of $13.9tn in Q3 2026 (+49% YoY) and mint-plus-redeem volume of $208bn (+42%). — [FXC Intelligence](https://www.fxcintel.com/research/analysis/ct-circle-q3-2026-earnings)
- Stripe's 2025 letter (snippet-level): Bridge volume more than quadrupled in 2025; stablecoin payments volume about $400bn with an estimated 60% B2B. Businesses on Stripe generated $1.9tn in 2025. — [crypto.jobs summary](https://crypto.jobs/news/stripe-s-bridge-platform-reports-4x-growth-in-stablecoin-volume-despite-market-downturn); [Stripe annual letter page](https://stripe.com/annual-updates/2025)
- Stablecoins are under 1% of cross-border payment flows. — [FXC Intelligence](https://www.fxcintel.com/research/reports/ct-mastercard-bvnk-acquisition)

**GENIUS Act implementation**
- The OCC issued its final rule on 21 Oct 2026 (Federal Register 23 Oct 2026); effective 18 Jan 2027, the date the Act takes effect and unlicensed issuance becomes unlawful. — [Gibson Dunn](https://www.gibsondunn.com/the-genius-act-occ-finalizes-its-payment-stablecoin-framework/)
- Reserves: 1:1 at all times; at least 5% in demand deposits or Fed balances; no more than 40% with one counterparty (with exclusions); Treasuries limited to 93 days or less remaining. Capital: minimum $5m, plus assets covering 12 months of expenses. — [Gibson Dunn](https://www.gibsondunn.com/the-genius-act-occ-finalizes-its-payment-stablecoin-framework/)
- Yield: issuers cannot pay interest or yield solely for holding. The final rule dropped the proposed rebuttable presumption against affiliate and third-party reward arrangements but gave no safe harbor; each arrangement is judged on its facts. — [Gibson Dunn](https://www.gibsondunn.com/the-genius-act-occ-finalizes-its-payment-stablecoin-framework/); [Arnold & Porter](https://www.arnoldporter.com/en/perspectives/advisories/2026/10/implementing-the-genius-act-the-occs-final-rule)
- Licensing clock: 30 days for a completeness determination; deemed approval 120 days after a substantially complete application; earliest deemed approval for new applicants is 18 May 2027; pending applicants may seek a waiver of up to 12 months. State issuers above $10bn must move to the federal framework within 360 days or stop net issuance. — [Gibson Dunn](https://www.gibsondunn.com/the-genius-act-occ-finalizes-its-payment-stablecoin-framework/)
- Other agencies: Fed proposals issued 29 Sep 2026 with comments due 30 Nov 2026; FDIC proposal April 2026; NCUA supplemental proposal May 2026; Treasury issuance/offer/sale rules proposed 18 Aug 2026 and a state-certification interim final rule on 30 Sep 2026; FinCEN/OFAC AML proposal April 2026. Treasury has made no foreign-regime comparability determinations. — [Gibson Dunn](https://www.gibsondunn.com/the-genius-act-occ-finalizes-its-payment-stablecoin-framework/)

**Issuer economics**
- Circle Q3 2026: total revenue and reserve income $865m (+17% YoY); reserve income $658m (-7.5%); reserve return rate down 61bp to 3.5%; other revenue excluding Arc down 11% (subscription and services $20m, transaction revenue $5m); $182m from the Arc token presale (21% of revenue). Revenue less distribution costs (RLDC) $453m, a 52% margin; adjusted EBITDA $317m; net income from continuing operations $226m; 5% workforce reduction. — [FXC Intelligence](https://www.fxcintel.com/research/analysis/ct-circle-q3-2026-earnings); [The Block, 4 Nov 2026](https://www.theblock.co/news/business/2026-11-04-circle-reports-865-million-in-q3-revenue-and-reserve-income-discloses-5-percent-workforce-reduction-432671)
- Circle guidance: FY2026 other revenue $310-330m; RLDC margin 41.7-43.7%. — [FXC Intelligence](https://www.fxcintel.com/research/analysis/ct-circle-q3-2026-earnings)
- Circle Payments Network: annualised TPV $41.3bn in Q3 (+181% QoQ), above $58bn by end-October; 205 financial institutions enrolled; fee monetisation has started but is not yet in results, with material revenue expected in 2027. Circle agreed to buy Tazapay for $400m (about $25bn annualised volume, roughly 60% stablecoin). Arc mainnet launched 16 Sep 2026 with over $1bn daily volume. — [FXC Intelligence](https://www.fxcintel.com/research/analysis/ct-circle-q3-2026-earnings)
- Tether Q3 2026: net operating profit $1.5bn (same as Q2), $4.5bn for nine months; total assets $191.45bn; excess reserves $7.95bn; US Treasury exposure $132.4bn; secured loans $14.18bn; precious metals about $19.1bn; bitcoin $8.37bn. — [Crypto Briefing, 30 Oct 2026](https://www.cryptobriefing.com/tether-q3-2026-profit-reserve-buffer/)
- For comparison, Tether reported profits above $10bn for the first nine months of 2025 (headline, 2025 data). — [The Block](https://www.theblock.co/amp/post/377120/tethers-annual-profits-top-10-billion-as-treasury-holdings-swell)
- Coinbase drew about 23% of net revenue from stablecoins in Q1 2026. — [Architect Partners, 17 Jun 2026](https://architectpartners.com/wp-content/uploads/2026/06/Crypto-Payments-Infrastructure-Part-IV.pdf)

**Orchestration and B2B payment firms**
- Mastercard agreed in March 2026 to buy BVNK for up to $1.8bn ($1.5bn plus $300m contingent). BVNK processed $30bn in 2025 (+180%), was valued at $750m in Dec 2024, and holds 25+ licences with 370+ enterprise clients. Coinbase had earlier held exclusivity at a rumoured price of up to $2bn. — [FXC Intelligence](https://www.fxcintel.com/research/reports/ct-mastercard-bvnk-acquisition); [Fintech Blueprint](https://lex.substack.com/p/analysis-mastercard-buys-bvnk-for); [Architect Partners](https://architectpartners.com/wp-content/uploads/2026/06/Crypto-Payments-Infrastructure-Part-IV.pdf)
- BVNK take rate: about 13bp blended per the CEO of m0; the analyst's revenue estimate is $50-150m annualised (10-40bp on $30bn), implying 15-50x revenue. By corridor: FX-premium emerging-market corridors (NGN, ARS, KES) earn 50-150bp, dollar on/off-ramp 5-15bp, stable-to-stable orchestration 1-5bp. — [Fintech Blueprint](https://lex.substack.com/p/analysis-mastercard-buys-bvnk-for)
- Older BVNK figure (snippet-level): about $40m revenue as of late 2024. — [Cryptonews Australia](https://cryptonews.com.au/news/mastercard-bets-big-on-stablecoins-to-bridge-crypto-and-traditional-payments-133409/)
- Other deals: Stripe/Bridge $1.1bn (Oct 2024); Ripple/GTreasury $1.0bn (Oct 2025); Kraken/Reap $600m (May 2026); Polygon Labs/Coinme and Sequence for more than $250m (Jan 2026); OpenPayd SPAC at $1.1bn with more than $240bn annualised volume and 1,100 customers. Crypto payment orchestration accounts for 51 acquisitions and about $6.2bn of disclosed value since 2022. Announced M&A value is up 3x in the past four quarters versus the prior eight; Visa and JPMorgan are "still largely absent" as buyers. — [Architect Partners, 17 Jun 2026](https://architectpartners.com/wp-content/uploads/2026/06/Crypto-Payments-Infrastructure-Part-IV.pdf)
- Private financings in crypto payments peaked at $996m in Q4 2025 and fell to $608m in Q1 2026 and $250m in Q2 2026 (partial quarter, through 12 June); average deal size fell from $13.5m to $7.6m. — [Architect Partners](https://architectpartners.com/wp-content/uploads/2026/06/Crypto-Payments-Infrastructure-Part-IV.pdf)
- Zerohash: Mastercard's reported $1.5-2bn acquisition was abandoned in January 2026; Zerohash then sought $250m at a $1.5bn valuation. A 2025 podcast cited $45bn of volume. — [FXC Intelligence](https://www.fxcintel.com/research/reports/ct-mastercard-bvnk-acquisition); [Fintech Blueprint](https://lex.substack.com/p/analysis-mastercard-buys-bvnk-for)
- Rain was valued at $1.95bn in January 2026, roughly triple five months earlier. — [Forbes Australia](https://www.forbes.com.au/news/innovation/the-50-hottest-fintech-startups-in-2026/)

**Bank tokens and tokenized deposits**
- JPMorgan extended its JPM Coin deposit token (JPMD) from Base (Nov 2025) to Ethereum in October 2026. Kinexys has processed over $4tn cumulatively and averages $7bn a day. JPMorgan launched tokenized money market funds in Dec 2025 and May 2026. — [The Block, 19 Oct 2026](https://theblock.co/news/business/2026-10-19-jpmorgan-jpm-coin-deposit-token-ethereum-418874)
- Citi Token Services was moving close to $1bn a day for hundreds of clients across five locations (Investor Day, May 2026); Japan launch planned for late 2026 (snippet-level). — [Zacks](https://www.zacks.com/stock/news/2987694/c-pushes-tokenized-deposits-deeper-into-asia-with-japan-expansion)
- Consortia (snippet-level, secondary): JPMorgan, Bank of America, Citi and Wells Fargo are building a shared tokenized deposit network through The Clearing House for H1 2027; the Cari Network of regional banks (Huntington, First Horizon, KeyCorp, M&T, Old National) targets a Q4 2026 launch. — [KuCoin news citing CoinDesk](https://www.kucoin.com/news/flash/jpmorgan-citi-and-major-u-s-banks-plan-tokenized-deposit-network-by-2027)

**Tokenized treasuries and funds**
- Tokenized US Treasury products total $14.09bn as of 24 Nov 2026, down 3.89% in 30 days, with 86,527 holders and a 3.68% 7-day APY. Largest products: Ondo USDY $2.38bn, Circle USYC $2.02bn, Franklin iBENJI $1.72bn, BlackRock BUIDL $1.55bn, Franklin BENJI $1.39bn, JPMorgan JLTXX $765m, WisdomTree WTGXX $674m, Invesco USTB $476m, Ondo OUSG $314m. — [rwa.xyz](https://app.rwa.xyz/treasuries)
- Total tokenized real-world assets: $46.3bn per Token Terminal (Treasuries $13.3bn, yield strategies $11.6bn, credit funds $5.7bn) versus about $38-39bn per rwa.xyz, as of late October 2026. — [Crypto Briefing, 26 Oct 2026](https://cryptobriefing.com/tokenized-rwa-market-hits-46-billion/)

### Inferences
- Circle's distribution and transaction costs were about $412m in Q3 2026 (derived: $865m less $453m RLDC). Excluding the one-off Arc presale, RLDC would have been about $271m on $683m of revenue, a margin near 40% (derived). Distribution partners, chiefly Coinbase, keep roughly half of the reserve income.
- Tether's nine-month operating profit of $4.5bn in 2026 against more than $10bn reported for nine months of 2025 points to a sharp fall in issuer earnings as rates fell and mark-to-market gains faded. The two figures may not be defined the same way (net operating profit versus total profit including gold and bitcoin marks).
- BVNK at 13bp on $30bn implies about $39m of revenue (derived), which would make the $1.8bn price roughly 46x. Buyers are paying for licences, enterprise connections and volume, not current earnings. Acquisition by a network or exchange has been the main exit.
- Supply growth has stopped while velocity rises. A business paid on float (issuer) is exposed to rates and flat balances; a business paid on flow earns 1-15bp on dollar corridors, so it needs either emerging-market FX corridors (50-150bp) or very large volume.
- Tokenized Treasuries are small ($14bn) and shrinking month on month. BUIDL at $1.55bn is well below the $2.5bn reported for May 2026 (snippet-level), which fits balances rotating between products with yields, not net new demand.
- The GENIUS timeline creates a dated compliance purchase: every prospective issuer needs reserve operations, attestations, AML programmes and an application package between now and mid-2027.

### Gaps
- Paxos, Bridge (inside Stripe), Conduit and Mesh revenue or margin: nothing retrieved. Sacra pages for Bridge and Zerohash returned 404.
- Number of GENIUS issuer applications filed or in preparation: not stated in the law-firm summaries.
- A November 2026 total stablecoin supply from a primary dashboard: DefiLlama returned 403.
- B2B share of stablecoin volume for 2026 from Artemis or Visa: not retrieved.
- Tokenized equities value and volumes: see section 7 gaps.
- Fee levels charged by tokenized fund issuers and transfer agents (for example Securitize): rwa.xyz fee data is login-gated.

---

## 4. Agentic commerce and machine payments: actual volumes and revenue

### Takeaway
Measured agent-payment volume is tiny. The largest open protocol, x402, has settled about $53m in total since May 2025, roughly half of which survives basic wash screens, and genuinely agent-driven volume is estimated at $5,000-11,000 a month. Visa, Mastercard, Google and OpenAI/Stripe have published partner lists but no transaction volumes. I found no evidence of material revenue for anyone.

### Cited Findings
- TRM Labs (9 Sep 2026): about $52.7m across 198.9m settlement transactions through known x402 facilitators on Base, Solana and Polygon since May 2025; 99.6% in USDC. After removing self-payments, bulk flows from one or two payers and sellers with fewer than ten buyers, $25.62m remains. Between 0.6% and 7.5% of that screened commerce looks agentic. Agent-driven volume is roughly $5,000-11,000 a month. — [TRM Labs](https://www.trmlabs.com/trm-tech-blog/whos-actually-paying-measuring-ai-agent-payments-onchain)
- Visa with Artemis (data as of 21 Apr 2026): x402 adjusted volume about $15.0m across 109.6m adjusted transactions since May 2025. Stripe/Tempo's Machine Payments Protocol settled about $25,000 across roughly 115,000 transactions in its first weeks after a mid-March 2026 launch. — [Visa](https://www.visa.com/en-us/thought-leadership/innovation/agentic-payments-from-the-ground-up)
- Trend: x402 monthly volume fell about 77% from $5.15m (Nov 2025 peak) to $1.19m (May 2026); average transaction $0.52; monthly transactions 2.89m in May 2026. — [CryptoSlate, 27 May 2026](https://cryptoslate.com/tiny-x402-payments-expose-gap-holding-ai-agents-back/)
- American Banker (18 Sep 2026) reports a 93% volume decline in 2026 on one agentic rail after a late-2025 spike. — [American Banker](https://www.americanbanker.com/payments/news/agentic-payment-rail-shows-volume-decline)
- Fee model: Coinbase's facilitator charges $0.001 per transaction beyond a free tier of 1,000 a month. A developer blog estimates real commercial x402 volume at about $5m annualised (low-reliability source). — [DEV Community, 6 May 2026](https://dev.to/kirothebot/the-agent-payment-wars-x402-mpp-and-ap2-what-actually-shipped-in-q2-2026-24mm)
- Governance: x402 moved to a Linux Foundation body in April 2026 with 22 founding members including Visa, Stripe, Mastercard, American Express, Google, AWS and Microsoft. Google donated AP2 to the FIDO Alliance in April 2026; AP2 volume is not disclosed. — [DEV Community](https://dev.to/kirothebot/the-agent-payment-wars-x402-mpp-and-ap2-what-actually-shipped-in-q2-2026-24mm); [CryptoSlate](https://cryptoslate.com/tiny-x402-payments-expose-gap-holding-ai-agents-back/)
- Card networks: Mastercard's CEO said its "first agentic transaction" took place in the quarter to October 2025. Visa said in late 2025 that "hundreds" of controlled agent-initiated transactions had been completed with partners. Stripe's Shared Payment Tokens support Visa Intelligent Commerce and Mastercard Agent Pay (March 2026). No counts or revenue are given. — [Digital Commerce 360, 2 Apr 2026](https://www.digitalcommerce360.com/2026/04/02/visa-mastercard-in-agentic-commerce/); [Visa press release](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-partners-complete-secure-agentic-transactions.html)

### Inferences
- At $0.001 per transaction, all 198.9m x402 transactions to date would have produced under $200,000 of facilitator fees (derived). There is no revenue pool here yet.
- The data supports TRM's conclusion that most on-chain "agent" volume is scripts, tests and token speculation. The unsolved problems named by TRM and CryptoSlate are attribution, approval and compliance, which are services a company could sell, but to buyers who do not yet have volume.
- Consumer agentic checkout through cards will accrue to existing networks and processors; they have set the standards bodies and token formats. A startup's opening is narrow (identity, mandate and dispute tooling) and dependent on incumbents' roadmaps.

### Gaps
- No volume, GMV or revenue for OpenAI Instant Checkout/ACP, Google AP2/UCP, Visa Intelligent Commerce or Mastercard Agent Pay. My searches for 2026 earnings-call disclosures failed on the search budget.
- No Q3 or Q4 2026 on-chain data for x402 or MPP beyond TRM's September figures.
- Skyfire, Nekuda, Catena and similar startups: no financials found.

---

## 5. Insurance and guarantees: AI liability, data center and compute cover, surety

### Takeaway
Insurers began attaching standard generative-AI exclusions to general liability policies from January 2026, and affirmative AI cover remains small (limits of $2-50m, no disclosed premium volume). The larger, better-evidenced shortfall is in physical and project cover: a single hyperscale campus carries $10-30bn of insurable value against typical limits of $1.5-3.5bn, and US-style 100% performance bonds cannot be written for multi-billion-dollar projects.

### Cited Findings

**AI liability and performance**
- Verisk/ISO made three generative-AI exclusion endorsements available for commercial general liability from 1 Jan 2026: CG 40 47, CG 40 48 and CG 35 08. — [Insurance Journal, 17 Aug 2026](https://www.insurancejournal.com/magazines/mag-features/2026/08/17/881424.htm)
- Berkshire Hathaway, Chubb and Travelers sought state approval to exclude AI-related damages from general liability; regulators approved over 80% of requests. W. R. Berkley introduced absolute AI exclusions across D&O, E&O and fiduciary liability. ISO forms underpin roughly 82% of US P&C policies. — [PYMNTS, 1 May 2026](https://www.pymnts.com/artificial-intelligence-2/2026/big-insurance-backs-away-from-ai-risk-and-startups-rush-in/)
- Standalone AI liability policies from Munich Re, Corgi, Armilla, Mayflower Specialty and Embroker carry limits of $2m to $50m; annual premiums range "from a few hundred dollars to several hundred thousand dollars". — [PYMNTS](https://www.pymnts.com/artificial-intelligence-2/2026/big-insurance-backs-away-from-ai-risk-and-startups-rush-in/)
- A broker expects "rapid adoption of some version of an AI exclusion in most lines of coverage", with E&O and D&O first. AI-related lawsuits rose 978% from 2021 to 2025 and 137% from 2024 to 2025 (Gallagher). — [Insurance Journal](https://www.insurancejournal.com/magazines/mag-features/2026/08/17/881424.htm)
- Armilla raised its policy limit to $25m (January 2026; this is capacity, not equity). It became a Lloyd's coverholder in 2024 and launched the policy in April 2025. — [FinTech Global, 23 Jan 2026](https://fintech.global/2026/01/23/armilla-ai-raises-25m-to-expand-ai-liability-coverage)
- AIUC raised a $40m Series A led by Ribbit (September 2026), $55m in total; AIUC-1 certified companies include Cursor, ElevenLabs, Harvey, KPMG, Lovable, UiPath and Fin. — [FinTech Global, 17 Sep 2026](https://fintech.global/2026/09/17/aiuc-raises-40m-to-police-risk-in-frontier-ai-agents/)
- Munich Re's aiSure is being used as the reinsurance behind third-party warranties (for example Barker's GPU value warranty). — [Reinsurance News](https://www.reinsurancene.ws/usd-ai-barker-launch-insured-gpu-loan-coverage-backed-by-munich-re/)

**Data center and compute property, delay and SLA cover**
- S&P estimates about $10bn of new data center premiums in 2026; Swiss Re puts the premium pool at about $10.6bn today and $24.2bn by 2030 (insurer forecasts). — [ENR, 28 Apr 2026](https://www.enr.com/articles/62899-report-billions-of-dollars-in-data-center-construction-risk-is-uninsured)
- Insurable value per hyperscale location is $10-30bn; project sizes went from $1-2.5bn two years ago to $5-25bn. Typical mega-project policy limits are $1.5-3.5bn and only three placements have exceeded $5bn. The insured share of campus value is "only a third, maybe at best half" (S&P). Requiring delay-in-startup cover is the main limiter. — [ENR](https://www.enr.com/articles/62899-report-billions-of-dollars-in-data-center-construction-risk-is-uninsured)
- Broker facilities: Aon's Data Center Lifecycle programme expanded to $3.5bn in April 2026; Marsh's Nimbus facility offers up to $2.7bn including delay-in-startup and business interruption. — [ENR](https://www.enr.com/articles/62899-report-billions-of-dollars-in-data-center-construction-risk-is-uninsured)
- Ryan Specialty's Tera programme: over $1bn per policy for GPU/ASIC hardware on a $625m lead binder. — [Reinsurance News](https://www.reinsurancene.ws/ryan-specialtys-tera-launches-insurance-programme-for-industrial-scale-computing-hardware/)

**Surety and performance security**
- Aon: "There is an inherent upper limit to deployable bonding capacity"; an $8bn project cannot be backed by an $8bn bond. Typical performance bond levels are 100% of contract value in the US, 50% in Canada, 10% in EMEA. Co-surety and syndicated programmes are growing. On-demand instruments tied to power purchase and interconnection agreements can be required within five days and consume significant capacity. — [Aon, 1 Apr 2026](https://www.aon.com/en/insights/articles/performance-security-megaprojects-capacity-clarity)
- Brokers disagree on tightness: Lockton sees a stable contract surety market with no industry-wide shifts expected in 2026 (snippet-level). — [Lockton](https://insights.lockton.com/construction/market-update-feb26/contract-surety)
- Switch closed a multi-billion-dollar performance letter-of-credit facility in 2026. — [SemiAnalysis](https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw)

### Inferences
- The exclusions create a coverage hole first, and demand second. Buyers only pay for affirmative AI cover when a counterparty, regulator or board requires it. The one disclosed premium range (hundreds to hundreds of thousands of dollars per policy) suggests a market in the tens of millions of premium, not billions. That is my inference; nobody has published a total.
- Certification-plus-insurance (AIUC, Armilla) sells the audit as much as the policy. Revenue may sit in assessment fees until loss data justifies larger limits.
- The data center property and delay-in-startup shortfall is measured in billions of limit per project and has paying buyers today. It is a capacity problem, which favours those who can bring capital (reinsurers, ILS, sidecars) over a pure distribution MGA.
- Performance security for power and interconnection obligations is being met with bank letters of credit. Surety-backed or insurer-backed replacements for those LCs are a plausible product, but I found no pricing.

### Gaps
- No gross written premium, loss ratio or policy count for Armilla, AIUC, Munich Re aiSure, Testudo, Corgi or any Lloyd's AI product. Nothing found on Testudo at all.
- No MGA economics specific to these lines (commission rates, profit commission, capacity terms).
- No sourced data on energy performance warranties, battery performance insurance or surety pricing for compute and power projects.
- The count of carrier groups filing AI exclusions ("more than 60") appeared only in a search snippet without an openable source.

---

## 6. Private credit and market structure: growth, stress, data, valuation, secondaries

### Takeaway
The stress in 2026 has been a liquidity and trust event more than a default event: redemption requests at the largest non-traded BDCs averaged 12.1% in Q1 2026 against 5% gates, listed BDCs trade around 0.85x NAV, and reported non-accruals remain low while PIK income rises. The clearest structural response is the credit secondary market, which did $20.4bn in H1 2026 (more than all of 2025), 83% GP-led and 81% intermediated by advisors.

### Cited Findings
- Market size: private credit is $2-3tn; BDC assets $475bn, 65% non-traded; US semi-liquid credit funds grew from $75bn (2022) to $188bn (2024); bank lending to non-depository financial institutions rose from $322bn (2015) to $1.28tn (2025), over half undrawn. — [State Street, Apr 2026](https://www.statestreet.com/us/en/insights/private-credit-stress)
- Redemptions (Q1 2026): requests at the 12 largest non-traded BDCs averaged 12.1% of NAV (median 10.1%); total requests a little over $15bn, 53.4% honoured; seven funds gated at 5%. Requests by manager: Blue Owl Tech 40.7%, Blue Owl 21.9%, Ares 11.6%, Barings 11.3%, Apollo 11.2%, Morgan Stanley 10.9%, HPS 9.3%, Oaktree 8.5%, Blackstone 7.9%. — [With Intelligence, 30 Apr 2026](https://www.withintelligence.com/insights/what-is-actually-going-on-in-bdc-portfolios/)
- Credit metrics: non-traded BDC non-accruals average 0.6% and PIK 4.6%; top-20 listed BDCs 2.1% non-accruals and 8.1% PIK; one Blue Owl fund has 12% PIK income. PIK share of investments rose from 2.5% (Q4 2021) to 6.4% (Q4 2025). Around 10% of loans have interest coverage below 1.0x (Adams Street). — [With Intelligence](https://www.withintelligence.com/insights/what-is-actually-going-on-in-bdc-portfolios/); [State Street](https://www.statestreet.com/us/en/insights/private-credit-stress)
- Software exposure averages 19.7% of BDC portfolios, 35.6% including software-adjacent sectors. — [With Intelligence](https://www.withintelligence.com/insights/what-is-actually-going-on-in-bdc-portfolios/)
- Valuation distrust: listed BDCs traded at 0.85x NAV on average (median 0.80x) on 24 Apr 2026; "the market largely believes BDC NAVs are overstated". — [With Intelligence](https://www.withintelligence.com/insights/what-is-actually-going-on-in-bdc-portfolios/)
- Events: First Brands and Tricolor bankruptcies (2025); UK lender Market Financial Solutions entered insolvency in early 2026 amid fraud allegations over collateral pledged to multiple counterparties; Blue Owl halted redemptions at one non-traded fund in February 2026; Q1 2026 software loan sell-off tied to AI disruption. — [With Intelligence](https://www.withintelligence.com/insights/what-is-actually-going-on-in-bdc-portfolios/); [State Street](https://www.statestreet.com/us/en/insights/private-credit-stress)
- State Street: formal default rates are "increasingly poor diagnostics" because PIK, amendments and selective defaults defer recognition; loans are marked to model. — [State Street](https://www.statestreet.com/us/en/insights/private-credit-stress)
- Credit secondaries: H1 2026 volume $20.4bn, +122% YoY and above full-year 2025; GP-led $17bn (+183%), LP-led $3bn (+7%). GP-led deals priced at about 99% of fair market value on average; high-quality first-lien portfolios in the high 90s. Dedicated equity dry powder about $30.5bn. BDCs, semi-liquid vehicles and interval funds are expected to drive about 25% of 2026 volume. — [Evercore H1 2026 Credit Secondary Market Review](https://www.evercore.com/wp-content/uploads/2026/07/H1-2026-Credit-Secondaries-Market-Report.pdf)
- Secondaries market practice: 81% of deals were intermediated; 25% included deferred consideration; 34% of GP-led deals had an unlevered sleeve; buyers of senior/unitranche target 10-15% levered net IRR at about 50%+ LTV; 89% of capital targets senior/unitranche; diligence requests in Evercore-advised GP-led processes ran into the hundreds per deal. Evercore advised on about $22bn over the last twelve months. — [Evercore](https://www.evercore.com/wp-content/uploads/2026/07/H1-2026-Credit-Secondaries-Market-Report.pdf)
- 2025 baseline: credit secondary volume $20.0bn in 2025 versus $10.9bn in 2024 (snippet-level). — [Evercore 2025 survey](https://www.evercore.com/wp-content/uploads/2026/01/2025-Credit-Secondary-Market-Survey.pdf)
- AI lending: more than $200bn of private credit loans outstanding to AI-related companies. — [Bloomberg via Insurance Journal](https://insurancejournal.com/news/international/2026/02/03/856623.htm)

### Inferences
- The gap between reported NAV (non-accruals under 1%) and market price (15-20% discount) is a measurable demand for independent loan-level valuation and monitoring. Secondary buyers already pay for it through diligence.
- The secondary market is advisor-run and bespoke. One advisor (Evercore) reports about $22bn of advised volume in a market of roughly $30-40bn annualised (derived from H1), so intermediation is concentrated. A venue or data utility would have to win against advisors who control the processes.
- If advisory fees are near 1% of volume (my assumption, not sourced), the whole fee pool on $40bn is around $400m a year. That is a real but bounded market.
- Collateral double-pledging (MFS, and the First Brands and Tricolor allegations) is a recurring failure that a collateral registry or verification service addresses directly; lenders have a reason to pay after losses.

### Gaps
- Events after June 2026: my searches for H2 2026 defaults, markdowns, gating and regulatory actions failed on the search budget. The picture above is mostly Q1-Q2 2026.
- No current private credit default rate from Fitch, Moody's, KBRA or Proskauer was retrieved.
- No revenue or adoption data for valuation and data vendors (73 Strings, Octus, iCapital, Kroll, S&P) or for any electronic private-loan trading venue.
- No direct evidence on valuation dispersion (different managers marking the same loan differently) for 2026.

---

## 7. Capital markets venues: prediction markets, new exchanges, 24/7 trading, tokenized equities, power and compute derivatives

### Takeaway
Prediction markets are the one new venue category with large, fast revenue: Kalshi is estimated at about $5bn of annualized revenue (October 2026) on a $40bn valuation and about 81% of US volume, with roughly 80% of fee-generating volume from sports. Compute derivatives have venues and indices but no confirmed volume. I could not retrieve data on tokenized equities, 24-hour equity trading or power futures before the search budget ran out.

### Cited Findings
- US prediction market volume was $120.73bn in October 2026 across eight exchanges, up 64.1% from September: Kalshi $98.15bn (81.3%), Polymarket US $14.77bn (12.2%), Novig $3.27bn, Crypto.com/Nadex $2.19bn, Underdog $1.98bn. The figures count contracts at $1 notional, not cash at execution price. Combination (parlay) contracts were at least $79.46bn of the total and at least 68.1% of Kalshi's volume. — [DeFi Rate](https://defirate.com/news/prediction-market-volume-reaches-120-7-billion-october/)
- July 2026: combined Kalshi and Polymarket volume $50.59bn (Kalshi $37.7bn, Polymarket global $7.9bn, Polymarket US $5bn); open interest across the three fell from about $2bn to about $1.2bn during the month. — [The Block, 3 Aug 2026](https://theblock.co/post/410382/kalshi-polymarket-volume-july)
- Kalshi revenue (Sacra estimate, annualized): about $25m at end-2024, $735m at end-2025, $4bn in July 2026, $5bn at end-October 2026. Monthly volume: $226m (Dec 2024), $6.6bn (Dec 2025), $29.2bn (June 2026). — [Sacra: Kalshi](https://sacra.com/c/kalshi/)
- Kalshi fees and mix: taker-only fees of 0.07% to 7% depending on contract probability; sports about 80% of fee-generating volume in June 2026; parlays about 50% of volume during the World Cup; Robinhood accounts for more than half of volume (undated). — [Sacra: Kalshi](https://sacra.com/c/kalshi/)
- Kalshi funding: $2bn valuation (June 2025), $5bn (Oct 2025), $11bn (Dec 2025), $22bn (May 2026), $40bn post-money on a $1bn Series G (29 Oct 2026); talks at $65bn reported in November 2026, unconfirmed. Kalshi launched its own clearinghouse (March 2026) and perpetual futures on 50+ stocks (November 2026). — [Sacra: Kalshi](https://sacra.com/c/kalshi/)
- Polymarket revenue (Sacra estimate, annualized): zero through 2025 (no fees), about $375m in May 2026, $1bn in June 2026, $1.8bn at end-October 2026. Fees began in January 2026. Blended take rate about 0.3% of volume versus Kalshi's about 1.2% (May 2026). ICE holds about 23% of outstanding shares after investing $1.0bn (Oct 2025) and $600m (Mar 2026). Talks at a $15bn valuation were reported in April 2026. — [Sacra: Polymarket](https://sacra.com/c/polymarket/); [Sacra research note](https://sacra.com/research/polymarket-at-375m-year-revenue/)
- Category mix since July 2024: sports is 80% of Kalshi volume and 39% of Polymarket's; combined monthly volume went from under $5bn (Sept 2025) to about $24bn (April 2026), against about $14bn a month wagered at US legal sportsbooks in 2025. — [Pew Research Center, 27 May 2026](https://www.pewresearch.org/short-reads/2026/05/27/trading-volume-on-prediction-markets-has-soared-in-recent-months/)
- Legal risk: more than a dozen state regulators have accused Kalshi and Polymarket of unlicensed gambling; Arizona filed criminal charges against Kalshi in March 2026 (later paused by a federal judge); the Third Circuit ruled 2-1 that New Jersey cannot regulate Kalshi's sports markets; the CFTC sued several states. — [The Block](https://theblock.co/post/410382/kalshi-polymarket-volume-july); [Sacra: Kalshi](https://sacra.com/c/kalshi/)
- Hyperliquid (on-chain perpetuals venue, founded 2023, core team of 11): retained revenue about $818m in 2025 (gross fees about $972m) and $403m through August 2026; fees typically 0.027% of volume. — [Sacra: Hyperliquid](https://sacra.com/c/hyperliquid/)
- Power derivatives: Nodal Exchange holds more than half the open interest in US electricity futures and is pairing power with compute contracts. — [FIA MarketVoice](https://www.fia.org/marketvoice/articles/explainer-what-are-compute-futures-and-how-do-they-work)
- Compute derivatives: see section 1 (CME/Silicon Data, ICE/Ornn, ICE/NATIVX, Nodal/Compute Desk, Architect, BGC, Kalshi curves). No volumes disclosed. — [GARP](https://www.garp.org/risk-intelligence/technology/cant-get-enough-compute-260828)

### Inferences
- Kalshi's estimated $5bn run-rate against about $1.2tn of annualised October notional (derived: $98bn x 12) is about 0.4% of notional. Sacra's 1.2% take rate is measured on a different volume base, so the two cannot be compared directly.
- Prediction-market revenue is sports wagering revenue under a federal derivatives licence. Its growth came from a regulatory arbitrage against state-licensed sportsbooks plus brokerage distribution (Robinhood). The same arbitrage is the main risk.
- New-venue economics reward the first liquid venue almost exclusively (Kalshi 81% of US prediction volume; Forbes credits Hyperliquid with "about 80%" of the perpetual futures market, which I read as on-chain perps). A sixth compute futures venue or a third prediction market has poor odds without captive order flow.
- Hyperliquid's 2026 revenue pace (about $605m annualised, derived from eight months) is below 2025, which shows venue revenue is cyclical even for the leader.

### Gaps
- Tokenized equities (value outstanding, volumes, issuers), 24-hour or 23/5 equity trading launches at NYSE, Nasdaq, Cboe or 24X, and DTCC tokenization pilots: nothing retrieved; the searches failed on the search budget.
- Power futures volumes and open interest for 2026 at Nodal, ICE and CME, and data-center-driven hedging demand: not retrieved.
- Company-reported (not estimated) revenue for Kalshi or Polymarket: none public that I found.
- Kalshi's and Polymarket's market-maker incentive costs, clearing costs and net margins: not disclosed.

---

## 8. Fintech or financial infrastructure companies founded 2019-2025 that reached $100m+ net revenue within about 24 months of launch

### Takeaway
The companies that clearly did it sold access to leveraged or speculative trading (Hyperliquid, Pump.fun, Ethena) or event contracts once fees were switched on (Polymarket; Kalshi was founded in 2018). The one conventional B2B example is Ramp, which sold a free corporate card and spend software paid by interchange, and the sources disagree on whether it took two or three years. In every case the fast revenue came from taking a small cut of a very large flow that the product itself created or captured, with a very small team.

### Cited Findings
- Pump.fun (launched January 2024): reached $100m of cumulative revenue in 217 days (Dune data). It sells token creation and trading on Solana and "charges the highest fees of any DEX on chain". — [Decrypt, 2 Sep 2024](https://decrypt.co/247522/pump-fun-solana-meme-coins-fastest-growing-app)
- Ethena: reached $100m about 34 days slower than Pump.fun, so roughly 251 days (derived by the article's comparison). Other comparisons: Convex 306 days, PancakeSwap 325, Aerodrome 338. These are protocol revenue figures from Token Terminal and DefiLlama. — [Decrypt](https://decrypt.co/247522/pump-fun-solana-meme-coins-fastest-growing-app)
- Hyperliquid (founded 2023): revenue of $10.5m in 2024 and about $818m in 2025 net of about $154m of pass-throughs (gross fees about $972m). It sells perpetual futures trading at about 0.027% of volume. Forbes cites $844m of revenue on $2.95tn of volume "less than two years after launch". — [Sacra: Hyperliquid](https://sacra.com/c/hyperliquid/); [Forbes Australia](https://www.forbes.com.au/news/innovation/the-50-hottest-fintech-startups-in-2026/)
- Polymarket (founded 2020, but charged no fees until January 2026): estimated annualized revenue went from zero at end-2025 to $1bn in June 2026 and $1.8bn in October 2026. These are run-rates on roughly ten months of fee history. — [Sacra: Polymarket](https://sacra.com/c/polymarket/)
- Kalshi (founded 2018, so outside the window; CFTC-regulated exchange live since 2021): about $25m annualized at end-2024, $735m at end-2025, $5bn at end-October 2026 (Sacra estimates). It sells event contracts with taker fees. — [Sacra: Kalshi](https://sacra.com/c/kalshi/)
- Ramp (founded 2019): co-founder Eric Glyman says it passed $100m of revenue within two years of launch (snippet-level); TechCrunch says it crossed $100m of annualized revenue before its third birthday in March 2022. It reached $1bn annualized in August 2025 and about $2bn in October 2026 (Sacra estimate) at a $60bn valuation. Total payment volume was $57bn in 2024; revenue is interchange share plus software, and Sacra does not say whether it is net of rewards and partner costs. — [Fortune](https://fortune.com/article/ramp-founder-eric-glyman-titans-and-disruptors); [TechCrunch, 3 Mar 2025](https://techcrunch.com/2025/03/03/ramp-has-more-than-doubled-its-annualized-revenue-to-700-million); [Sacra: Ramp](https://sacra.com/c/ramp/)
- Circle's Arc token presale recognised $182m of revenue in one quarter (Q3 2026) from a network that reached mainnet on 16 Sep 2026. This is a token sale, not recurring revenue. — [FXC Intelligence](https://www.fxcintel.com/research/analysis/ct-circle-q3-2026-earnings)
- Not in the window but useful comparators: Mercury (founded 2017) is at about $1bn annualized (Sept 2026), mostly interest on about $20bn of deposits shared with partner banks; Column (bank charter) made more than $200m in 2025. — [Sacra: Mercury](https://sacra.com/c/mercury/); [Forbes Australia](https://www.forbes.com.au/news/innovation/the-50-hottest-fintech-startups-in-2026/)
- Volume is not revenue: BVNK's $30bn of 2025 payment volume corresponds to an estimated $39-150m of revenue; OpenPayd's $240bn of annualised volume supports a $1.1bn valuation; Ramp's $57bn TPV (2024) sits beside roughly $700m of annualized revenue in early 2025. — [Fintech Blueprint](https://lex.substack.com/p/analysis-mastercard-buys-bvnk-for); [Architect Partners](https://architectpartners.com/wp-content/uploads/2026/06/Crypto-Payments-Infrastructure-Part-IV.pdf); [TechCrunch](https://techcrunch.com/2025/03/03/ramp-has-more-than-doubled-its-annualized-revenue-to-700-million)

### Inferences
- I found no company founded 2019-2025 that reached $100m of net revenue within 24 months by selling infrastructure to institutions (data, valuation, insurance distribution, B2B stablecoin orchestration, structuring). BVNK took about four years to reach an estimated $40-150m. The fast cases are all venues or consumer-facing flow businesses.
- The fast cases share three features: revenue is a fee on turnover, the customer brings leverage or repeat betting so turnover is many times balances, and distribution was borrowed (Robinhood for Kalshi, on-chain wallets for Hyperliquid and Pump.fun, card rails for Ramp).
- For a founder with capital-markets and enterprise sales skills, the closer precedents are slower: an arranger or MGA earns 1-3% of placed volume or 10-25% of premium (my general-knowledge range, not sourced here), so $100m of net revenue needs roughly $3-10bn of placed debt or $400m-1bn of premium a year.

### Gaps
- No audited or company-reported net revenue for any of these private companies; all figures are estimates, on-chain data or founder statements.
- Deel, Rippling (founded 2016), Rain, Phantom, Tether-backed ventures, Clear Street and others: no revenue timeline retrieved.
- I did not find a systematic list from a primary source; this is a sample from what could be retrieved, and other qualifying companies probably exist.
- Stripe-owned Bridge's revenue and the time it took are not public in what I could open.
