# AI compute and datacenter buildout: economics and bottlenecks (as of 24 Nov 2026)

Research note on method. The shared web-search budget ran out after about 24 searches, so the second half of this work used direct page fetches of URLs already found, plus navigation of known sites (SEC EDGAR, TrendForce, Utility Dive, Sacra, Epoch AI). Several pages returned HTTP 403 (Axios, DCD, Fierce Network, Morningstar, S&P, Oracle's press site, Eaton). Component-level questions (CDUs, optics, switchgear vendors, Eaton, Micron, xAI) are therefore thin and are listed under Gaps.

Confidence labels used on every finding:
- **[V]** verified: company filing, press release or earnings-call transcript, opened and read.
- **[R]** reported: named press outlet citing documents or sources, page opened.
- **[E]** third-party estimate (Sacra, Epoch, analysts, price trackers).
- **[S]** search-result snippet only; the page was not opened or was blocked. Treat as unconfirmed.
- **[U]** rumor or single weak source.

## 1. Capex of Microsoft, Alphabet, Amazon, Meta, Oracle and the private buyers; what constrains them (Q3 2026 calls)

### Takeaway
The four hyperscalers guide to roughly $720-740B of 2026 capex, with Alphabet and Amazon both saying 2027 will be significantly higher; every one of them still describes demand as running ahead of capacity. The named constraints in Q3 2026 are delivery of third-party capacity, accelerated compute, memory pricing and power at specific sites, and the binding financial constraint has become free cash flow and debt-market appetite.

### Cited Findings
**Microsoft**
- [V/R] Q1 FY27 (Jul-Sep 2026): revenue $92.28B, Azure +48%, cash PP&E capex $39.37B (more than double a year earlier), commercial RPO $677B (+73%) — [24/7 Wall St, 28 Oct 2026](https://247wallst.com/cards/microsoft-q1-2027-earnings-msft-01m6223bcjxyqzvby9cw8yzzqb)
- [R] Call summary: calendar-2026 capex about $170B; Q2 FY27 capex to exceed $50B; third-party GPU-as-a-service capacity deliveries were delayed in Q1 and shift to H2 FY27; demand continues to outpace supply; Azure growth can fluctuate with token pricing and timing of third-party GPU lease deliveries; time to bring new GPUs into service cut 20% — [Business Insider Japan](https://www.businessinsider.jp/article/2611-earnings-microsoft-corporation-q1-2027-earnings-call-summary/)
- [S] Capex including finance leases was $45.2B in the quarter, below expectations because third-party deliveries slipped — [Zacks](https://www.zacks.com/stock/news/3018768/microsoft-q1-earnings-beat-estimates-as-cloud-accelerates)
- [R] In April 2026 Microsoft guided calendar-2026 capex to $190B, of which $25B was attributed to higher component pricing. By August the figure cited was about $175B and by October about $170B. A roughly $255B figure for fiscal 2027 is cited as the only management target for that period — [Yahoo Finance, 29 Apr 2026](https://finance.yahoo.com/markets/article/magnificent-7-earnings-rush-reveals-ai-spending-surge-with-hyperscaler-capex-set-to-reach-725-billion-in-2026-224901707.html); [Motley Fool, 3 Aug 2026](https://www.fool.com/investing/2026/08/03/microsoft-and-amazon-won-the-ai-spending-week/)

**Alphabet**
- [V] Q3 2026 capex $51.4B (about 65% servers and networking, 35% data centers); 2026 guidance $195-205B unchanged; "we continue to expect our CapEx to increase significantly in 2027", number due on the Q4 call — [Q3 2026 call transcript](https://singjupost.com/alphabet-googl-q3-2026-earnings-call-transcript/)
- [V] CFO cited "the supply constrained environment" as the reason Google began renting third-party compute at end of Q3, a Q4 Cloud margin headwind. Kurian: Google "could obviously serve a lot more demand with capacity" and cited "the scarcity of accelerated compute". Cloud backlog $561B, just over 55% to convert in 24 months — [same transcript](https://singjupost.com/alphabet-googl-q3-2026-earnings-call-transcript/)
- [V] TPU system sales to third parties were "a meaningful contributor" to Cloud growth; nearly 100 TPU customers including Anthropic (direct and via Broadcom), Apple and Oracle; inventory is built only after contracts are signed — [same transcript](https://singjupost.com/alphabet-googl-q3-2026-earnings-call-transcript/)
- [S] One outlet says 2027 capex is "set to top $300B"; this number is not in the transcript — [AI Weekly](https://aiweekly.co/alerts/alphabet-posts-1276b-q3-with-google-cloud-up-103-to-307b-as-2027-capex-set-to)

**Amazon**
- [R] Q3 2026: AWS revenue $46B (+39%), AWS operating income $17.8B, backlog $578B; about $220B cash capex in 2026; 2027 "meaningfully more"; Q3 PP&E purchases $77.3B vs $35.1B a year earlier; trailing-12-month free cash flow minus $42.4B; $48.1B of long-term debt raised in the quarter; Jassy expects AWS growth above 40% in 2027 and 2028 and said "we're installing an AI accelerator about every 14 seconds" — [The Next Web, Oct 2026](https://thenextweb.com/news/amazon-q3-earnings-aws-39-free-cash-flow-2027-capex)
- [S] The July raise of 2026 capex by about $20B to $220B was attributed partly to memory prices; Amazon said it was on pace to double 2025 power capacity by end-2027 — [Fierce Network](https://www.fierce-network.com/cloud/memory-drives-amazon-capex-another-20b-2026)

**Meta**
- [V] Q3 2026 capex $34.91B including finance-lease principal; 2026 capex guidance $135-145B (narrowed from $130-145B); Q3 free cash flow minus $2.12B; long-term debt $80.92B vs $58.74B at end-2025; no 2027 capex number, "investing aggressively" — [Meta Q3 2026 release via Finviz](https://finviz.com/news/405782/meta-reports-third-quarter-2026-results)
- [R] The April 2026 raise of $10B was attributed to higher component pricing and, to a lesser extent, data center costs — [Yahoo Finance](https://finance.yahoo.com/markets/article/magnificent-7-earnings-rush-reveals-ai-spending-surge-with-hyperscaler-capex-set-to-reach-725-billion-in-2026-224901707.html)

**Oracle**
- [S] Q1 FY27 (reported 10 Sep 2026): RPO $664B; OCI revenue $7.4B (+121%); free cash flow about minus $5B in the quarter; FY27 capex $90-95B gross; $20B of stock sold through an at-the-market program; borrowings about $125.3B — [Oracle release](https://www.oracle.com/news/announcement/q1fy27-earnings-release-2026-09-10/); [Zacks](https://zacks.com/stock/news/2988454/oracle-q1-earnings-beat-estimates-cloud-growth-accelerates)
- [R] FY27 capex is about $70B net of customer prepayments, $90-95B gross — [Motley Fool, 3 Aug 2026](https://www.fool.com/investing/2026/08/03/microsoft-and-amazon-won-the-ai-spending-week/)
- [S] FY26 capex $55.7B; FY26 free cash flow minus $23.7B; RPO $638B at FY26 year-end with BofA estimating more than half from OpenAI — [Motley Fool, 10 Jun 2026](https://www.fool.com/investing/2026/06/10/oracle-just-revealed-a-massive-638-billion-backlog/)
- [R] S&P cut Oracle to BBB- in July 2026, citing OpenAI-linked leases — [Capacity, 19 Nov 2026](https://capacityglobal.com/news/nvidia-trims-neocloud-commitments/)

**OpenAI / Stargate**
- [R] OpenAI told investors in February 2026 that compute spend would be about $600B by 2030; a July 2026 presentation shows about $856B for 2026-2030 (categories may differ). Projected negative free cash flow 2026-2030 is $278B (was $305B in May). 2026 revenue forecast about $36B. $122B raised in March 2026 at $852B; FT says the money runs out by 2028. Nvidia is in talks to guarantee $250B of data center debt — [The Next Web citing FT/CNBC, 19 Sep 2026](https://thenextweb.com/news/openai-856bn-compute-vs-600bn-reset-burn-improved)
- [E] Abilene: 824 MW IT estimated operational as of 1 Nov 2026 (six of eight buildings confirmed by Oracle on 10 Sep; buildings 7-8 extrapolated), about 1.02M H100-equivalents, capital cost estimate $31.2B — [Epoch AI directory](https://epoch.ai/data/ai-data-centers/directory/openai-stargate-abilene)
- [E] As of April 2026 the seven US Stargate sites totalled over 9 GW planned with only about 0.3 GW running, all at Abilene; the other six are due by Q4 2028 — [Epoch AI](https://epoch.ai/blog/openai-stargate-where-the-us-sites-stand)

**Anthropic**
- [R] Draft IPO prospectus seen by Reuters: at least $518B of infrastructure commitments over about a decade, about 80% non-cancellable: Google $111.1B (Apr 2026-Jul 2033, payable regardless of usage), Amazon $110B (May 2026-Apr 2036), Microsoft $31.4B, Broadcom equipment leases about $161.2B, SpaceX/xAI up to $84.5B through 2029 (cancellable on 90 days' notice), AMD over $20B — [Reuters via Business Day, 29 Sep 2026](https://www.businessday.co.za/world/international-companies/2026-09-29-anthropic-plans-518bn-ai-infrastructure-spend-80-non-cancellable/)
- [R] 2025: revenue nearly $4.6B, compute and infrastructure cost $7.33B, operating loss $8.06B — [The Next Web citing Reuters](https://thenextweb.com/news/anthropic-ipo-prospectus-42bn-loss-518bn-compute)
- [S] A later amended filing reportedly lifts commitments to $895.4B — [Boing Boing, 3 Nov 2026](https://boingboing.net/2026/11/03/anthropic-895-billion-compute-commitments.html)
- [V] Anthropic announced about 3.5 GW of Google TPU capacity via Broadcom starting 2027 — [Anthropic, 6 Apr 2026](https://www.anthropic.com/news/google-broadcom-partnership-compute)

**xAI**
- [R] Colossus 2 has about 950 MW running; xAI is now also a seller of capacity to Anthropic — [NewMarketPitch, 21 Oct 2026](https://newmarketpitch.com/blogs/news/ai-data-center-who-is-ahead); [Reuters via Business Day](https://www.businessday.co.za/world/international-companies/2026-09-29-anthropic-plans-518bn-ai-infrastructure-spend-80-non-cancellable/)

**Aggregate**
- [R] Hyperscaler capex is projected at almost $1T in 2027, up from $785B in 2026; hyperscaler debt has doubled to $460B since end-2024; data center lease liabilities of the six largest (incl. Oracle and CoreWeave) are $1.2T, of which $820B is not yet on balance sheets; Amazon, Microsoft, Alphabet and Oracle hold a $2.1T contract backlog — [IFR](https://www.ifre.com/bonds/2463746/bond-market-begins-to-question-ai-boom-as-beignet-sequel-falls-flat)
- [V] Nvidia Q3 FY27 (to 25 Oct 2026): revenue $115.8B (+103%), data center $107.6B (+110%), GAAP gross margin 74.8%, Q4 guide $130B — [Nvidia release via Let's Data Science](https://letsdatascience.com/news/nvidia-reports-third-quarter-revenue-of-1158-billion-up-103-385a5092)

### Inferences
- Summing the latest guides (Microsoft about $170B, Alphabet $195-205B, Amazon about $220B, Meta $135-145B) gives $720-740B for 2026, before Oracle's $90-95B fiscal-year figure.
- Three of the four (Amazon, Meta, and Alphabet in Q3) now run negative free cash flow in at least one period, so 2027 growth depends on bond markets, leases and prepayments, not on operating cash.
- Microsoft's calendar-2026 number has drifted down ($190B to $175B to $170B) because suppliers delivered late, not because it chose to spend less. That is evidence of a supply-side bottleneck at third-party builders.
- Abilene's Epoch estimate implies about $38M of capital per MW of IT load including chips.

### Gaps
- Full-year 2025 capex actuals per company were not retrieved from a filing in this session (search budget ran out). Only year-ago quarter comparisons are cited above.
- No hard 2027 capex number from Amazon, Meta or Alphabet. Microsoft's roughly $255B FY27 figure is a secondary-source citation.
- No sourced capex figure for xAI/SpaceX. No statement on labor or cooling as a constraint was found in any Q3 call summary.

## 2. Inference demand growth, price per token, and GPU-hour rental prices through 2026

### Takeaway
Lab revenue and token volumes grew 3-7x in a year, and unlike 2023-2025, GPU rental prices rose through 2026 across every generation. Price per token for a fixed capability kept falling (43% in ten weeks mid-year on one index), which squeezes anyone who buys GPU-hours and sells tokens.

### Cited Findings
- [E] OpenAI run-rate rose from about $13B (Aug 2025) to over $40B (Aug 2026). Anthropic went from $9B at end-2025 to a reported $65B at end-July 2026. Combined they grew from $30B at the start of 2026 to about $105B by August. The labs count cloud-channel revenue differently (Anthropic gross, OpenAI net) — [Epoch AI, 27 Aug 2026](https://epoch.ai/gradient-updates/an-update-on-ais-most-important-number)
- [R] Anthropic quarterly revenue: Q1 2026 $4.73B; Q2 2026 more than $11.5B (preliminary) vs $787M in Q2 2025; run-rate $47B in May and above $65B at end-July — [Channel Insider citing Bloomberg/Axios, 18 Aug 2026](https://www.channelinsider.com/news-and-trends/news-anthropic-revenue-run-rate-outpaces-openai/)
- [S] OpenAI's run-rate was reported near $70B in late September by Axios, while another report put it near $50B. These conflict — [Axios, 29 Sep 2026](https://axios.com/2026/09/29/scoop-openais-annual-recurring-revenue-nears-70b); [Crypto Briefing](https://cryptobriefing.com/openai-revenue-run-rate-nears-50-billion/)
- [V] Google first-party model APIs process nearly 32 billion tokens per minute, up 40% quarter on quarter and more than 4x year on year. More than 2,600 customers each used at least 100 billion tokens in the past 12 months — [Alphabet Q3 2026 call](https://singjupost.com/alphabet-googl-q3-2026-earnings-call-transcript/)
- [R] Microsoft Foundry revenue grew more than 3x year on year in Q1 FY27 — [Business Insider Japan](https://www.businessinsider.jp/article/2611-earnings-microsoft-corporation-q1-2027-earnings-call-summary/)
- [R] Average price per million tokens on one tracker fell from $2.04 (end-May 2026) to about $1.16-1.18 (early August), a 43% drop. OpenAI cut GPT-5.6 Luna prices 80% in late July to $0.20 input and $1.20 output — [Crypto Briefing, 1 Sep 2026](https://cryptobriefing.com/ai-token-prices-record-lows/)
- [E] H100 rental history: composite index $6.62/hr in 2H 2023, $3.34 in 2Q 2025, flat at $2.79-2.90 from July 2025 to March 2026. The one-year contract range rose from $1.45-2.00 (late 2025) to $2.10-2.70 (April 2026), with some terms marked sold out — [SemiAnalysis GPU index](https://gpu-index.semianalysis.com/)
- [E] On-demand list medians on 7 Oct 2026: H100 $4.20 (GPU clouds $3.95, hyperscalers $10.53), H200 $5.70, B200 $8.19, B300 $9.50, GB200 $16.00 (three providers). Nebius raised H100 from $3.85 to $4.50 and H200 from $4.50 to $5.40 on 1 Oct 2026. AWS raised Capacity Block prices about 15%. Ornn settlement 6 Oct: H100 $2.86, H200 $5.04, B200 $7.56 — [Uvik GPU price index](https://uvik.net/blog/gpu-price-index/)
- [E] B200 spot rose from $2.31 (early March 2026) to $4.95 (late April), +114% in six weeks, on the Ornn index — [Tomasz Tunguz, 27 Apr 2026](https://www.tomtunguz.com/b200-gpu-pricing-spot-market-model-releases/index.md)
- [R] Year to date to mid-October 2026: H200 rents up about 160%, B200 about 120%, H100 about 35% (no index named) — [Crypto Briefing, 24 Oct 2026](https://cryptobriefing.com/nvidia-h200-rental-costs-rise-160-percent/)
- [R] CoreWeave said prices for older Ampere and Hopper capacity rose 30-50% quarter on quarter in Q3 2026 — [The Tech Capital](https://thetechcapital.com/coreweave-revenue-surges-168-interest-bill-709m-loss/)

### Inferences
- 32 billion tokens per minute is about 1.4 quadrillion tokens a month on Google's developer APIs alone (own arithmetic).
- An inference reseller faced input costs up 35-160% and output prices down 40-80% inside 2026. Reported gross margins of 45-50% at Together and Fireworks (section 7) are consistent with that squeeze.
- Old GPUs are appreciating, which contradicts the 2025 "H100s will be worthless" thesis for now. It also means the residual-value risk lenders worry about has not shown up in spot prices yet.

### Gaps
- No rental price series for Rubin (Vera Rubin NVL72 only began shipping in Q3 FY27) and only two list prices for GB300.
- No audited API-only revenue split for OpenAI, Anthropic or Google. No OpenAI token-volume figure for 2026.
- Token price indices come from trackers with undocumented methods; flagship model prices reportedly rose in 2026 (snippet only), so "price per token is falling" holds for fixed capability, not for the frontier.

## 3. Neocloud financial performance

### Takeaway
Revenue and backlog are enormous and growing fast, but the model runs on debt: CoreWeave's quarterly interest ($846M) is more than twice its adjusted operating income ($379M), and its bonds traded at 15-16% yields in October 2026. Delivery delays at third-party sites, not demand, are what cut guidance at Nebius and Nscale.

### Cited Findings
**CoreWeave** (founded 2017, IPO March 2025)
- [V/R] Q3 2026: revenue $3.661B (+168%), backlog about $132.5B (from $104B in June), adjusted EBITDA $2.256B (62%), adjusted operating income $379M (10%), net interest expense $846M, net loss $709M, Q3 capex $14.511B, nine-month capex $30.65B; more than 1.7 GW active and more than 4.6 GW contracted; 2026 guide: revenue $13.0-13.3B, capex $37-39B, year-end run-rate $20-21B; Q4 interest expense $1.05-1.15B — [The Tech Capital](https://thetechcapital.com/coreweave-revenue-surges-168-interest-bill-709m-loss/); [Pulse 2.0](https://pulse2.com/coreweave-record-q3-revenue-reaches-3-66-billion-as-backlog-grows-to-132-5-billion/)
- [R] Debt almost $47B at quarter end; some bonds topped 16% yield; shares fell more than 40% in the month before results — [Let's Data Science citing CNBC/LSEG](https://letsdatascience.com/news/coreweave-beats-q3-revenue-estimates-raises-2026-guidance-ba-f4170a31)
- [R] 2025 revenue $5.13B. Total debt was about $30B in June 2026. Meta has committed $35B in total — [The Next Web, 11 Jun 2026](https://thenextweb.com/news/coreweave-credit-rebound-applied-digital-junk-bond-data-center)
- [R] CoreWeave plans to fund most remaining backlog with contract-matched loans and expects about $9B of customer prepayments in three months — [The Tech Capital](https://thetechcapital.com/coreweave-revenue-surges-168-interest-bill-709m-loss/)

**Nebius**
- [V] Q3 2026: revenue $980.8M (+571% YoY), of which about $325M was non-recurring "asset-light" revenue; adjusted EBITDA $465.8M (47%); ARR $6.4B at end-September (from $3.0B in June); RPO $38.7B; Q3 capex about $7.3B; 2026 capex about $27B (was $20-25B); 2026 revenue at the low end of $3.0-3.4B; 2027 guide revenue $12-13B and capex $40-45B; asset-backed facility priced at SOFR + 2.50%; $5.75B converts in August — [Nebius 6-K shareholder letter, Nov 2026](https://www.sec.gov/Archives/edgar/data/0001513845/000110465926126008/tm2629571d1_ex99-2.htm)
- [V] Cause of the guide-down: "Where we rely on third parties, there have been delays." A New Jersey site retired temporary generation before permanent power was ready; Nebius is switching to Bloom fuel cells; several colocation dates moved into 1H 2027 — [same 6-K](https://www.sec.gov/Archives/edgar/data/0001513845/000110465926126008/tm2629571d1_ex99-2.htm)

**Nscale** (founded 2024, London)
- [R] IPO filing: H1 2026 revenue $140.6M (vs $10.4M), H1 loss $1.02B; one customer was 52% of revenue; more than $103B contracted (Anthropic $44.6B, Microsoft about $43.8B through 2033); about 55 MW live at end-August (7 MW owned); about 25,000 GPUs deployed vs 461,000 contracted; Glomfjord about six months late; Microsoft exited the Loughton UK site in October 2026; about $3.69B equity raised plus $3.36B converts; Nvidia guarantees $860M of Texas lease obligations — [NewMarketPitch summary of filing and FT/Reuters, 21 Oct 2026](https://newmarketpitch.com/blogs/news/ai-data-center-who-is-ahead)
- [E] Funding path: $30M seed (Dec 2023), $155M Series A (Dec 2024), $1.1B Series B (Sep 2025), $2B Series C at $14.6B (Mar 2026) — [Sacra](https://sacra.com/research/nscale)

**Crusoe** (founded 2018)
- [E] Revenue $276M in 2024, about $500M in 2025, company projection $2B for 2026; Abilene debt of $9.6B plus a $7.1B construction loan from JPMorgan — [Sacra](https://sacra.com/c/crusoe/)
- [R] $3.9B first close of Series F at $30.9B (Sep 2026); about 1 GW operating, more than 6 GW and $140B contracted (company-stated); a 1.8 GW Wyoming campus was paused in June 2026 — [NewMarketPitch](https://newmarketpitch.com/blogs/news/ai-data-center-who-is-ahead)

**Lambda** (founded 2012)
- [E] Revenue about $425M in 2024 and $700M in 2025; H1 2025 gross margin about 50%; about $2.9B secured debt; 2026 projection above $1.5B; reported $35B Anthropic deal; Nvidia rents back about 10,000 chips for $1.3B over four years — [Sacra](https://sacra.com/c/lambda-labs/)
- [R] Backlog reportedly rose from about $15B (June 2026) to about $50B (September); raising up to $4B at $14.5B pre-money; 2027 IPO planned — [NewMarketPitch citing WSJ/Reuters](https://newmarketpitch.com/blogs/news/ai-data-center-who-is-ahead)

**Fluidstack** (founded 2017/2018)
- [E] Revenue $25M in 2023; ARR $180M in December 2024; 62% private cloud with contracts over $100M; Google backstops $3.2B and $1.3B of TeraWulf leases and $1.73B at Cipher — [Sacra](https://sacra.com/c/fluidstack/)
- [R] $1.5B round led by Jane Street at about $18B (Sep 2026) — [ValueAdd VC, 6 Sep 2026](https://valueaddvc.com/pulse/ai-compute-4-8-billion-week-crusoe-fluidstack-gimlet-2026)

**Together AI** (founded 2022)
- [E] Annualized revenue about $618M at end-2025 and $1B in February 2026; gross margin about 45%; GPU rental is the larger share and per-token API 30-40%; $800M Series C at $8.3B in July 2026 — [Sacra](https://sacra.com/c/together-ai/)

**Sector signals**
- [R] Nvidia's rent-back commitments to neoclouds fell to $32B at end-October from $36B; interim CEO Kress said Nvidia will be "disciplined and selective"; total Nvidia commitments are near $670B including $118B of guarantees ($105B for an OpenAI Ohio campus) — [Capacity, 19 Nov 2026](https://capacityglobal.com/news/nvidia-trims-neocloud-commitments/)
- [R] Firmus shelved an IPO that sought more than $30B; SB Energy and AirTrunk listings were postponed; Gartner says over 80% of neoclouds may not be independent by 2030 — [Coin Edition citing FT, 19 Oct 2026](https://coinedition.com/u-s-ai-data-center-boom-faces-debt-risks-as-costs-rise-and-projects-stall/)

### Inferences
- CoreWeave spends about $2.90 of capex per $1 of 2026 revenue and pays 23% of revenue in interest. Equity value depends on refinancing at lower rates than the 15% the market asked in October.
- Speed to revenue (own calculation from the figures above): CoreWeave reached $5.13B in its eighth year; Nscale reached a roughly $280M annualized rate within about 24-30 months of founding after raising about $3.7B of equity; Fluidstack went from $25M to $180M ARR in one year.
- Customer concentration is extreme everywhere: one customer is 52% of Nscale, two customers are 85% of its backlog, and Lambda, Fluidstack and Nscale all lean on Anthropic and Microsoft.
- No default by a named neocloud was found. Distress so far shows in bond yields, shelved IPOs and paused sites.

### Gaps
- No 2026 audited revenue for Crusoe, Lambda, Fluidstack or Together; all figures are Sacra estimates or company projections.
- CoreWeave's customer-concentration percentage and weighted cost of debt for Q3 2026 were not retrieved (10-Q not opened).

## 4. Components with the longest lead times and largest price increases

### Takeaway
Memory is the sharpest price shock of 2026 (DRAM contract prices up in the high-20% range in one quarter, capacity sold out through 2029), followed by power equipment where waits are measured in years (transformers 128+ weeks, gas turbines booked to 2030-31). Advanced packaging is easing: the CoWoS gap is expected to halve by year-end.

### Cited Findings
- [R] SK hynix Q3 2026: revenue 104.6T won, operating profit 83.3T won (about 80% margin); DRAM ASP up in the high-20% range and NAND in the mid-20% range quarter on quarter; DRAM and HBM "effectively sold out" through 2029; long-term agreements with 14 customers covering more than half of 2027 and 2028 capacity — [Korea JoongAng Daily, 28 Oct 2026](https://koreajoongangdaily.com/business/sk-hynix-says-dram-hbm-booked-through-2029-as-profit-soars-to-62b/12942008)
- [R] AI server prices rose up to 45% for some customers; GPU server prices at least 20-30%; CPU server node prices more than tripled; memory is the main driver. HPE now reprices between quote and shipment. Dell asked XTX Markets for an extra $62-70M on a $549M contract — [TrendForce citing FT, 23 Nov 2026](https://www.trendforce.com/news/2026/11/23/news-ai-server-prices-reportedly-rise-up-to-45-as-dell-hpe-and-others-raise-prices-after-deals/)
- [R] Samsung and SK hynix plan 800T won for four new fabs; tool competition (EUV, etch, deposition) is tightening — [TrendForce, 30 Jun 2026](https://www.trendforce.com/news/2026/06/30/news-samsung-sk-hynix-800-trillion-won-expansion-strains-chipmaking-tool-supply-potentially-pressures-tsmc-and-intel/)
- [E] NAND prices are expected to fall in 2027 as supply grows and Chinese cloud providers cut enterprise SSD orders — [TrendForce, 19 Nov 2026](https://www.trendforce.com/presscenter/news/20261119-13314.html)
- [R] CoWoS: TSMC capacity 120,000-140,000 wafers a month in 2026 plus 50,000-60,000 at OSATs; supply-demand gap about 20% narrowing to about 10% by end-2026; TSMC plans more than 60% expansion by 2027 — [TrendForce, 15 Jun 2026](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/)
- [R] ASE raised advanced-packaging quotes by more than 20% (July 2026); a CoWoS wafer ASP is around $10,000 — [TrendForce CoWoS tag page](https://www.trendforce.com/news/tag/cowos/)
- [R] Optics: indium phosphide substrate supply "remains tight"; JX Advanced Metals will invest JPY 120B through FY2030 to expand InP capacity up to 10x — [TrendForce CPO tag page](https://www.trendforce.com/news/tag/cpo/)
- [S] Nvidia's filing shows $390B of supply commitments and new capacity deals with Amkor, Foxconn, Kinsus, Samsung Electro-Mechanics, SPIL and TSMC for packaging and substrate capacity arriving 2027-2029 — [AI Weekly](https://aiweekly.co/alerts/nvidia-q3-revenue-hits-1158b-up-103-data-center-1076b-guides-q4-to-130b)
- [R] Transformers: large units now take 3-5 years against 24-30 months before the boom; average US lead time about 128 weeks; switchgear is "effectively booked through 2028 at some suppliers"; Hitachi Energy's new Virginia plant arrives in 2028 — [The Next Web, 9 Jul 2026](https://thenextweb.com/news/us-power-companies-scramble-data-centre-equipment)
- [R] GE Vernova: gas turbine backlog plus slot reservations 116 GW at Q2 2026 (83 GW at end-2025); reservations run 4-5 years out, 2031 slots open; output 20 GW a year rising to 30 GW by 2030; data centers are about 20% of turbine customers; electrification backlog $41B (+69%); analyst price estimates $790/kW heavy-duty and $1,800/kW aeroderivative — [Utility Dive, 23 Jul 2026](https://www.utilitydive.com/news/ge-vernova-gas-turbine-backlog-climbs-to-116-gw/826039/)
- [S] GE Vernova's Q3 2026 contracted total rose only to 122 GW as orders and reservations slowed — [Utility Dive](https://www.utilitydive.com/news/ge-vernova-in-9b-deal-to-buy-high-voltage-manufacturer-as-gas-turbine-orde/873223/)
- [R] Siemens Energy: backlog EUR 164B, gas turbine backlog 65 GW; data center customers are about EUR 15B, under 10%; US orders +70%; North Carolina hub sold out for its first two years; Q4 turbine orders "moderated" — [Utility Dive, 17 Nov 2026](https://www.utilitydive.com/news/elevated-demand-for-gas-turbines-could-persist-through-2035-siemens-energy/874839/)
- [R] Mitsubishi Heavy: 37 GW large-frame backlog; 94% of 2024-25 orders came from utilities and IPPs; CEO says off-grid costs will push data centers back to utilities; no cancellations in two years — [Utility Dive, 23 Nov 2026](https://www.utilitydive.com/news/data-centers-mitsubishi-gas-turbines-earnings/875146/)
- [R] Vertiv Q3 2026: sales $4.31B (+61%), organic orders more than doubled, adjusted operating margin 25.2%, 2026 sales guide raised to $14.45-14.85B — [24/7 Wall St, 28 Oct 2026](https://247wallst.com/cards/vertiv-q3-2026-earnings-vrt-01m60zybj74azc2wscfpvp2ym4)
- [S] Vertiv's backlog was $15.0B at end-2025 (+109%) and the company has since stopped disclosing orders — [Nasdaq](https://www.nasdaq.com/articles/vertivs-15-billion-backlog-loudest-ai-signal-2026)

### Inferences
- The margin winners of 2026 are memory makers (about 80% operating margin at SK hynix), Nvidia (75% gross margin) and thermal/power vendors (Vertiv 25%). Server OEMs and neoclouds absorb the cost.
- Power equipment makers say data centers are only 10-20% of their order books, so their backlogs would survive an AI pause. A startup selling into that queue competes with utility demand too.
- Packaging is no longer the tightest link. Memory, power gear and site delivery are.

### Gaps
- No sourced 2026 lead times or backlog for liquid-cooling CDUs, optical transceivers, gensets or ABF substrate/T-glass. The TrendForce liquid-cooling tag had nothing newer than 2025. Eaton's and Micron's releases could not be opened.
- No transformer or switchgear price-increase percentages for 2026.

## 5. Time to power

### Takeaway
Grid connection for a large load takes 3-7 years in the main US markets, and queue numbers are inflated by speculation (ERCOT 438 GW of requests, over 300 GW without studies). Regulators are rewriting the rules right now: FERC forced every RTO to file large-load reforms in November 2026, and Texas paused new data center interconnections over the summer.

### Cited Findings
- [R] ERCOT large-load requests: about 63 GW at end-2024, 226 GW in November 2025 (77% data centers), 438 GW in late May 2026 with more than 300 GW having no studies submitted; ERCOT moved to a batch study framework after 10 July 2026 — [Latitude Media, 3 Dec 2025](https://www.latitudemedia.com/news/ercots-large-load-queue-has-nearly-quadrupled-in-a-single-year/); [New Project Media, May 2026](https://newprojectmedia.com/?p=19583)
- [R] Texas Gov. Abbott paused new data center interconnections in summer 2026 pending a queue audit; an estimated 191 GW of planned capacity is at risk in Texas, Ohio and Georgia; AEP Ohio's pipeline fell from over 30 GW to about 13 GW — [Utility Dive, 17 Nov 2026](https://www.utilitydive.com/news/data-center-slowdown-raises-risks-for-utility-investments/874924/)
- [R] AEP Ohio tariff (approved July 2025): loads above 25 MW pay for at least 85% of requested capacity for up to 12 years, with exit fees and financial guarantees — [same Utility Dive article](https://www.utilitydive.com/news/data-center-slowdown-raises-risks-for-utility-investments/874924/)
- [R] FERC issued show-cause orders in June 2026; on 13-16 November 2026 PJM, MISO, CAISO, NYISO and ISO-NE filed. PJM proposes a one-year combined load-plus-generation study ("about twice as fast"), ISO-NE would require large loads to bring their own new capacity, MISO and NYISO create non-firm or flexible service classes — [Utility Dive, 17 Nov 2026](https://www.utilitydive.com/news/pjm-rto-large-load-interconnection-ferc-show-cause/874872/)
- [R] PJM's market monitor says data center demand has raised capacity costs by $29.4B so far and that speculative data centers in the forecast could add $5-10B; consumer advocates want the December 2026 auction delayed — [Utility Dive, 19 Nov 2026](https://www.utilitydive.com/news/ratepayer-advocates-pjm-market-monitor-capacity-auction/875165/)
- [E] Generation projects in data center growth zones of PJM and ERCOT wait 3-4 years; over 300 GW across about 1,500 projects is queued — [Carbon Direct/Relae, 11 May 2026](https://relae.co/insight/ai-meets-the-grid-interconnection-queue-analysis-in-pjm-and-ercot)
- [S] PJM waits approach 7 years for large campuses in Northern Virginia — [Electric Choice](https://www.electricchoice.com/datacenters/interconnection-queue/)
- [S] PJM's reopened generation queue drew 811 projects totalling 220 GW (April 2026); withdrawn US queue capacity tops 1.8 TW — [S&P Global, 20 Aug 2026](https://www.spglobal.com/market-intelligence/en/news-insights/research/2026/08/us-interconnection-queue-reforms-make-impact-as-withdrawn-capacity-tops-1-8-tw)
- [R] Sites delayed by power: Oracle sent a force majeure notice on the 2.45 GW Project Jupiter (New Mexico) after a gas pipeline for its Bloom fuel cells slipped to 1 Feb 2027 and an air permit stayed pending — [TechCrunch, 24 Sep 2026](https://techcrunch.com/2026/09/24/oracle-sends-force-majeure-notice-on-its-new-mexico-stargate-data-center/)
- [V] Nebius's New Jersey site lost its schedule when temporary generation was retired before permanent power — [Nebius 6-K](https://www.sec.gov/Archives/edgar/data/0001513845/000110465926126008/tm2629571d1_ex99-2.htm)
- [R] Crusoe paused a 1.8 GW Wyoming campus (June 2026); OpenAI paused Stargate UK over energy costs — [NewMarketPitch](https://newmarketpitch.com/blogs/news/ai-data-center-who-is-ahead); [The Next Web](https://thenextweb.com/news/openai-856bn-compute-vs-600bn-reset-burn-improved)
- [R] At least 47 major US data center projects were delayed, withdrawn or blocked in 2026; more than 1,000 communities sought moratoriums or restrictions; Bernstein judges about 35% of the planned US pipeline credible — [Coin Edition citing FT, 19 Oct 2026](https://coinedition.com/u-s-ai-data-center-boom-faces-debt-risks-as-costs-rise-and-projects-stall/)
- [E] Build speed when power is on site: Abilene went from land clearing (May 2024) to first 103 MW building operational (Sep 2025) and about 824 MW by Nov 2026 — [Epoch AI](https://epoch.ai/data/ai-data-centers/directory/openai-stargate-abilene)

### Inferences
- Behind-the-meter gas and fuel cells are the standard workaround, and they now fail on their own inputs (pipelines, air permits, turbine slots to 2030-31).
- Local politics is now a first-order schedule risk: ballot measures, moratoriums and a governor's race in Texas all moved timelines in 2026.
- New non-firm and flexible-load service classes are being created in several RTOs at once. Whoever can make a campus qualify as flexible gets connected sooner.

### Gaps
- LBNL "Queued Up 2026" could not be parsed (file too large), so no LBNL median queue-duration figure is cited. No EIA load-growth figure was retrieved.
- No data for time to power outside the US beyond the UK and Norway anecdotes.
- The outcome of the Texas pause and of the FERC filings is unknown as of today.

## 6. Evidence of overbuild or a demand pause

### Takeaway
There is no demand pause in the operating data (GPU rents rising, backlogs up, capacity sold out). There is a financing pause: AI-related debt issuance fell from $113B in June to $23B in September 2026, CoreWeave paper yields 15%, and Oracle is using force majeure to defer rent.

### Cited Findings
- [R] Global AI-related debt issuance was $113B in June 2026 and $23B in September (FT) — [Coin Edition, 19 Oct 2026](https://coinedition.com/u-s-ai-data-center-boom-faces-debt-risks-as-costs-rise-and-projects-stall/)
- [R] CoreWeave bonds issued in June at 9.675% traded at about 15% in mid-October; shares fell about 16% on 14 Oct; S&P rates it B+; a hot inflation print the same day moved traders toward a December Fed hike — [Reuters via The Star, 16 Oct 2026](https://www.thestar.com.my/tech/tech-news/2026/10/16/coreweave-bond-rout-tests-market039s-math-on-ai-buildout); [InvestingLive](https://investinglive.com/stocks/coreweave-bonds-trade-like-distressed-debt-as-ai-spending-outpaces-balance-sheets/)
- [S] CoreWeave CDS reached roughly 1,000 bp in October — [Finviz](https://finviz.com/news/403777/coreweave-bond-yields-reach-15-as-investors-reassess-ai-infrastructure-financing-risks)
- [R] For comparison, CoreWeave five-year CDS peaked at 8.81 points in December 2025 and fell to 4.52 in June 2026, when Applied Digital sold $1.59B of bonds at 7% with a 5x book — [The Next Web, 11 Jun 2026](https://thenextweb.com/news/coreweave-credit-rebound-applied-digital-junk-bond-data-center)
- [R] Alphabet, Amazon, Meta and Oracle issued more than $228B of bonds in 2026 to 13 October, more than double all of 2025; Oracle 2032 notes yielded about 7.24% — [InvestingLive citing LSEG](https://investinglive.com/stocks/coreweave-bonds-trade-like-distressed-debt-as-ai-spending-outpaces-balance-sheets/)
- [R] Meta's $12.5B Sopaipilla data center bond drew only $20B of orders and priced at 7.50%; the earlier Beignet (Hyperion) bond moved from a 5.60% yield to 7.10% — [IFR](https://www.ifre.com/bonds/2463746/bond-market-begins-to-question-ai-boom-as-beignet-sequel-falls-flat)
- [R] About $18B of bank loans tied to Oracle's New Mexico campus are described as stressed; Oracle's notice could defer rent if the 2028 start is missed — [Coin Edition](https://coinedition.com/u-s-ai-data-center-boom-faces-debt-risks-as-costs-rise-and-projects-stall/); [TechCrunch](https://techcrunch.com/2026/09/24/oracle-sends-force-majeure-notice-on-its-new-mexico-stargate-data-center/)
- [S] Those loans reportedly traded near 90 cents on the dollar (FT via Gizmodo); Oracle five-year CDS reached about 203 bp, the highest since 2008 (date unclear) — [Gizmodo](https://gizmodo.com/ai-bubble-watch-oracle-seeks-financial-shield-from-massive-data-center-project-2000816870); [Sherwood](https://sherwood.news/tech/oracle-is-trying-really-hard-to-convince-investors-it-wont-have-a-debt-problem/)
- [R] Data center debt kept selling off in early October; hyperscaler CDS near the year's widest — [Bloomberg Law, 6 Oct 2026](https://news.bgov.com/bankruptcy-law/distress-watch-data-center-debt-selloff-snags-ai-buildouts)
- [R] Oracle needed PIMCO to anchor $10B of a $16.3B data center financing after US banks pulled back — [The Next Web](https://thenextweb.com/news/openai-856bn-compute-vs-600bn-reset-burn-improved)
- [R] Counter-evidence: Dan Ives estimates only 5-10% of planned projects will not be built; Wells Fargo says "an abrupt funding shutout looks remote" — [Reuters via The Star](https://www.thestar.com.my/tech/tech-news/2026/10/16/coreweave-bond-rout-tests-market039s-math-on-ai-buildout); [IFR](https://www.ifre.com/bonds/2463746/bond-market-begins-to-question-ai-boom-as-beignet-sequel-falls-flat)
- [R] Gartner: providers may spend about $7T on infrastructure through 2030 against at most $3.6T of related revenue, and more than $4T of assets could be written down through 2032 — [Coin Edition](https://coinedition.com/u-s-ai-data-center-boom-faces-debt-risks-as-costs-rise-and-projects-stall/)
- [R] Older precedent: Microsoft cancelled several hundred MW of US leases — this report is from 24 February 2025, not 2026 — [Capacity](https://capacityglobal.com/news/microsoft-cancels-ai-data-centre-leases-amid-oversupply-concerns-report/)
- [R] Nvidia leadership turbulence in November 2026: Jensen Huang resigned as CEO on 11 November with CFO Kress as interim; TrendForce reports on 24 November that he is returning — [Capacity](https://capacityglobal.com/news/nvidia-trims-neocloud-commitments/); [TrendForce](https://www.trendforce.com/news/2026/11/24/news-from-no-return-to-unanimous-yes-huang-retakes-nvidias-helm-key-dates-ahead-and-a-potential-new-playbook/)

### Inferences
- The stress is in the capital stack below investment grade and in single-tenant project debt, while physical capacity is still short. A company selling into the buildout should expect customers who want the product and cannot always finance it.
- CoreWeave's Q3 beat on 10 November partly reversed the October rout, so credit conditions are volatile, not closed.
- A large share of announced capacity is not real: 35% credible (Bernstein), over 300 GW of ERCOT requests with no studies, AEP Ohio's pipeline halved. Suppliers who booked against announcements carry double-ordering risk.

### Gaps
- No GPU-backed ABS deal data, residual-value assumptions or write-down amounts were retrieved (Morningstar page blocked).
- No 2026 hyperscaler lease cancellation was found other than Microsoft leaving Nscale's Loughton site. The FT issuance figures were read second-hand.

## 7. Startups founded 2022-2025 that reached $100M+ revenue within 24 months, and what they sold

### Takeaway
The verified list is short. The clearest cases are inference platforms selling tokens and dedicated GPU capacity on open models (Fireworks, Together, both about $1B annualized by mid-2026 on Sacra estimates) and one neocloud (Nscale, $140.6M in H1 2026, founded 2024). All of them resell scarce compute and needed hundreds of millions to billions of capital.

### Cited Findings
- [R] Nscale (founded 2024): H1 2026 revenue $140.6M from GPU capacity contracts; H1 loss $1.02B; about $3.7B equity raised — [NewMarketPitch](https://newmarketpitch.com/blogs/news/ai-data-center-who-is-ahead); [Sacra](https://sacra.com/research/nscale)
- [E] Fireworks AI (founded 2022): annualized revenue about $37M at end-2024, $305M at end-2025, about $1B by June-July 2026; gross margin about 50%; sells serverless per-token inference, fine-tuning and dedicated deployments; raised about $327M before its $1.5B Series D at $17.5B (July 2026) — [Sacra](https://sacra.com/c/fireworks-ai/)
- [E] Together AI (founded 2022; one field says 2021): annualized revenue about $618M at end-2025 and $1B in February 2026; gross margin about 45%; GPU server rental is the larger share and per-token API 30-40%; raised about $530M before its $800M Series C — [Sacra](https://sacra.com/c/together-ai/)
- [E] Baseten (founded 2019 or 2021, so outside the window): annualized revenue $200M in December 2025 and $600M in March 2026; inference volume grew 100x in 2025; $1.5B Series F at $13B in June 2026 — [Sacra](https://sacra.com/c/baseten/)
- [E] Outside the founding window but relevant benchmarks: Fluidstack $25M (2023) to $180M ARR (Dec 2024); Cerebras about $290M (2024) and $510M (2025), Q2 2026 revenue $180.1M, IPO May 2026, OpenAI contract over $20B — [Sacra Fluidstack](https://sacra.com/c/fluidstack/); [Sacra Cerebras](https://sacra.com/c/cerebras-systems/)
- [R] Gimlet Labs: $300M Series B at $3B for a multi-silicon inference cloud, $392M raised in total; no revenue disclosed — [ValueAdd VC, 6 Sep 2026](https://valueaddvc.com/pulse/ai-compute-4-8-billion-week-crusoe-fluidstack-gimlet-2026)

### Inferences
- Strictly, only Nscale is confirmed (via an IPO filing as reported) to have passed $100M of revenue within about 24 months of founding. Fireworks took about three years to pass a $100M run-rate, then went from $305M to $1B in roughly six months. Together's date of crossing $100M was not found.
- Every fast grower sold compute itself: tokens, GPU-hours or contracted megawatts. No hardware-component, power or cooling startup from 2022-2025 with $100M+ revenue was found in this research.
- Capital needed scales with how much of the stack is owned: about $0.3-0.5B for an asset-light inference platform to reach hundreds of millions of run-rate, about $3.7B of equity plus debt for a neocloud to reach $280M annualized.

Five plausible entry points for a company with $5-50M (synthesis of sections 1-7):
1. **Flexible-load and interconnection enablement** (controls, batteries and compliance that let a campus qualify for the new non-firm or fast-track service classes filed at FERC in November 2026). Main failure mode: the rules are not final, and utilities or hyperscalers build it in-house.
2. **Delivery and commissioning for third-party capacity** (rack integration, liquid-cooling and power commissioning, deployment tooling). Microsoft, Nebius and Nscale all missed numbers on late third-party sites. Main failure mode: it is a low-margin services business with concentrated customers exposed to the financing cycle.
3. **Collateral, pricing and risk infrastructure for compute finance** (GPU price data, residual-value monitoring, verification that guaranteed capacity is operational). Lenders hold $1.2T of lease exposure and say they cannot see the collateral. Main failure mode: deal flow collapses when issuance does ($113B to $23B in three months), and Ornn, Silicon Data and SemiAnalysis already publish indices.
4. **Inference cost reduction software** (memory-per-token and utilization gains, multi-silicon routing) sold to the inference platforms and enterprises squeezed between rising GPU rents and falling token prices. Main failure mode: labs and hyperscalers ship the same optimizations for free, and the memory cycle turns (NAND is already forecast to fall in 2027).
5. **Modular power packaging for the gap between site and grid** (medium-voltage skids, bridge-power integration, refurbished or alternative switchgear) where incumbents are booked through 2028. Main failure mode: it depends on the same scarce breakers, cores and turbines, incumbents' new plants arrive in 2028, and announced demand is 35% credible.

Becoming a neocloud or building chips is not a $5-50M entry: the smallest successful example needed about $3.7B of equity.

### Gaps
- No systematic list of 2022-2025 startups by revenue exists in the sources reached; Sacra figures are estimates. Lists of power, cooling or optics startups with $100M+ revenue could not be searched for.
- Founding dates conflict across sources for Together (2021/2022), Baseten (2019/2021) and Fluidstack (2017/2018).
