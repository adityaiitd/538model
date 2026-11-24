# Fast-ramp precedents (founded 2021–2025) and the AI lab data supply market, as of 24 Nov 2026

Reader notes
- Target ramp being tested: about $40M gross revenue within 12–18 months of first sale and about $100M within 36 months, on $5–10M of starting capital.
- Revenue labels: **run-rate / ARR** = annualized snapshot (latest month x12 or latest quarter x4), not recognized revenue. **Gross** = before contractor, supplier or user payouts. **Recognized** = booked for a period. **Cumulative fees** = lifetime protocol fees.
- Evidence tags: **[P]** primary (company statement, filing, first-party page). **[R]** reputable press or press quoted by an aggregator that names it. **[E]** third-party estimate (Sacra and similar). **[W]** weak: aggregator, vendor blog, or a figure seen only in a search-result summary where the page itself could not be opened.
- "Verified" in this file means [P] or [R] with the page opened. "Reported" means [R] via a secondary page. "Estimated" means [E]. Nothing here is audited except where a filing is named.
- Clocks differ by company (founding, launch, first $1M). True "months from first sale" is almost never disclosed. The clock used is stated in each row.
- Earlier notes at `research_notes/Hundred billion company simulation/ai_services.md` (sections 2, 3, 5) cover Cursor, Cognition, Harvey, Sierra, Decagon, Glean, OpenEvidence, Thrive Holdings, Long Lake and the first pass on Mercor, Handshake, Fleet. They are referenced, not repeated.
- Pages that refused to open (403 or paywall): fourweekmba.com, moneywise.com, pe-insights.com, deutsche-startups.de, newsbytesapp.com, ai2.work, arr.club, cryptobriefing.com, The Information, Sacra chat pages. Figures from them are tagged [W] and "via search summary".

---

## A1. Which companies hit roughly this ramp, and what happened next

### Takeaway
About 25 companies founded 2021–2025 reached roughly $40M within 18 months and $100M within 36 months of launch. The ones that did it on under $20M of equity fall into three groups: gross-billed expert labor and data for AI labs, self-serve AI apps, and thin consumer or trading front-ends on someone else's regulated or financial rails. No acquisition-led or equipment-leasing company was found that hit the ramp on small equity.

### Cited Findings

**Supplier to AI labs (expert data, RL environments)**

| Company (founded) | What is sold, to whom, unit | Ramp and revenue basis | Margin | Capital before ~$40M | Team | Status late 2026 | Sources |
|---|---|---|---|---|---|---|---|
| Mercor (Jan 2023) | Vetted experts and their output to frontier labs. Billed per contractor hour plus markup (~35% in Feb 2024) | Gross run-rate: $1M end-2023; $34.6M end-2024 [E]; $75M Feb 2025; ~$100M Mar 2025 (11 to 15 months from $1M, depending on source); $450M Sep 2025; $760M end-2025 [E]; $2B Jun 2026; $3B end-Oct 2026 [E]. Recognized gross H1 2026: $614M | Gross margin 27% in 2025, 33% in Q2 2026; ~two-thirds paid to contractors; $6M profit H1 2025 | About $33.6M (derived: $483.6M total less $100M Series B and $350M Series C; pre-B rounds not itemized) | 30 US staff + 20 India contractors at $50M ARR; 400+ now | Growing. March 2026 breach; Meta paused work indefinitely; contractor lawsuits; reported $20B round talks | [Sacra](https://sacra.com/c/mercor/) [E]; [Contrary](https://research.contrary.com/report/mercor) [R]; [New Market Pitch](https://newmarketpitch.com/blogs/news/ai-infrastructure-fastest-100m-arr) [W]; [Business Model Analyst citing The Information](https://businessmodelanalyst.com/ai-data-factories-physical-ai-margins/) [R]; [TechCrunch](https://techcrunch.com/2026/04/09/after-data-breach-10b-valued-startup-mercor-is-having-a-month) [R] |
| micro1 (2021; pivoted from an AI recruiter) | Expert data and RL work for labs incl. Microsoft; marks up expert labor | ~$7M ARR early 2025; under $50M Sep 2025; >$100M ARR Dec 2025 [P]; ~$300M Apr 2026 [E]; $500M gross run-rate Aug 2026 [R]; >$1B run-rate 12 Oct 2026 [P, gross vs net not stated] | Retains ~30–40% of gross, so ~$150–200M net at $500M gross; says profitable | $6.6M before a $35M Series A (Sep 2025, $500M valuation) | ~180 core staff at $1B | Growing. Series B at $4B. CEO says it "lost 60% of its revenue overnight" about three years earlier | [TechCrunch](https://techcrunch.com/2025/12/04/micro1-a-scale-ai-competitor-touts-crossing-100m-arr) [R]; [Sacra](https://sacra.com/c/micro1/) [E]; [Dealroom](https://dealroom.co/news/161913-micro1-passes-a-1b-run-rate-with-about-180-staff-three-years-after-nearl) [R]; [New Market Pitch](https://newmarketpitch.com/blogs/news/ai-training-data-business-model) [W] |
| AfterQuery (Jan–Feb 2025, YC W25; pivoted from finance agents) | Expert "reasoning" datasets and RL environments to labs; customers named: Nvidia, Thinking Machines Lab, Legora | $100M run-rate Apr 2026 (14–15 months from founding; gross vs net not stated) [P via press]; "hundreds of millions" by Jul 2026 [P, founder post] | One Forbes source says profitable | Not disclosed. Only YC and BoxGroup money before the $30M Series A announced at the $100M mark | ~30 [W] | $3.2B valuation round reported Sep 2026, not confirmed closed | [Dealroom](https://dealroom.co/news/127302-afterquery-hits-100m-run-rate-as-it-reveals-30m-series-a-backed-by-ai-la/) [R]; [Decrypt citing Forbes](https://decrypt.co/377231/afterquery-ai-tradining-data-unicorn-y-combinator) [R]; [New Market Pitch](https://newmarketpitch.com/blogs/news/ai-infrastructure-fastest-100m-arr) [W] |
| Fleet (founding date not found) | RL environments that replicate enterprise software, to labs and large enterprises | ~$1M annualized 2025 to ~$60M Apr 2026 (latest quarter x4) [E]. A Chinese investor note says it then "doubled again" and expects >$150M [W] | Not disclosed; each new domain needs engineering | $15M seed (Sequoia, Menlo, SV Angel) | Not disclosed | In talks for $50M+ at ~$750M; started with DeepMind computer-use work per [W] | [Sacra](https://sacra.com/c/fleet) [E]; [Shixiang note on Tencent News](https://news.qq.com/rain/a/20260804A08FN500) [W] |
| Handshake AI (new line inside a 2014 company) | Expert labor from an 18M-student network | AI training gross run-rate: $5–10M shortly after launch; $550M Jan 2026; ~$1B Apr 2026 | Net "approaches $300M" [R] vs ~$450M [E]; payouts 60–70% | Not a start-up; $434M raised historically | n/a | Growing; bought Cleanlab (Jan 2026) | [Dealroom citing The Information](https://dealroom.co/news/127345-handshakes-arr-crosses-1b-as-ai-training-revenue-surges/) [R]; [Sacra](https://sacra.com/research/handshake-indeed-for-data-labelers/) [E] |
| Surge AI (2021 per Sacra) | Per-task annotation and RLHF bundles to ~12 labs | $1.2B annualized in 2024 [E] | "Strong"; not quantified | $0; profitable and bootstrapped until a first raise sought in Jul 2025 | ~130 staff, ~50,000 contractors | No 2026 figure found | [Sacra](https://sacra.com/c/surge-ai) [E] |

**AI application, self-serve or per seat**

| Company (founded) | What, unit | Ramp (basis) | Margin | Capital before ~$40M | Team | Status | Sources |
|---|---|---|---|---|---|---|---|
| Lovable (2023; relaunched Nov 2024) | App builder, $25–$50/month | ARR: $7M end-2024; $17M Feb 2025; $100M Jul 2025 (8 months); $200M Nov 2025; $400M Mar 2026; $600M Sep 2026 | 36% gross May 2025 | $7.46M listed before the $200M Series A (Jul 2025); other small rounds may be unlisted | 45 at ~$200M | Growing; ~$950M raised | [Sacra](https://www.sacra.com/c/lovable) [E]; [AI Native GTM](https://ainativegtm.substack.com/p/benchmarking-fast-growing-ai-native) [W] |
| Bolt.new (pivot of StackBlitz, late 2024) | App builder subscription | $30M+ ARR in just over 4 months; $40M in 5 months | n/a | Not found | 20–24 | No 2026 figure found | [AIM, Mar 2025](https://analyticsindiamag.com/global-tech/ai-startups-hit-30m-200m-arr-in-quick-time-with-tiny-teams) [R]; [AI Native GTM](https://ainativegtm.substack.com/p/benchmarking-fast-growing-ai-native) [W] |
| Emergent (2025) | App builder | Run-rate: $15M at 3 months; $50M at 7; $100M at 8 (Feb 2026) | n/a | Not itemized; $230M raised in total | n/a | Growing | [Dealroom](https://dealroom.co/news/125967-emergent-hits-100m-arr-in-8-months-as-ai-coding-boom-accelerates/) [R] |
| Genspark | Agent workspace | $100M ARR in ~9 months; $155M at month 10 | n/a | $360M raised (timing unknown) | ~30–50 | Growing | [ProductLed](https://productled.com/blog/warp-speed-how-genspark-hit-155m-arr-in-10-months) [W]; [AI Native GTM](https://ainativegtm.substack.com/p/benchmarking-fast-growing-ai-native) [W] |
| Manus | General agent | $100M ARR ~8 months after launch (Dec 2025) | n/a | Not found | ~120 | — | [New Market Pitch](https://newmarketpitch.com/blogs/news/ai-infrastructure-fastest-100m-arr) [W] |
| Cursor (2022) | Coding, $20–$200/month | $100M ARR in ~20 months with ~20 staff; ~$4B by mid-2026 | Near zero until Apr 2026 | Not sourced here | 20 at $100M | Sold to SpaceX for $60B stock (earlier notes) | [AIM](https://analyticsindiamag.com/global-tech/ai-startups-hit-30m-200m-arr-in-quick-time-with-tiny-teams) [R]; [Sacra](https://sacra.com/c/cursor) [E] |
| Midjourney (2021–22) | Image generation, $10–$120/month | $200M ARR 2023 [E]; $500M listed Nov 2025 [W] | GPU-heavy, undisclosed | $0 external (page header conflicts with a "$50M" entry) | 11 [R] to 40–45 [E] | No decline data found | [Sacra](https://sacra.com/c/midjourney) [E]; [AIM](https://analyticsindiamag.com/global-tech/ai-startups-hit-30m-200m-arr-in-quick-time-with-tiny-teams) [R]; [AI Native GTM](https://ainativegtm.substack.com/p/benchmarking-fast-growing-ai-native) [W] |
| ElevenLabs (2022) | Voice, subscription and usage | ~$90M ARR with ~50 staff (Mar 2025); $330M end-2025; $600M Jun 2026 | n/a | Unknown; $80M Series B in Jan 2024 | 50 then 400 | Growing; $781M raised | [AIM](https://analyticsindiamag.com/global-tech/ai-startups-hit-30m-200m-arr-in-quick-time-with-tiny-teams) [R]; [Sacra](https://sacra.com/c/elevenlabs) [E] |
| Legora, Harvey, Sierra, Decagon, Glean, OpenEvidence | Per seat or per resolution | All passed $100M ARR within ~3 years (earlier notes) | Mostly undisclosed | Large: Harvey $1.01B, Sierra $635M raised | 200–350 | Growing | [AI Native GTM](https://ainativegtm.substack.com/p/benchmarking-fast-growing-ai-native) [W]; [New Market Pitch](https://newmarketpitch.com/blogs/news/ai-infrastructure-fastest-100m-arr) [W] |
| Arena | Model evaluation, consumption revenue | $100M annualized ~8 months from commercial launch (Jun 2026); CEO says it is not recurring | n/a | n/a | n/a | $200M Series B Oct 2026 | [New Market Pitch](https://newmarketpitch.com/blogs/news/ai-infrastructure-fastest-100m-arr) [W] |
| Jasper (2021) | AI copywriting subscription | ~$72–80M ARR in 2022; had forecast $140M | n/a | Raised $125M at $1.5B in Oct 2022 | n/a | **Stalled**: 2023 forecast cut 30%+, layoffs Jul 2023, 2024 revenue estimates $35–55M | [Maginative](https://www.maginative.com/article/jasper-cuts-internal-valuation-as-ai-growth-slows/) [R]; [Voicebot](https://voicebot.ai/2023/07/17/jasper-ai-laying-off-staff-9-months-after-125m-raise/) [R]; [Sacra](https://sacra.com/research/copy-ai-jasper-ai-writing-tools) [E] (figures via search summary) |

**Consumer cash-pay, trading venues, reseller, leasing, roll-up, contingency**

| Company (founded) | Model | Ramp (basis) | Margin | Capital | Team | Status | Sources |
|---|---|---|---|---|---|---|---|
| Medvi (launched Sep 2024) | Consumer cash-pay compounded GLP-1 telehealth, from $179 first month; clinicians, pharmacy and compliance outsourced to CareValidate and OpenLoop; Facebook ads | $401M sales in 2025 (gross; NYT says it reviewed financials); projected $1.8B for 2026 | $65M net profit, 16.2% | $20,000, no outside funding | 2 | **At risk**: FDA warning letter 20 Feb 2026; lawsuits; AI-generated doctor ads; 250,000-patient data exposure; FDA narrowing the compounding exemption | [Dealroom citing NYT and Forbes](https://dealroom.co/news/127216-from-20k-to-1-8b-in-revenue-how-one-founder-built-a-telehealth-giant-wit/) [R]; [Drug Discovery & Development](https://www.drugdiscoverytrends.com/the-new-york-times-spotlighted-medvi-the-fda-had-already-warned-the-self-proclaimed-fastest-growing-company-in-history/) [R] |
| Axiom (YC W25, launched Jan–Feb 2025) | Solana trading terminal, 0.75–0.95% fee per swap | $100M cumulative fees in under 4 months (gross; up to 43% returned to users as rewards); $200M by day 202 and $300M by day 263 [W] | Net well below gross | $500K pre-seed | 2 founders | No 2026 trend found | [The Block](https://theblock.co/post/355676/axiom-exchange-hits-100-million-in-revenue-just-four-months-after-launch) [R]; [Sacra](https://sacra.com/c/axiom) [E]; [RootData](https://www.rootdata.com/projects/detail/axiom?k=MTM1ODQ%3D) [W]; [Phemex](https://phemex.com/news/article/axiom-exchange-sets-record-with-300m-revenue-in-263-days-25598) [W] |
| Hyperliquid (2023) | Perpetuals exchange, fee on volume | Retained revenue $10.5M in 2024, $818M in 2025 (of $972M gross fees), $403M through Aug 2026 | ~84% of fees retained in 2025, falling in 2026 | $0 venture | 11 | Below 2025 pace ($403M in eight months); retained share shrinking as builder markets grow | [Sacra](https://sacra.com/c/hyperliquid) [E]; [crypto.news](https://crypto.news/hyperliquid-how-an-11-person-crypto-dex-generates-over-1-billion-a-year/) [R] |
| Pump.fun (2024) | Memecoin launchpad, fee on trades | $100M cumulative in ~8 months; ~$651M in 2025; ~$476M annualized pace in Mar 2026 | Most revenue spent on token buybacks | Not found pre-ramp; $600M token sale later | n/a | Down from 2025 pace; token down 77% from high | [Sherwood](https://sherwood.news/crypto/meme-coin-factory-pump-fun-passes-usd1-billion-in-revenue/) [R]; [The Block](https://theblock.co/post/355676/axiom-exchange-hits-100-million-in-revenue-just-four-months-after-launch) [R]; [Blockworks](https://blockworks.co/news/pump-fun-500m-ico-twitch) [R] |
| Fuse Energy (2022) | Retail electricity and gas supplier with own trading and generation (principal reseller) | $90M annual revenue before its latest round; >$300M ARR Sep 2025; $400M ARR Dec 2025 [P via W] | Not disclosed | $100M raised in total by Sep 2025 | n/a | Growing; ~$5B valuation Dec 2025 | [BusinessCloud](https://businesscloud.co.uk/news/revolut-executives-fuse-energy-powers-past-300m-revenue/) [R]; [DataCentreNews UK](https://datacentrenews.uk/story/fuse-energy-hits-5bn-valuation-plans-international-expansion) [W, via search summary] |
| Fluidstack (2018, outside window; ramp 2023–24) | GPU capacity: brokers third-party GPUs and owns private clusters | $25M 2023 to $180M ARR Dec 2024 [E] | Marketplace low margin; private cloud higher | Ramp funded by $3M seed, $24.7M SAFE, $37.5M debt | n/a | Growing; up to $10B GPU-secured debt capacity | [Sacra](https://www.sacra.com/c/fluidstack) [E] |
| TensorWave (Dec 2023) | AMD GPU rental at $1.50–$2.25 per GPU-hour | ~$5M run-rate 2024; company **projected** >$100M run-rate by end-2025 (outcome not confirmed) | n/a | $43M SAFE + $100M Series A; one cluster estimated at ~$365M | n/a | $350M Series B reported Jun 2026 [W] | [The Next Platform](https://www.nextplatform.com/compute/2025/05/16/how-is-neocloud-tensorwave-paying-for-its-fairly-large-amd-cluster/1633111) [R]; [multiples.vc](https://multiples.vc/private-comps/tensorwave) [W] |
| General Compute (2026) | Bare-metal inference capacity | One customer contract worth $100M ARR | n/a | $100M Series A + $400M chip debt facility | n/a | Early | [TechCrunch](https://techcrunch.com/2026/10/27/general-compute-raises-100-million-series-a-countering-the-neocloud-disaster-narrative/) [R] |
| Crete Professionals Alliance, now "Current" (2023) | Accounting-firm roll-up backed by Thrive | 40+ firms; "$300M+" revenue (2025 secondary, earlier notes). Partner firm Reid Advisors went $25M to $55M via six acquisitions in a year | n/a | Institutional (Thrive, Bessemer) | n/a | Still acquiring | [CPA Practice Advisor](https://www.cpapracticeadvisor.com/tag/crete/) [R, via search summary]; [Business Wire](https://www.businesswire.com/news/home/20260128993106/en/) [P, via search summary] |
| Innovation Refunds (ERC claims) | Contingency: 25% of the tax refund once paid | Processed >$4B of claims by May 2023, "nearly $7B" later; company revenue not disclosed | n/a | n/a | n/a | **Collapsed with the program**: IRS moratorium 14 Sep 2023, then >40% of staff laid off and ads paused | [CNBC](https://www.cnbc.com/2023/10/27/how-innovation-refunds-cashed-in-on-the-employee-retention-credit.html) [R] |

- Scale AI is the reference case for customer flight: Google (about $150M spend in 2024, $200M planned for 2025) and OpenAI cut ties after Meta bought 49% for $14.3B in June 2025; Scale then cut ~200 staff (14%) and 500 contractors [E] — [Sacra](https://sacra.com/research/scale-ai)
- Appen precedent: 2025 operating revenue $230.8M after a $4.3B valuation in 2020 [W] — [New Market Pitch](https://newmarketpitch.com/blogs/news/ai-training-data-business-model)

### Inferences
- Gross versus net changes the answer. Mercor at $100M gross was roughly $30M net; Axiom's $100M of fees was up to 43% rebated; Medvi's $401M includes drug cost. The founder's $40M and $100M targets are gross, which favors pass-through models.
- AI app companies that hit the ramp did so on product virality, not enterprise sales, and most had 20–50 staff at $40M. A founder without proprietary technology has no obvious way into that group.
- Lab suppliers reached $40M with 30–50 staff and under ~$35M raised, and their buyers are a handful of large accounts. That matches an enterprise-sales skill set better than any other group.

### Gaps
- Capital raised before $40M is not disclosed for Cursor, Bolt, AfterQuery, Emergent, Genspark, Manus. Mercor's figure is derived, not reported.
- No verified founding-era revenue for Innovation Refunds or other ERC firms; no revenue found for any firm working IEEPA tariff refunds on contingency.
- Gamma ($100M ARR, ~50 staff, profitable) and Lovable's "45 people at $100M" appeared only in search summaries.
- Bolt.new and Manus 2026 status not found.

---

## A2. Grouping by model: which hit the ramp most often on under $20M raised

### Takeaway
On under $20M of equity, the verified or reported hits are: lab data suppliers (micro1, Fleet, Surge, probably AfterQuery), self-serve AI apps (Lovable, Midjourney), and thin consumer or trading front-ends (Medvi, Axiom, Hyperliquid). Roll-ups, GPU leasing and energy retail reached the revenue but needed $100M or more of equity or debt.

### Cited Findings

| Model | Hit ~$40M in 18 months | Of which on under $20M equity | Typical gross margin | Sources |
|---|---|---|---|---|
| Supplier to AI labs | Mercor, micro1, AfterQuery, Fleet, Handshake AI, Surge | micro1 ($6.6M until a $35M Series A in Sep 2025, when ARR was still under $50M), Fleet ($15M seed), Surge ($0); AfterQuery likely (seed size undisclosed); Mercor about $33.6M | 27–40% on labor resale; higher on reusable datasets (micro1 claims 80–90% on some off-the-shelf sets [W]) | [Sacra micro1](https://sacra.com/c/micro1/); [Sacra Fleet](https://sacra.com/c/fleet); [Sacra Surge](https://sacra.com/c/surge-ai); [New Market Pitch](https://newmarketpitch.com/blogs/news/ai-training-data-business-model) |
| AI app, self-serve subscription | Lovable, Bolt, Emergent, Genspark, Manus, Cursor, Midjourney, ElevenLabs | Lovable ($7.46M listed), Midjourney ($0); others unknown or large | 0–36% where inference is the main cost | [Sacra Lovable](https://www.sacra.com/c/lovable); [Sacra Midjourney](https://sacra.com/c/midjourney) |
| AI app, enterprise per seat or outcome | Harvey, Sierra, Decagon, Legora | None found | Undisclosed | [AI Native GTM](https://ainativegtm.substack.com/p/benchmarking-fast-growing-ai-native) |
| Consumer cash-pay | Medvi | Medvi ($20K) | 16% net | [Dealroom](https://dealroom.co/news/127216-from-20k-to-1-8b-in-revenue-how-one-founder-built-a-telehealth-giant-wit/) |
| Trading venue or marketplace (crypto) | Axiom, Pump.fun, Hyperliquid | Axiom ($500K), Hyperliquid ($0) | 41–84% of fees retained | [The Block](https://theblock.co/post/355676/axiom-exchange-hits-100-million-in-revenue-just-four-months-after-launch); [Sacra Hyperliquid](https://sacra.com/c/hyperliquid) |
| Reseller or principal | Fuse Energy; Fluidstack marketplace | None (Fuse $100M; Fluidstack ~$28M equity plus $37.5M debt) | Low on brokered volume | [BusinessCloud](https://businesscloud.co.uk/news/revolut-executives-fuse-energy-powers-past-300m-revenue/); [Sacra Fluidstack](https://www.sacra.com/c/fluidstack) |
| Equipment rental or leasing (GPUs) | TensorWave (projected only), General Compute (one contract) | None | n/a | [The Next Platform](https://www.nextplatform.com/compute/2025/05/16/how-is-neocloud-tensorwave-paying-for-its-fairly-large-amd-cluster/1633111); [TechCrunch](https://techcrunch.com/2026/10/27/general-compute-raises-100-million-series-a-countering-the-neocloud-disaster-narrative/) |
| Acquisition-led roll-up | Crete/Current, Thrive Holdings platforms, Long Lake | None | Target-level EBITDA | [TechCrunch](https://techcrunch.com/2026/08/12/openai-backed-thrive-holdings-raises-2b-to-bring-ai-to-the-enterprise/) |
| Outcome or contingency | Innovation Refunds (claims volume only) | Unknown | 25% of refund, shared with tax attorneys | [CNBC](https://www.cnbc.com/2023/10/27/how-innovation-refunds-cashed-in-on-the-employee-retention-credit.html) |

### Inferences
- Count of sub-$20M hits by model: lab supply 3–4, self-serve AI apps 2, crypto venues 2, consumer cash-pay 1, everything else 0.
- The common feature of every small-capital hit is that the customer pays before or as the cost is incurred (contractors paid after the lab is billed, subscribers pay upfront, trading fees are instant). Working capital, not equity, is what the $5–10M would fund.
- Leasing and roll-ups can be financed with debt, which fits a capital-markets founder, but the evidence shows equity of $100M+ came first in every case found.

### Gaps
- No complete list exists of failures by model, so hit rates are survivor counts, not probabilities.
- Payment terms that labs give suppliers (days to pay) were not found; they determine how far $5–10M stretches.

---

## A3. Acquisition-led cases and prices paid

### Takeaway
Roll-ups founded 2023–2024 reached nine-figure revenue quickly but only with institutional capital, and none disclosed purchase prices. Broker data puts small IT-services targets at about 5.5–8x EBITDA and $10–25M-revenue targets at 9–13.5x; no revenue multiples for operating firms were found.

### Cited Findings
- Thrive Holdings: $2B raised at $12B (Aug 2026), 70+ businesses; accounting platform has 50+ firms [R] — [TechCrunch](https://techcrunch.com/2026/08/12/openai-backed-thrive-holdings-raises-2b-to-bring-ai-to-the-enterprise/)
- Crete, founded 2023 and rebranded "Current" in June 2026, serves 40+ firms; partner Reid Advisors grew from about $25M to $55M through six acquisitions between Jan 2025 and Jan 2026 [R/P, via search summary] — [CPA Practice Advisor](https://www.cpapracticeadvisor.com/tag/crete/); [Business Wire](https://www.businesswire.com/news/home/20260128993106/en/)
- Long Lake: 40 acquisitions in about 2.5 years, no financials disclosed [P] — [General Catalyst](https://www.generalcatalyst.com/stories/manufacturing-outliers-long-lake)
- Beacon Software raised $250M to buy profitable software firms with under $20M of recurring revenue [R, via search summary] — [Yahoo](https://www.yahoo.com/news/articles/beacon-software-raises-250-million-101047785.html)
- MSP multiples, adjusted EBITDA, 2024 to Q2 2026: 5.5–8.0x at $1–3M revenue; 6–11x at $3–10M; 9–13.5x at $10–25M; 11–14.5x above $25M. All below 2020–2022 peaks. Broker guide built from anonymized aggregates [W] — [CT Acquisitions](https://www.ctacquisitions.com/guides/msp-ma-multiples-2026/)
- Accounting: 90% of executives are involved in acquisition decisions; multiples "have risen" with private-equity competition, no figures given [R] — [William Blair](https://www.williamblair.com/Insights/Private-Equity-M-and-A-and-the-New-Shape-of-Accounting)
- Six or so top venture firms were backing roll-ups by mid-2025 [R] — [Newcomer](https://www.newcomer.co/p/ai-roll-up-deals-accelerate-as-top)

### Inferences
- At 6–8x EBITDA, and assuming 15–20% EBITDA margins (an assumption, not sourced), buying $40M of revenue costs roughly $36–64M before debt (arithmetic on the broker ranges, not a reported figure). With 50–60% leverage the equity need is still above $10M, so the $50M post-validation tranche, not the first $5–10M, is what makes this model reachable.
- The founder would bid against Thrive, General Catalyst and Bessemer-backed buyers that have lab partnerships and cheaper capital.

### Gaps
- No disclosed purchase price or multiple for any Crete, Long Lake, Titan or Shield deal.
- A claim that some AI roll-ups reached $100M EBITDA within two years comes from one page that could not be opened ([deutsche-startups](https://www.deutsche-startups.de/2026/05/18/roll-ups-die-neue-goldgrube-der-startup-szene/)) and is unverified.

---

## A4. Which collapsed or stalled after a fast start, and why

### Takeaway
Fast starts failed for four reasons: a platform owner entered (Jasper), a rule changed (Innovation Refunds, and now Medvi's exposure), one or two customers left (Scale, micro1's early crisis, Mercor with Meta), or the fee pool was speculative volume (Pump.fun, Hyperliquid's retained share).

### Cited Findings
- Jasper: ARR about $72–80M in 2022 against a $140M forecast; ChatGPT's launch removed prosumer demand; 2023 forecast cut at least 30%; layoffs July 2023 [R, via search summary] — [Maginative](https://www.maginative.com/article/jasper-cuts-internal-valuation-as-ai-growth-slows/); [Voicebot](https://voicebot.ai/2023/07/17/jasper-ai-laying-off-staff-9-months-after-125m-raise/)
- Innovation Refunds: laid off more than 40% of staff and paused advertising days after the IRS moratorium of 14 Sep 2023 [R] — [CNBC](https://www.cnbc.com/2023/10/27/how-innovation-refunds-cashed-in-on-the-employee-retention-credit.html)
- Medvi: FDA warning letter (20 Feb 2026) for misbranding; FDA statement of 1 Apr 2026 targets the vitamin-B12 compounding workaround; spam and consumer suits filed; Meta ads fell from 5,000+ to about 2,800 after press scrutiny [R] — [Drug Discovery & Development](https://www.drugdiscoverytrends.com/the-new-york-times-spotlighted-medvi-the-fda-had-already-warned-the-self-proclaimed-fastest-growing-company-in-history/)
- Scale AI: its two largest customers left after the Meta deal; staff and contractor cuts followed in July 2025 [E] — [Sacra](https://sacra.com/research/scale-ai)
- Mercor: Meta paused all work indefinitely after the March 2026 breach; OpenAI investigated but did not pause; other labs reported to be weighing the relationship [R] — [TechCrunch](https://techcrunch.com/2026/04/09/after-data-breach-10b-valued-startup-mercor-is-having-a-month)
- Mercor's Meta project "Musen" ended 11 Nov 2025 with 5,000+ contractors at peak; workers were offered a successor project at $16 an hour, $5 less [R] — [Business Insider via AOL](https://www.aol.com/articles/ai-startup-powering-meta-openai-230627434.html)
- micro1 "lost 60% of its revenue overnight" about three years before reaching $1B [P] — [Dealroom](https://dealroom.co/news/161913-micro1-passes-a-1b-run-rate-with-about-180-staff-three-years-after-nearl)
- Pump.fun: 2026 pace about $476M versus $651M in 2025 [R] — [Sherwood](https://sherwood.news/crypto/meme-coin-factory-pump-fun-passes-usd1-billion-in-revenue/)
- CoreWeave stock at a 12-month low in Oct 2026 with $35B of debt at 30 Jun 2026; Elon Musk predicted "200+ neoclouds" face consolidation [R] — [TechCrunch](https://techcrunch.com/2026/10/27/general-compute-raises-100-million-series-a-countering-the-neocloud-disaster-narrative/); [Capacity](https://capacityglobal.com/news/coreweaves-debt-hits-35bn/) [via search summary]

### Inferences
- In lab supply the failure is abrupt and customer-driven, not gradual: revenue disappears in days when one buyer pauses.
- Regulatory-arbitrage models (ERC claims, compounded GLP-1s) produce the highest revenue per dollar of capital and the shortest lives.

### Gaps
- No named neocloud bankruptcy in 2026 was found.
- No data on how many RL-environment start-ups have shut down.

---

## B1. 2026 spend on human data, RL environments, evaluation and physical-world data; supplier revenue

### Takeaway
Disclosed supplier run-rates imply labs and large tech companies buy roughly $7–9B a year of external human data (gross, an inference from the figures below). Anthropic's own filing shows its data and evaluation vendor costs rose by $757M year on year in nine months. Robotics data is funded but small in revenue terms, and the largest robotics buyer disclosed (Figure) built in-house.

### Cited Findings

**Buyer spend**
- Anthropic S-1/A: vendor costs "related to data quality and performance evaluation services" rose $757M in the nine months to 30 Sep 2026 versus the same period of 2025; the first S-1 showed a $251M rise for H1. Implied Q3 rise of about $506M is the analyst's subtraction. Booked in "other operating and administrative" [W: secondary reading of the filing, seen via search summary; not checked against EDGAR] — [FourWeekMBA](https://fourweekmba.com/ai-anthropics-data-vendor-costs-rose-506m-yoy-in-q3-2x-h1/)
- Anthropic discussed spending over $1B on RL environments in the year from Sep 2025 [R] — [Epoch AI](https://epoch.ai/gradient-updates/state-of-rl-envs). A venture note instead estimated tens of millions a year in 2025 growing 3–5x in 2026 [W] — [Wing VC](https://www.wing.vc/content/rl-environments-for-agentic-ai-who-will-win-the-training-verification-layer-by-2030). Not reconciled.
- Several US frontier labs each spend on the order of $1B a year on external data; the top human-data vendors take over 60% of that; pilots run from a few hundred thousand dollars to $1M and mature programs from several million to tens of millions [W, investor research note] — [Shixiang on Tencent News](https://news.qq.com/rain/a/20260804A08FN500)
- OpenAI outspends other labs on data but uses fewer vendors; Anthropic uses more than a dozen RL-environment vendors [R] — [SemiAnalysis, Jan 2026](https://newsletter.semianalysis.com/p/rl-environments-and-rl-for-science)
- Google expected to spend about $200M with Scale in 2025 before leaving [R] — [New Market Pitch citing Reuters](https://newmarketpitch.com/blogs/news/ai-training-data-business-model)
- Figure committed "over $1B the next 12 months on data and compute" and had paid $15M to video contributors by 25 Aug 2026 [P] — [Figure](https://figure.ai/news/introducing-index)

**Supplier revenue, 2026**

| Supplier | Latest figure | Basis | Source |
|---|---|---|---|
| Mercor | $3B annualized end-Oct 2026; $614M H1 2026; 33% gross margin Q2 | Gross; estimate, then internal documents | [Sacra](https://sacra.com/c/mercor/) [E]; [Business Model Analyst](https://businessmodelanalyst.com/ai-data-factories-physical-ai-margins/) [R] |
| Handshake AI | ~$1B Apr 2026 | Gross run-rate | [Dealroom](https://dealroom.co/news/127345-handshakes-arr-crosses-1b-as-ai-training-revenue-surges/) [R] |
| micro1 | >$1B 12 Oct 2026 | Run-rate, gross vs net unstated | [Dealroom](https://dealroom.co/news/161913-micro1-passes-a-1b-run-rate-with-about-180-staff-three-years-after-nearl) [P] |
| Surge | $1.2B (2024) | Annualized estimate; no 2026 figure | [Sacra](https://sacra.com/c/surge-ai) [E] |
| Scale | $2B in 2025 (estimate) vs CEO expecting ">$1B" in 2026 | Conflicting | [Sacra](https://sacra.com/research/scale-ai) [E]; [KuCoin](https://www.kucoin.com/news/flash/scale-ai-revenue-expected-to-exceed-1-billion-in-2026-as-enterprise-ai-applications-grow) [W] |
| Turing | >$300M ARR Dec 2025 | Company; no 2026 figure | [Frontier Ventures](https://frontier.ventures/turing-surpasses-300m-arr-in-a-profitable-year-scaling-for-the-future-of-ai/) [P, via search summary] |
| Invisible | $134M (2024) | No reliable 2026 figure | [Enterprise DNA](https://enterprisedna.co/resources/ai-map/data) [W] |
| Snorkel | >$350M, reported $375M, Sep 2026 | Run-rate, company | [Enterprise DNA](https://enterprisedna.co/resources/ai-map/data) [W]; [New Market Pitch](https://newmarketpitch.com/blogs/news/ai-training-data-business-model) [W] |
| Fleet | ~$60M Apr 2026 | Quarter x4 | [Sacra](https://sacra.com/c/fleet) [E] |
| AfterQuery | "hundreds of millions" Jul 2026 | Founder statement | [Decrypt](https://decrypt.co/377231/afterquery-ai-tradining-data-unicorn-y-combinator) [R] |
| Appen | A$119.9M H1 2026 | Recognized, ASX filing | [Enterprise DNA](https://enterprisedna.co/resources/ai-map/data) [W] |

**Physical-world data**
- Scale: 10 robotics customers added in 2025, 150,000+ hours delivered, now 1,000+ demonstration hours a day; customers include Physical Intelligence, Generalist AI and Cobot [P via W] — [New Market Pitch](https://newmarketpitch.com/blogs/news/ai-training-data-business-model); [Sacra](https://sacra.com/research/scale-ai)
- XDOF (founded Oct 2024): $70M raised, ~60 staff, ~20 customers including several frontier labs; revenue undisclosed [R] — [TechCrunch](https://techcrunch.com/2026/06/17/collecting-robot-training-data-is-dirty-unglamorous-work-some-ai-labs-are-already-paying-xdof-to-do-it/)
- Memories.ai: $16M raised; 1M+ hours of first-person video in its first beta month; sells to three of the top five labs [R] — [Fortune, 10 Nov 2026](https://fortune.com/2026/11/10/exclusive-in-the-race-for-robot-training-data-ex-meta-researchers-startup-turns-to-gig-workers-with-cameras/)
- Encord: $60M at $550M (Feb 2026); physical-AI revenue up tenfold [R] — [Business Model Analyst](https://businessmodelanalyst.com/ai-data-factories-physical-ai-margins/)
- Dyna Robotics pretrained on 1M+ hours of egocentric video; task score rose from 20% to 53% between 1,000 and 1,000,000 hours [W, vendor blog citing Dyna] — [CloudPano](https://www.cloudpano.com/blog/why-robotics-labs-are-buying-egocentric-video)
- Lightwheel (China): revenue above RMB100M in 2025, and Q1 2026 above all of 2025 [W, via search summary] — [GII Research](https://www.giiresearch.com/report/rinc2027361-embodied-artificial-intelligence-eai-robot-data.html)

### Inferences
- Sum of 2026 run-rates (Mercor ~$3B, Handshake ~$1B, micro1 ~$1B, Surge ~$1B+, Scale ~$1–2B, Turing, Snorkel, AfterQuery, Invisible) is about $7–9B gross, up from the $5–7B inferred in the earlier notes. Definitions differ, so treat this as an order of magnitude.
- If the Anthropic vendor-cost figures are right, one lab's data and evaluation spend is running well above $1B a year and rising faster in Q3 than in H1.
- Robotics data has buyers with budgets (Figure's $1B covers data and compute together) but no supplier has disclosed revenue near $40M.

### Gaps
- No split of lab spend between expert data, RL environments, evaluation and robotics.
- No OpenAI, Google, Meta or xAI data-spend figure for 2026.
- No revenue for any robotics-data supplier except Lightwheel. A claim that micro1 collects 160,000+ hours of chore video a month (attributed to MIT Technology Review, April 2026) appeared only in a search summary with no page identified.
- One profile attributes a "$2B gross run-rate in June 2026" to Turing; this matches Mercor's figure and looks like a mislabel ([Enterprise DNA](https://enterprisedna.co/resources/ai-map/company/turing)).

---

## B2. Under-supplied domains and prices

### Takeaway
Buyers and suppliers describe shortage in four places: real expert workflow data (traces of actual work), quality control for long-horizon tasks, physical-world data at scale and diversity, and wet-lab science data. Prices are documented for environments and expert hours; no per-trajectory price was found.

### Cited Findings

**What is short**
- The market has "a shortage of high-quality supply, not of budget"; the newest demand is process data from real workflows (browser traces, Slack and ERP records, private codebases); themes rotate every few months (computer use, coding, automated research); Anthropic bought heavily in cybersecurity in Jan 2026 and biology in Mar–Apr 2026 [W] — [Shixiang on Tencent News](https://news.qq.com/rain/a/20260804A08FN500)
- Observed expert behavior on real white-collar work, good QA for unverifiable and long-horizon tasks, and niche-language goal-oriented audio are in "short supply"; many labs now want raw data and build environments themselves [R, practitioner, Feb 2026] — [Sean Cai](https://seanzcai.substack.com/p/an-ai-bubble-is-a-human-data-problem)
- Coding is highest demand; computer use, ML tasks and creative domains follow; finance, healthcare, chip design, accounting and health-record workflows are expanding; biology and materials need physical lab data at hundreds to thousands of dollars per experiment [R] — [SemiAnalysis](https://newsletter.semianalysis.com/p/rl-environments-and-rl-for-science)
- "Finding the experts isn't that hard, but managing them and doing quality control is hard"; many vibe-coded environments are "useless"; long-horizon tasks are "the future direction" [R, interviews] — [Epoch AI](https://epoch.ai/gradient-updates/state-of-rl-envs)
- Robotics: "Vendors couldn't hit the throughput, diversity, or quality bar Helix requires, so we built the pipeline ourselves" [P] — [Figure](https://figure.ai/news/introducing-index). XDOF's CEO says robot data needs warehouses with hundreds of robots [R] — [TechCrunch](https://techcrunch.com/2026/06/17/collecting-robot-training-data-is-dirty-unglamorous-work-some-ai-labs-are-already-paying-xdof-to-do-it/)
- Encord estimates densely annotated data is worth about 100x raw egocentric footage for a task and costs about 20x more to make [R] — [Business Model Analyst](https://businessmodelanalyst.com/ai-data-factories-physical-ai-margins/)
- Non-English text is described as sourceable and machine-translatable, so not scarce [R] — [SemiAnalysis](https://newsletter.semianalysis.com/p/rl-environments-and-rl-for-science)

**Prices**
- RL environments: website clone about $20K (OpenAI bought hundreds); complex enterprise replica several hundred thousand dollars; tasks a few hundred to a few thousand dollars each; contracts six to seven figures per quarter; exclusivity costs several times more [R] — [SemiAnalysis](https://newsletter.semianalysis.com/p/rl-environments-and-rl-for-science); [Sapphire Ventures, Apr 2026](https://sapphireventures.com/?p=258819)
- Expert pay (cost side): Mercor average $85–95 an hour, up to $200; micro1 near $100; Handshake at least $50 on an OpenAI-related project; Deccan $10–700; Surge 30–40 cents per working minute; generalist projects $16–21 an hour; QA often $20 an hour [R/W] — [Contrary](https://research.contrary.com/report/mercor); [TechCrunch](https://techcrunch.com/2025/12/04/micro1-a-scale-ai-competitor-touts-crossing-100m-arr); [New Market Pitch](https://newmarketpitch.com/blogs/news/ai-training-data-business-model); [Sacra](https://sacra.com/c/surge-ai); [AOL](https://www.aol.com/articles/ai-startup-powering-meta-openai-230627434.html); [Sean Cai](https://seanzcai.substack.com/p/an-ai-bubble-is-a-human-data-problem)
- First-person video collection pay: up to $20 an hour (Craigslist ad), up to $50 an hour (micro1), about $150 an hour for technical tasks such as surgical equipment (Encord); unused creator footage $1–4 a minute (dated Oct 2025) [R] — [Entrepreneur](https://www.entrepreneur.com/business-news/ai-robotics-companies-will-pay-to-watch-you-cook-and-clean/498204)
- Automated labeling of robot video listed at $9 per video-hour, about $29 with add-ons [W, vendor list price via search summary] — [FourWeekMBA](https://fourweekmba.com/ai-perceptron-puts-robot-video-labels-at-9-an-hour-astra-76/)
- Licensed operational datasets: from about $50K for small sets to $1M+ for enterprise partnerships [W] — [New Market Pitch](https://newmarketpitch.com/blogs/news/ai-training-data-business-model)

### Inferences
- The shortage is in supervision and provenance (QA, real workflow traces, physical capture), not in headcount of experts. A sales-led entrant adds most value where it can contract for data that enterprises already own, since most real-world data contracts are non-exclusive and resellable.
- Chip design, science and health records are named as expanding but no price or volume evidence was found; these are leads, not validated gaps.

### Gaps
- No price per computer-use trajectory or per robot trajectory was found.
- Buyer prices per hour of egocentric or teleoperation data were not found in any page that opened. A range of $3–25 per worker-hour for egocentric video and $118–200 per loaded hour for teleoperation appeared in a search summary with no identifiable page.
- No buyer statement on voice data or chip-design data shortages.

---

## B3. How fast the newest entrants reached $10M and $40M; contracts and concentration

### Takeaway
The fastest recent entrant (AfterQuery) went from founding to a $100M run-rate in 14–15 months with about 30 people; Fleet went from $1M to $60M in about six months. Every supplier with disclosed data depends on a handful of buyers.

### Cited Findings
- AfterQuery: founded Jan–Feb 2025; $100M run-rate Apr 2026; "multiples past" that by 12 Jul 2026; $30M Series A; ~100,000 verified professionals [R] — [Dealroom](https://dealroom.co/news/127302-afterquery-hits-100m-run-rate-as-it-reveals-30m-series-a-backed-by-ai-la/); [Decrypt](https://decrypt.co/377231/afterquery-ai-tradining-data-unicorn-y-combinator)
- Fleet: ~$1M (Oct 2025) to $60M (Apr 2026) [E/W] — [Sacra](https://sacra.com/c/fleet); [Shixiang](https://news.qq.com/rain/a/20260804A08FN500)
- micro1: $7M to $100M in 2025, $100M to $500M gross in eight months of 2026 [R] — [TechCrunch](https://techcrunch.com/2025/12/04/micro1-a-scale-ai-competitor-touts-crossing-100m-arr); [New Market Pitch](https://newmarketpitch.com/blogs/news/ai-training-data-business-model)
- Handshake AI: $5–10M to $550M in under a year [R] — [Dealroom](https://dealroom.co/news/127345-handshakes-arr-crosses-1b-as-ai-training-revenue-surges/)
- More than a dozen YC data and RL-environment start-ups reportedly sell over $10M a year to labs [W] — [Digg](https://digg.com/ai/aqq1dhu0)
- Deeptune: $43M Series A (Mar 2026), ~20 staff, "hundreds" of environments built, later acquired by Mercor (price undisclosed) [R/W] — [Fortune](https://fortune.com/2026/03/19/andreessen-horowitz-ai-startups-deeptune-series-a/); [New Market Pitch](https://newmarketpitch.com/blogs/news/ai-training-data-business-model)
- Mercor also bought Sepal AI (Feb 2026); Applied Compute's valuation went from $500M to $1.3B in three months; Idler raised a $9M seed (Aug 2026) [R/W] — [Contrary](https://research.contrary.com/report/mercor); [Shixiang](https://news.qq.com/rain/a/20260804A08FN500); [Dealroom](https://dealroom.co/news/146192-idler-raises-9m-seed-from-paradigm-to-build-rl-environments/)
- Concentration: Mercor 91% of H1 2026 revenue from foundation-model companies (one republication says OpenAI and Anthropic combined); Surge about 12 customers for over $1B; Deccan's top five are ~80%; most RL-environment firms have 1–3 customers [R/E/W] — [New Market Pitch](https://newmarketpitch.com/blogs/news/ai-training-data-business-model); [AI Weekly](https://aiweekly.co/alerts/mercor-books-614m-in-h1-2026-leaning-on-openai-anthropic); [Sacra](https://sacra.com/c/surge-ai); [SemiAnalysis](https://newsletter.semianalysis.com/p/rl-environments-and-rl-for-science)
- Contract shape: expert-data contracts last at least a quarter; RL environments are one-off deliveries with a useful life of about six months and no automatic repeat; without exclusivity a product reaches rival labs within months [R/W] — [SemiAnalysis](https://newsletter.semianalysis.com/p/rl-environments-and-rl-for-science); [Shixiang](https://news.qq.com/rain/a/20260804A08FN500)
- Valuation: leaders priced at about 10x run-rate [W] versus about 30x net revenue [E] — [Shixiang](https://news.qq.com/rain/a/20260804A08FN500); [Sacra](https://sacra.com/research/handshake-indeed-for-data-labelers/)

### Inferences
- For the winners, the observed time from first meaningful revenue to $40M gross is roughly 6–12 months (Fleet, micro1, AfterQuery), inside the founder's target, and it has been done with 20–50 staff. First-contract dates are not disclosed, so this is approximate.
- AfterQuery's angels include staff of DeepMind, OpenAI, Anthropic and Meta, and data budgets are often held by researchers, not procurement. Enterprise-sales skill helps only if it converts into access to those few buyers or into exclusive data sources.

### Gaps
- No month-by-month revenue for any 2025–2026 entrant; no disclosed contract values or payment terms.
- No count of entrants that failed to reach $10M.

---

## B4. Evidence of labs moving work in-house or cutting suppliers in 2026

### Takeaway
There is no evidence of total lab spend falling in 2026; Anthropic's vendor costs rose sharply. The evidence is of labs taking over design and tooling, buying raw inputs, cutting individual vendors abruptly, and repricing generalist work downward.

### Cited Findings
- Meta paused all Mercor work indefinitely after the March 2026 breach; affected contractors could not log hours [R] — [TechCrunch](https://techcrunch.com/2026/04/09/after-data-breach-10b-valued-startup-mercor-is-having-a-month); [TechRepublic](https://www.techrepublic.com/article/news-meta-pauses-work-with-mercor-after-data-breach/)
- OpenAI is building an in-house human-data platform ("Feather") to avoid vendor margins; xAI has hired its own tutors since launch [R, Jan 2026] — [SemiAnalysis](https://newsletter.semianalysis.com/p/rl-environments-and-rl-for-science). OpenAI job postings cover both vendor management and direct acquisition of skilled labelers [P] — [OpenAI careers](https://openai.com/careers/program-manager-human-data)
- "Substantially more in-housing" recently, to avoid margins and keep training priorities confidential [R, founder interview] — [Epoch AI](https://epoch.ai/gradient-updates/state-of-rl-envs)
- Many top labs have built their own environment-creation systems and now buy raw data [R] — [Sean Cai](https://seanzcai.substack.com/p/an-ai-bubble-is-a-human-data-problem). The most sophisticated buyers only need vendors to deliver containers to spec [W] — [Shixiang](https://news.qq.com/rain/a/20260804A08FN500)
- Some labs run internal data-operations teams between researchers and vendors [R] — [Sapphire Ventures](https://sapphireventures.com/?p=258819)
- Figure moved robot-data collection in-house in Aug 2026 after vendors missed its bar [P] — [Figure](https://figure.ai/news/introducing-index)
- The Information ran "How Microsoft, Meta, xAI Get AI Training Data From Their Employees" (headline only; paywalled) [R] — [The Information](https://theinformation.com/articles/microsoft-meta-xai-get-ai-training-data-employees)
- Earlier cuts for scale: Scale lost Google and OpenAI in mid-2025; xAI cut 500+ labelers in Sep 2025; Meta's Musen project at Mercor ended Nov 2025 and was replaced at lower pay [R] — [Sacra](https://sacra.com/research/scale-ai); [AOL](https://www.aol.com/articles/ai-startup-powering-meta-openai-230627434.html)
- Counter-evidence: Anthropic's data and evaluation vendor costs rose $757M year on year in nine months of 2026 [W] — [FourWeekMBA](https://fourweekmba.com/ai-anthropics-data-vendor-costs-rose-506m-yoy-in-q3-2x-h1/); Mercor's gross margin rose from 27% to 33% [R] — [Business Model Analyst](https://businessmodelanalyst.com/ai-data-factories-physical-ai-margins/)

### Inferences
- In-housing is taking the design layer (environment harnesses, task specification) and leaving suppliers the labor, raw data and capture layers. Supplier margin is safest where the supplier controls a source the lab cannot hire or scrape.
- Vendor risk in 2026 was operational and binary (a breach, a conflict of interest) more than a budget cut. A new entrant should plan for losing its largest customer without notice.

### Gaps
- No confirmed 2026 case of a lab ending a vendor to replace it with in-house staff.
- Claims that Google cut contractor budgets and OpenAI cut non-engineering hiring in 2026 come from one unverified blog and are excluded.
- Whether Meta resumed work with Mercor after April 2026 was not found.
